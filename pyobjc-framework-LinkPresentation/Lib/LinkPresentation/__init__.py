"""
Python mapping for the LinkPresentation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="LinkPresentation",
        frameworkIdentifier="com.apple.LinkPresentation",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/LinkPresentation.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("LPLinkView", b"initWithCoder:"),
        ("LPLinkView", b"encodeWithCoder:"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["LinkPresentation._metadata"]


globals().pop("_setup")()
