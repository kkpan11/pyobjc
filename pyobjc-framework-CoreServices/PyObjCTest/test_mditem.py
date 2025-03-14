import CoreServices
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestMDImport(TestCase):
    @expectedFailure
    def test_types(self):
        self.assertIsCFType(CoreServices.MDItemRef)

    def test_functions(self):
        self.assertIsInstance(CoreServices.MDItemGetTypeID(), int)

        self.assertResultIsCFRetained(CoreServices.MDItemCreate)
        self.assertResultIsCFRetained(CoreServices.MDItemCreateWithURL)
        self.assertResultIsCFRetained(CoreServices.MDItemsCreateWithURLs)
        self.assertResultIsCFRetained(CoreServices.MDItemCopyAttribute)
        self.assertResultIsCFRetained(CoreServices.MDItemCopyAttributes)

        self.assertResultIsCFRetained(CoreServices.MDItemCopyAttributeNames)

    @min_os_level("10.12")
    def test_functions10_10(self):
        # Documented on 10.11, but not available there
        self.assertResultIsCFRetained(CoreServices.MDItemsCopyAttributes)

    @min_os_level("15.2")
    def test_functions15_2(self):
        self.assertArgIsBlock(
            CoreServices.MDItemGetCacheFileDescriptors, 1, b"v^{__CFArray=}"
        )

    @expectedFailure
    def test_functions_missing(self):
        # Link error on 10.13
        self.assertIsNullTerminated(CoreServices.MDItemCopyAttributeList)
        self.assertResultIsCFRetained(CoreServices.MDItemCopyAttributeList)

    def test_constants(self):
        self.assertIsInstance(CoreServices.kMDItemAttributeChangeDate, str)
        self.assertIsInstance(CoreServices.kMDItemContentType, str)
        self.assertIsInstance(CoreServices.kMDItemKeywords, str)
        self.assertIsInstance(CoreServices.kMDItemTitle, str)
        self.assertIsInstance(CoreServices.kMDItemAuthors, str)
        self.assertIsInstance(CoreServices.kMDItemProjects, str)
        self.assertIsInstance(CoreServices.kMDItemWhereFroms, str)
        self.assertIsInstance(CoreServices.kMDItemComment, str)
        self.assertIsInstance(CoreServices.kMDItemCopyright, str)
        self.assertIsInstance(CoreServices.kMDItemLastUsedDate, str)
        self.assertIsInstance(CoreServices.kMDItemContentCreationDate, str)
        self.assertIsInstance(CoreServices.kMDItemContentModificationDate, str)
        self.assertIsInstance(CoreServices.kMDItemDurationSeconds, str)
        self.assertIsInstance(CoreServices.kMDItemContactKeywords, str)
        self.assertIsInstance(CoreServices.kMDItemVersion, str)
        self.assertIsInstance(CoreServices.kMDItemPixelHeight, str)
        self.assertIsInstance(CoreServices.kMDItemPixelWidth, str)
        self.assertIsInstance(CoreServices.kMDItemColorSpace, str)
        self.assertIsInstance(CoreServices.kMDItemBitsPerSample, str)
        self.assertIsInstance(CoreServices.kMDItemFlashOnOff, str)
        self.assertIsInstance(CoreServices.kMDItemFocalLength, str)
        self.assertIsInstance(CoreServices.kMDItemAcquisitionMake, str)
        self.assertIsInstance(CoreServices.kMDItemAcquisitionModel, str)
        self.assertIsInstance(CoreServices.kMDItemISOSpeed, str)
        self.assertIsInstance(CoreServices.kMDItemOrientation, str)
        self.assertIsInstance(CoreServices.kMDItemLayerNames, str)
        self.assertIsInstance(CoreServices.kMDItemWhiteBalance, str)
        self.assertIsInstance(CoreServices.kMDItemAperture, str)
        self.assertIsInstance(CoreServices.kMDItemProfileName, str)
        self.assertIsInstance(CoreServices.kMDItemResolutionWidthDPI, str)
        self.assertIsInstance(CoreServices.kMDItemResolutionHeightDPI, str)
        self.assertIsInstance(CoreServices.kMDItemExposureMode, str)
        self.assertIsInstance(CoreServices.kMDItemExposureTimeSeconds, str)
        self.assertIsInstance(CoreServices.kMDItemEXIFVersion, str)
        self.assertIsInstance(CoreServices.kMDItemCodecs, str)
        self.assertIsInstance(CoreServices.kMDItemMediaTypes, str)
        self.assertIsInstance(CoreServices.kMDItemStreamable, str)
        self.assertIsInstance(CoreServices.kMDItemTotalBitRate, str)
        self.assertIsInstance(CoreServices.kMDItemVideoBitRate, str)
        self.assertIsInstance(CoreServices.kMDItemAudioBitRate, str)
        self.assertIsInstance(CoreServices.kMDItemDeliveryType, str)
        self.assertIsInstance(CoreServices.kMDItemAlbum, str)
        self.assertIsInstance(CoreServices.kMDItemHasAlphaChannel, str)
        self.assertIsInstance(CoreServices.kMDItemRedEyeOnOff, str)
        self.assertIsInstance(CoreServices.kMDItemMeteringMode, str)
        self.assertIsInstance(CoreServices.kMDItemMaxAperture, str)
        self.assertIsInstance(CoreServices.kMDItemFNumber, str)
        self.assertIsInstance(CoreServices.kMDItemExposureProgram, str)
        self.assertIsInstance(CoreServices.kMDItemExposureTimeString, str)
        self.assertIsInstance(CoreServices.kMDItemHeadline, str)
        self.assertIsInstance(CoreServices.kMDItemInstructions, str)
        self.assertIsInstance(CoreServices.kMDItemCity, str)
        self.assertIsInstance(CoreServices.kMDItemStateOrProvince, str)
        self.assertIsInstance(CoreServices.kMDItemCountry, str)
        self.assertIsInstance(CoreServices.kMDItemFSName, str)
        self.assertIsInstance(CoreServices.kMDItemDisplayName, str)
        self.assertIsInstance(CoreServices.kMDItemPath, str)
        self.assertIsInstance(CoreServices.kMDItemFSSize, str)
        self.assertIsInstance(CoreServices.kMDItemFSCreationDate, str)
        self.assertIsInstance(CoreServices.kMDItemFSContentChangeDate, str)
        self.assertIsInstance(CoreServices.kMDItemFSOwnerUserID, str)
        self.assertIsInstance(CoreServices.kMDItemFSOwnerGroupID, str)
        self.assertIsInstance(CoreServices.kMDItemFSExists, str)
        self.assertIsInstance(CoreServices.kMDItemFSIsReadable, str)
        self.assertIsInstance(CoreServices.kMDItemFSIsWriteable, str)
        self.assertIsInstance(CoreServices.kMDItemFSHasCustomIcon, str)
        self.assertIsInstance(CoreServices.kMDItemFSIsExtensionHidden, str)
        self.assertIsInstance(CoreServices.kMDItemFSIsStationery, str)
        self.assertIsInstance(CoreServices.kMDItemFSInvisible, str)
        self.assertIsInstance(CoreServices.kMDItemFSLabel, str)
        self.assertIsInstance(CoreServices.kMDItemFSNodeCount, str)
        self.assertIsInstance(CoreServices.kMDItemTextContent, str)
        self.assertIsInstance(CoreServices.kMDItemAudioSampleRate, str)
        self.assertIsInstance(CoreServices.kMDItemAudioChannelCount, str)
        self.assertIsInstance(CoreServices.kMDItemTempo, str)
        self.assertIsInstance(CoreServices.kMDItemKeySignature, str)
        self.assertIsInstance(CoreServices.kMDItemTimeSignature, str)
        self.assertIsInstance(CoreServices.kMDItemAudioEncodingApplication, str)
        self.assertIsInstance(CoreServices.kMDItemComposer, str)
        self.assertIsInstance(CoreServices.kMDItemLyricist, str)
        self.assertIsInstance(CoreServices.kMDItemAudioTrackNumber, str)
        self.assertIsInstance(CoreServices.kMDItemRecordingDate, str)
        self.assertIsInstance(CoreServices.kMDItemMusicalGenre, str)
        self.assertIsInstance(CoreServices.kMDItemIsGeneralMIDISequence, str)
        self.assertIsInstance(CoreServices.kMDItemRecordingYear, str)
        self.assertIsInstance(CoreServices.kMDItemOrganizations, str)
        self.assertIsInstance(CoreServices.kMDItemLanguages, str)
        self.assertIsInstance(CoreServices.kMDItemRights, str)
        self.assertIsInstance(CoreServices.kMDItemPublishers, str)
        self.assertIsInstance(CoreServices.kMDItemContributors, str)
        self.assertIsInstance(CoreServices.kMDItemCoverage, str)
        self.assertIsInstance(CoreServices.kMDItemSubject, str)
        self.assertIsInstance(CoreServices.kMDItemTheme, str)
        self.assertIsInstance(CoreServices.kMDItemDescription, str)
        self.assertIsInstance(CoreServices.kMDItemIdentifier, str)
        self.assertIsInstance(CoreServices.kMDItemAudiences, str)
        self.assertIsInstance(CoreServices.kMDItemNumberOfPages, str)
        self.assertIsInstance(CoreServices.kMDItemPageWidth, str)
        self.assertIsInstance(CoreServices.kMDItemPageHeight, str)
        self.assertIsInstance(CoreServices.kMDItemSecurityMethod, str)
        self.assertIsInstance(CoreServices.kMDItemCreator, str)
        self.assertIsInstance(CoreServices.kMDItemEncodingApplications, str)
        self.assertIsInstance(CoreServices.kMDItemDueDate, str)
        self.assertIsInstance(CoreServices.kMDItemStarRating, str)
        self.assertIsInstance(CoreServices.kMDItemPhoneNumbers, str)
        self.assertIsInstance(CoreServices.kMDItemEmailAddresses, str)
        self.assertIsInstance(CoreServices.kMDItemInstantMessageAddresses, str)
        self.assertIsInstance(CoreServices.kMDItemKind, str)
        self.assertIsInstance(CoreServices.kMDItemRecipients, str)
        self.assertIsInstance(CoreServices.kMDItemFinderComment, str)
        self.assertIsInstance(CoreServices.kMDItemFonts, str)
        self.assertIsInstance(CoreServices.kMDItemAppleLoopsRootKey, str)
        self.assertIsInstance(CoreServices.kMDItemAppleLoopsKeyFilterType, str)
        self.assertIsInstance(CoreServices.kMDItemAppleLoopsLoopMode, str)
        self.assertIsInstance(CoreServices.kMDItemAppleLoopDescriptors, str)
        self.assertIsInstance(CoreServices.kMDItemMusicalInstrumentCategory, str)
        self.assertIsInstance(CoreServices.kMDItemMusicalInstrumentName, str)

    @min_os_level("10.5")
    def test_constants10_5(self):
        self.assertIsInstance(CoreServices.kMDItemContentTypeTree, str)
        self.assertIsInstance(CoreServices.kMDItemEditors, str)
        self.assertIsInstance(CoreServices.kMDItemEXIFGPSVersion, str)
        self.assertIsInstance(CoreServices.kMDItemAltitude, str)
        self.assertIsInstance(CoreServices.kMDItemLatitude, str)
        self.assertIsInstance(CoreServices.kMDItemLongitude, str)
        self.assertIsInstance(CoreServices.kMDItemSpeed, str)
        self.assertIsInstance(CoreServices.kMDItemTimestamp, str)
        self.assertIsInstance(CoreServices.kMDItemGPSTrack, str)
        self.assertIsInstance(CoreServices.kMDItemImageDirection, str)
        self.assertIsInstance(CoreServices.kMDItemCFBundleIdentifier, str)
        self.assertIsInstance(CoreServices.kMDItemSupportFileType, str)
        self.assertIsInstance(CoreServices.kMDItemInformation, str)
        self.assertIsInstance(CoreServices.kMDItemDirector, str)
        self.assertIsInstance(CoreServices.kMDItemProducer, str)
        self.assertIsInstance(CoreServices.kMDItemGenre, str)
        self.assertIsInstance(CoreServices.kMDItemPerformers, str)
        self.assertIsInstance(CoreServices.kMDItemOriginalFormat, str)
        self.assertIsInstance(CoreServices.kMDItemOriginalSource, str)
        self.assertIsInstance(CoreServices.kMDItemAuthorEmailAddresses, str)
        self.assertIsInstance(CoreServices.kMDItemRecipientEmailAddresses, str)
        self.assertIsInstance(CoreServices.kMDItemURL, str)

    @min_os_level("10.6")
    def test_constants10_6(self):
        self.assertIsInstance(CoreServices.kMDItemParticipants, str)
        self.assertIsInstance(CoreServices.kMDItemPixelCount, str)
        self.assertIsInstance(CoreServices.kMDItemNamedLocation, str)
        self.assertIsInstance(CoreServices.kMDItemAuthorAddresses, str)
        self.assertIsInstance(CoreServices.kMDItemRecipientAddresses, str)

    @min_os_level("10.7")
    def test_constants10_7(self):
        self.assertIsInstance(CoreServices.kMDItemDownloadedDate, str)
        self.assertIsInstance(CoreServices.kMDItemDateAdded, str)
        self.assertIsInstance(CoreServices.kMDItemCameraOwner, str)
        self.assertIsInstance(CoreServices.kMDItemFocalLength35mm, str)
        self.assertIsInstance(CoreServices.kMDItemLensModel, str)
        self.assertIsInstance(CoreServices.kMDItemGPSStatus, str)
        self.assertIsInstance(CoreServices.kMDItemGPSMeasureMode, str)
        self.assertIsInstance(CoreServices.kMDItemGPSDOP, str)
        self.assertIsInstance(CoreServices.kMDItemGPSMapDatum, str)
        self.assertIsInstance(CoreServices.kMDItemGPSDestLatitude, str)
        self.assertIsInstance(CoreServices.kMDItemGPSDestLongitude, str)
        self.assertIsInstance(CoreServices.kMDItemGPSDestBearing, str)
        self.assertIsInstance(CoreServices.kMDItemGPSDestDistance, str)
        self.assertIsInstance(CoreServices.kMDItemGPSProcessingMethod, str)
        self.assertIsInstance(CoreServices.kMDItemGPSAreaInformation, str)
        self.assertIsInstance(CoreServices.kMDItemGPSDateStamp, str)
        self.assertIsInstance(CoreServices.kMDItemGPSDifferental, str)
        self.assertIsInstance(CoreServices.kMDItemLabelIcon, str)
        self.assertIsInstance(CoreServices.kMDItemLabelID, str)
        self.assertIsInstance(CoreServices.kMDItemLabelKind, str)
        self.assertIsInstance(CoreServices.kMDItemLabelUUID, str)
        self.assertIsInstance(CoreServices.kMDItemIsLikelyJunk, str)
        self.assertIsInstance(CoreServices.kMDItemExecutableArchitectures, str)
        self.assertIsInstance(CoreServices.kMDItemExecutablePlatform, str)
        self.assertIsInstance(CoreServices.kMDItemApplicationCategories, str)
        self.assertIsInstance(CoreServices.kMDItemIsApplicationManaged, str)

    @min_os_level("10.11")
    def test_constants10_11(self):
        self.assertIsInstance(CoreServices.kMDItemHTMLContent, str)

    @min_os_level("15.0")
    def test_constants15_0(self):
        self.assertIsInstance(CoreServices.kMDItemXMPCredit, str)
        self.assertIsInstance(CoreServices.kMDItemXMPDigitalSourceType, str)
        self.assertIsInstance(CoreServices.kMDItemMediaExtensions, str)
