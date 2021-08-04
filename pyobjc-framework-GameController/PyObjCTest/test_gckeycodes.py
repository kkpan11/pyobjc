from PyObjCTools.TestSupport import TestCase, min_os_level
import GameController


class TestGCKeyCodes(TestCase):
    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(GameController.GCKeyCodeKeyA, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyB, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyC, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyD, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyE, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyF, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyG, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyH, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyI, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyJ, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyK, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyL, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyM, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyN, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyO, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyP, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyQ, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyR, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyS, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyT, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyU, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyV, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyW, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyX, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyY, int)
        self.assertIsInstance(GameController.GCKeyCodeKeyZ, int)
        self.assertIsInstance(GameController.GCKeyCodeOne, int)
        self.assertIsInstance(GameController.GCKeyCodeTwo, int)
        self.assertIsInstance(GameController.GCKeyCodeThree, int)
        self.assertIsInstance(GameController.GCKeyCodeFour, int)
        self.assertIsInstance(GameController.GCKeyCodeFive, int)
        self.assertIsInstance(GameController.GCKeyCodeSix, int)
        self.assertIsInstance(GameController.GCKeyCodeSeven, int)
        self.assertIsInstance(GameController.GCKeyCodeEight, int)
        self.assertIsInstance(GameController.GCKeyCodeNine, int)
        self.assertIsInstance(GameController.GCKeyCodeZero, int)
        self.assertIsInstance(GameController.GCKeyCodeReturnOrEnter, int)
        self.assertIsInstance(GameController.GCKeyCodeEscape, int)
        self.assertIsInstance(GameController.GCKeyCodeDeleteOrBackspace, int)
        self.assertIsInstance(GameController.GCKeyCodeTab, int)
        self.assertIsInstance(GameController.GCKeyCodeSpacebar, int)
        self.assertIsInstance(GameController.GCKeyCodeHyphen, int)
        self.assertIsInstance(GameController.GCKeyCodeEqualSign, int)
        self.assertIsInstance(GameController.GCKeyCodeOpenBracket, int)
        self.assertIsInstance(GameController.GCKeyCodeCloseBracket, int)
        self.assertIsInstance(GameController.GCKeyCodeBackslash, int)
        self.assertIsInstance(GameController.GCKeyCodeNonUSPound, int)
        self.assertIsInstance(GameController.GCKeyCodeSemicolon, int)
        self.assertIsInstance(GameController.GCKeyCodeQuote, int)
        self.assertIsInstance(GameController.GCKeyCodeGraveAccentAndTilde, int)
        self.assertIsInstance(GameController.GCKeyCodeComma, int)
        self.assertIsInstance(GameController.GCKeyCodePeriod, int)
        self.assertIsInstance(GameController.GCKeyCodeSlash, int)
        self.assertIsInstance(GameController.GCKeyCodeCapsLock, int)

        self.assertIsInstance(GameController.GCKeyCodeF1, int)
        self.assertIsInstance(GameController.GCKeyCodeF2, int)
        self.assertIsInstance(GameController.GCKeyCodeF3, int)
        self.assertIsInstance(GameController.GCKeyCodeF4, int)
        self.assertIsInstance(GameController.GCKeyCodeF5, int)
        self.assertIsInstance(GameController.GCKeyCodeF6, int)
        self.assertIsInstance(GameController.GCKeyCodeF7, int)
        self.assertIsInstance(GameController.GCKeyCodeF8, int)
        self.assertIsInstance(GameController.GCKeyCodeF9, int)
        self.assertIsInstance(GameController.GCKeyCodeF10, int)
        self.assertIsInstance(GameController.GCKeyCodeF11, int)
        self.assertIsInstance(GameController.GCKeyCodeF12, int)

        self.assertIsInstance(GameController.GCKeyCodePrintScreen, int)
        self.assertIsInstance(GameController.GCKeyCodeScrollLock, int)
        self.assertIsInstance(GameController.GCKeyCodePause, int)
        self.assertIsInstance(GameController.GCKeyCodeInsert, int)
        self.assertIsInstance(GameController.GCKeyCodeHome, int)
        self.assertIsInstance(GameController.GCKeyCodePageUp, int)
        self.assertIsInstance(GameController.GCKeyCodeDeleteForward, int)
        self.assertIsInstance(GameController.GCKeyCodeEnd, int)
        self.assertIsInstance(GameController.GCKeyCodePageDown, int)
        self.assertIsInstance(GameController.GCKeyCodeRightArrow, int)
        self.assertIsInstance(GameController.GCKeyCodeLeftArrow, int)
        self.assertIsInstance(GameController.GCKeyCodeDownArrow, int)
        self.assertIsInstance(GameController.GCKeyCodeUpArrow, int)

        self.assertIsInstance(GameController.GCKeyCodeKeypadNumLock, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypadSlash, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypadAsterisk, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypadHyphen, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypadPlus, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypadEnter, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypad1, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypad2, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypad3, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypad4, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypad5, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypad6, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypad7, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypad8, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypad9, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypad0, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypadPeriod, int)
        self.assertIsInstance(GameController.GCKeyCodeKeypadEqualSign, int)
        self.assertIsInstance(GameController.GCKeyCodeNonUSBackslash, int)

        self.assertIsInstance(GameController.GCKeyCodeApplication, int)
        self.assertIsInstance(GameController.GCKeyCodePower, int)

        self.assertIsInstance(GameController.GCKeyCodeInternational1, int)
        self.assertIsInstance(GameController.GCKeyCodeInternational2, int)
        self.assertIsInstance(GameController.GCKeyCodeInternational3, int)
        self.assertIsInstance(GameController.GCKeyCodeInternational4, int)
        self.assertIsInstance(GameController.GCKeyCodeInternational5, int)
        self.assertIsInstance(GameController.GCKeyCodeInternational6, int)
        self.assertIsInstance(GameController.GCKeyCodeInternational7, int)
        self.assertIsInstance(GameController.GCKeyCodeInternational8, int)
        self.assertIsInstance(GameController.GCKeyCodeInternational9, int)

        self.assertIsInstance(GameController.GCKeyCodeLANG1, int)

        self.assertIsInstance(GameController.GCKeyCodeLANG2, int)

        self.assertIsInstance(GameController.GCKeyCodeLANG3, int)

        self.assertIsInstance(GameController.GCKeyCodeLANG4, int)

        self.assertIsInstance(GameController.GCKeyCodeLANG5, int)

        self.assertIsInstance(GameController.GCKeyCodeLANG6, int)
        self.assertIsInstance(GameController.GCKeyCodeLANG7, int)
        self.assertIsInstance(GameController.GCKeyCodeLANG8, int)
        self.assertIsInstance(GameController.GCKeyCodeLANG9, int)

        self.assertIsInstance(GameController.GCKeyCodeLeftControl, int)
        self.assertIsInstance(GameController.GCKeyCodeLeftShift, int)
        self.assertIsInstance(GameController.GCKeyCodeLeftAlt, int)
        self.assertIsInstance(GameController.GCKeyCodeLeftGUI, int)
        self.assertIsInstance(GameController.GCKeyCodeRightControl, int)
        self.assertIsInstance(GameController.GCKeyCodeRightShift, int)
        self.assertIsInstance(GameController.GCKeyCodeRightAlt, int)
        self.assertIsInstance(GameController.GCKeyCodeRightGUI, int)
