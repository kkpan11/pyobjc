# This file is generated by objective.metadata
#
# Last update: Sun Mar  2 11:17:27 2025
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
misc.update(
    {
        "VTInt32Point": objc.createStructType(
            "VideoToolbox.VTInt32Point", b"{VTInt32Point=ii}", ["x", "y"]
        ),
        "VTInt32Size": objc.createStructType(
            "VideoToolbox.VTInt32Size", b"{VTInt32Size=ii}", ["width", "height"]
        ),
    }
)
constants = """$VTFrameProcessorErrorDomain$kVTAlphaChannelMode_PremultipliedAlpha$kVTAlphaChannelMode_StraightAlpha$kVTCompressionPropertyKey_AllowFrameReordering$kVTCompressionPropertyKey_AllowOpenGOP$kVTCompressionPropertyKey_AllowTemporalCompression$kVTCompressionPropertyKey_AlphaChannelMode$kVTCompressionPropertyKey_AspectRatio16x9$kVTCompressionPropertyKey_AverageBitRate$kVTCompressionPropertyKey_BaseLayerBitRateFraction$kVTCompressionPropertyKey_BaseLayerFrameRate$kVTCompressionPropertyKey_BaseLayerFrameRateFraction$kVTCompressionPropertyKey_CalculateMeanSquaredError$kVTCompressionPropertyKey_CleanAperture$kVTCompressionPropertyKey_ColorPrimaries$kVTCompressionPropertyKey_ConstantBitRate$kVTCompressionPropertyKey_ContentLightLevelInfo$kVTCompressionPropertyKey_DataRateLimits$kVTCompressionPropertyKey_Depth$kVTCompressionPropertyKey_EnableLTR$kVTCompressionPropertyKey_EncoderID$kVTCompressionPropertyKey_EstimatedAverageBytesPerFrame$kVTCompressionPropertyKey_ExpectedDuration$kVTCompressionPropertyKey_ExpectedFrameRate$kVTCompressionPropertyKey_FieldCount$kVTCompressionPropertyKey_FieldDetail$kVTCompressionPropertyKey_GammaLevel$kVTCompressionPropertyKey_H264EntropyMode$kVTCompressionPropertyKey_HDRMetadataInsertionMode$kVTCompressionPropertyKey_HasLeftStereoEyeView$kVTCompressionPropertyKey_HasRightStereoEyeView$kVTCompressionPropertyKey_HeroEye$kVTCompressionPropertyKey_HorizontalDisparityAdjustment$kVTCompressionPropertyKey_HorizontalFieldOfView$kVTCompressionPropertyKey_ICCProfile$kVTCompressionPropertyKey_MVHEVCLeftAndRightViewIDs$kVTCompressionPropertyKey_MVHEVCVideoLayerIDs$kVTCompressionPropertyKey_MVHEVCViewIDs$kVTCompressionPropertyKey_MasteringDisplayColorVolume$kVTCompressionPropertyKey_MaxAllowedFrameQP$kVTCompressionPropertyKey_MaxFrameDelayCount$kVTCompressionPropertyKey_MaxH264SliceBytes$kVTCompressionPropertyKey_MaxKeyFrameInterval$kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration$kVTCompressionPropertyKey_MaximizePowerEfficiency$kVTCompressionPropertyKey_MaximumRealTimeFrameRate$kVTCompressionPropertyKey_MinAllowedFrameQP$kVTCompressionPropertyKey_MoreFramesAfterEnd$kVTCompressionPropertyKey_MoreFramesBeforeStart$kVTCompressionPropertyKey_MultiPassStorage$kVTCompressionPropertyKey_NumberOfPendingFrames$kVTCompressionPropertyKey_OutputBitDepth$kVTCompressionPropertyKey_PixelAspectRatio$kVTCompressionPropertyKey_PixelBufferPoolIsShared$kVTCompressionPropertyKey_PixelTransferProperties$kVTCompressionPropertyKey_PreserveAlphaChannel$kVTCompressionPropertyKey_PreserveDynamicHDRMetadata$kVTCompressionPropertyKey_PrioritizeEncodingSpeedOverQuality$kVTCompressionPropertyKey_ProfileLevel$kVTCompressionPropertyKey_ProgressiveScan$kVTCompressionPropertyKey_ProjectionKind$kVTCompressionPropertyKey_Quality$kVTCompressionPropertyKey_RealTime$kVTCompressionPropertyKey_RecommendedParallelizationLimit$kVTCompressionPropertyKey_RecommendedParallelizedSubdivisionMinimumDuration$kVTCompressionPropertyKey_RecommendedParallelizedSubdivisionMinimumFrameCount$kVTCompressionPropertyKey_ReferenceBufferCount$kVTCompressionPropertyKey_SourceFrameCount$kVTCompressionPropertyKey_SpatialAdaptiveQPLevel$kVTCompressionPropertyKey_StereoCameraBaseline$kVTCompressionPropertyKey_SuggestedLookAheadFrameCount$kVTCompressionPropertyKey_SupportsBaseFrameQP$kVTCompressionPropertyKey_TargetQualityForAlpha$kVTCompressionPropertyKey_TransferFunction$kVTCompressionPropertyKey_UsingGPURegistryID$kVTCompressionPropertyKey_UsingHardwareAcceleratedVideoEncoder$kVTCompressionPropertyKey_VideoEncoderPixelBufferAttributes$kVTCompressionPropertyKey_ViewPackingKind$kVTCompressionPropertyKey_YCbCrMatrix$kVTDecompressionPropertyKey_AllowBitstreamToChangeFrameDimensions$kVTDecompressionPropertyKey_ContentHasInterframeDependencies$kVTDecompressionPropertyKey_DecoderProducesRAWOutput$kVTDecompressionPropertyKey_DeinterlaceMode$kVTDecompressionPropertyKey_FieldMode$kVTDecompressionPropertyKey_GeneratePerFrameHDRDisplayMetadata$kVTDecompressionPropertyKey_MaxOutputPresentationTimeStampOfFramesBeingDecoded$kVTDecompressionPropertyKey_MaximizePowerEfficiency$kVTDecompressionPropertyKey_MinOutputPresentationTimeStampOfFramesBeingDecoded$kVTDecompressionPropertyKey_NumberOfFramesBeingDecoded$kVTDecompressionPropertyKey_OnlyTheseFrames$kVTDecompressionPropertyKey_OutputPoolRequestedMinimumBufferCount$kVTDecompressionPropertyKey_PixelBufferPool$kVTDecompressionPropertyKey_PixelBufferPoolIsShared$kVTDecompressionPropertyKey_PixelFormatsWithReducedResolutionSupport$kVTDecompressionPropertyKey_PixelTransferProperties$kVTDecompressionPropertyKey_PropagatePerFrameHDRDisplayMetadata$kVTDecompressionPropertyKey_RealTime$kVTDecompressionPropertyKey_ReducedCoefficientDecode$kVTDecompressionPropertyKey_ReducedFrameDelivery$kVTDecompressionPropertyKey_ReducedResolutionDecode$kVTDecompressionPropertyKey_RequestRAWOutput$kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs$kVTDecompressionPropertyKey_SuggestedQualityOfServiceTiers$kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByPerformance$kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByQuality$kVTDecompressionPropertyKey_ThreadCount$kVTDecompressionPropertyKey_UsingGPURegistryID$kVTDecompressionPropertyKey_UsingHardwareAcceleratedVideoDecoder$kVTDecompressionProperty_DeinterlaceMode_Temporal$kVTDecompressionProperty_DeinterlaceMode_VerticalFilter$kVTDecompressionProperty_FieldMode_BothFields$kVTDecompressionProperty_FieldMode_BottomFieldOnly$kVTDecompressionProperty_FieldMode_DeinterlaceFields$kVTDecompressionProperty_FieldMode_SingleField$kVTDecompressionProperty_FieldMode_TopFieldOnly$kVTDecompressionProperty_OnlyTheseFrames_AllFrames$kVTDecompressionProperty_OnlyTheseFrames_IFrames$kVTDecompressionProperty_OnlyTheseFrames_KeyFrames$kVTDecompressionProperty_OnlyTheseFrames_NonDroppableFrames$kVTDecompressionProperty_TemporalLevelLimit$kVTDecompressionResolutionKey_Height$kVTDecompressionResolutionKey_Width$kVTDownsamplingMode_Average$kVTDownsamplingMode_Decimate$kVTEncodeFrameOptionKey_AcknowledgedLTRTokens$kVTEncodeFrameOptionKey_BaseFrameQP$kVTEncodeFrameOptionKey_ForceKeyFrame$kVTEncodeFrameOptionKey_ForceLTRRefresh$kVTExtensionProperties_CodecNameKey$kVTExtensionProperties_ContainingBundleNameKey$kVTExtensionProperties_ContainingBundleURLKey$kVTExtensionProperties_ExtensionIdentifierKey$kVTExtensionProperties_ExtensionNameKey$kVTExtensionProperties_ExtensionURLKey$kVTH264EntropyMode_CABAC$kVTH264EntropyMode_CAVLC$kVTHDRMetadataInsertionMode_Auto$kVTHDRMetadataInsertionMode_None$kVTHDRPerFrameMetadataGenerationHDRFormatType_DolbyVision$kVTHDRPerFrameMetadataGenerationOptionsKey_HDRFormats$kVTMultiPassStorageCreationOption_DoNotDelete$kVTPixelRotationPropertyKey_FlipHorizontalOrientation$kVTPixelRotationPropertyKey_FlipVerticalOrientation$kVTPixelRotationPropertyKey_Rotation$kVTPixelTransferPropertyKey_DestinationCleanAperture$kVTPixelTransferPropertyKey_DestinationColorPrimaries$kVTPixelTransferPropertyKey_DestinationICCProfile$kVTPixelTransferPropertyKey_DestinationPixelAspectRatio$kVTPixelTransferPropertyKey_DestinationTransferFunction$kVTPixelTransferPropertyKey_DestinationYCbCrMatrix$kVTPixelTransferPropertyKey_DownsamplingMode$kVTPixelTransferPropertyKey_RealTime$kVTPixelTransferPropertyKey_ScalingMode$kVTProfileLevel_H263_Profile0_Level10$kVTProfileLevel_H263_Profile0_Level45$kVTProfileLevel_H263_Profile3_Level45$kVTProfileLevel_H264_Baseline_1_3$kVTProfileLevel_H264_Baseline_3_0$kVTProfileLevel_H264_Baseline_3_1$kVTProfileLevel_H264_Baseline_3_2$kVTProfileLevel_H264_Baseline_4_0$kVTProfileLevel_H264_Baseline_4_1$kVTProfileLevel_H264_Baseline_4_2$kVTProfileLevel_H264_Baseline_5_0$kVTProfileLevel_H264_Baseline_5_1$kVTProfileLevel_H264_Baseline_5_2$kVTProfileLevel_H264_Baseline_AutoLevel$kVTProfileLevel_H264_ConstrainedBaseline_AutoLevel$kVTProfileLevel_H264_ConstrainedHigh_AutoLevel$kVTProfileLevel_H264_Extended_5_0$kVTProfileLevel_H264_Extended_AutoLevel$kVTProfileLevel_H264_High_3_0$kVTProfileLevel_H264_High_3_1$kVTProfileLevel_H264_High_3_2$kVTProfileLevel_H264_High_4_0$kVTProfileLevel_H264_High_4_1$kVTProfileLevel_H264_High_4_2$kVTProfileLevel_H264_High_5_0$kVTProfileLevel_H264_High_5_1$kVTProfileLevel_H264_High_5_2$kVTProfileLevel_H264_High_AutoLevel$kVTProfileLevel_H264_Main_3_0$kVTProfileLevel_H264_Main_3_1$kVTProfileLevel_H264_Main_3_2$kVTProfileLevel_H264_Main_4_0$kVTProfileLevel_H264_Main_4_1$kVTProfileLevel_H264_Main_4_2$kVTProfileLevel_H264_Main_5_0$kVTProfileLevel_H264_Main_5_1$kVTProfileLevel_H264_Main_5_2$kVTProfileLevel_H264_Main_AutoLevel$kVTProfileLevel_HEVC_Main10_AutoLevel$kVTProfileLevel_HEVC_Main42210_AutoLevel$kVTProfileLevel_HEVC_Main_AutoLevel$kVTProfileLevel_HEVC_Monochrome10_AutoLevel$kVTProfileLevel_HEVC_Monochrome_AutoLevel$kVTProfileLevel_MP4V_AdvancedSimple_L0$kVTProfileLevel_MP4V_AdvancedSimple_L1$kVTProfileLevel_MP4V_AdvancedSimple_L2$kVTProfileLevel_MP4V_AdvancedSimple_L3$kVTProfileLevel_MP4V_AdvancedSimple_L4$kVTProfileLevel_MP4V_Main_L2$kVTProfileLevel_MP4V_Main_L3$kVTProfileLevel_MP4V_Main_L4$kVTProfileLevel_MP4V_Simple_L0$kVTProfileLevel_MP4V_Simple_L1$kVTProfileLevel_MP4V_Simple_L2$kVTProfileLevel_MP4V_Simple_L3$kVTPropertyDocumentationKey$kVTPropertyReadWriteStatusKey$kVTPropertyReadWriteStatus_ReadOnly$kVTPropertyReadWriteStatus_ReadWrite$kVTPropertyShouldBeSerializedKey$kVTPropertySupportedValueListKey$kVTPropertySupportedValueMaximumKey$kVTPropertySupportedValueMinimumKey$kVTPropertyTypeKey$kVTPropertyType_Boolean$kVTPropertyType_Enumeration$kVTPropertyType_Number$kVTRAWProcessingParameterListElement_Description$kVTRAWProcessingParameterListElement_Label$kVTRAWProcessingParameterListElement_ListElementID$kVTRAWProcessingParameterValueType_Boolean$kVTRAWProcessingParameterValueType_Float$kVTRAWProcessingParameterValueType_Integer$kVTRAWProcessingParameterValueType_List$kVTRAWProcessingParameterValueType_SubGroup$kVTRAWProcessingParameter_CameraValue$kVTRAWProcessingParameter_CurrentValue$kVTRAWProcessingParameter_Description$kVTRAWProcessingParameter_Enabled$kVTRAWProcessingParameter_InitialValue$kVTRAWProcessingParameter_Key$kVTRAWProcessingParameter_ListArray$kVTRAWProcessingParameter_MaximumValue$kVTRAWProcessingParameter_MinimumValue$kVTRAWProcessingParameter_Name$kVTRAWProcessingParameter_NeutralValue$kVTRAWProcessingParameter_SubGroup$kVTRAWProcessingParameter_ValueType$kVTRAWProcessingPropertyKey_MetalDeviceRegistryID$kVTRAWProcessingPropertyKey_OutputColorAttachments$kVTRotation_0$kVTRotation_180$kVTRotation_CCW90$kVTRotation_CW90$kVTSampleAttachmentKey_QualityMetrics$kVTSampleAttachmentKey_RequireLTRAcknowledgementToken$kVTSampleAttachmentQualityMetricsKey_ChromaBlueMeanSquaredError$kVTSampleAttachmentQualityMetricsKey_ChromaRedMeanSquaredError$kVTSampleAttachmentQualityMetricsKey_LumaMeanSquaredError$kVTScalingMode_CropSourceToCleanAperture$kVTScalingMode_Letterbox$kVTScalingMode_Normal$kVTScalingMode_Trim$kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder$kVTVideoDecoderSpecification_PreferredDecoderGPURegistryID$kVTVideoDecoderSpecification_RequireHardwareAcceleratedVideoDecoder$kVTVideoDecoderSpecification_RequiredDecoderGPURegistryID$kVTVideoEncoderListOption_IncludeStandardDefinitionDVEncoders$kVTVideoEncoderList_CodecName$kVTVideoEncoderList_CodecType$kVTVideoEncoderList_DisplayName$kVTVideoEncoderList_EncoderID$kVTVideoEncoderList_EncoderName$kVTVideoEncoderList_GPURegistryID$kVTVideoEncoderList_InstanceLimit$kVTVideoEncoderList_IsHardwareAccelerated$kVTVideoEncoderList_PerformanceRating$kVTVideoEncoderList_QualityRating$kVTVideoEncoderList_SupportedSelectionProperties$kVTVideoEncoderList_SupportsFrameReordering$kVTVideoEncoderList_SupportsMultiPass$kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder$kVTVideoEncoderSpecification_EnableLowLatencyRateControl$kVTVideoEncoderSpecification_EncoderID$kVTVideoEncoderSpecification_PreferredEncoderGPURegistryID$kVTVideoEncoderSpecification_RequireHardwareAcceleratedVideoEncoder$kVTVideoEncoderSpecification_RequiredEncoderGPURegistryID$"""
enums = """$VTFrameProcessorFatalError@-19734$VTFrameProcessorInitializationFailed@-19736$VTFrameProcessorInvalidFrameTiming@-19742$VTFrameProcessorInvalidParameterError@-19741$VTFrameProcessorMemoryAllocationFailure@-19738$VTFrameProcessorProcessingError@-19740$VTFrameProcessorRevisionNotSupported@-19739$VTFrameProcessorSessionAlreadyActive@-19733$VTFrameProcessorSessionLevelError@-19735$VTFrameProcessorSessionNotStarted@-19732$VTFrameProcessorUnknownError@-19730$VTFrameProcessorUnsupportedInput@-19737$VTFrameProcessorUnsupportedResolution@-19731$VTFrameRateConversionConfigurationQualityPrioritizationNormal@1$VTFrameRateConversionConfigurationQualityPrioritizationQuality@2$VTFrameRateConversionConfigurationRevision1@1$VTFrameRateConversionParametersSubmissionModeRandom@1$VTFrameRateConversionParametersSubmissionModeSequential@2$VTMotionBlurConfigurationQualityPrioritizationNormal@1$VTMotionBlurConfigurationQualityPrioritizationQuality@2$VTMotionBlurConfigurationRevision1@1$VTMotionBlurParametersSubmissionModeRandom@1$VTMotionBlurParametersSubmissionModeSequential@2$VTOpticalFlowConfigurationQualityPrioritizationNormal@1$VTOpticalFlowConfigurationQualityPrioritizationQuality@2$VTOpticalFlowConfigurationRevision1@1$VTOpticalFlowParametersSubmissionModeRandom@1$VTOpticalFlowParametersSubmissionModeSequential@2$kVTAllocationFailedErr@-12904$kVTColorCorrectionImageRotationFailedErr@-12219$kVTColorCorrectionPixelTransferFailedErr@-12212$kVTColorSyncTransformConvertFailedErr@-12919$kVTCompressionSessionBeginFinalPass@1$kVTCouldNotCreateColorCorrectionDataErr@-12918$kVTCouldNotCreateInstanceErr@-12907$kVTCouldNotFindExtensionErr@-19510$kVTCouldNotFindTemporalFilterErr@-12217$kVTCouldNotFindVideoDecoderErr@-12906$kVTCouldNotFindVideoEncoderErr@-12908$kVTCouldNotOutputTaggedBufferGroupErr@-17699$kVTDecodeFrame_1xRealTimePlayback@4$kVTDecodeFrame_DoNotOutputFrame@2$kVTDecodeFrame_EnableAsynchronousDecompression@1$kVTDecodeFrame_EnableTemporalProcessing@8$kVTDecodeInfo_Asynchronous@1$kVTDecodeInfo_FrameDropped@2$kVTDecodeInfo_ImageBufferModifiable@4$kVTDecodeInfo_SkippedLeadingFrameDropped@8$kVTEncodeInfo_Asynchronous@1$kVTEncodeInfo_FrameDropped@2$kVTExtensionConflictErr@-19511$kVTExtensionDisabledErr@-17697$kVTFormatDescriptionChangeNotSupportedErr@-12916$kVTFrameSiloInvalidTimeRangeErr@-12216$kVTFrameSiloInvalidTimeStampErr@-12215$kVTImageRotationNotSupportedErr@-12914$kVTInsufficientSourceColorDataErr@-12917$kVTInvalidSessionErr@-12903$kVTMultiPassStorageIdentifierMismatchErr@-12213$kVTMultiPassStorageInvalidErr@-12214$kVTParameterErr@-12902$kVTPixelRotationNotSupportedErr@-12914$kVTPixelTransferNotPermittedErr@-12218$kVTPixelTransferNotSupportedErr@-12905$kVTPropertyNotSupportedErr@-12900$kVTPropertyReadOnlyErr@-12901$kVTQPModulationLevel_Default@-1$kVTQPModulationLevel_Disable@0$kVTSessionMalfunctionErr@-17691$kVTUnlimitedFrameDelayCount@-1$kVTVideoDecoderAuthorizationErr@-12210$kVTVideoDecoderBadDataErr@-12909$kVTVideoDecoderCallbackMessagingErr@-17695$kVTVideoDecoderMalfunctionErr@-12911$kVTVideoDecoderNeedsRosettaErr@-17692$kVTVideoDecoderNotAvailableNowErr@-12913$kVTVideoDecoderReferenceMissingErr@-17694$kVTVideoDecoderRemovedErr@-17690$kVTVideoDecoderUnknownErr@-17696$kVTVideoDecoderUnsupportedDataFormatErr@-12910$kVTVideoEncoderAuthorizationErr@-12211$kVTVideoEncoderMVHEVCVideoLayerIDsMismatchErr@-17698$kVTVideoEncoderMalfunctionErr@-12912$kVTVideoEncoderNeedsRosettaErr@-17693$kVTVideoEncoderNotAvailableNowErr@-12915$"""
misc.update(
    {
        "VTOpticalFlowConfigurationQualityPrioritization": NewType(
            "VTOpticalFlowConfigurationQualityPrioritization", int
        ),
        "VTFrameRateConversionConfigurationRevision": NewType(
            "VTFrameRateConversionConfigurationRevision", int
        ),
        "VTOpticalFlowParametersSubmissionMode": NewType(
            "VTOpticalFlowParametersSubmissionMode", int
        ),
        "VTMotionBlurConfigurationRevision": NewType(
            "VTMotionBlurConfigurationRevision", int
        ),
        "VTDecodeInfoFlags": NewType("VTDecodeInfoFlags", int),
        "VTMotionBlurConfigurationQualityPrioritization": NewType(
            "VTMotionBlurConfigurationQualityPrioritization", int
        ),
        "VTFrameRateConversionParametersSubmissionMode": NewType(
            "VTFrameRateConversionParametersSubmissionMode", int
        ),
        "VTFrameRateConversionConfigurationQualityPrioritization": NewType(
            "VTFrameRateConversionConfigurationQualityPrioritization", int
        ),
        "VTMotionBlurParametersSubmissionMode": NewType(
            "VTMotionBlurParametersSubmissionMode", int
        ),
        "VTCompressionSessionOptionFlags": NewType(
            "VTCompressionSessionOptionFlags", int
        ),
        "VTOpticalFlowConfigurationRevision": NewType(
            "VTOpticalFlowConfigurationRevision", int
        ),
        "VTDecodeFrameFlags": NewType("VTDecodeFrameFlags", int),
        "VTEncodeInfoFlags": NewType("VTEncodeInfoFlags", int),
        "VTFrameProcessorError": NewType("VTFrameProcessorError", int),
    }
)
misc.update(
    {
        "VTHDRPerFrameMetadataGenerationHDRFormatType": NewType(
            "VTHDRPerFrameMetadataGenerationHDRFormatType", str
        ),
        "VTExtensionPropertiesKey": NewType("VTExtensionPropertiesKey", str),
    }
)
misc.update({})
functions = {
    "VTPixelTransferSessionCreate": (
        b"i^{__CFAllocator=}^^{OpaqueVTPixelTransferSession=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "VTCreateCGImageFromCVPixelBuffer": (
        b"i^{__CVBuffer=}^{__CFDictionary=}^^{CGImage=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "VTCompressionSessionEndPass": (
        b"i^{OpaqueVTCompressionSession=}^Z^I",
        "",
        {"arguments": {1: {"type_modifier": "o"}, 2: {"type_modifier": "o"}}},
    ),
    "VTDecompressionSessionFinishDelayedFrames": (
        b"i^{OpaqueVTDecompressionSession=}",
    ),
    "VTSessionCopySupportedPropertyDictionary": (
        b"i@^^{__CFDictionary=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "VTPixelRotationSessionCreate": (
        b"i^{__CFAllocator=}^^{OpaqueVTPixelRotationSession=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "VTHDRPerFrameMetadataGenerationSessionGetTypeID": (b"Q",),
    "VTCompressionSessionEncodeMultiImageFrameWithOutputHandler": (
        b"i^{OpaqueVTCompressionSession=}^{OpaqueCMTaggedBufferGroup=}{CMTime=qiIq}{CMTime=qiIq}^{__CFDictionary=}^I@?",
        "",
        {
            "arguments": {
                5: {"type_modifier": "o"},
                6: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"type": "i"},
                            2: {"type": "Q"},
                            3: {"type": "^{opaqueCMSampleBuffer=}"},
                        },
                    }
                },
            }
        },
    ),
    "VTSessionSetProperty": (b"i@^{__CFString=}@",),
    "VTPixelTransferSessionTransferImage": (
        b"i^{OpaqueVTPixelTransferSession=}^{__CVBuffer=}^{__CVBuffer=}",
    ),
    "VTDecompressionSessionSetMultiImageCallback": (
        b"i^{OpaqueVTDecompressionSession=}^?^v",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"^v"},
                            2: {"type": b"i"},
                            3: {"type": b"Q"},
                            4: {"type": b"^{OpaqueCMTaggedBufferGroup=}"},
                            5: {"type": b"{CMTime=qiIq}"},
                            6: {"type": b"{CMTime=qiIq}"},
                        },
                    },
                    "callable_retained": True,
                }
            }
        },
    ),
    "VTMultiPassStorageClose": (b"i^{OpaqueVTMultiPassStorage=}",),
    "VTIsHardwareDecodeSupported": (b"ZI",),
    "VTCompressionSessionPrepareToEncodeFrames": (b"i^{OpaqueVTCompressionSession=}",),
    "VTCompressionSessionInvalidate": (b"v^{OpaqueVTCompressionSession=}",),
    "VTRAWProcessingSessionSetParameterChangedHander": (
        b"i^{OpaqueVTRAWProcessingSession=}@?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}, 1: {"type": "@"}},
                    }
                }
            }
        },
    ),
    "VTPixelRotationSessionGetTypeID": (b"Q",),
    "VTCompressionSessionCompleteFrames": (
        b"i^{OpaqueVTCompressionSession=}{CMTime=qiIq}",
    ),
    "VTDecompressionSessionDecodeFrameWithMultiImageCapableOutputHandler": (
        b"i^{OpaqueVTDecompressionSession=}^{opaqueCMSampleBuffer=}I^I@?",
        "",
        {
            "arguments": {
                3: {"already_cfretained": True, "type_modifier": "o"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"type": "i"},
                            2: {"type": "Q"},
                            3: {"type": "^{__CVBuffer=}"},
                            4: {"type": "^{OpaqueCMTaggedBufferGroup=}"},
                            5: {"type": "{CMTime=qiIq}"},
                            6: {"type": "{CMTime=qiIq}"},
                        },
                    }
                },
            }
        },
    ),
    "VTSessionCopyProperty": (
        b"i@^{__CFString=}^{__CFAllocator=}^@",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {3: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "VTCopyRAWProcessorExtensionProperties": (
        b"i^{opaqueCMFormatDescription=}^^{__CFDictionary=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "VTCompressionSessionBeginPass": (
        b"i^{OpaqueVTCompressionSession=}I^I",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "VTRegisterProfessionalVideoWorkflowVideoDecoders": (b"v",),
    "VTRAWProcessingSessionProcessFrame": (
        b"i^{OpaqueVTRAWProcessingSession=}^{__CVBuffer=}^{__CFDictionary=}@?",
        "",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"type": "i"},
                            2: {"type": "@"},
                        },
                    }
                }
            }
        },
    ),
    "VTDecompressionSessionDecodeFrame": (
        b"i^{OpaqueVTDecompressionSession=}^{opaqueCMSampleBuffer=}I^v^I",
        "",
        {"arguments": {4: {"type_modifier": "o"}}},
    ),
    "VTRegisterProfessionalVideoWorkflowVideoEncoders": (b"v",),
    "VTCompressionSessionEncodeMultiImageFrame": (
        b"i^{OpaqueVTCompressionSession=}^{OpaqueCMTaggedBufferGroup=}{CMTime=qiIq}{CMTime=qiIq}^{__CFDictionary=}^v^I",
        "",
        {"arguments": {6: {"type_modifier": "o"}}},
    ),
    "VTRAWProcessingSessionCompleteFrames": (b"i^{OpaqueVTRAWProcessingSession=}",),
    "VTCompressionSessionEncodeFrameWithOutputHandler": (
        b"i^{OpaqueVTCompressionSession=}^{__CVBuffer=}{CMTime=qiIq}{CMTime=qiIq}^{__CFDictionary=}^I@?",
        "",
        {
            "arguments": {
                5: {"type_modifier": "o"},
                6: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"type": "i"},
                            2: {"type": "Q"},
                            3: {"type": "^{opaqueCMSampleBuffer=}"},
                        },
                    }
                },
            }
        },
    ),
    "VTPixelTransferSessionGetTypeID": (b"Q",),
    "VTFrameSiloAddSampleBuffer": (b"i^{OpaqueVTFrameSilo=}^{opaqueCMSampleBuffer=}",),
    "VTCopySupportedPropertyDictionaryForEncoder": (
        b"iiiI^{__CFDictionary=}^^{__CFString=}^^{__CFDictionary=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                4: {"already_cfretained": True, "type_modifier": "o"},
                5: {"already_cfretained": True, "type_modifier": "o"},
            },
        },
    ),
    "VTHDRPerFrameMetadataGenerationSessionCreate": (
        b"i^{__CFAllocator=}f^{__CFDictionary=}^^{OpaqueVTHDRPerFrameMetadataGenerationSession=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {3: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "VTPixelRotationSessionRotateImage": (
        b"i^{OpaqueVTPixelRotationSession=}^{__CVBuffer=}^{__CVBuffer=}",
    ),
    "VTCompressionSessionGetPixelBufferPool": (
        b"^{__CVPixelBufferPool=}^{OpaqueVTCompressionSession=}",
    ),
    "VTRegisterSupplementalVideoDecoderIfAvailable": (b"vI",),
    "VTFrameSiloCallFunctionForEachSampleBuffer": (
        b"i^{OpaqueVTFrameSilo=}{CMTimeRange={CMTime=qiIq}{CMTime=qiIq}}^v^?",
        "",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"i"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"^{opaqueCMSampleBuffer=}"},
                        },
                    },
                    "callable_retained": False,
                }
            }
        },
    ),
    "VTMultiPassStorageGetTypeID": (b"Q",),
    "VTDecompressionSessionCopyBlackPixelBuffer": (
        b"i^{OpaqueVTDecompressionSession=}^^{__CVBuffer=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "VTRAWProcessingSessionCreate": (
        b"i^{__CFAllocator=}^{opaqueCMFormatDescription=}^{__CFDictionary=}^{__CFDictionary=}^^{OpaqueVTRAWProcessingSession=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {4: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "VTRAWProcessingSessionGetTypeID": (b"Q",),
    "VTDecompressionSessionCanAcceptFormatDescription": (
        b"Z^{OpaqueVTDecompressionSession=}^{opaqueCMFormatDescription=}",
    ),
    "VTCopyVideoEncoderList": (
        b"i^{__CFDictionary=}^^{__CFArray=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "VTMultiPassStorageCreate": (
        b"i^{__CFAllocator=}^{__CFURL=}{CMTimeRange={CMTime=qiIq}{CMTime=qiIq}}^{__CFDictionary=}^^{OpaqueVTMultiPassStorage=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {4: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "VTDecompressionSessionGetTypeID": (b"Q",),
    "VTSessionSetProperties": (b"i@^{__CFDictionary=}",),
    "VTDecompressionSessionWaitForAsynchronousFrames": (
        b"i^{OpaqueVTDecompressionSession=}",
    ),
    "VTFrameSiloSetTimeRangesForNextPass": (
        b"i^{OpaqueVTFrameSilo=}q^{CMTimeRange={CMTime=qiIq}{CMTime=qiIq}}",
        "",
        {"arguments": {2: {"c_array_length_in_arg": 1, "type_modifier": "n"}}},
    ),
    "VTHDRPerFrameMetadataGenerationSessionAttachMetadata": (
        b"i^{OpaqueVTHDRPerFrameMetadataGenerationSession=}^{__CVBuffer=}Z",
    ),
    "VTPixelRotationSessionInvalidate": (b"v^{OpaqueVTPixelRotationSession=}",),
    "VTFrameSiloCallBlockForEachSampleBuffer": (
        b"i^{OpaqueVTFrameSilo=}{CMTimeRange={CMTime=qiIq}{CMTime=qiIq}}@?",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"i"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"^{opaqueCMSampleBuffer=}"},
                        },
                    }
                }
            }
        },
    ),
    "VTPixelTransferSessionInvalidate": (b"v^{OpaqueVTPixelTransferSession=}",),
    "VTRAWProcessingSessionCopyProcessingParameters": (
        b"i^{OpaqueVTRAWProcessingSession=}^^{__CFArray=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "VTDecompressionSessionDecodeFrameWithOutputHandler": (
        b"i^{OpaqueVTDecompressionSession=}^{opaqueCMSampleBuffer=}I^I@?",
        "",
        {
            "arguments": {
                3: {"type_modifier": "o"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"type": "i"},
                            2: {"type": "I"},
                            3: {"type": "^{__CVBuffer=}"},
                            4: {"type": "{CMTime=qiIq}"},
                            5: {"type": "{CMTime=qiIq}"},
                        },
                    }
                },
            }
        },
    ),
    "VTCopyVideoDecoderExtensionProperties": (
        b"i^{opaqueCMFormatDescription=}^^{__CFDictionary=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "VTRAWProcessingSessionInvalidate": (b"v^{OpaqueVTRAWProcessingSession=}",),
    "VTCompressionSessionEncodeFrame": (
        b"i^{OpaqueVTCompressionSession=}^{__CVBuffer=}{CMTime=qiIq}{CMTime=qiIq}^{__CFDictionary=}^v^I",
        "",
        {"arguments": {6: {"type_modifier": "o"}}},
    ),
    "VTFrameSiloCreate": (
        b"i^{__CFAllocator=}^{__CFURL=}{CMTimeRange={CMTime=qiIq}{CMTime=qiIq}}^{__CFDictionary=}^^{OpaqueVTFrameSilo=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {4: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "VTIsStereoMVHEVCDecodeSupported": (b"Z",),
    "VTFrameSiloGetProgressOfCurrentPass": (
        b"i^{OpaqueVTFrameSilo=}^f",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "VTDecompressionSessionInvalidate": (b"v^{OpaqueVTDecompressionSession=}",),
    "VTCompressionSessionGetTypeID": (b"Q",),
    "VTFrameSiloGetTypeID": (b"Q",),
    "VTSessionCopySerializableProperties": (
        b"i@^{__CFAllocator=}^^{__CFDictionary=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "VTIsStereoMVHEVCEncodeSupported": (b"Z",),
    "VTRAWProcessingSessionSetProcessingParameters": (
        b"i^{OpaqueVTRAWProcessingSession=}^{__CFDictionary=}",
    ),
    "VTCompressionSessionCreate": (
        b"i^{__CFAllocator=}iiI^{__CFDictionary=}^{__CFDictionary=}^{__CFAllocator=}^?^v^^{OpaqueVTCompressionSession=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                9: {"already_cfretained": True, "type_modifier": "o"},
                7: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"^v"},
                            2: {"type": b"i"},
                            3: {"type": b"I"},
                            4: {"type": b"^{opaqueCMSampleBuffer=}"},
                        },
                    },
                    "callable_retained": True,
                },
            },
        },
    ),
}
aliases = {"VT_SUPPORT_COLORSYNC_PIXEL_TRANSFER": "COREMEDIA_TRUE"}
cftypes = [
    (
        "VTMultiPassStorageRef",
        b"^{OpaqueVTMultiPassStorage=}",
        ":VTMultiPassStorageGetTypeID",
        None,
    ),
    (
        "VTRAWProcessingSessionRef",
        b"^{OpaqueVTRAWProcessingSession=}",
        "VTRAWProcessingSessionGetTypeID",
        None,
    ),
    (
        "VTDecompressionSessionRef",
        b"^{OpaqueVTDecompressionSession=}",
        ":VTDecompressionSessionGetTypeID",
        None,
    ),
    (
        "VTPixelTransferSessionRef",
        b"^{OpaqueVTPixelTransferSession=}",
        "VTPixelTransferSessionGetTypeID",
        None,
    ),
    (
        "VTHDRPerFrameMetadataGenerationSessionRef",
        b"^{OpaqueVTHDRPerFrameMetadataGenerationSession=}",
        "VTHDRPerFrameMetadataGenerationSessionGetTypeID",
        None,
    ),
    (
        "VTPixelRotationSessionRef",
        b"^{OpaqueVTPixelRotationSession=}",
        "VTPixelRotationSessionGetTypeID",
        None,
    ),
    ("VTFrameSiloRef", b"^{OpaqueVTFrameSilo=}", ":VTFrameSiloGetTypeID", None),
    ("VTSessionRef", b"^{OpaqueVTSession=}", ":VTSessionGetTypeID", None),
]
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"destinationPixelBufferAttributes",
        {"required": True, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"frameSupportedPixelFormats",
        {"required": True, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"maximumDimensions",
        {"required": False, "retval": {"type": b"{CMVideoDimensions=ii}"}},
    )
    r(
        b"NSObject",
        b"minimumDimensions",
        {"required": False, "retval": {"type": b"{CMVideoDimensions=ii}"}},
    )
    r(b"NSObject", b"nextFrameCount", {"required": False, "retval": {"type": b"q"}})
    r(b"NSObject", b"previousFrameCount", {"required": False, "retval": {"type": b"q"}})
    r(b"NSObject", b"processorSupported", {"required": True, "retval": {"type": b"Z"}})
    r(b"NSObject", b"sourceFrame", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"sourcePixelBufferAttributes",
        {"required": True, "retval": {"type": b"@"}},
    )
    r(
        b"VTFrameProcessor",
        b"processWithCommandBuffer:parameters:completionHandler:",
        {
            "arguments": {
                4: {
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
        b"VTFrameProcessor",
        b"processWithParameters:completionHandler:",
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
        b"VTFrameProcessor",
        b"processWithParameters:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"VTFrameProcessor",
        b"startSessionWithConfiguration:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"VTFrameRateConversionConfiguration",
        b"initWithFrameWidth:frameHeight:usePrecomputedFlow:qualityPrioritization:revision:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"VTFrameRateConversionConfiguration",
        b"processorSupported",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"VTFrameRateConversionConfiguration",
        b"usePrecomputedFlow",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"VTMotionBlurConfiguration",
        b"initWithFrameWidth:frameHeight:usePrecomputedFlow:qualityPrioritization:revision:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(b"VTMotionBlurConfiguration", b"processorSupported", {"retval": {"type": b"Z"}})
    r(b"VTMotionBlurConfiguration", b"usePrecomputedFlow", {"retval": {"type": b"Z"}})
    r(b"VTOpticalFlowConfiguration", b"processorSupported", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector(
    "VTFrameProcessorFrame", b"initWithBuffer:presentationTimeStamp:"
)
objc.registerNewKeywordsFromSelector(
    "VTFrameProcessorOpticalFlow", b"initWithForwardFlow:backwardFlow:"
)
objc.registerNewKeywordsFromSelector(
    "VTFrameRateConversionConfiguration",
    b"initWithFrameWidth:frameHeight:usePrecomputedFlow:qualityPrioritization:revision:",
)
objc.registerNewKeywordsFromSelector(
    "VTFrameRateConversionParameters",
    b"initWithSourceFrame:nextFrame:opticalFlow:interpolationPhase:submissionMode:destinationFrames:",
)
objc.registerNewKeywordsFromSelector(
    "VTMotionBlurConfiguration",
    b"initWithFrameWidth:frameHeight:usePrecomputedFlow:qualityPrioritization:revision:",
)
objc.registerNewKeywordsFromSelector(
    "VTMotionBlurParameters",
    b"initWithSourceFrame:nextFrame:previousFrame:nextOpticalFlow:previousOpticalFlow:motionBlurStrength:submissionMode:destinationFrame:",
)
objc.registerNewKeywordsFromSelector(
    "VTOpticalFlowConfiguration",
    b"initWithFrameWidth:frameHeight:qualityPrioritization:revision:",
)
objc.registerNewKeywordsFromSelector(
    "VTOpticalFlowParameters",
    b"initWithSourceFrame:nextFrame:submissionMode:destinationOpticalFlow:",
)
expressions = {}

# END OF FILE
