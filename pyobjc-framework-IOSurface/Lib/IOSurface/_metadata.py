# This file is generated by objective.metadata
#
# Last update: Tue Jun 11 10:12:28 2024
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$IOSurfacePropertyAllocSizeKey$IOSurfacePropertyKeyAllocSize$IOSurfacePropertyKeyBytesPerElement$IOSurfacePropertyKeyBytesPerRow$IOSurfacePropertyKeyCacheMode$IOSurfacePropertyKeyElementHeight$IOSurfacePropertyKeyElementWidth$IOSurfacePropertyKeyHeight$IOSurfacePropertyKeyName$IOSurfacePropertyKeyOffset$IOSurfacePropertyKeyPixelFormat$IOSurfacePropertyKeyPixelSizeCastingAllowed$IOSurfacePropertyKeyPlaneBase$IOSurfacePropertyKeyPlaneBytesPerElement$IOSurfacePropertyKeyPlaneBytesPerRow$IOSurfacePropertyKeyPlaneElementHeight$IOSurfacePropertyKeyPlaneElementWidth$IOSurfacePropertyKeyPlaneHeight$IOSurfacePropertyKeyPlaneInfo$IOSurfacePropertyKeyPlaneOffset$IOSurfacePropertyKeyPlaneSize$IOSurfacePropertyKeyPlaneWidth$IOSurfacePropertyKeyWidth$kIOSurfaceAllocSize$kIOSurfaceBytesPerElement$kIOSurfaceBytesPerRow$kIOSurfaceCacheMode$kIOSurfaceColorSpace$kIOSurfaceContentHeadroom$kIOSurfaceElementHeight$kIOSurfaceElementWidth$kIOSurfaceHeight$kIOSurfaceICCProfile$kIOSurfaceIsGlobal$kIOSurfaceName$kIOSurfaceOffset$kIOSurfacePixelFormat$kIOSurfacePixelSizeCastingAllowed$kIOSurfacePlaneBase$kIOSurfacePlaneBitsPerElement$kIOSurfacePlaneBytesPerElement$kIOSurfacePlaneBytesPerRow$kIOSurfacePlaneComponentBitDepths$kIOSurfacePlaneComponentBitOffsets$kIOSurfacePlaneComponentNames$kIOSurfacePlaneComponentRanges$kIOSurfacePlaneComponentTypes$kIOSurfacePlaneElementHeight$kIOSurfacePlaneElementWidth$kIOSurfacePlaneHeight$kIOSurfacePlaneInfo$kIOSurfacePlaneOffset$kIOSurfacePlaneSize$kIOSurfacePlaneWidth$kIOSurfaceSubsampling$kIOSurfaceWidth$"""
enums = """$IOSURFACE_API_H@1$IOSURFACE_H@1$IOSURFACE_REF_H@1$_IOSURFACE_API_H@1$_IOSURFACE_H@1$kIOSurfaceComponentNameAlpha@1$kIOSurfaceComponentNameBlue@4$kIOSurfaceComponentNameChromaBlue@7$kIOSurfaceComponentNameChromaRed@6$kIOSurfaceComponentNameGreen@3$kIOSurfaceComponentNameLuma@5$kIOSurfaceComponentNameRed@2$kIOSurfaceComponentNameUnknown@0$kIOSurfaceComponentRangeFullRange@1$kIOSurfaceComponentRangeUnknown@0$kIOSurfaceComponentRangeVideoRange@2$kIOSurfaceComponentRangeWideRange@3$kIOSurfaceComponentTypeFloat@3$kIOSurfaceComponentTypeSignedInteger@2$kIOSurfaceComponentTypeSignedNormalized@4$kIOSurfaceComponentTypeUnknown@0$kIOSurfaceComponentTypeUnsignedInteger@1$kIOSurfaceCopybackCache@3$kIOSurfaceCopybackInnerCache@5$kIOSurfaceDefaultCache@0$kIOSurfaceInhibitCache@1$kIOSurfaceLockAvoidSync@2$kIOSurfaceLockReadOnly@1$kIOSurfaceMapCacheShift@8$kIOSurfaceMapCopybackCache@768$kIOSurfaceMapCopybackInnerCache@1280$kIOSurfaceMapDefaultCache@0$kIOSurfaceMapInhibitCache@256$kIOSurfaceMapWriteCombineCache@1024$kIOSurfaceMapWriteThruCache@512$kIOSurfaceMemoryLedgerFlagNoFootprint@1$kIOSurfaceMemoryLedgerTagDefault@1$kIOSurfaceMemoryLedgerTagGraphics@4$kIOSurfaceMemoryLedgerTagMedia@3$kIOSurfaceMemoryLedgerTagNetwork@2$kIOSurfaceMemoryLedgerTagNeural@5$kIOSurfacePurgeableEmpty@2$kIOSurfacePurgeableKeepCurrent@3$kIOSurfacePurgeableNonVolatile@0$kIOSurfacePurgeableVolatile@1$kIOSurfaceSubsampling411@4$kIOSurfaceSubsampling420@3$kIOSurfaceSubsampling422@2$kIOSurfaceSubsamplingNone@1$kIOSurfaceSubsamplingUnknown@0$kIOSurfaceWriteCombineCache@4$kIOSurfaceWriteThruCache@2$"""
misc.update(
    {
        "IOSurfaceMemoryLedgerFlags": NewType("IOSurfaceMemoryLedgerFlags", int),
        "IOSurfacePurgeabilityState": NewType("IOSurfacePurgeabilityState", int),
        "IOSurfaceComponentRange": NewType("IOSurfaceComponentRange", int),
        "IOSurfaceLockOptions": NewType("IOSurfaceLockOptions", int),
        "IOSurfaceComponentType": NewType("IOSurfaceComponentType", int),
        "IOSurfaceSubsampling": NewType("IOSurfaceSubsampling", int),
        "IOSurfaceComponentName": NewType("IOSurfaceComponentName", int),
        "IOSurfaceMemoryLedgerTags": NewType("IOSurfaceMemoryLedgerTags", int),
    }
)
misc.update({})
misc.update({})
functions = {
    "IOSurfaceGetSeed": (b"I^{__IOSurface=}",),
    "IOSurfaceGetRangeOfComponentOfPlane": (b"i^{__IOSurface=}QQ",),
    "IOSurfaceLookupFromMachPort": (
        b"^{__IOSurface=}I",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "IOSurfaceGetBytesPerRow": (b"Q^{__IOSurface=}",),
    "IOSurfaceGetUseCount": (b"i^{__IOSurface=}",),
    "IOSurfaceSetValue": (b"v^{__IOSurface=}^{__CFString=}@",),
    "IOSurfaceGetPlaneCount": (b"Q^{__IOSurface=}",),
    "IOSurfaceLock": (
        b"i^{__IOSurface=}I^I",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "IOSurfaceDecrementUseCount": (b"v^{__IOSurface=}",),
    "IOSurfaceGetTypeOfComponentOfPlane": (b"i^{__IOSurface=}QQ",),
    "IOSurfaceLookupFromXPCObject": (
        b"^{__IOSurface=}@",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "IOSurfaceSetOwnershipIdentity": (b"i^{__IOSurface=}IiI",),
    "IOSurfaceGetElementHeight": (b"Q^{__IOSurface=}",),
    "IOSurfaceGetBaseAddressOfPlane": (
        b"^v^{__IOSurface=}Q",
        "",
        {"retval": {"c_array_of_variable_length": True}},
    ),
    "IOSurfaceGetSubsampling": (b"i^{__IOSurface=}",),
    "IOSurfaceLookup": (
        b"^{__IOSurface=}I",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "IOSurfaceGetPixelFormat": (b"I^{__IOSurface=}",),
    "IOSurfaceGetBitOffsetOfComponentOfPlane": (b"Q^{__IOSurface=}QQ",),
    "IOSurfaceCopyValue": (
        b"@^{__IOSurface=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "IOSurfaceIncrementUseCount": (b"v^{__IOSurface=}",),
    "IOSurfaceGetElementWidthOfPlane": (b"Q^{__IOSurface=}Q",),
    "IOSurfaceGetID": (b"I^{__IOSurface=}",),
    "IOSurfaceSetValues": (b"v^{__IOSurface=}^{__CFDictionary=}",),
    "IOSurfaceRemoveAllValues": (b"v^{__IOSurface=}",),
    "IOSurfaceGetTypeID": (b"Q",),
    "IOSurfaceCreateXPCObject": (
        b"@^{__IOSurface=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "IOSurfaceGetAllocSize": (b"Q^{__IOSurface=}",),
    "IOSurfaceGetBitDepthOfComponentOfPlane": (b"Q^{__IOSurface=}QQ",),
    "IOSurfaceGetElementWidth": (b"Q^{__IOSurface=}",),
    "IOSurfaceGetBytesPerElementOfPlane": (b"Q^{__IOSurface=}Q",),
    "IOSurfaceCreateMachPort": (
        b"I^{__IOSurface=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "IOSurfaceGetNumberOfComponentsOfPlane": (b"Q^{__IOSurface=}Q",),
    "IOSurfaceGetWidth": (b"Q^{__IOSurface=}",),
    "IOSurfaceRemoveValue": (b"v^{__IOSurface=}^{__CFString=}",),
    "IOSurfaceGetHeightOfPlane": (b"Q^{__IOSurface=}Q",),
    "IOSurfaceGetHeight": (b"Q^{__IOSurface=}",),
    "IOSurfaceGetBaseAddress": (
        b"^v^{__IOSurface=}",
        "",
        {"retval": {"c_array_of_variable_length": True}},
    ),
    "IOSurfaceAlignProperty": (b"Q^{__CFString=}Q",),
    "IOSurfaceGetBytesPerRowOfPlane": (b"Q^{__IOSurface=}Q",),
    "IOSurfaceCreate": (
        b"^{__IOSurface=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "IOSurfaceGetElementHeightOfPlane": (b"Q^{__IOSurface=}Q",),
    "IOSurfaceGetBytesPerElement": (b"Q^{__IOSurface=}",),
    "IOSurfaceGetPropertyAlignment": (b"Q^{__CFString=}",),
    "IOSurfaceGetNameOfComponentOfPlane": (b"i^{__IOSurface=}QQ",),
    "IOSurfaceSetPurgeable": (
        b"i^{__IOSurface=}I^I",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "IOSurfaceUnlock": (
        b"i^{__IOSurface=}I^I",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "IOSurfaceGetPropertyMaximum": (b"Q^{__CFString=}",),
    "IOSurfaceGetWidthOfPlane": (b"Q^{__IOSurface=}Q",),
    "IOSurfaceIsInUse": (b"Z^{__IOSurface=}",),
    "IOSurfaceAllowsPixelSizeCasting": (b"Z^{__IOSurface=}",),
    "IOSurfaceCopyAllValues": (
        b"^{__CFDictionary=}^{__IOSurface=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
}
aliases = {
    "IOSFC_AVAILABLE_BUT_DEPRECATED": "__OSX_AVAILABLE_BUT_DEPRECATED",
    "IOSFC_AVAILABLE_STARTING": "__OSX_AVAILABLE_STARTING",
    "kIOSurfaceSuccess": "KERN_SUCCESS",
    "IOSFC_DEPRECATED": "DEPRECATED_ATTRIBUTE",
}
cftypes = [("IOSurfaceRef", b"^{__IOSurface=}", "IOSurfaceGetTypeID", None)]
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"IOSurface", b"allowsPixelSizeCasting", {"retval": {"type": "Z"}})
    r(
        b"IOSurface",
        b"baseAddressOfPlaneAtIndex:",
        {"retval": {"c_array_of_variable_length": True}},
    )
    r(b"IOSurface", b"isInUse", {"retval": {"type": "Z"}})
    r(
        b"IOSurface",
        b"lockWithOptions:seed:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"IOSurface",
        b"setPurgeable:oldState:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"IOSurface",
        b"unlockWithOptions:seed:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
