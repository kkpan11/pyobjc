#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

static NSMapTable* _Nonnull python_proxies;
static NSMapTable* _Nonnull objc_proxies;

int
PyObjC_InitProxyRegistry(PyObject* module __attribute__((__unused__)))
{
    python_proxies = NSCreateMapTable(PyObjCUtil_PointerKeyCallBacks,
                                      PyObjCUtil_PointerValueCallBacks, 0);

    if (python_proxies == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot create NSMapTable for python_proxies");
        return -1;
        // LCOV_EXCL_STOP
    }

    objc_proxies = NSCreateMapTable(PyObjCUtil_PointerKeyCallBacks,
                                    PyObjCUtil_PointerValueCallBacks, 0);
    if (objc_proxies == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_RuntimeError, "Cannot create NSMapTable for objc_proxies");
        return -1;
        // LCOV_EXCL_STOP
    }
    return 0;
}

/*
 * XXX: Add locking
 */
PyObject*
PyObjC_RegisterPythonProxy(id original, PyObject* proxy)
{
    NSMapInsert(python_proxies, original, proxy);

    Py_INCREF(proxy);
    return proxy;
}

/*
 * XXX: Add locking
 */
id
PyObjC_RegisterObjCProxy(PyObject* original, id proxy)
{
    NSMapInsert(objc_proxies, original, proxy);
    return proxy;
}

/*
 * XXX: Add locking
 */
void
PyObjC_UnregisterPythonProxy(id original, PyObject* proxy)
{
    PyObject* v;

    if (original == nil)
        return;

    v = NSMapGet(python_proxies, original);
    if (v == proxy) {
        NSMapRemove(python_proxies, original);
    }
}

/*
 * XXX: Add locking
 */
void
PyObjC_UnregisterObjCProxy(PyObject* original, id proxy)
{
    id v;

    if (original == NULL)
        return;

    v = NSMapGet(objc_proxies, original);
    if (v == proxy) {
        NSMapRemove(objc_proxies, original);
    }
}

PyObject* _Nullable PyObjC_FindPythonProxy(id original)
{
    PyObject* v;

    if (original == nil)           // LCOV_BR_EXCL_LINE
        PyObjCErr_InternalError(); // LCOV_EXCL_LINE

    v = NSMapGet(python_proxies, original);
    Py_XINCREF(v);
    return v;
}

id _Nullable PyObjC_FindObjCProxy(PyObject* original)
{
    if (original == Py_None)       // LCOV_BR_EXCL_LINE
        PyObjCErr_InternalError(); // LCOV_EXCL_LINE

    return NSMapGet(objc_proxies, original);
}

NS_ASSUME_NONNULL_END
