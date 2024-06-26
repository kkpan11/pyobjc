"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""

from setuptools import setup

plist = {
    "CFBundleDocumentTypes": [
        {
            "CFBundleTypeExtensions": ["mht"],
            "CFBundleTypeName": "Internet Explorer Web Archive",
            "CFBundleTypeRole": "Editor",
            "NSDocumentClass": "MHTDocument",
        }
    ]
}

setup(
    name="MHTViewer",
    app=["main.py"],
    data_files=["MainMenu.nib", "MHTDocument.nib"],
    options={"py2app": {"plist": plist}},
    setup_requires=["py2app", "pyobjc-framework-Cocoa", "pyobjc-framework-WebKit"],
)
