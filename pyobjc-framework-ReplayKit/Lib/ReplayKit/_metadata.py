# This file is generated by objective.metadata
#
# Last update: Sat May 18 09:35:41 2024
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
constants = """$RPApplicationInfoBundleIdentifierKey$RPRecordingErrorDomain$RPVideoSampleOrientationKey$SCStreamErrorDomain$"""
enums = """$RPCameraPositionBack@2$RPCameraPositionFront@1$RPRecordingErrorActivePhoneCall@-5811$RPRecordingErrorAttemptToStartInRecordingState@-5830$RPRecordingErrorAttemptToStopNonRecording@-5829$RPRecordingErrorBroadcastInvalidSession@-5808$RPRecordingErrorBroadcastSetupFailed@-5819$RPRecordingErrorCarPlay@-5813$RPRecordingErrorCodeSuccessful@0$RPRecordingErrorContentResize@-5807$RPRecordingErrorDisabled@-5802$RPRecordingErrorEntitlements@-5810$RPRecordingErrorExportClipToURLInProgress@-5836$RPRecordingErrorFailed@-5804$RPRecordingErrorFailedApplicationConnectionInterrupted@-5815$RPRecordingErrorFailedApplicationConnectionInvalid@-5814$RPRecordingErrorFailedAssetWriterExportCanceled@-5828$RPRecordingErrorFailedAssetWriterExportFailed@-5826$RPRecordingErrorFailedAssetWriterFailedToSave@-5823$RPRecordingErrorFailedAssetWriterInWrongState@-5825$RPRecordingErrorFailedIncorrectTimeStamps@-5821$RPRecordingErrorFailedMediaServicesFailure@-5817$RPRecordingErrorFailedNoAssetWriter@-5824$RPRecordingErrorFailedNoMatchingApplicationContext@-5816$RPRecordingErrorFailedToObtainURL@-5820$RPRecordingErrorFailedToProcessFirstSample@-5822$RPRecordingErrorFailedToRemoveFile@-5827$RPRecordingErrorFailedToSave@-5812$RPRecordingErrorFailedToStart@-5803$RPRecordingErrorFailedToStartCaptureStack@-5833$RPRecordingErrorFilePermissions@-5835$RPRecordingErrorInsufficientStorage@-5805$RPRecordingErrorInterrupted@-5806$RPRecordingErrorInvalidParameter@-5834$RPRecordingErrorPhotoFailure@-5831$RPRecordingErrorRecordingInvalidSession@-5832$RPRecordingErrorSystemDormancy@-5809$RPRecordingErrorUnknown@-5800$RPRecordingErrorUserDeclined@-5801$RPRecordingErrorVideoMixingFailure@-5818$RPSampleBufferTypeAudioApp@2$RPSampleBufferTypeAudioMic@3$RPSampleBufferTypeVideo@1$"""
misc.update(
    {
        "RPRecordingErrorCode": NewType("RPRecordingErrorCode", int),
        "RPCameraPosition": NewType("RPCameraPosition", int),
        "RPSampleBufferType": NewType("RPSampleBufferType", int),
    }
)
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSExtensionContext",
        b"loadBroadcastingApplicationInfoWithCompletion:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"NSObject",
        b"broadcastActivityController:didFinishWithBroadcastController:error:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"broadcastController:didFinishWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"broadcastController:didUpdateBroadcastURL:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"broadcastController:didUpdateServiceInfo:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"previewController:didFinishWithActivityTypes:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"previewControllerDidFinish:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"screenRecorder:didStopRecordingWithError:previewViewController:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"screenRecorder:didStopRecordingWithPreviewViewController:error:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"screenRecorderDidChangeAvailability:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"RPBroadcastActivityController",
        b"showBroadcastPickerAtPoint:fromWindow:preferredExtensionIdentifier:completionHandler:",
        {
            "arguments": {
                5: {
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
        b"RPBroadcastController",
        b"finishBroadcastWithHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(b"RPBroadcastController", b"isBroadcasting", {"retval": {"type": b"Z"}})
    r(b"RPBroadcastController", b"isPaused", {"retval": {"type": b"Z"}})
    r(
        b"RPBroadcastController",
        b"startBroadcastWithHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"RPScreenRecorder",
        b"discardRecordingWithHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(
        b"RPScreenRecorder",
        b"exportClipToURL:duration:completionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
            }
        },
    )
    r(b"RPScreenRecorder", b"isAvailable", {"retval": {"type": b"Z"}})
    r(b"RPScreenRecorder", b"isCameraEnabled", {"retval": {"type": b"Z"}})
    r(b"RPScreenRecorder", b"isMicrophoneEnabled", {"retval": {"type": b"Z"}})
    r(b"RPScreenRecorder", b"isRecording", {"retval": {"type": b"Z"}})
    r(b"RPScreenRecorder", b"setCameraEnabled:", {"arguments": {2: {"type": b"Z"}}})
    r(b"RPScreenRecorder", b"setMicrophoneEnabled:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"RPScreenRecorder",
        b"startCaptureWithHandler:completionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"^{opaqueCMSampleBuffer=}"},
                            2: {"type": b"q"},
                            3: {"type": b"@"},
                        },
                    }
                },
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
            }
        },
    )
    r(
        b"RPScreenRecorder",
        b"startClipBufferingWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"RPScreenRecorder",
        b"startRecordingWithHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"RPScreenRecorder",
        b"startRecordingWithMicrophoneEnabled:handler:",
        {
            "arguments": {
                2: {"type": b"Z"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
            }
        },
    )
    r(
        b"RPScreenRecorder",
        b"stopCaptureWithHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"RPScreenRecorder",
        b"stopClipBufferingWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"RPScreenRecorder",
        b"stopRecordingWithHandler:",
        {
            "arguments": {
                2: {
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
        b"RPScreenRecorder",
        b"stopRecordingWithOutputURL:completionHandler:",
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
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
