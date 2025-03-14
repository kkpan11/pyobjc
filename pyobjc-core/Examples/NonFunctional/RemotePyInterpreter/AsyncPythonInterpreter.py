__all__ = ["AsyncPythonInterpreter"]

import fcntl
import os
import socket
import sys

import objc
from Foundation import (
    NSObject,
    NSUserDefaults,
    NSLog,
    NSFileHandle,
    NSNotificationCenter,
    NSFileHandleConnectionAcceptedNotification,
    NSTask,
    NSTaskDidTerminateNotification,
    NSFileHandleNotificationFileHandleItem,
    NSFileHandleReadCompletionNotification,
    NSFileHandleError,
    NSData,
    NSFileHandleNotificationDataItem,
)


IMPORT_MODULES = ["netrepr", "remote_console", "remote_pipe", "remote_bootstrap"]
source = []
for fn in IMPORT_MODULES:
    for line in open(fn + ".py"):
        source.append(line)
    source.append("\n\n")
SOURCE = repr("".join(source)) + "\n"


def bind_and_listen(hostport):
    if isinstance(hostport, str):
        host, port = hostport.split(":")
        hostport = (host, int(port))
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set close-on-exec
    if hasattr(fcntl, "FD_CLOEXEC"):
        old = fcntl.fcntl(serversock.fileno(), fcntl.F_GETFD)
        fcntl.fcntl(serversock.fileno(), fcntl.F_SETFD, old | fcntl.FD_CLOEXEC)
    # allow the address to be reused in a reasonable amount of time
    if os.name == "posix" and sys.platform != "cygwin":
        serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    serversock.bind(hostport)
    serversock.listen(5)
    return serversock


