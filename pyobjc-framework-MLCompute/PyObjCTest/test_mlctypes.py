from PyObjCTools.TestSupport import TestCase

import MLCompute


class MLCTypes(TestCase):
    def test_constants(self):
        self.assertEqual(MLCompute.MLCDataTypeInvalid, 0)
        self.assertEqual(MLCompute.MLCDataTypeFloat32, 1)
        self.assertEqual(MLCompute.MLCDataTypeBoolean, 4)
        self.assertEqual(MLCompute.MLCDataTypeInt64, 5)
        self.assertEqual(MLCompute.MLCDataTypeCount, 6)

        self.assertEqual(MLCompute.MLCRandomInitializerTypeInvalid, 0)
        self.assertEqual(MLCompute.MLCRandomInitializerTypeUniform, 1)
        self.assertEqual(MLCompute.MLCRandomInitializerTypeGlorotUniform, 2)
        self.assertEqual(MLCompute.MLCRandomInitializerTypeXavier, 3)
        self.assertEqual(MLCompute.MLCRandomInitializerTypeCount, 4)

        self.assertEqual(MLCompute.MLCDeviceTypeCPU, 0)
        self.assertEqual(MLCompute.MLCDeviceTypeGPU, 1)
        self.assertEqual(MLCompute.MLCDeviceTypeAny, 2)
        self.assertEqual(MLCompute.MLCDeviceTypeCount, 3)

        self.assertEqual(MLCompute.MLCGraphCompilationOptionsNone, 0x00)
        self.assertEqual(MLCompute.MLCGraphCompilationOptionsDebugLayers, 0x01)
        self.assertEqual(MLCompute.MLCGraphCompilationOptionsDisableLayerFusion, 0x02)
        self.assertEqual(MLCompute.MLCGraphCompilationOptionsLinkGraphs, 0x04)
        self.assertEqual(MLCompute.MLCGraphCompilationOptionsComputeAllGradients, 0x08)

        self.assertEqual(MLCompute.MLCExecutionOptionsNone, 0x00)
        self.assertEqual(
            MLCompute.MLCExecutionOptionsSkipWritingInputDataToDevice, 0x01
        )
        self.assertEqual(MLCompute.MLCExecutionOptionsSynchronous, 0x02)
        self.assertEqual(MLCompute.MLCExecutionOptionsProfiling, 0x04)
        self.assertEqual(MLCompute.MLCExecutionOptionsForwardForInference, 0x08)

        self.assertEqual(MLCompute.MLCArithmeticOperationAdd, 0)
        self.assertEqual(MLCompute.MLCArithmeticOperationSubtract, 1)
        self.assertEqual(MLCompute.MLCArithmeticOperationMultiply, 2)
        self.assertEqual(MLCompute.MLCArithmeticOperationDivide, 3)
        self.assertEqual(MLCompute.MLCArithmeticOperationFloor, 4)
        self.assertEqual(MLCompute.MLCArithmeticOperationRound, 5)
        self.assertEqual(MLCompute.MLCArithmeticOperationCeil, 6)
        self.assertEqual(MLCompute.MLCArithmeticOperationSqrt, 7)
        self.assertEqual(MLCompute.MLCArithmeticOperationRsqrt, 8)
        self.assertEqual(MLCompute.MLCArithmeticOperationSin, 9)
        self.assertEqual(MLCompute.MLCArithmeticOperationCos, 10)
        self.assertEqual(MLCompute.MLCArithmeticOperationTan, 11)
        self.assertEqual(MLCompute.MLCArithmeticOperationAsin, 12)
        self.assertEqual(MLCompute.MLCArithmeticOperationAcos, 13)
        self.assertEqual(MLCompute.MLCArithmeticOperationAtan, 14)
        self.assertEqual(MLCompute.MLCArithmeticOperationSinh, 15)
        self.assertEqual(MLCompute.MLCArithmeticOperationCosh, 16)
        self.assertEqual(MLCompute.MLCArithmeticOperationTanh, 17)
        self.assertEqual(MLCompute.MLCArithmeticOperationAsinh, 18)
        self.assertEqual(MLCompute.MLCArithmeticOperationAcosh, 19)
        self.assertEqual(MLCompute.MLCArithmeticOperationAtanh, 20)
        self.assertEqual(MLCompute.MLCArithmeticOperationPow, 21)
        self.assertEqual(MLCompute.MLCArithmeticOperationExp, 22)
        self.assertEqual(MLCompute.MLCArithmeticOperationExp2, 23)
        self.assertEqual(MLCompute.MLCArithmeticOperationLog, 24)
        self.assertEqual(MLCompute.MLCArithmeticOperationLog2, 25)
        self.assertEqual(MLCompute.MLCArithmeticOperationCount, 26)

        self.assertEqual(MLCompute.MLCLossTypeMeanAbsoluteError, 0)
        self.assertEqual(MLCompute.MLCLossTypeMeanSquaredError, 1)
        self.assertEqual(MLCompute.MLCLossTypeSoftmaxCrossEntropy, 2)
        self.assertEqual(MLCompute.MLCLossTypeSigmoidCrossEntropy, 3)
        self.assertEqual(MLCompute.MLCLossTypeCategoricalCrossEntropy, 4)
        self.assertEqual(MLCompute.MLCLossTypeHinge, 5)
        self.assertEqual(MLCompute.MLCLossTypeHuber, 6)
        self.assertEqual(MLCompute.MLCLossTypeCosineDistance, 7)
        self.assertEqual(MLCompute.MLCLossTypeLog, 8)
        self.assertEqual(MLCompute.MLCLossTypeCount, 9)

        self.assertEqual(MLCompute.MLCActivationTypeNone, 0)
        self.assertEqual(MLCompute.MLCActivationTypeReLU, 1)
        self.assertEqual(MLCompute.MLCActivationTypeLinear, 2)
        self.assertEqual(MLCompute.MLCActivationTypeSigmoid, 3)
        self.assertEqual(MLCompute.MLCActivationTypeHardSigmoid, 4)
        self.assertEqual(MLCompute.MLCActivationTypeTanh, 5)
        self.assertEqual(MLCompute.MLCActivationTypeAbsolute, 6)
        self.assertEqual(MLCompute.MLCActivationTypeSoftPlus, 7)
        self.assertEqual(MLCompute.MLCActivationTypeSoftSign, 8)
        self.assertEqual(MLCompute.MLCActivationTypeELU, 9)
        self.assertEqual(MLCompute.MLCActivationTypeReLUN, 10)
        self.assertEqual(MLCompute.MLCActivationTypeLogSigmoid, 11)
        self.assertEqual(MLCompute.MLCActivationTypeSELU, 12)
        self.assertEqual(MLCompute.MLCActivationTypeCELU, 13)
        self.assertEqual(MLCompute.MLCActivationTypeHardShrink, 14)
        self.assertEqual(MLCompute.MLCActivationTypeSoftShrink, 15)
        self.assertEqual(MLCompute.MLCActivationTypeTanhShrink, 16)
        self.assertEqual(MLCompute.MLCActivationTypeThreshold, 17)
        self.assertEqual(MLCompute.MLCActivationTypeGELU, 18)
        self.assertEqual(MLCompute.MLCActivationTypeCount, 19)

        self.assertEqual(MLCompute.MLCConvolutionTypeStandard, 0)
        self.assertEqual(MLCompute.MLCConvolutionTypeTransposed, 1)
        self.assertEqual(MLCompute.MLCConvolutionTypeDepthwise, 2)

        self.assertEqual(MLCompute.MLCPaddingPolicySame, 0)
        self.assertEqual(MLCompute.MLCPaddingPolicyValid, 1)
        self.assertEqual(MLCompute.MLCPaddingPolicyUsePaddingSize, 2)

        self.assertEqual(MLCompute.MLCPaddingTypeZero, 0)
        self.assertEqual(MLCompute.MLCPaddingTypeReflect, 1)
        self.assertEqual(MLCompute.MLCPaddingTypeSymmetric, 2)
        self.assertEqual(MLCompute.MLCPaddingTypeConstant, 3)

        self.assertEqual(MLCompute.MLCPoolingTypeMax, 1)
        self.assertEqual(MLCompute.MLCPoolingTypeAverage, 2)
        self.assertEqual(MLCompute.MLCPoolingTypeL2Norm, 3)
        self.assertEqual(MLCompute.MLCPoolingTypeCount, 4)

        self.assertEqual(MLCompute.MLCReductionTypeNone, 0)
        self.assertEqual(MLCompute.MLCReductionTypeSum, 1)
        self.assertEqual(MLCompute.MLCReductionTypeMean, 2)
        self.assertEqual(MLCompute.MLCReductionTypeMax, 3)
        self.assertEqual(MLCompute.MLCReductionTypeMin, 4)
        self.assertEqual(MLCompute.MLCReductionTypeArgMax, 5)
        self.assertEqual(MLCompute.MLCReductionTypeArgMin, 6)
        self.assertEqual(MLCompute.MLCReductionTypeCount, 7)

        self.assertEqual(MLCompute.MLCRegularizationTypeNone, 0)
        self.assertEqual(MLCompute.MLCRegularizationTypeL1, 1)
        self.assertEqual(MLCompute.MLCRegularizationTypeL2, 2)

        self.assertEqual(MLCompute.MLCSampleModeNearest, 0)
        self.assertEqual(MLCompute.MLCSampleModeLinear, 1)

        self.assertEqual(MLCompute.MLCSoftmaxOperationSoftmax, 0)
        self.assertEqual(MLCompute.MLCSoftmaxOperationLogSoftmax, 1)

        self.assertEqual(MLCompute.MLCLSTMResultModeOutput, 0x00)
        self.assertEqual(MLCompute.MLCLSTMResultModeOutputAndStates, 0x01)

    def test_functions(self):
        MLCompute.MLCActivationTypeDebugDescription
        MLCompute.MLCArithmeticOperationDebugDescription
        MLCompute.MLCPaddingPolicyDebugDescription
        MLCompute.MLCLossTypeDebugDescription
        MLCompute.MLCReductionTypeDebugDescription
        MLCompute.MLCPaddingTypeDebugDescription
        MLCompute.MLCConvolutionTypeDebugDescription
        MLCompute.MLCPoolingTypeDebugDescription
        MLCompute.MLCSoftmaxOperationDebugDescription
        MLCompute.MLCSampleModeDebugDescription
