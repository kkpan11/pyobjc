"""
Script for building the example.

Usage:
    python3 setup.py py2app

Then install the bundle in dist into ~/Library/Automator.
"""

from setuptools import setup

infoPlist = {
    "AMAccepts": {
        "Container": "List",
        "Optional": False,
        "Types": ["com.apple.addressbook.person-object"],
    },
    "AMApplication": ["Address Book", "iChat"],
    "AMCanShowWhenRun": True,
    "AMCategory": "iChat",
    "AMDefaultParameters": {},
    "AMDescription": {
        "AMDAlert": "iChat must be running for this action to work properly.",
        "AMDNote": "Information will not be returned for the current user.",
        "AMDSummary": "This action returns the Instant Message information "
        "of the people passed from the previous action.",
    },
    "AMIconName": "iChat",
    "AMKeywords": ("Instant", "Message", "IM"),
    "AMName": "Get Buddy Info",
    "AMProvides": {"Container": "List", "Types": ["com.apple.cocoa.string"]},
}

setup(
    name="Get Buddy Info",
    plugin=["GetBuddyInfo.py"],
    data_files=[],
    options={"py2app": {"extension": ".action", "plist": infoPlist}},
    setup_requires=[
        "py2app",
        "pyobjc-framework-Automator",
        "pyobjc-framework-AddressBook",
        "pyobjc-framework-InstantMessage",
        "pyobjc-framework-Cocoa",
    ],
)