class AsyncPythonInterpreter(NSObject):
    commandReactor = objc.IBOutlet("commandReactor")

    def init(self):
        self = super().init()
        self.host = None
        self.port = None
        self.interpreterPath = None
        self.scriptPath = None
        self.commandReactor = None
        self.serverSocket = None
        self.serverFileHandle = None
        self.buffer = ""
        self.serverFileHandle = None
        self.remoteFileHandle = None
        self.childTask = None
        return self

    def initWithHost_port_interpreterPath_scriptPath_commandReactor_(
        self, host, port, interpreterPath, scriptPath, commandReactor
    ):
        self = self.init()
        self.host = host
        self.port = port
        self.interpreterPath = interpreterPath
        self.scriptPath = scriptPath
        self.commandReactor = commandReactor
        self.serverSocket = None
        return self

    def awakeFromNib(self):
        defaults = NSUserDefaults.standardUserDefaults()

        def default(k, v, typeCheck=None):
            rval = defaults.objectForKey_(k)
            if typeCheck is not None and rval is not None:
                try:
                    rval = typeCheck(rval)
                except TypeError:
                    NSLog(
                        "%s failed type check %s with value %s",
                        k,
                        typeCheck.__name__,
                        rval,
                    )
                    rval = None
            if rval is None:
                defaults.setObject_forKey_(v, k)
                rval = v
            return rval

        self.host = default("AsyncPythonInterpreterInterpreterHost", "127.0.0.1", str)
        self.port = default("AsyncPythonInterpreterInterpreterPort", 0, int)
        self.interpreterPath = default(
            "AsyncPythonInterpreterInterpreterPath", "/usr/bin/python", str
        )
        self.scriptPath = (
            type(self).bundleForClass().pathForResource_ofType_("tcpinterpreter", "py")
        )

    def connect(self):
        # NSLog(u'connect')
        self.serverSocket = bind_and_listen((self.host, self.port))
        self.serverFileHandle = NSFileHandle.alloc().initWithFileDescriptor_(
            self.serverSocket.fileno()
        )
        nc = NSNotificationCenter.defaultCenter()
        nc.addObserver_selector_name_object_(
            self,
            "remoteSocketAccepted:",
            NSFileHandleConnectionAcceptedNotification,
            self.serverFileHandle,
        )
        self.serverFileHandle.acceptConnectionInBackgroundAndNotify()
        self.remoteFileHandle = None
        for k in os.environ.keys():
            if k.startswith("PYTHON"):
                del os.environ[k]
        self.childTask = NSTask.launchedTaskWithLaunchPath_arguments_(
            self.interpreterPath,
            [self.scriptPath, repr(self.serverSocket.getsockname())],
        )
        nc.addObserver_selector_name_object_(
            self, "childTaskTerminated:", NSTaskDidTerminateNotification, self.childTask
        )
        return self

    def remoteSocketAccepted_(self, notification):
        # NSLog(u'remoteSocketAccepted_')
        self.serverFileHandle.closeFile()
        self.serverFileHandle = None
        ui = notification.userInfo()
        self.remoteFileHandle = ui.objectForKey_(NSFileHandleNotificationFileHandleItem)
        nc = NSNotificationCenter.defaultCenter()
        nc.addObserver_selector_name_object_(
            self,
            "remoteFileHandleReadCompleted:",
            NSFileHandleReadCompletionNotification,
            self.remoteFileHandle,
        )
        self.writeBytes_(SOURCE)
        self.remoteFileHandle.readInBackgroundAndNotify()
        self.commandReactor.connectionEstablished_(self)
        NSNotificationCenter.defaultCenter().postNotificationName_object_(
            "AsyncPythonInterpreterOpened", self
        )

    def remoteFileHandleReadCompleted_(self, notification):
        # NSLog(u'remoteFileHandleReadCompleted_')
        ui = notification.userInfo()
        newData = ui.objectForKey_(NSFileHandleNotificationDataItem)
        if newData is None:
            self.close()
            NSLog("Error: %@", ui.objectForKey_(NSFileHandleError))
            return
        data_bytes = newData.bytes()[:]
        if len(data_bytes) == 0:
            self.close()
            return
        self.remoteFileHandle.readInBackgroundAndNotify()
        start = len(self.buffer)
        buff = self.buffer + newData.bytes()[:]
        # NSLog(u'current buffer: %s', buff)
        lines = []
        while True:
            linebreak = buff.find("\n", start) + 1
            if linebreak == 0:
                break
            lines.append(buff[:linebreak])
            buff = buff[linebreak:]
            start = 0
        # NSLog(u'lines: %s', lines)
        self.buffer = buff
        for line in lines:
            self.commandReactor.lineReceived_fromConnection_(line, self)

    def writeBytes_(self, data):
        # NSLog(u'Writing bytes: %s', data)
        try:
            self.remoteFileHandle.writeData_(
                NSData.dataWithBytes_length_(data, len(data))
            )
        except objc.error:
            self.close()
        # NSLog(u'bytes written.')

    def childTaskTerminated_(self, notification):
        # NSLog(u'childTaskTerminated_')
        self.close()

    def closeServerFileHandle(self):
        # NSLog(u'closeServerFileHandle')
        if self.serverFileHandle is not None:
            try:
                self.serverFileHandle.closeFile()
            except objc.error:
                pass
            self.serverFileHandle = None

    def closeRemoteFileHandle(self):
        # NSLog(u'closeRemoteFileHandle')
        if self.remoteFileHandle is not None:
            try:
                self.remoteFileHandle.closeFile()
            except objc.error:
                pass
            self.remoteFileHandle = None

    def terminateChildTask(self):
        # NSLog(u'terminateChildTask')
        if self.childTask is not None:
            try:
                self.childTask.terminate()
            except objc.error:
                pass
            self.childTask = None

    def close(self):
        # NSLog(u'close')
        NSNotificationCenter.defaultCenter().removeObserver_(self)
        self.finalClose()
        NSNotificationCenter.defaultCenter().postNotificationName_object_(
            "AsyncPythonInterpreterClosed", self
        )

    def finalClose(self):
        if self.commandReactor is not None:
            self.commandReactor.connectionClosed_(self)
            self.commandReactor = None
        self.closeServerFileHandle()
        self.closeRemoteFileHandle()
        self.terminateChildTask()


def test_console():
    from PyObjCTools import AppHelper
    from ConsoleReactor import ConsoleReactor

    host = "127.0.0.1"
    port = 0
    interpreterPath = sys.executable
    scriptPath = os.path.abspath("tcpinterpreter.py")
    commandReactor = ConsoleReactor.alloc().init()
    interp = AsyncPythonInterpreter.alloc().initWithHost_port_interpreterPath_scriptPath_commandReactor_(  # noqa: B950
        host, port, interpreterPath, scriptPath, commandReactor
    )
    interp.connect()

    class ThisEventLoopStopper(NSObject):
        def interpFinished_(self, notification):
            AppHelper.stopEventLoop()

    stopper = ThisEventLoopStopper.alloc().init()
    NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
        stopper, "interpFinished:", "AsyncPythonInterpreterClosed", interp
    )
    AppHelper.runConsoleEventLoop(installInterrupt=True)


def main():
    test_console()


if __name__ == "__main__":
    main()
