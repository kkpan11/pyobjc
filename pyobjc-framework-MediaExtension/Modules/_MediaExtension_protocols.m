/*
 * This file is generated by objective.metadata
 *
 * Last update: Fri Jun 14 22:03:01 2024
 */

static void __attribute__((__used__)) use_protocols(void)
{
#if PyObjC_BUILD_RELEASE >= 1500
    PyObject* p __attribute__((__unused__));
    p = PyObjC_IdToPython(@protocol(MEFormatReader)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MEFormatReaderExtension)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MERAWProcessor)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MERAWProcessorExtension)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MESampleCursor)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(METrackReader)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MEVideoDecoder)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MEVideoDecoderExtension)); Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1500 */
}