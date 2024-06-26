import Security
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestSecImportExport(TestCase):
    def test_constants(self):
        self.assertEqual(Security.kSecFormatUnknown, 0)
        self.assertEqual(Security.kSecFormatOpenSSL, 1)
        self.assertEqual(Security.kSecFormatSSH, 2)
        self.assertEqual(Security.kSecFormatBSAFE, 3)
        self.assertEqual(Security.kSecFormatRawKey, 4)
        self.assertEqual(Security.kSecFormatWrappedPKCS8, 5)
        self.assertEqual(Security.kSecFormatWrappedOpenSSL, 6)
        self.assertEqual(Security.kSecFormatWrappedSSH, 7)
        self.assertEqual(Security.kSecFormatWrappedLSH, 8)
        self.assertEqual(Security.kSecFormatX509Cert, 9)
        self.assertEqual(Security.kSecFormatPEMSequence, 10)
        self.assertEqual(Security.kSecFormatPKCS7, 11)
        self.assertEqual(Security.kSecFormatPKCS12, 12)
        self.assertEqual(Security.kSecFormatNetscapeCertSequence, 13)
        self.assertEqual(Security.kSecFormatSSHv2, 14)

        self.assertEqual(Security.kSecItemTypeUnknown, 0)
        self.assertEqual(Security.kSecItemTypePrivateKey, 1)
        self.assertEqual(Security.kSecItemTypePublicKey, 2)
        self.assertEqual(Security.kSecItemTypeSessionKey, 3)
        self.assertEqual(Security.kSecItemTypeCertificate, 4)
        self.assertEqual(Security.kSecItemTypeAggregate, 5)

        self.assertEqual(Security.kSecItemPemArmour, 0x00000001)

        self.assertEqual(Security.kSecKeyImportOnlyOne, 0x00000001)
        self.assertEqual(Security.kSecKeySecurePassphrase, 0x00000002)
        self.assertEqual(Security.kSecKeyNoAccessControl, 0x00000004)

        self.assertEqual(Security.SEC_KEY_IMPORT_EXPORT_PARAMS_VERSION, 0)

        self.assertIsInstance(Security.kSecImportExportPassphrase, str)
        self.assertIsInstance(Security.kSecImportExportKeychain, str)
        self.assertIsInstance(Security.kSecImportExportAccess, str)

        self.assertIsInstance(Security.kSecImportItemLabel, str)
        self.assertIsInstance(Security.kSecImportItemKeyID, str)
        self.assertIsInstance(Security.kSecImportItemTrust, str)
        self.assertIsInstance(Security.kSecImportItemCertChain, str)
        self.assertIsInstance(Security.kSecImportItemIdentity, str)

    @min_os_level("15.0")
    def test_constants15_0(self):
        self.assertIsInstance(Security.kSecImportToMemoryOnly, str)

    def test_structs(self):
        v = Security.SecItemImportExportKeyParameters()
        self.assertEqual(v.version, 0)
        self.assertEqual(v.flags, 0)
        self.assertEqual(v.passphrase, None)
        self.assertEqual(v.alertTitle, None)
        self.assertEqual(v.alertPrompt, None)
        self.assertEqual(v.accessRef, None)
        self.assertEqual(v.keyUsage, None)
        self.assertEqual(v.keyAttributes, None)
        self.assertPickleRoundTrips(v)

    def test_functions(self):
        self.assertArgIsIn(Security.SecKeychainItemExport, 3)
        self.assertArgIsOut(Security.SecKeychainItemExport, 4)
        self.assertArgIsCFRetained(Security.SecKeychainItemExport, 4)

        self.assertArgIsInOut(Security.SecKeychainItemImport, 2)
        self.assertArgIsInOut(Security.SecKeychainItemImport, 3)
        self.assertArgIsIn(Security.SecKeychainItemImport, 5)
        self.assertArgIsCFRetained(Security.SecKeychainItemImport, 7)

        self.assertResultHasType(Security.SecItemExport, objc._C_INT)
        self.assertArgHasType(Security.SecItemExport, 0, objc._C_ID)
        self.assertArgHasType(Security.SecItemExport, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecItemExport, 2, objc._C_UINT)
        self.assertArgHasType(
            Security.SecItemExport,
            3,
            objc._C_IN
            + objc._C_PTR
            + Security.SecItemImportExportKeyParameters.__typestr__,
        )
        self.assertArgHasType(
            Security.SecItemExport, 4, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecItemExport, 4)

        self.assertResultHasType(Security.SecItemImport, objc._C_INT)
        self.assertArgHasType(Security.SecItemImport, 0, objc._C_ID)
        self.assertArgHasType(Security.SecItemImport, 1, objc._C_ID)
        self.assertArgHasType(
            Security.SecItemImport, 2, objc._C_INOUT + objc._C_PTR + objc._C_UINT
        )
        self.assertArgHasType(
            Security.SecItemImport, 3, objc._C_INOUT + objc._C_PTR + objc._C_UINT
        )
        self.assertArgHasType(Security.SecItemImport, 4, objc._C_UINT)
        self.assertArgHasType(
            Security.SecItemImport,
            5,
            objc._C_IN
            + objc._C_PTR
            + Security.SecItemImportExportKeyParameters.__typestr__,
        )
        self.assertArgHasType(Security.SecItemImport, 6, objc._C_ID)
        self.assertArgHasType(
            Security.SecItemImport, 7, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecItemImport, 7)

        self.assertResultHasType(Security.SecPKCS12Import, objc._C_INT)
        self.assertArgHasType(Security.SecPKCS12Import, 0, objc._C_ID)
        self.assertArgHasType(Security.SecPKCS12Import, 1, objc._C_ID)
        self.assertArgHasType(
            Security.SecPKCS12Import, 2, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecPKCS12Import, 2)
