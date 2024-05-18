# This file is generated by objective.metadata
#
# Last update: Sat May 18 09:37:47 2024
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
constants = """$ISyncAvailabilityChangedNotification$ISyncChangePropertyActionKey$ISyncChangePropertyClear$ISyncChangePropertyNameKey$ISyncChangePropertySet$ISyncChangePropertyValueIsDefaultKey$ISyncChangePropertyValueKey$ISyncClientTypeApplication$ISyncClientTypeDevice$ISyncClientTypePeer$ISyncClientTypeServer$ISyncErrorDomain$ISyncInvalidArgumentsException$ISyncInvalidEntityException$ISyncInvalidRecordException$ISyncInvalidRecordIdentifiersKey$ISyncInvalidRecordReasonsKey$ISyncInvalidRecordsKey$ISyncInvalidSchemaException$ISyncRecordEntityNameKey$ISyncServerUnavailableException$ISyncSessionCancelledException$ISyncSessionUnavailableException$ISyncUnsupportedEntityException$"""
enums = """$ISyncChangeTypeAdd@1$ISyncChangeTypeDelete@3$ISyncChangeTypeModify@2$ISyncChangeTypeNone@0$ISyncServerDisabledReasonByPreference@1001$ISyncServerDisabledReasonNone@1000$ISyncServerDisabledReasonSharedNetworkHome@1002$ISyncServerDisabledReasonUnknown@1004$ISyncServerDisabledReasonUnresponsive@1003$ISyncSessionClientAlreadySyncingError@100$ISyncSessionDriverChangeAccepted@1$ISyncSessionDriverChangeError@3$ISyncSessionDriverChangeIgnored@2$ISyncSessionDriverChangeRefused@0$ISyncSessionDriverFatalError@300$ISyncSessionDriverModeFast@1$ISyncSessionDriverModeRefresh@3$ISyncSessionDriverModeSlow@2$ISyncSessionDriverPullFailureError@201$ISyncSessionDriverRegistrationError@200$ISyncSessionUserCanceledSessionError@101$ISyncStatusCancelled@5$ISyncStatusErrors@4$ISyncStatusFailed@6$ISyncStatusNever@7$ISyncStatusRunning@1$ISyncStatusSuccess@2$ISyncStatusWarnings@3$"""
misc.update(
    {
        "ISyncServerDisabledReason": NewType("ISyncServerDisabledReason", int),
        "ISyncSessionDriverMode": NewType("ISyncSessionDriverMode", int),
        "__ISyncChangeType": NewType("__ISyncChangeType", int),
        "__ISyncStatus": NewType("__ISyncStatus", int),
        "ISyncSessionDriverChangeResult": NewType(
            "ISyncSessionDriverChangeResult", int
        ),
    }
)
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"ISyncClient", b"canPullChangesForEntityName:", {"retval": {"type": "Z"}})
    r(b"ISyncClient", b"canPushChangesForEntityName:", {"retval": {"type": "Z"}})
    r(b"ISyncClient", b"formatsRelationships", {"retval": {"type": "Z"}})
    r(b"ISyncClient", b"isEnabledForEntityName:", {"retval": {"type": "Z"}})
    r(b"ISyncClient", b"setEnabled:forEntityNames:", {"arguments": {2: {"type": "Z"}}})
    r(b"ISyncClient", b"setFormatsRelationships:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"ISyncClient",
        b"setShouldReplaceClientRecords:forEntityNames:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"ISyncClient",
        b"setShouldSynchronize:withClientsOfType:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"ISyncClient",
        b"setSyncAlertHandler:selector:",
        {"arguments": {3: {"sel_of_type": b"v@:@@"}}},
    )
    r(
        b"ISyncClient",
        b"shouldReplaceClientRecordsForEntityName:",
        {"retval": {"type": "Z"}},
    )
    r(b"ISyncClient", b"shouldSynchronizeWithClientsOfType:", {"retval": {"type": "Z"}})
    r(
        b"ISyncManager",
        b"clientWithIdentifier:needsSyncing:",
        {"arguments": {3: {"type": "Z"}}},
    )
    r(b"ISyncManager", b"isEnabled", {"retval": {"type": "Z"}})
    r(b"ISyncManager", b"registerSchemaWithBundlePath:", {"retval": {"type": "Z"}})
    r(
        b"ISyncRecordSnapshot",
        b"recordIdentifierForReference:isModified:",
        {"arguments": {3: {"type": "^Z", "type_modifier": b"o"}}},
    )
    r(
        b"ISyncSession",
        b"beginSessionInBackgroundWithClient:entityNames:target:selector:",
        {"arguments": {5: {"sel_of_type": b"v@:@@"}}},
    )
    r(
        b"ISyncSession",
        b"beginSessionInBackgroundWithClient:entityNames:target:selector:lastAnchors:",
        {"arguments": {5: {"sel_of_type": b"v@:@@"}}},
    )
    r(
        b"ISyncSession",
        b"clientLostRecordWithIdentifier:shouldReplaceOnNextSync:",
        {"arguments": {3: {"type": "Z"}}},
    )
    r(b"ISyncSession", b"isCancelled", {"retval": {"type": "Z"}})
    r(
        b"ISyncSession",
        b"prepareToPullChangesForEntityNames:beforeDate:",
        {"retval": {"type": "Z"}},
    )
    r(
        b"ISyncSession",
        b"prepareToPullChangesInBackgroundForEntityNames:target:selector:",
        {"arguments": {4: {"sel_of_type": b"v@:@@"}}},
    )
    r(b"ISyncSession", b"shouldPullChangesForEntityName:", {"retval": {"type": "Z"}})
    r(b"ISyncSession", b"shouldPushAllRecordsForEntityName:", {"retval": {"type": "Z"}})
    r(b"ISyncSession", b"shouldPushChangesForEntityName:", {"retval": {"type": "Z"}})
    r(
        b"ISyncSession",
        b"shouldReplaceAllRecordsOnClientForEntityName:",
        {"retval": {"type": "Z"}},
    )
    r(b"ISyncSessionDriver", b"handlesSyncAlerts", {"retval": {"type": "Z"}})
    r(
        b"ISyncSessionDriver",
        b"setHandlesSyncAlerts:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"ISyncSessionDriver",
        b"startAsynchronousSync:",
        {"retval": {"type": "Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(b"ISyncSessionDriver", b"sync", {"retval": {"type": "Z"}})
    r(
        b"NSObject",
        b"applyChange:forEntityName:remappedRecordIdentifier:formattedRecord:error:",
        {
            "required": True,
            "retval": {"type": "i"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": "^@", "type_modifier": b"o"},
                5: {"type": "^@", "type_modifier": b"o"},
                6: {"type": "^@", "type_modifier": b"o"},
            },
        },
    )
    r(
        b"NSObject",
        b"attributedStringForIdentityPropertiesWithNames:inRecord:comparisonRecords:firstLineAttributes:secondLineAttributes:",
        {
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {"type": b"@"},
                6: {"type": b"@"},
            },
        },
    )
    r(
        b"NSObject",
        b"attributedStringForPropertiesWithNames:inRecord:comparisonRecords:defaultAttributes:",
        {
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {"type": b"@"},
            },
        },
    )
    r(
        b"NSObject",
        b"changedRecordsForEntityName:moreComing:error:",
        {
            "required": False,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": "^Z", "type_modifier": b"o"},
                4: {"type": "^@", "type_modifier": b"o"},
            },
        },
    )
    r(
        b"NSObject",
        b"changesForEntityName:moreComing:error:",
        {
            "required": False,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": "^Z", "type_modifier": b"o"},
                4: {"type": "^@", "type_modifier": b"o"},
            },
        },
    )
    r(
        b"NSObject",
        b"clientDescriptionURL",
        {"required": True, "retval": {"type": b"@"}},
    )
    r(b"NSObject", b"clientIdentifier", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"deleteAllRecordsForEntityName:error:",
        {
            "required": True,
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "^@", "type_modifier": b"o"}},
        },
    )
    r(b"NSObject", b"entityNamesToPull", {"required": False, "retval": {"type": b"@"}})
    r(b"NSObject", b"entityNamesToSync", {"required": False, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"identifiersForRecordsToDeleteForEntityName:moreComing:error:",
        {
            "required": False,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": "^Z", "type_modifier": b"o"},
                4: {"type": "^@", "type_modifier": b"o"},
            },
        },
    )
    r(
        b"NSObject",
        b"isEqual:",
        {"required": True, "retval": {"type": "Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"isRelationship", {"retval": {"type": "Z"}})
    r(b"NSObject", b"isRequired", {"retval": {"type": "Z"}})
    r(b"NSObject", b"isToMany", {"retval": {"type": "Z"}})
    r(
        b"NSObject",
        b"lastAnchorForEntityName:",
        {"required": False, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"managedObjectContextsToMonitorWhenSyncingPersistentStoreCoordinator:",
        {"required": False, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"managedObjectContextsToReloadAfterSyncingPersistentStoreCoordinator:",
        {"required": False, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"nextAnchorForEntityName:",
        {"required": False, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"persistentStoreCoordinator:didApplyChange:toManagedObject:inSyncSession:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {"type": b"@"},
            },
        },
    )
    r(
        b"NSObject",
        b"persistentStoreCoordinator:didCancelSyncSession:error:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"persistentStoreCoordinator:didCommitChanges:inSyncSession:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"persistentStoreCoordinator:didFinishSyncSession:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"persistentStoreCoordinator:didPullChangesInSyncSession:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"persistentStoreCoordinator:didPushChangesInSyncSession:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"persistentStoreCoordinator:willApplyChange:toManagedObject:inSyncSession:",
        {
            "required": False,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {"type": b"@"},
            },
        },
    )
    r(
        b"NSObject",
        b"persistentStoreCoordinator:willDeleteRecordWithIdentifier:inSyncSession:",
        {
            "required": False,
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"persistentStoreCoordinator:willPullChangesInSyncSession:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"persistentStoreCoordinator:willPushChangesInSyncSession:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"persistentStoreCoordinator:willPushRecord:forManagedObject:inSyncSession:",
        {
            "required": False,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {"type": b"@"},
            },
        },
    )
    r(
        b"NSObject",
        b"persistentStoreCoordinatorShouldStartSyncing:",
        {"required": False, "retval": {"type": "Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"preferredSyncModeForEntityName", {"retval": {"type": "i"}})
    r(
        b"NSObject",
        b"preferredSyncModeForEntityName:",
        {"required": True, "retval": {"type": b"I"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"recordsForEntityName:moreComing:error:",
        {
            "required": True,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": "^Z", "type_modifier": b"o"},
                4: {"type": "^@", "type_modifier": b"o"},
            },
        },
    )
    r(b"NSObject", b"schemaBundleURLs", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"sessionBeginTimeout",
        {"required": False, "retval": {"type": b"d"}},
    )
    r(
        b"NSObject",
        b"sessionDriver:didNegotiateAndReturnError:",
        {
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"sessionDriver:didPullAndReturnError:",
        {
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"sessionDriver:didPushAndReturnError:",
        {
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"sessionDriver:didReceiveSyncAlertAndReturnError:",
        {
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"sessionDriver:didRegisterClientAndReturnError:",
        {
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"sessionDriver:willFinishSessionAndReturnError:",
        {
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"sessionDriver:willNegotiateAndReturnError:",
        {
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"sessionDriver:willPullAndReturnError:",
        {
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"sessionDriver:willPushAndReturnError:",
        {
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"sessionDriverDidCancelSession:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"sessionDriverDidFinishSession:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"sessionDriverWillCancelSession:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"sessionPullChangesTimeout",
        {"required": False, "retval": {"type": b"d"}},
    )
    r(
        b"NSObject",
        b"shouldApplyRecord:withRecordIdentifier:",
        {
            "required": True,
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"supportedEntityNames",
        {"required": True, "retval": {"type": b"@"}},
    )
    r(
        b"NSPersistentStoreCoordinator",
        b"syncWithClient:inBackground:handler:error:",
        {
            "retval": {"type": "Z"},
            "arguments": {3: {"type": "Z"}, 5: {"type": "^@", "type_modifier": b"o"}},
        },
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector(
    "ISyncChange", b"initWithChangeType:recordIdentifier:changes:"
)
protocols = {
    "ISyncSessionDriverDelegate": objc.informal_protocol(
        "ISyncSessionDriverDelegate",
        [
            objc.selector(
                None,
                b"sessionDriver:willPullAndReturnError:",
                b"Z@:@^@",
                isRequired=False,
            ),
            objc.selector(
                None,
                b"sessionDriver:willPushAndReturnError:",
                b"Z@:@^@",
                isRequired=False,
            ),
            objc.selector(
                None,
                b"sessionDriver:didRegisterClientAndReturnError:",
                b"Z@:@^@",
                isRequired=False,
            ),
            objc.selector(
                None,
                b"sessionDriver:willFinishSessionAndReturnError:",
                b"Z@:@^@",
                isRequired=False,
            ),
            objc.selector(
                None,
                b"sessionDriver:willNegotiateAndReturnError:",
                b"Z@:@^@",
                isRequired=False,
            ),
            objc.selector(
                None,
                b"sessionDriver:didPullAndReturnError:",
                b"Z@:@^@",
                isRequired=False,
            ),
            objc.selector(
                None, b"sessionDriverDidFinishSession:", b"v@:@", isRequired=False
            ),
            objc.selector(
                None,
                b"sessionDriver:didNegotiateAndReturnError:",
                b"Z@:@^@",
                isRequired=False,
            ),
            objc.selector(
                None,
                b"sessionDriver:didPushAndReturnError:",
                b"Z@:@^@",
                isRequired=False,
            ),
            objc.selector(
                None,
                b"sessionDriver:didReceiveSyncAlertAndReturnError:",
                b"Z@:@^@",
                isRequired=False,
            ),
            objc.selector(
                None, b"sessionDriverWillCancelSession:", b"v@:@", isRequired=False
            ),
            objc.selector(
                None, b"sessionDriverDidCancelSession:", b"v@:@", isRequired=False
            ),
        ],
    ),
    "ISyncSessionDriverDataSourceOptionalMethods": objc.informal_protocol(
        "ISyncSessionDriverDataSourceOptionalMethods",
        [
            objc.selector(None, b"entityNamesToSync", b"@@:", isRequired=False),
            objc.selector(None, b"entityNamesToPull", b"@@:", isRequired=False),
            objc.selector(None, b"sessionBeginTimeout", b"d@:", isRequired=False),
            objc.selector(None, b"sessionPullChangesTimeout", b"d@:", isRequired=False),
            objc.selector(None, b"lastAnchorForEntityName:", b"@@:@", isRequired=False),
            objc.selector(None, b"nextAnchorForEntityName:", b"@@:@", isRequired=False),
            objc.selector(
                None,
                b"changedRecordsForEntityName:moreComing:error:",
                b"@@:@^Z^@",
                isRequired=False,
            ),
            objc.selector(
                None,
                b"changesForEntityName:moreComing:error:",
                b"@@:@^Z^@",
                isRequired=False,
            ),
            objc.selector(
                None,
                b"identifiersForRecordsToDeleteForEntityName:moreComing:error:",
                b"@@:@^Z^@",
                isRequired=False,
            ),
        ],
    ),
    "SyncUIHelperInformalProtocol": objc.informal_protocol(
        "SyncUIHelperInformalProtocol",
        [
            objc.selector(
                None,
                b"attributedStringForIdentityPropertiesWithNames:inRecord:comparisonRecords:firstLineAttributes:secondLineAttributes:",
                b"@@:@@@@@",
                isRequired=False,
            ),
            objc.selector(
                None,
                b"attributedStringForPropertiesWithNames:inRecord:comparisonRecords:defaultAttributes:",
                b"@@:@@@@",
                isRequired=False,
            ),
        ],
    ),
}
expressions = {}

# END OF FILE
