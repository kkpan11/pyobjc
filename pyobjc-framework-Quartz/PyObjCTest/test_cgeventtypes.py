from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCGEventTypes(TestCase):
    def testTypes(self):
        self.assertIsCFType(Quartz.CGEventRef)
        self.assertIsCFType(Quartz.CGEventSourceRef)

    def testConstants(self):
        self.assertEqual(Quartz.kCGMomentumScrollPhaseNone, 0)
        self.assertEqual(Quartz.kCGMomentumScrollPhaseBegin, 1)
        self.assertEqual(Quartz.kCGMomentumScrollPhaseContinue, 2)
        self.assertEqual(Quartz.kCGMomentumScrollPhaseEnd, 3)

        self.assertEqual(Quartz.kCGScrollPhaseBegan, 1)
        self.assertEqual(Quartz.kCGScrollPhaseChanged, 2)
        self.assertEqual(Quartz.kCGScrollPhaseEnded, 4)
        self.assertEqual(Quartz.kCGScrollPhaseCancelled, 8)
        self.assertEqual(Quartz.kCGScrollPhaseMayBegin, 128)

        self.assertEqual(Quartz.kCGGesturePhaseNone, 0)
        self.assertEqual(Quartz.kCGGesturePhaseBegan, 1)
        self.assertEqual(Quartz.kCGGesturePhaseChanged, 2)
        self.assertEqual(Quartz.kCGGesturePhaseEnded, 4)
        self.assertEqual(Quartz.kCGGesturePhaseCancelled, 8)
        self.assertEqual(Quartz.kCGGesturePhaseMayBegin, 128)

        self.assertEqual(Quartz.kCGMouseButtonLeft, 0)
        self.assertEqual(Quartz.kCGMouseButtonRight, 1)
        self.assertEqual(Quartz.kCGMouseButtonCenter, 2)

        self.assertEqual(Quartz.kCGScrollEventUnitPixel, 0)
        self.assertEqual(Quartz.kCGScrollEventUnitLine, 1)

        self.assertEqual(Quartz.kCGEventFlagMaskAlphaShift, 0x00010000)
        self.assertEqual(Quartz.kCGEventFlagMaskShift, 0x00020000)
        self.assertEqual(Quartz.kCGEventFlagMaskControl, 0x00040000)
        self.assertEqual(Quartz.kCGEventFlagMaskAlternate, 0x00080000)
        self.assertEqual(Quartz.kCGEventFlagMaskCommand, 0x00100000)
        self.assertEqual(Quartz.kCGEventFlagMaskHelp, 0x00400000)
        self.assertEqual(Quartz.kCGEventFlagMaskSecondaryFn, 0x00800000)
        self.assertEqual(Quartz.kCGEventFlagMaskNumericPad, 0x00200000)
        self.assertEqual(Quartz.kCGEventFlagMaskNonCoalesced, 0x00000100)

        self.assertEqual(Quartz.kCGEventNull, 0)
        self.assertEqual(Quartz.kCGEventLeftMouseDown, 1)
        self.assertEqual(Quartz.kCGEventLeftMouseUp, 2)
        self.assertEqual(Quartz.kCGEventRightMouseDown, 3)
        self.assertEqual(Quartz.kCGEventRightMouseUp, 4)
        self.assertEqual(Quartz.kCGEventMouseMoved, 5)
        self.assertEqual(Quartz.kCGEventLeftMouseDragged, 6)
        self.assertEqual(Quartz.kCGEventRightMouseDragged, 7)
        self.assertEqual(Quartz.kCGEventKeyDown, 10)
        self.assertEqual(Quartz.kCGEventKeyUp, 11)
        self.assertEqual(Quartz.kCGEventFlagsChanged, 12)
        self.assertEqual(Quartz.kCGEventScrollWheel, 22)
        self.assertEqual(Quartz.kCGEventTabletPointer, 23)
        self.assertEqual(Quartz.kCGEventTabletProximity, 24)
        self.assertEqual(Quartz.kCGEventOtherMouseDown, 25)
        self.assertEqual(Quartz.kCGEventOtherMouseUp, 26)
        self.assertEqual(Quartz.kCGEventOtherMouseDragged, 27)
        self.assertEqual(Quartz.kCGEventTapDisabledByTimeout, 0xFFFFFFFE)
        self.assertEqual(Quartz.kCGEventTapDisabledByUserInput, 0xFFFFFFFF)

        self.assertEqual(Quartz.kCGMouseEventNumber, 0)
        self.assertEqual(Quartz.kCGMouseEventClickState, 1)
        self.assertEqual(Quartz.kCGMouseEventPressure, 2)
        self.assertEqual(Quartz.kCGMouseEventButtonNumber, 3)
        self.assertEqual(Quartz.kCGMouseEventDeltaX, 4)
        self.assertEqual(Quartz.kCGMouseEventDeltaY, 5)
        self.assertEqual(Quartz.kCGMouseEventInstantMouser, 6)
        self.assertEqual(Quartz.kCGMouseEventSubtype, 7)
        self.assertEqual(Quartz.kCGKeyboardEventAutorepeat, 8)
        self.assertEqual(Quartz.kCGKeyboardEventKeycode, 9)
        self.assertEqual(Quartz.kCGKeyboardEventKeyboardType, 10)
        self.assertEqual(Quartz.kCGScrollWheelEventDeltaAxis1, 11)
        self.assertEqual(Quartz.kCGScrollWheelEventDeltaAxis2, 12)
        self.assertEqual(Quartz.kCGScrollWheelEventDeltaAxis3, 13)
        self.assertEqual(Quartz.kCGScrollWheelEventFixedPtDeltaAxis1, 93)
        self.assertEqual(Quartz.kCGScrollWheelEventFixedPtDeltaAxis2, 94)
        self.assertEqual(Quartz.kCGScrollWheelEventFixedPtDeltaAxis3, 95)
        self.assertEqual(Quartz.kCGScrollWheelEventPointDeltaAxis1, 96)
        self.assertEqual(Quartz.kCGScrollWheelEventPointDeltaAxis2, 97)
        self.assertEqual(Quartz.kCGScrollWheelEventPointDeltaAxis3, 98)
        self.assertEqual(Quartz.kCGScrollWheelEventScrollPhase, 99)
        self.assertEqual(Quartz.kCGScrollWheelEventScrollCount, 100)
        self.assertEqual(Quartz.kCGScrollWheelEventMomentumPhase, 123)
        self.assertEqual(Quartz.kCGScrollWheelEventInstantMouser, 14)
        self.assertEqual(Quartz.kCGTabletEventPointX, 15)
        self.assertEqual(Quartz.kCGTabletEventPointY, 16)
        self.assertEqual(Quartz.kCGTabletEventPointZ, 17)
        self.assertEqual(Quartz.kCGTabletEventPointButtons, 18)
        self.assertEqual(Quartz.kCGTabletEventPointPressure, 19)
        self.assertEqual(Quartz.kCGTabletEventTiltX, 20)
        self.assertEqual(Quartz.kCGTabletEventTiltY, 21)
        self.assertEqual(Quartz.kCGTabletEventRotation, 22)
        self.assertEqual(Quartz.kCGTabletEventTangentialPressure, 23)
        self.assertEqual(Quartz.kCGTabletEventDeviceID, 24)
        self.assertEqual(Quartz.kCGTabletEventVendor1, 25)
        self.assertEqual(Quartz.kCGTabletEventVendor2, 26)
        self.assertEqual(Quartz.kCGTabletEventVendor3, 27)
        self.assertEqual(Quartz.kCGTabletProximityEventVendorID, 28)
        self.assertEqual(Quartz.kCGTabletProximityEventTabletID, 29)
        self.assertEqual(Quartz.kCGTabletProximityEventPointerID, 30)
        self.assertEqual(Quartz.kCGTabletProximityEventDeviceID, 31)
        self.assertEqual(Quartz.kCGTabletProximityEventSystemTabletID, 32)
        self.assertEqual(Quartz.kCGTabletProximityEventVendorPointerType, 33)
        self.assertEqual(Quartz.kCGTabletProximityEventVendorPointerSerialNumber, 34)
        self.assertEqual(Quartz.kCGTabletProximityEventVendorUniqueID, 35)
        self.assertEqual(Quartz.kCGTabletProximityEventCapabilityMask, 36)
        self.assertEqual(Quartz.kCGTabletProximityEventPointerType, 37)
        self.assertEqual(Quartz.kCGTabletProximityEventEnterProximity, 38)
        self.assertEqual(Quartz.kCGEventTargetProcessSerialNumber, 39)
        self.assertEqual(Quartz.kCGEventTargetUnixProcessID, 40)
        self.assertEqual(Quartz.kCGEventSourceUnixProcessID, 41)
        self.assertEqual(Quartz.kCGEventSourceUserData, 42)
        self.assertEqual(Quartz.kCGEventSourceUserID, 43)
        self.assertEqual(Quartz.kCGEventSourceGroupID, 44)
        self.assertEqual(Quartz.kCGEventSourceStateID, 45)
        self.assertEqual(Quartz.kCGScrollWheelEventIsContinuous, 88)
        self.assertEqual(Quartz.kCGMouseEventWindowUnderMousePointer, 91)
        self.assertEqual(
            Quartz.kCGMouseEventWindowUnderMousePointerThatCanHandleThisEvent, 92
        )
        self.assertEqual(Quartz.kCGEventUnacceleratedPointerMovementX, 170)
        self.assertEqual(Quartz.kCGEventUnacceleratedPointerMovementY, 171)
        self.assertEqual(Quartz.kCGScrollWheelEventMomentumOptionPhase, 173)
        self.assertEqual(Quartz.kCGScrollWheelEventAcceleratedDeltaAxis1, 176)
        self.assertEqual(Quartz.kCGScrollWheelEventAcceleratedDeltaAxis2, 175)
        self.assertEqual(Quartz.kCGScrollWheelEventRawDeltaAxis1, 178)
        self.assertEqual(Quartz.kCGScrollWheelEventRawDeltaAxis2, 177)

        self.assertEqual(Quartz.kCGEventMouseSubtypeDefault, 0)
        self.assertEqual(Quartz.kCGEventMouseSubtypeTabletPoint, 1)
        self.assertEqual(Quartz.kCGEventMouseSubtypeTabletProximity, 2)

        self.assertEqual(Quartz.kCGHIDEventTap, 0)
        self.assertEqual(Quartz.kCGSessionEventTap, 1)
        self.assertEqual(Quartz.kCGAnnotatedSessionEventTap, 2)

        self.assertEqual(Quartz.kCGHeadInsertEventTap, 0)
        self.assertEqual(Quartz.kCGTailAppendEventTap, 1)

        self.assertEqual(Quartz.kCGEventTapOptionDefault, 0x00000000)
        self.assertEqual(Quartz.kCGEventTapOptionListenOnly, 0x00000001)

        self.assertEqual(
            Quartz.kCGNotifyEventTapAdded, b"com.apple.coregraphics.eventTapAdded"
        )
        self.assertEqual(
            Quartz.kCGNotifyEventTapRemoved, b"com.apple.coregraphics.eventTapRemoved"
        )

        self.assertEqual(Quartz.kCGEventSourceStatePrivate, -1)
        self.assertEqual(Quartz.kCGEventSourceStateCombinedSessionState, 0)
        self.assertEqual(Quartz.kCGEventSourceStateHIDSystemState, 1)

        self.assertEqual(Quartz.kCGAnyInputEventType, 0xFFFFFFFF)
        self.assertEqual(Quartz.kCGEventMaskForAllEvents, 0xFFFFFFFFFFFFFFFF)

    def testStructs(self):
        v = Quartz.CGEventTapInformation()
        self.assertTrue(hasattr(v, "eventTapID"))
        self.assertTrue(hasattr(v, "tapPoint"))
        self.assertTrue(hasattr(v, "options"))
        self.assertTrue(hasattr(v, "eventsOfInterest"))
        self.assertTrue(hasattr(v, "tappingProcess"))
        self.assertTrue(hasattr(v, "processBeingTapped"))
        self.assertTrue(hasattr(v, "enabled"))
        self.assertTrue(hasattr(v, "minUsecLatency"))
        self.assertTrue(hasattr(v, "avgUsecLatency"))
        self.assertTrue(hasattr(v, "maxUsecLatency"))
        self.assertPickleRoundTrips(v)

    def testInline(self):
        self.assertEqual(Quartz.CGEventMaskBit(10), 1 << 10)
