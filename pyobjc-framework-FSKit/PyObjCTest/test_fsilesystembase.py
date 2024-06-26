from PyObjCTools.TestSupport import TestCase
import objc

import FSKit  # noqa: F401


class TestFSFileSystemBaseHelper(FSKit.NSObject):
    def containerState(self):
        return 1

    def setContainerState_(self, a):
        pass

    def wipeResource_includingRanges_excludingRanges_replyHandler_(self, a, b, c, d):
        pass


class TestFSFileSystemBase(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("FSFileSystemBase")

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestFSFileSystemBaseHelper.containerState, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestFSFileSystemBaseHelper.setContainerState_, 0, objc._C_NSInteger
        )

        self.assertArgIsBlock(
            TestFSFileSystemBaseHelper.wipeResource_includingRanges_excludingRanges_replyHandler_,
            3,
            b"v@",
        )
