/*
 * This file is generated by objective.metadata
 *
 * Last update: Sat Mar  8 09:53:28 2025
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1016
    p = PyObjC_IdToPython(@protocol(CXCallDirectoryExtensionContextDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CXCallObserverDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CXProviderDelegate)); Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1016 */
}
