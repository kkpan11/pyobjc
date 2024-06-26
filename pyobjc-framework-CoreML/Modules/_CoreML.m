#define Py_LIMITED_API 0x03090000
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <CoreML/CoreML.h>
#import <Foundation/Foundation.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_CoreML_protocols.m"

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

/* Python glue */
static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_CoreML", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__CoreML(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__CoreML(void)
{
    PyObject* m;
    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) == -1)
        return NULL;

    return m;
}
