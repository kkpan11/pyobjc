# This file is generated by objective.metadata
#
# Last update: Thu Jul 23 14:18:11 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
constants = """$kCFDNSServiceFailureKey$kCFErrorDomainCFNetwork$kCFErrorDomainWinSock$kCFFTPResourceGroup$kCFFTPResourceLink$kCFFTPResourceModDate$kCFFTPResourceMode$kCFFTPResourceName$kCFFTPResourceOwner$kCFFTPResourceSize$kCFFTPResourceType$kCFFTPStatusCodeKey$kCFGetAddrInfoFailureKey$kCFHTTPAuthenticationAccountDomain$kCFHTTPAuthenticationPassword$kCFHTTPAuthenticationSchemeBasic$kCFHTTPAuthenticationSchemeDigest$kCFHTTPAuthenticationSchemeKerberos$kCFHTTPAuthenticationSchemeNTLM$kCFHTTPAuthenticationSchemeNegotiate$kCFHTTPAuthenticationSchemeNegotiate2$kCFHTTPAuthenticationSchemeOAuth1$kCFHTTPAuthenticationSchemeXMobileMeAuthToken$kCFHTTPAuthenticationUsername$kCFHTTPVersion1_0$kCFHTTPVersion1_1$kCFHTTPVersion2_0$kCFHTTPVersion3_0$kCFNetworkProxiesExceptionsList$kCFNetworkProxiesExcludeSimpleHostnames$kCFNetworkProxiesFTPEnable$kCFNetworkProxiesFTPPassive$kCFNetworkProxiesFTPPort$kCFNetworkProxiesFTPProxy$kCFNetworkProxiesGopherEnable$kCFNetworkProxiesGopherPort$kCFNetworkProxiesGopherProxy$kCFNetworkProxiesHTTPEnable$kCFNetworkProxiesHTTPPort$kCFNetworkProxiesHTTPProxy$kCFNetworkProxiesHTTPSEnable$kCFNetworkProxiesHTTPSPort$kCFNetworkProxiesHTTPSProxy$kCFNetworkProxiesProxyAutoConfigEnable$kCFNetworkProxiesProxyAutoConfigJavaScript$kCFNetworkProxiesProxyAutoConfigURLString$kCFNetworkProxiesProxyAutoDiscoveryEnable$kCFNetworkProxiesRTSPEnable$kCFNetworkProxiesRTSPPort$kCFNetworkProxiesRTSPProxy$kCFNetworkProxiesSOCKSEnable$kCFNetworkProxiesSOCKSPort$kCFNetworkProxiesSOCKSProxy$kCFProxyAutoConfigurationHTTPResponseKey$kCFProxyAutoConfigurationJavaScriptKey$kCFProxyAutoConfigurationURLKey$kCFProxyHostNameKey$kCFProxyPasswordKey$kCFProxyPortNumberKey$kCFProxyTypeAutoConfigurationJavaScript$kCFProxyTypeAutoConfigurationURL$kCFProxyTypeFTP$kCFProxyTypeHTTP$kCFProxyTypeHTTPS$kCFProxyTypeKey$kCFProxyTypeNone$kCFProxyTypeSOCKS$kCFProxyUsernameKey$kCFSOCKSNegotiationMethodKey$kCFSOCKSStatusCodeKey$kCFSOCKSVersionKey$kCFStreamErrorDomainFTP@i$kCFStreamErrorDomainHTTP@i$kCFStreamErrorDomainMach@i$kCFStreamErrorDomainNetDB@i$kCFStreamErrorDomainNetServices@i$kCFStreamErrorDomainSOCKS@i$kCFStreamErrorDomainSSL@i$kCFStreamErrorDomainSystemConfiguration@i$kCFStreamErrorDomainWinSock@q$kCFStreamNetworkServiceType$kCFStreamNetworkServiceTypeAVStreaming$kCFStreamNetworkServiceTypeBackground$kCFStreamNetworkServiceTypeCallSignaling$kCFStreamNetworkServiceTypeResponsiveAV$kCFStreamNetworkServiceTypeResponsiveData$kCFStreamNetworkServiceTypeVideo$kCFStreamNetworkServiceTypeVoIP$kCFStreamNetworkServiceTypeVoice$kCFStreamPropertyAllowConstrainedNetworkAccess$kCFStreamPropertyAllowExpensiveNetworkAccess$kCFStreamPropertyConnectionIsCellular$kCFStreamPropertyConnectionIsExpensive$kCFStreamPropertyFTPAttemptPersistentConnection$kCFStreamPropertyFTPFetchResourceInfo$kCFStreamPropertyFTPFileTransferOffset$kCFStreamPropertyFTPPassword$kCFStreamPropertyFTPProxy$kCFStreamPropertyFTPProxyHost$kCFStreamPropertyFTPProxyPassword$kCFStreamPropertyFTPProxyPort$kCFStreamPropertyFTPProxyUser$kCFStreamPropertyFTPResourceSize$kCFStreamPropertyFTPUsePassiveMode$kCFStreamPropertyFTPUserName$kCFStreamPropertyHTTPAttemptPersistentConnection$kCFStreamPropertyHTTPFinalRequest$kCFStreamPropertyHTTPFinalURL$kCFStreamPropertyHTTPProxy$kCFStreamPropertyHTTPProxyHost$kCFStreamPropertyHTTPProxyPort$kCFStreamPropertyHTTPRequestBytesWrittenCount$kCFStreamPropertyHTTPResponseHeader$kCFStreamPropertyHTTPSProxyHost$kCFStreamPropertyHTTPSProxyPort$kCFStreamPropertyHTTPShouldAutoredirect$kCFStreamPropertyNoCellular$kCFStreamPropertyProxyLocalBypass$kCFStreamPropertySOCKSPassword$kCFStreamPropertySOCKSProxy$kCFStreamPropertySOCKSProxyHost$kCFStreamPropertySOCKSProxyPort$kCFStreamPropertySOCKSUser$kCFStreamPropertySOCKSVersion$kCFStreamPropertySSLContext$kCFStreamPropertySSLPeerCertificates$kCFStreamPropertySSLPeerTrust$kCFStreamPropertySSLSettings$kCFStreamPropertyShouldCloseNativeSocket$kCFStreamPropertySocketExtendedBackgroundIdleMode$kCFStreamPropertySocketRemoteHost$kCFStreamPropertySocketRemoteNetService$kCFStreamPropertySocketSecurityLevel$kCFStreamSSLAllowsAnyRoot$kCFStreamSSLAllowsExpiredCertificates$kCFStreamSSLAllowsExpiredRoots$kCFStreamSSLCertificates$kCFStreamSSLIsServer$kCFStreamSSLLevel$kCFStreamSSLPeerName$kCFStreamSSLValidatesCertificateChain$kCFStreamSocketSOCKSVersion4$kCFStreamSocketSOCKSVersion5$kCFStreamSocketSecurityLevelNegotiatedSSL$kCFStreamSocketSecurityLevelNone$kCFStreamSocketSecurityLevelSSLv2$kCFStreamSocketSecurityLevelSSLv3$kCFStreamSocketSecurityLevelTLSv1$kCFURLErrorFailingURLErrorKey$kCFURLErrorFailingURLStringErrorKey$"""
enums = """$kCFErrorHTTPAuthenticationTypeUnsupported@300$kCFErrorHTTPBadCredentials@301$kCFErrorHTTPBadProxyCredentials@307$kCFErrorHTTPBadURL@305$kCFErrorHTTPConnectionLost@302$kCFErrorHTTPParseFailure@303$kCFErrorHTTPProxyConnectionFailure@306$kCFErrorHTTPRedirectionLoopDetected@304$kCFErrorHTTPSProxyConnectionFailure@310$kCFErrorPACFileAuth@309$kCFErrorPACFileError@308$kCFFTPErrorUnexpectedStatusCode@200$kCFHTTPCookieCannotParseCookieFile@-4000$kCFHostAddresses@0$kCFHostErrorHostNotFound@1$kCFHostErrorUnknown@2$kCFHostNames@1$kCFHostReachability@2$kCFNetDiagnosticConnectionDown@-66557$kCFNetDiagnosticConnectionIndeterminate@-66558$kCFNetDiagnosticConnectionUp@-66559$kCFNetDiagnosticErr@-66560$kCFNetDiagnosticNoErr@0$kCFNetServiceErrorBadArgument@-72004$kCFNetServiceErrorCancel@-72005$kCFNetServiceErrorCollision@-72001$kCFNetServiceErrorDNSServiceFailure@-73000$kCFNetServiceErrorInProgress@-72003$kCFNetServiceErrorInvalid@-72006$kCFNetServiceErrorNotFound@-72002$kCFNetServiceErrorTimeout@-72007$kCFNetServiceErrorUnknown@-72000$kCFNetServiceFlagIsDefault@4$kCFNetServiceFlagIsDomain@2$kCFNetServiceFlagIsRegistrationDomain@4$kCFNetServiceFlagMoreComing@1$kCFNetServiceFlagNoAutoRename@1$kCFNetServiceFlagRemove@8$kCFNetServiceMonitorTXT@1$kCFNetServicesErrorBadArgument@-72004$kCFNetServicesErrorCancel@-72005$kCFNetServicesErrorCollision@-72001$kCFNetServicesErrorInProgress@-72003$kCFNetServicesErrorInvalid@-72006$kCFNetServicesErrorMissingRequiredConfiguration@-72008$kCFNetServicesErrorNotFound@-72002$kCFNetServicesErrorTimeout@-72007$kCFNetServicesErrorUnknown@-72000$kCFSOCKS4ErrorIdConflict@112$kCFSOCKS4ErrorIdentdFailed@111$kCFSOCKS4ErrorRequestFailed@110$kCFSOCKS4ErrorUnknownStatusCode@113$kCFSOCKS5ErrorBadCredentials@122$kCFSOCKS5ErrorBadResponseAddr@121$kCFSOCKS5ErrorBadState@120$kCFSOCKS5ErrorNoAcceptableMethod@124$kCFSOCKS5ErrorUnsupportedNegotiationMethod@123$kCFSOCKSErrorUnknownClientVersion@100$kCFSOCKSErrorUnsupportedServerVersion@101$kCFStreamErrorHTTPAuthenticationBadPassword@-1002$kCFStreamErrorHTTPAuthenticationBadUserName@-1001$kCFStreamErrorHTTPAuthenticationTypeUnsupported@-1000$kCFStreamErrorHTTPBadURL@-3$kCFStreamErrorHTTPParseFailure@-1$kCFStreamErrorHTTPRedirectionLoop@-2$kCFStreamErrorHTTPSProxyFailureUnexpectedResponseToCONNECTMethod@311$kCFStreamErrorSOCKS4IdConflict@93$kCFStreamErrorSOCKS4IdentdFailed@92$kCFStreamErrorSOCKS4RequestFailed@91$kCFStreamErrorSOCKS4SubDomainResponse@2$kCFStreamErrorSOCKS5BadResponseAddr@1$kCFStreamErrorSOCKS5BadState@2$kCFStreamErrorSOCKS5SubDomainMethod@4$kCFStreamErrorSOCKS5SubDomainResponse@5$kCFStreamErrorSOCKS5SubDomainUserPass@3$kCFStreamErrorSOCKSSubDomainNone@0$kCFStreamErrorSOCKSSubDomainVersionCode@1$kCFStreamErrorSOCKSUnknownClientVersion@3$kCFStreamSocketSecurityNone@0$kCFStreamSocketSecuritySSLv2@1$kCFStreamSocketSecuritySSLv23@3$kCFStreamSocketSecuritySSLv3@2$kCFStreamSocketSecurityTLSv1@4$kCFURLErrorAppTransportSecurityRequiresSecureConnection@-1022$kCFURLErrorBackgroundSessionInUseByAnotherProcess@-996$kCFURLErrorBackgroundSessionWasDisconnected@-997$kCFURLErrorBadServerResponse@-1011$kCFURLErrorBadURL@-1000$kCFURLErrorCallIsActive@-1019$kCFURLErrorCancelled@-999$kCFURLErrorCannotCloseFile@-3002$kCFURLErrorCannotConnectToHost@-1004$kCFURLErrorCannotCreateFile@-3000$kCFURLErrorCannotDecodeContentData@-1016$kCFURLErrorCannotDecodeRawData@-1015$kCFURLErrorCannotFindHost@-1003$kCFURLErrorCannotLoadFromNetwork@-2000$kCFURLErrorCannotMoveFile@-3005$kCFURLErrorCannotOpenFile@-3001$kCFURLErrorCannotParseResponse@-1017$kCFURLErrorCannotRemoveFile@-3004$kCFURLErrorCannotWriteToFile@-3003$kCFURLErrorClientCertificateRejected@-1205$kCFURLErrorClientCertificateRequired@-1206$kCFURLErrorDNSLookupFailed@-1006$kCFURLErrorDataLengthExceedsMaximum@-1103$kCFURLErrorDataNotAllowed@-1020$kCFURLErrorDownloadDecodingFailedMidStream@-3006$kCFURLErrorDownloadDecodingFailedToComplete@-3007$kCFURLErrorFileDoesNotExist@-1100$kCFURLErrorFileIsDirectory@-1101$kCFURLErrorFileOutsideSafeArea@-1104$kCFURLErrorHTTPTooManyRedirects@-1007$kCFURLErrorInternationalRoamingOff@-1018$kCFURLErrorNetworkConnectionLost@-1005$kCFURLErrorNoPermissionsToReadFile@-1102$kCFURLErrorNotConnectedToInternet@-1009$kCFURLErrorRedirectToNonExistentLocation@-1010$kCFURLErrorRequestBodyStreamExhausted@-1021$kCFURLErrorResourceUnavailable@-1008$kCFURLErrorSecureConnectionFailed@-1200$kCFURLErrorServerCertificateHasBadDate@-1201$kCFURLErrorServerCertificateHasUnknownRoot@-1203$kCFURLErrorServerCertificateNotYetValid@-1204$kCFURLErrorServerCertificateUntrusted@-1202$kCFURLErrorTimedOut@-1001$kCFURLErrorUnknown@-998$kCFURLErrorUnsupportedURL@-1002$kCFURLErrorUserAuthenticationRequired@-1013$kCFURLErrorUserCancelledAuthentication@-1012$kCFURLErrorZeroByteResource@-1014$kSOCKS5NoAcceptableMethod@255$"""
misc.update({})
functions = {
    "CFNetworkExecuteProxyAutoConfigurationURL": (
        b"^{__CFRunLoopSource=}^{__CFURL=}^{__CFURL=}^?^{_CFStreamClientContext=q^v^?^?^?}",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"^{__CFArray=}"},
                            2: {"type": b"^{__CFError=}"},
                        },
                    }
                }
            }
        },
    ),
    "CFHTTPAuthenticationRequiresOrderedRequests": (b"Z^{_CFHTTPAuthentication=}",),
    "CFHTTPAuthenticationCreateFromResponse": (
        b"^{_CFHTTPAuthentication=}^{__CFAllocator=}^{__CFHTTPMessage=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetServiceBrowserGetTypeID": (b"Q",),
    "CFHostCreateWithName": (
        b"^{__CFHost=}^{__CFAllocator=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFHostGetAddressing": (
        b"^{__CFArray=}^{__CFHost=}^Z",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "CFHTTPMessageSetBody": (b"v^{__CFHTTPMessage=}^{__CFData=}",),
    "CFHTTPAuthenticationGetTypeID": (b"Q",),
    "CFNetDiagnosticCreateWithStreams": (
        b"^{__CFNetDiagnostic=}^{__CFAllocator=}^{__CFReadStream=}^{__CFWriteStream=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFSocketStreamSOCKSGetError": (b"i^{_CFStreamError=qi}",),
    "CFHostCreateWithAddress": (
        b"^{__CFHost=}^{__CFAllocator=}^{__CFData=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetServiceBrowserSearchForDomains": (
        b"Z^{__CFNetServiceBrowser=}Z^{_CFStreamError=qi}",
    ),
    "CFNetServiceUnscheduleFromRunLoop": (
        b"v^{__CFNetService=}^{__CFRunLoop=}^{__CFString=}",
    ),
    "CFNetServiceMonitorStop": (b"v^{__CFNetServiceMonitor=}^{_CFStreamError=qi}",),
    "CFNetworkCopySystemProxySettings": (
        b"^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFHostGetReachability": (
        b"^{__CFData=}^{__CFHost=}^Z",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "CFHTTPMessageIsHeaderComplete": (b"Z^{__CFHTTPMessage=}",),
    "CFHTTPMessageGetTypeID": (b"Q",),
    "CFNetServiceMonitorGetTypeID": (b"Q",),
    "CFNetServiceGetPortNumber": (b"i^{__CFNetService=}",),
    "CFHTTPMessageCreateRequest": (
        b"^{__CFHTTPMessage=}^{__CFAllocator=}^{__CFString=}^{__CFURL=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetServiceCreateCopy": (
        b"^{__CFNetService=}^{__CFAllocator=}^{__CFNetService=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetServiceGetName": (b"^{__CFString=}^{__CFNetService=}",),
    "CFHTTPMessageCopyRequestMethod": (
        b"^{__CFString=}^{__CFHTTPMessage=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFHTTPAuthenticationCopyRealm": (
        b"^{__CFString=}^{_CFHTTPAuthentication=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetServiceMonitorInvalidate": (b"v^{__CFNetServiceMonitor=}",),
    "CFNetServiceGetProtocolSpecificInformation": (b"@^{__CFNetService=}",),
    "CFNetServiceCancel": (b"v^{__CFNetService=}",),
    "CFNetServiceMonitorCreate": (
        b"^{__CFNetServiceMonitor=}^{__CFAllocator=}^{__CFNetService=}^?^{CFNetServiceClientContext=q^v^?^?^?}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^{__CFNetServiceMonitor=}"},
                            1: {"type": b"^{__CFNetService=}"},
                            2: {"type": b"i"},
                            3: {"type": b"^{__CFData=}"},
                            4: {"type": b"^{_CFStreamError=qi}"},
                            5: {"type": b"^v"},
                        },
                    }
                }
            },
        },
    ),
    "CFWriteStreamCreateWithFTPURL": (
        b"^{__CFWriteStream=}^{__CFAllocator=}^{__CFURL=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetServiceBrowserUnscheduleFromRunLoop": (
        b"v^{__CFNetServiceBrowser=}^{__CFRunLoop=}^{__CFString=}",
    ),
    "CFHTTPMessageCopyRequestURL": (
        b"^{__CFURL=}^{__CFHTTPMessage=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFHTTPMessageCopyVersion": (
        b"^{__CFString=}^{__CFHTTPMessage=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetServiceCreate": (
        b"^{__CFNetService=}^{__CFAllocator=}^{__CFString=}^{__CFString=}^{__CFString=}i",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetServiceMonitorUnscheduleFromRunLoop": (
        b"v^{__CFNetServiceMonitor=}^{__CFRunLoop=}^{__CFString=}",
    ),
    "CFHostScheduleWithRunLoop": (b"v^{__CFHost=}^{__CFRunLoop=}^{__CFString=}",),
    "CFNetServiceMonitorStart": (b"Z^{__CFNetServiceMonitor=}i^{_CFStreamError=qi}",),
    "CFHostGetNames": (
        b"^{__CFArray=}^{__CFHost=}^Z",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "CFNetDiagnosticCopyNetworkStatusPassively": (
        b"q^{__CFNetDiagnostic=}^^{__CFString=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CFHTTPMessageCopyResponseStatusLine": (
        b"^{__CFString=}^{__CFHTTPMessage=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetDiagnosticDiagnoseProblemInteractively": (b"q^{__CFNetDiagnostic=}",),
    "CFHTTPMessageAddAuthentication": (
        b"Z^{__CFHTTPMessage=}^{__CFHTTPMessage=}^{__CFString=}^{__CFString=}^{__CFString=}Z",
    ),
    "CFNetworkExecuteProxyAutoConfigurationScript": (
        b"^{__CFRunLoopSource=}^{__CFString=}^{__CFURL=}^?^{_CFStreamClientContext=q^v^?^?^?}",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"^{__CFArray=}"},
                            2: {"type": b"^{__CFError=}"},
                        },
                    }
                }
            }
        },
    ),
    "CFNetDiagnosticCreateWithURL": (
        b"^{__CFNetDiagnostic=}^{__CFAllocator=}^{__CFURL=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetServiceGetDomain": (b"^{__CFString=}^{__CFNetService=}",),
    "CFFTPCreateParsedResourceListing": (
        b"q^{__CFAllocator=}^vq^^{__CFDictionary=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                1: {"type_modifier": "n"},
                3: {"already_cfretained": True, "type_modifier": "o"},
            },
        },
    ),
    "CFNetServiceGetTypeID": (b"Q",),
    "CFHTTPMessageCreateEmpty": (
        b"^{__CFHTTPMessage=}^{__CFAllocator=}Z",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFHTTPMessageAppendBytes": (
        b"Z^{__CFHTTPMessage=}^Cq",
        "",
        {"arguments": {1: {"c_array_length_in_arg": 2, "type_modifier": "n"}}},
    ),
    "CFHostCancelInfoResolution": (b"v^{__CFHost=}i",),
    "CFNetServiceBrowserSearchForServices": (
        b"Z^{__CFNetServiceBrowser=}^{__CFString=}^{__CFString=}^{_CFStreamError=qi}",
        "",
        {"arguments": {3: {"type_modifier": "o"}}},
    ),
    "CFHTTPAuthenticationIsValid": (
        b"Z^{_CFHTTPAuthentication=}^{_CFStreamError=qi}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "CFHTTPAuthenticationAppliesToRequest": (
        b"Z^{_CFHTTPAuthentication=}^{__CFHTTPMessage=}",
    ),
    "CFNetServiceBrowserInvalidate": (b"v^{__CFNetServiceBrowser=}",),
    "CFNetServiceGetAddressing": (b"^{__CFArray=}^{__CFNetService=}",),
    "CFHTTPMessageSetHeaderFieldValue": (
        b"v^{__CFHTTPMessage=}^{__CFString=}^{__CFString=}",
    ),
    "CFNetServiceBrowserStopSearch": (
        b"v^{__CFNetServiceBrowser=}^{_CFStreamError=qi}",
    ),
    "CFHTTPMessageApplyCredentials": (
        b"Z^{__CFHTTPMessage=}^{_CFHTTPAuthentication=}^{__CFString=}^{__CFString=}^{_CFStreamError=qi}",
        "",
        {"arguments": {4: {"type_modifier": "o"}}},
    ),
    "CFHTTPReadStreamSetRedirectsAutomatically": (b"v^{__CFReadStream=}Z",),
    "CFNetServiceRegisterWithOptions": (
        b"Z^{__CFNetService=}Q^{_CFStreamError=qi}",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "CFHTTPAuthenticationCopyMethod": (
        b"^{__CFString=}^{_CFHTTPAuthentication=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetServiceBrowserCreate": (
        b"^{__CFNetServiceBrowser=}^{__CFAllocator=}^?^{CFNetServiceClientContext=q^v^?^?^?}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^{__CFNetServiceBrowser=}"},
                            1: {"type": b"Q"},
                            2: {"type": b"@"},
                            3: {"type": b"^{_CFStreamError=qi}"},
                            4: {"type": b"^v"},
                        },
                    }
                }
            },
        },
    ),
    "CFNetServiceGetTargetHost": (b"^{__CFString=}^{__CFNetService=}",),
    "CFNetworkCopyProxiesForAutoConfigurationScript": (
        b"^{__CFArray=}^{__CFString=}^{__CFURL=}^^{__CFError=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                2: {
                    "already_cfretained": True,
                    "type_modifier": "o",
                    "null_accepted": True,
                }
            },
        },
    ),
    "CFNetServiceCreateDictionaryWithTXTData": (
        b"^{__CFDictionary=}^{__CFAllocator=}^{__CFData=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetServiceRegister": (b"Z^{__CFNetService=}^{_CFStreamError=qi}",),
    "CFHTTPMessageCopySerializedMessage": (
        b"^{__CFData=}^{__CFHTTPMessage=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFHostCreateCopy": (
        b"^{__CFHost=}^{__CFAllocator=}^{__CFHost=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFHTTPAuthenticationRequiresAccountDomain": (b"Z^{_CFHTTPAuthentication=}",),
    "CFNetServiceSetTXTData": (b"Z^{__CFNetService=}^{__CFData=}",),
    "CFNetworkCopyProxiesForURL": (
        b"^{__CFArray=}^{__CFURL=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFReadStreamCreateForStreamedHTTPRequest": (
        b"^{__CFReadStream=}^{__CFAllocator=}^{__CFHTTPMessage=}^{__CFReadStream=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFReadStreamCreateForHTTPRequest": (
        b"^{__CFReadStream=}^{__CFAllocator=}^{__CFHTTPMessage=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFHTTPMessageCreateCopy": (
        b"^{__CFHTTPMessage=}^{__CFAllocator=}^{__CFHTTPMessage=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetServiceGetType": (b"^{__CFString=}^{__CFNetService=}",),
    "CFNetServiceScheduleWithRunLoop": (
        b"v^{__CFNetService=}^{__CFRunLoop=}^{__CFString=}",
    ),
    "CFHTTPMessageCopyHeaderFieldValue": (
        b"^{__CFString=}^{__CFHTTPMessage=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetServiceGetTXTData": (b"^{__CFData=}^{__CFNetService=}",),
    "CFHostStartInfoResolution": (
        b"Z^{__CFHost=}i^{_CFStreamError=qi}",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "CFHTTPAuthenticationRequiresUserNameAndPassword": (b"Z^{_CFHTTPAuthentication=}",),
    "CFNetDiagnosticSetName": (b"v^{__CFNetDiagnostic=}^{__CFString=}",),
    "CFNetServiceCreateTXTDataWithDictionary": (
        b"^{__CFData=}^{__CFAllocator=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFReadStreamCreateWithFTPURL": (
        b"^{__CFReadStream=}^{__CFAllocator=}^{__CFURL=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetServiceSetClient": (
        b"Z^{__CFNetService=}^?^{CFNetServiceClientContext=q^v^?^?^?}",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^{__CFNetService=}"},
                            1: {"type": b"^{_CFStreamError=qi}"},
                            2: {"type": b"^v"},
                        },
                    }
                }
            }
        },
    ),
    "CFNetServiceMonitorScheduleWithRunLoop": (
        b"v^{__CFNetServiceMonitor=}^{__CFRunLoop=}^{__CFString=}",
    ),
    "CFHostUnscheduleFromRunLoop": (b"v^{__CFHost=}^{__CFRunLoop=}^{__CFString=}",),
    "CFHTTPMessageApplyCredentialDictionary": (
        b"Z^{__CFHTTPMessage=}^{_CFHTTPAuthentication=}^{__CFDictionary=}^{_CFStreamError=qi}",
        "",
        {"arguments": {3: {"type_modifier": "o"}}},
    ),
    "CFHTTPMessageIsRequest": (b"Z^{__CFHTTPMessage=}",),
    "CFNetServiceResolve": (b"Z^{__CFNetService=}^{_CFStreamError=qi}",),
    "CFHTTPMessageCopyBody": (
        b"^{__CFData=}^{__CFHTTPMessage=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetServiceBrowserScheduleWithRunLoop": (
        b"v^{__CFNetServiceBrowser=}^{__CFRunLoop=}^{__CFString=}",
    ),
    "CFHTTPMessageCreateResponse": (
        b"^{__CFHTTPMessage=}^{__CFAllocator=}q^{__CFString=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFHostGetTypeID": (b"Q",),
    "CFHTTPMessageCopyAllHeaderFields": (
        b"^{__CFDictionary=}^{__CFHTTPMessage=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFHTTPMessageGetResponseStatusCode": (b"q^{__CFHTTPMessage=}",),
    "CFHTTPAuthenticationCopyDomains": (
        b"^{__CFArray=}^{_CFHTTPAuthentication=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CFNetServiceSetProtocolSpecificInformation": (b"v^{__CFNetService=}@",),
    "CFSocketStreamSOCKSGetErrorSubdomain": (b"i^{_CFStreamError=qi}",),
    "CFStreamCreatePairWithSocketToCFHost": (
        b"v^{__CFAllocator=}^{__CFHost=}i^^{__CFReadStream=}^^{__CFWriteStream=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                3: {"already_cfretained": True, "type_modifier": "o"},
                4: {"already_cfretained": True, "type_modifier": "o"},
            },
        },
    ),
    "CFStreamCreatePairWithSocketToNetService": (
        b"v^{__CFAllocator=}^{__CFNetService=}^^{__CFReadStream=}^^{__CFWriteStream=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                2: {"already_cfretained": True, "type_modifier": "o"},
                3: {"already_cfretained": True, "type_modifier": "o"},
            },
        },
    ),
    "CFNetServiceResolveWithTimeout": (
        b"Z^{__CFNetService=}d^{_CFStreamError=qi}",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "CFHostSetClient": (
        b"Z^{__CFHost=}^?^{CFHostClientContext=q^v^?^?^?}",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^{__CFHost=}"},
                            1: {"type": b"i"},
                            2: {"type": b"^{_CFStreamError=qi}"},
                            3: {"type": b"^v"},
                        },
                    }
                }
            }
        },
    ),
}
cftypes = [
    ("CFHTTPMessageRef", b"^{__CFHTTPMessage=}", "CFHTTPMessageGetTypeID", None),
    ("CFHostRef", b"^{__CFHost=}", "CFHostGetTypeID", None),
    ("CFNetDiagnosticRef", b"^{__CFNetDiagnostic=}", "CFNetDiagnosticGetTypeID", None),
    (
        "CFNetServiceBrowserRef",
        b"^{__CFNetServiceBrowser=}",
        "CFNetServiceBrowserGetTypeID",
        None,
    ),
    (
        "CFNetServiceMonitorRef",
        b"^{__CFNetServiceMonitor=}",
        "CFNetServiceMonitorGetTypeID",
        None,
    ),
    ("CFNetServiceRef", b"^{__CFNetService=}", "CFNetServiceGetTypeID", None),
    (
        "CFHTTPAuthenticationRef",
        b"^{_CFHTTPAuthentication}",
        "CFHTTPAuthenticationGetTypeID",
        None,
    ),
]
expressions = {}

# END OF FILE
