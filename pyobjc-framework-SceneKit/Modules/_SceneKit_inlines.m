#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"
#import <SceneKit/SceneKit.h>

/*
 * The definitions below can cause warnings when using
 * -Wunguarded-availability, but those warnings are harmless
 * because the functions are inline functions and hence will
 * be available on all macOS versions once compiled.
 */
#if PyObjC_BUILD_RELEASE >= 1013
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability"
#endif

static PyObjC_function_map function_map[] = {
    {"SCNMatrix4FromMat4", (PyObjC_Function_Pointer)&SCNMatrix4FromMat4},
    {"SCNMatrix4MakeScale", (PyObjC_Function_Pointer)&SCNMatrix4MakeScale},
    {"SCNMatrix4MakeTranslation", (PyObjC_Function_Pointer)&SCNMatrix4MakeTranslation},
    {"SCNMatrix4ToMat4", (PyObjC_Function_Pointer)&SCNMatrix4ToMat4},
    {"SCNMatrix4Translate", (PyObjC_Function_Pointer)&SCNMatrix4Translate},
    {"SCNVector3FromFloat3", (PyObjC_Function_Pointer)&SCNVector3FromFloat3},
    {"SCNVector3FromGLKVector3", (PyObjC_Function_Pointer)&SCNVector3FromGLKVector3},
    {"SCNVector3Make", (PyObjC_Function_Pointer)&SCNVector3Make},
    {"SCNVector3ToFloat3", (PyObjC_Function_Pointer)&SCNVector3ToFloat3},
    {"SCNVector3ToGLKVector3", (PyObjC_Function_Pointer)&SCNVector3ToGLKVector3},
    {"SCNVector4FromFloat4", (PyObjC_Function_Pointer)&SCNVector4FromFloat4},
    {"SCNVector4FromGLKVector4", (PyObjC_Function_Pointer)&SCNVector4FromGLKVector4},
    {"SCNVector4Make", (PyObjC_Function_Pointer)&SCNVector4Make},
    {"SCNVector4ToFloat4", (PyObjC_Function_Pointer)&SCNVector4ToFloat4},
    {"SCNVector4ToGLKVector4", (PyObjC_Function_Pointer)&SCNVector4ToGLKVector4},
    {0, 0}};

#if PyObjC_BUILD_RELEASE >= 1013
#pragma clang diagnostic pop
#endif

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

static int mod_exec_module(PyObject* m)
{
    if (PyModule_AddObject(m, "_inline_list_", PyObjC_CreateInlineTab(function_map)) < 0)
        return -1;

    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {
        .slot = Py_mod_exec,
        .value = (void*)mod_exec_module
    },
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot = Py_mod_multiple_interpreters,
        .value = Py_MOD_PER_INTERPRETER_GIL_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        /* The code in this extension should be safe to use without the GIL */
        .slot = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {  /* Sentinel */
        .slot = 0,
        .value = 0
    }
};

static struct PyModuleDef mod_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "_inlines",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit__inlines(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__inlines(void)
{
    return PyModuleDef_Init(&mod_module);
}
