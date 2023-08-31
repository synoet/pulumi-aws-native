// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker
{
    /// <summary>
    /// Resource Type definition for AWS::SageMaker::EndpointConfig
    /// </summary>
    [Obsolete(@"EndpointConfig is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:sagemaker:EndpointConfig")]
    public partial class EndpointConfig : global::Pulumi.CustomResource
    {
        [Output("asyncInferenceConfig")]
        public Output<Outputs.EndpointConfigAsyncInferenceConfig?> AsyncInferenceConfig { get; private set; } = null!;

        [Output("dataCaptureConfig")]
        public Output<Outputs.EndpointConfigDataCaptureConfig?> DataCaptureConfig { get; private set; } = null!;

        [Output("endpointConfigName")]
        public Output<string?> EndpointConfigName { get; private set; } = null!;

        [Output("explainerConfig")]
        public Output<Outputs.EndpointConfigExplainerConfig?> ExplainerConfig { get; private set; } = null!;

        [Output("kmsKeyId")]
        public Output<string?> KmsKeyId { get; private set; } = null!;

        [Output("productionVariants")]
        public Output<ImmutableArray<Outputs.EndpointConfigProductionVariant>> ProductionVariants { get; private set; } = null!;

        [Output("shadowProductionVariants")]
        public Output<ImmutableArray<Outputs.EndpointConfigProductionVariant>> ShadowProductionVariants { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.EndpointConfigTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a EndpointConfig resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public EndpointConfig(string name, EndpointConfigArgs args, CustomResourceOptions? options = null)
            : base("aws-native:sagemaker:EndpointConfig", name, args ?? new EndpointConfigArgs(), MakeResourceOptions(options, ""))
        {
        }

        private EndpointConfig(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:sagemaker:EndpointConfig", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "asyncInferenceConfig",
                    "dataCaptureConfig",
                    "endpointConfigName",
                    "explainerConfig",
                    "kmsKeyId",
                    "productionVariants[*]",
                    "shadowProductionVariants[*]",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing EndpointConfig resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static EndpointConfig Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new EndpointConfig(name, id, options);
        }
    }

    public sealed class EndpointConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("asyncInferenceConfig")]
        public Input<Inputs.EndpointConfigAsyncInferenceConfigArgs>? AsyncInferenceConfig { get; set; }

        [Input("dataCaptureConfig")]
        public Input<Inputs.EndpointConfigDataCaptureConfigArgs>? DataCaptureConfig { get; set; }

        [Input("endpointConfigName")]
        public Input<string>? EndpointConfigName { get; set; }

        [Input("explainerConfig")]
        public Input<Inputs.EndpointConfigExplainerConfigArgs>? ExplainerConfig { get; set; }

        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        [Input("productionVariants", required: true)]
        private InputList<Inputs.EndpointConfigProductionVariantArgs>? _productionVariants;
        public InputList<Inputs.EndpointConfigProductionVariantArgs> ProductionVariants
        {
            get => _productionVariants ?? (_productionVariants = new InputList<Inputs.EndpointConfigProductionVariantArgs>());
            set => _productionVariants = value;
        }

        [Input("shadowProductionVariants")]
        private InputList<Inputs.EndpointConfigProductionVariantArgs>? _shadowProductionVariants;
        public InputList<Inputs.EndpointConfigProductionVariantArgs> ShadowProductionVariants
        {
            get => _shadowProductionVariants ?? (_shadowProductionVariants = new InputList<Inputs.EndpointConfigProductionVariantArgs>());
            set => _shadowProductionVariants = value;
        }

        [Input("tags")]
        private InputList<Inputs.EndpointConfigTagArgs>? _tags;
        public InputList<Inputs.EndpointConfigTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.EndpointConfigTagArgs>());
            set => _tags = value;
        }

        public EndpointConfigArgs()
        {
        }
        public static new EndpointConfigArgs Empty => new EndpointConfigArgs();
    }
}
