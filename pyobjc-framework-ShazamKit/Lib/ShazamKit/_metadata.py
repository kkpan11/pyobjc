# This file is generated by objective.metadata
#
# Last update: Sun Feb 23 20:17:00 2025
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
constants = """$SHErrorDomain$SHMediaItemAppleMusicID$SHMediaItemAppleMusicURL$SHMediaItemArtist$SHMediaItemArtworkURL$SHMediaItemConfidence$SHMediaItemCreationDate$SHMediaItemExplicitContent$SHMediaItemFrequencySkew$SHMediaItemFrequencySkewRanges$SHMediaItemGenres$SHMediaItemISRC$SHMediaItemMatchOffset$SHMediaItemShazamID$SHMediaItemSubtitle$SHMediaItemTimeRanges$SHMediaItemTitle$SHMediaItemVideoURL$SHMediaItemWebURL$"""
enums = """$SHErrorCodeAudioDiscontinuity@101$SHErrorCodeCustomCatalogInvalid@300$SHErrorCodeCustomCatalogInvalidURL@301$SHErrorCodeInternalError@500$SHErrorCodeInvalidAudioFormat@100$SHErrorCodeMatchAttemptFailed@202$SHErrorCodeMediaItemFetchFailed@600$SHErrorCodeMediaLibrarySyncFailed@400$SHErrorCodeSignatureDurationInvalid@201$SHErrorCodeSignatureInvalid@200$"""
misc.update({"SHErrorCode": NewType("SHErrorCode", int)})
misc.update({"SHMediaItemProperty": NewType("SHMediaItemProperty", str)})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"session:didFindMatch:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"session:didNotFindMatchForSignature:error:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"SHCustomCatalog",
        b"addCustomCatalogFromURL:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"SHCustomCatalog",
        b"addReferenceSignature:representingMediaItems:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"SHCustomCatalog",
        b"initWithDataRepresentation:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"SHCustomCatalog",
        b"writeToURL:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(b"SHMediaItem", b"explicitContent", {"retval": {"type": b"Z"}})
    r(
        b"SHMediaItem",
        b"fetchMediaItemWithShazamID:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SHMediaLibrary",
        b"addMediaItems:completionHandler:",
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
    r(
        b"SHSignature",
        b"initWithDataRepresentation:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"SHSignature",
        b"signatureWithDataRepresentation:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"SHSignatureGenerator",
        b"appendBuffer:atTime:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"SHSignatureGenerator",
        b"generateSignatureFromAsset:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector(
    "SHCustomCatalog", b"initWithDataRepresentation:error:"
)
objc.registerNewKeywordsFromSelector("SHRange", b"initWithLowerBound:upperBound:")
objc.registerNewKeywordsFromSelector("SHSession", b"initWithCatalog:")
objc.registerNewKeywordsFromSelector(
    "SHSignature", b"initWithDataRepresentation:error:"
)
expressions = {}

# END OF FILE
