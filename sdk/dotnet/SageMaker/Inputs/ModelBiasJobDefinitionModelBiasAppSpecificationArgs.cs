// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html
    /// </summary>
    public sealed class ModelBiasJobDefinitionModelBiasAppSpecificationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-configuri
        /// </summary>
        [Input("configUri", required: true)]
        public Input<string> ConfigUri { get; set; } = null!;

        [Input("environment")]
        private InputMap<string>? _environment;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-environment
        /// </summary>
        public InputMap<string> Environment
        {
            get => _environment ?? (_environment = new InputMap<string>());
            set => _environment = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-imageuri
        /// </summary>
        [Input("imageUri", required: true)]
        public Input<string> ImageUri { get; set; } = null!;

        public ModelBiasJobDefinitionModelBiasAppSpecificationArgs()
        {
        }
    }
}
