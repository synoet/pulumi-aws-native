// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.SageMaker.Outputs
{

    [OutputType]
    public sealed class EndpointConfigProductionVariant
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-acceleratortype
        /// </summary>
        public readonly string? AcceleratorType;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-initialinstancecount
        /// </summary>
        public readonly int InitialInstanceCount;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-initialvariantweight
        /// </summary>
        public readonly double InitialVariantWeight;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-instancetype
        /// </summary>
        public readonly string InstanceType;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-modelname
        /// </summary>
        public readonly string ModelName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-variantname
        /// </summary>
        public readonly string VariantName;

        [OutputConstructor]
        private EndpointConfigProductionVariant(
            string? AcceleratorType,

            int InitialInstanceCount,

            double InitialVariantWeight,

            string InstanceType,

            string ModelName,

            string VariantName)
        {
            this.AcceleratorType = AcceleratorType;
            this.InitialInstanceCount = InitialInstanceCount;
            this.InitialVariantWeight = InitialVariantWeight;
            this.InstanceType = InstanceType;
            this.ModelName = ModelName;
            this.VariantName = VariantName;
        }
    }
}