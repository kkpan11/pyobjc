# This file is generated by objective.metadata
#
# Last update: Sat May 18 09:34:18 2024
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
constants = """$PHProjectCategoryBook$PHProjectCategoryCalendar$PHProjectCategoryCard$PHProjectCategoryOther$PHProjectCategoryPrints$PHProjectCategorySlideshow$PHProjectCategoryUndefined$PHProjectCategoryWallDecor$PHProjectTypeUndefined$"""
enums = """$PHLivePhotoViewContentModeAspectFill@1$PHLivePhotoViewContentModeAspectFit@0$PHLivePhotoViewPlaybackStyleFull@1$PHLivePhotoViewPlaybackStyleHint@2$PHLivePhotoViewPlaybackStyleUndefined@0$PHPickerCapabilitiesCollectionNavigation@4$PHPickerCapabilitiesNone@0$PHPickerCapabilitiesSearch@1$PHPickerCapabilitiesSelectionActions@8$PHPickerCapabilitiesSensitivityAnalysisIntervention@16$PHPickerCapabilitiesStagingArea@2$PHPickerConfigurationAssetRepresentationModeAutomatic@0$PHPickerConfigurationAssetRepresentationModeCompatible@2$PHPickerConfigurationAssetRepresentationModeCurrent@1$PHPickerConfigurationSelectionContinuous@2$PHPickerConfigurationSelectionContinuousAndOrdered@3$PHPickerConfigurationSelectionDefault@0$PHPickerConfigurationSelectionOrdered@1$PHPickerModeCompact@1$PHPickerModeDefault@0$PHProjectCreationSourceAlbum@2$PHProjectCreationSourceMemory@3$PHProjectCreationSourceMoment@4$PHProjectCreationSourceProject@20$PHProjectCreationSourceProjectBook@21$PHProjectCreationSourceProjectCalendar@22$PHProjectCreationSourceProjectCard@23$PHProjectCreationSourceProjectExtension@26$PHProjectCreationSourceProjectPrintOrder@24$PHProjectCreationSourceProjectSlideshow@25$PHProjectCreationSourceUndefined@0$PHProjectCreationSourceUserSelection@1$PHProjectSectionTypeAuxiliary@3$PHProjectSectionTypeContent@2$PHProjectSectionTypeCover@1$PHProjectSectionTypeUndefined@0$PHProjectTextElementTypeBody@0$PHProjectTextElementTypeSubtitle@2$PHProjectTextElementTypeTitle@1$"""
misc.update(
    {
        "PHPickerConfigurationAssetRepresentationMode": NewType(
            "PHPickerConfigurationAssetRepresentationMode", int
        ),
        "PHProjectCreationSource": NewType("PHProjectCreationSource", int),
        "PHPickerMode": NewType("PHPickerMode", int),
        "PHAssetPlaybackStyle": NewType("PHAssetPlaybackStyle", int),
        "PHLivePhotoViewPlaybackStyle": NewType("PHLivePhotoViewPlaybackStyle", int),
        "PHProjectSectionType": NewType("PHProjectSectionType", int),
        "PHProjectTextElementType": NewType("PHProjectTextElementType", int),
        "PHPickerCapabilities": NewType("PHPickerCapabilities", int),
        "PHPickerConfigurationSelection": NewType(
            "PHPickerConfigurationSelection", int
        ),
        "PHLivePhotoViewContentMode": NewType("PHLivePhotoViewContentMode", int),
    }
)
misc.update({"PHProjectCategory": NewType("PHProjectCategory", str)})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"beginProjectWithExtensionContext:projectInfo:completion:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": "@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"canHandleAdjustmentData:",
        {"required": True, "retval": {"type": "Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"cancelContentEditing",
        {"required": True, "retval": {"type": b"v"}},
    )
    r(
        b"NSObject",
        b"extensionWillDiscardDataSource",
        {"required": False, "retval": {"type": b"v"}},
    )
    r(
        b"NSObject",
        b"finishContentEditingWithCompletionHandler:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": "@?",
                }
            },
        },
    )
    r(
        b"NSObject",
        b"finishProjectWithCompletionHandler:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": "@?",
                }
            },
        },
    )
    r(
        b"NSObject",
        b"footerTextForSubtypesOfProjectType:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"invalidateFooterTextForSubtypesOfProjectType:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"invalidateTypeDescriptionForProjectType:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"livePhotoView:canBeginPlaybackWithStyle:",
        {
            "required": False,
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "q"}},
        },
    )
    r(
        b"NSObject",
        b"livePhotoView:didEndPlaybackWithStyle:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "q"}},
        },
    )
    r(
        b"NSObject",
        b"livePhotoView:willBeginPlaybackWithStyle:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "q"}},
        },
    )
    r(
        b"NSObject",
        b"picker:didFinishPicking:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"resumeProjectWithExtensionContext:completion:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": "@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"shouldShowCancelConfirmation",
        {"required": True, "retval": {"type": "Z"}},
    )
    r(
        b"NSObject",
        b"startContentEditingWithInput:placeholderImage:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"subtypesForProjectType:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"supportedProjectTypes",
        {"required": False, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"typeDescriptionDataSourceForCategory:invalidator:",
        {
            "required": False,
            "retval": {"type": b"@"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"typeDescriptionForProjectType:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"PHLivePhotoView", b"isMuted", {"retval": {"type": "Z"}})
    r(b"PHLivePhotoView", b"setMuted:", {"arguments": {2: {"type": "Z"}}})
    r(b"PHLivePhotoView", b"stopPlaybackAnimated:", {"arguments": {2: {"type": "Z"}}})
    r(b"PHProjectAssetElement", b"horizontallyFlipped", {"retval": {"type": b"Z"}})
    r(b"PHProjectAssetElement", b"verticallyFlipped", {"retval": {"type": b"Z"}})
    r(
        b"PHProjectExtensionContext",
        b"updatedProjectInfoFromProjectInfo:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(b"PHProjectInfo", b"brandingEnabled", {"retval": {"type": b"Z"}})
    r(b"PHProjectInfo", b"pageNumbersEnabled", {"retval": {"type": b"Z"}})
    r(b"PHProjectTypeDescription", b"canProvideSubtypes", {"retval": {"type": b"Z"}})
    r(
        b"PHProjectTypeDescription",
        b"initWithProjectType:title:attributedDescription:image:canProvideSubtypes:",
        {"arguments": {6: {"type": b"Z"}}},
    )
    r(
        b"PHProjectTypeDescription",
        b"initWithProjectType:title:description:image:canProvideSubtypes:",
        {"arguments": {6: {"type": b"Z"}}},
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector("PHPickerConfiguration", b"initWithPhotoLibrary:")
objc.registerNewKeywordsFromSelector("PHPickerViewController", b"initWithCoder:")
objc.registerNewKeywordsFromSelector(
    "PHPickerViewController", b"initWithConfiguration:"
)
objc.registerNewKeywordsFromSelector(
    "PHPickerViewController", b"initWithNibName:bundle:"
)
objc.registerNewKeywordsFromSelector(
    "PHProjectTypeDescription",
    b"initWithProjectType:title:attributedDescription:image:canProvideSubtypes:",
)
objc.registerNewKeywordsFromSelector(
    "PHProjectTypeDescription",
    b"initWithProjectType:title:attributedDescription:image:subtypeDescriptions:",
)
objc.registerNewKeywordsFromSelector(
    "PHProjectTypeDescription", b"initWithProjectType:title:description:image:"
)
objc.registerNewKeywordsFromSelector(
    "PHProjectTypeDescription",
    b"initWithProjectType:title:description:image:canProvideSubtypes:",
)
objc.registerNewKeywordsFromSelector(
    "PHProjectTypeDescription",
    b"initWithProjectType:title:description:image:subtypeDescriptions:",
)
expressions = {}

# END OF FILE
