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
    /// Resource Type definition for AWS::SageMaker::ModelPackage
    /// </summary>
    [AwsNativeResourceType("aws-native:sagemaker:ModelPackage")]
    public partial class ModelPackage : global::Pulumi.CustomResource
    {
        [Output("additionalInferenceSpecifications")]
        public Output<ImmutableArray<Outputs.ModelPackageAdditionalInferenceSpecificationDefinition>> AdditionalInferenceSpecifications { get; private set; } = null!;

        [Output("additionalInferenceSpecificationsToAdd")]
        public Output<ImmutableArray<Outputs.ModelPackageAdditionalInferenceSpecificationDefinition>> AdditionalInferenceSpecificationsToAdd { get; private set; } = null!;

        [Output("approvalDescription")]
        public Output<string?> ApprovalDescription { get; private set; } = null!;

        [Output("certifyForMarketplace")]
        public Output<bool?> CertifyForMarketplace { get; private set; } = null!;

        [Output("clientToken")]
        public Output<string?> ClientToken { get; private set; } = null!;

        [Output("creationTime")]
        public Output<string> CreationTime { get; private set; } = null!;

        [Output("customerMetadataProperties")]
        public Output<Outputs.ModelPackageCustomerMetadataProperties?> CustomerMetadataProperties { get; private set; } = null!;

        [Output("domain")]
        public Output<string?> Domain { get; private set; } = null!;

        [Output("driftCheckBaselines")]
        public Output<Outputs.ModelPackageDriftCheckBaselines?> DriftCheckBaselines { get; private set; } = null!;

        [Output("inferenceSpecification")]
        public Output<Outputs.ModelPackageInferenceSpecification?> InferenceSpecification { get; private set; } = null!;

        [Output("lastModifiedTime")]
        public Output<string?> LastModifiedTime { get; private set; } = null!;

        [Output("metadataProperties")]
        public Output<Outputs.ModelPackageMetadataProperties?> MetadataProperties { get; private set; } = null!;

        [Output("modelApprovalStatus")]
        public Output<Pulumi.AwsNative.SageMaker.ModelPackageModelApprovalStatus?> ModelApprovalStatus { get; private set; } = null!;

        [Output("modelMetrics")]
        public Output<Outputs.ModelPackageModelMetrics?> ModelMetrics { get; private set; } = null!;

        [Output("modelPackageArn")]
        public Output<string> ModelPackageArn { get; private set; } = null!;

        [Output("modelPackageDescription")]
        public Output<string?> ModelPackageDescription { get; private set; } = null!;

        [Output("modelPackageGroupName")]
        public Output<string?> ModelPackageGroupName { get; private set; } = null!;

        [Output("modelPackageName")]
        public Output<string?> ModelPackageName { get; private set; } = null!;

        [Output("modelPackageStatus")]
        public Output<Pulumi.AwsNative.SageMaker.ModelPackageStatus> ModelPackageStatus { get; private set; } = null!;

        [Output("modelPackageStatusDetails")]
        public Output<Outputs.ModelPackageStatusDetails?> ModelPackageStatusDetails { get; private set; } = null!;

        [Output("modelPackageVersion")]
        public Output<int?> ModelPackageVersion { get; private set; } = null!;

        [Output("samplePayloadUrl")]
        public Output<string?> SamplePayloadUrl { get; private set; } = null!;

        [Output("sourceAlgorithmSpecification")]
        public Output<Outputs.ModelPackageSourceAlgorithmSpecification?> SourceAlgorithmSpecification { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ModelPackageTag>> Tags { get; private set; } = null!;

        [Output("task")]
        public Output<string?> Task { get; private set; } = null!;

        [Output("validationSpecification")]
        public Output<Outputs.ModelPackageValidationSpecification?> ValidationSpecification { get; private set; } = null!;


        /// <summary>
        /// Create a ModelPackage resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ModelPackage(string name, ModelPackageArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:sagemaker:ModelPackage", name, args ?? new ModelPackageArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ModelPackage(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:sagemaker:ModelPackage", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "clientToken",
                    "domain",
                    "driftCheckBaselines",
                    "inferenceSpecification",
                    "metadataProperties",
                    "modelMetrics",
                    "modelPackageDescription",
                    "modelPackageGroupName",
                    "samplePayloadUrl",
                    "sourceAlgorithmSpecification",
                    "task",
                    "validationSpecification",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ModelPackage resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ModelPackage Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ModelPackage(name, id, options);
        }
    }

    public sealed class ModelPackageArgs : global::Pulumi.ResourceArgs
    {
        [Input("additionalInferenceSpecifications")]
        private InputList<Inputs.ModelPackageAdditionalInferenceSpecificationDefinitionArgs>? _additionalInferenceSpecifications;
        public InputList<Inputs.ModelPackageAdditionalInferenceSpecificationDefinitionArgs> AdditionalInferenceSpecifications
        {
            get => _additionalInferenceSpecifications ?? (_additionalInferenceSpecifications = new InputList<Inputs.ModelPackageAdditionalInferenceSpecificationDefinitionArgs>());
            set => _additionalInferenceSpecifications = value;
        }

        [Input("additionalInferenceSpecificationsToAdd")]
        private InputList<Inputs.ModelPackageAdditionalInferenceSpecificationDefinitionArgs>? _additionalInferenceSpecificationsToAdd;
        public InputList<Inputs.ModelPackageAdditionalInferenceSpecificationDefinitionArgs> AdditionalInferenceSpecificationsToAdd
        {
            get => _additionalInferenceSpecificationsToAdd ?? (_additionalInferenceSpecificationsToAdd = new InputList<Inputs.ModelPackageAdditionalInferenceSpecificationDefinitionArgs>());
            set => _additionalInferenceSpecificationsToAdd = value;
        }

        [Input("approvalDescription")]
        public Input<string>? ApprovalDescription { get; set; }

        [Input("certifyForMarketplace")]
        public Input<bool>? CertifyForMarketplace { get; set; }

        [Input("clientToken")]
        public Input<string>? ClientToken { get; set; }

        [Input("customerMetadataProperties")]
        public Input<Inputs.ModelPackageCustomerMetadataPropertiesArgs>? CustomerMetadataProperties { get; set; }

        [Input("domain")]
        public Input<string>? Domain { get; set; }

        [Input("driftCheckBaselines")]
        public Input<Inputs.ModelPackageDriftCheckBaselinesArgs>? DriftCheckBaselines { get; set; }

        [Input("inferenceSpecification")]
        public Input<Inputs.ModelPackageInferenceSpecificationArgs>? InferenceSpecification { get; set; }

        [Input("lastModifiedTime")]
        public Input<string>? LastModifiedTime { get; set; }

        [Input("metadataProperties")]
        public Input<Inputs.ModelPackageMetadataPropertiesArgs>? MetadataProperties { get; set; }

        [Input("modelApprovalStatus")]
        public Input<Pulumi.AwsNative.SageMaker.ModelPackageModelApprovalStatus>? ModelApprovalStatus { get; set; }

        [Input("modelMetrics")]
        public Input<Inputs.ModelPackageModelMetricsArgs>? ModelMetrics { get; set; }

        [Input("modelPackageDescription")]
        public Input<string>? ModelPackageDescription { get; set; }

        [Input("modelPackageGroupName")]
        public Input<string>? ModelPackageGroupName { get; set; }

        [Input("modelPackageName")]
        public Input<string>? ModelPackageName { get; set; }

        [Input("modelPackageStatusDetails")]
        public Input<Inputs.ModelPackageStatusDetailsArgs>? ModelPackageStatusDetails { get; set; }

        [Input("modelPackageVersion")]
        public Input<int>? ModelPackageVersion { get; set; }

        [Input("samplePayloadUrl")]
        public Input<string>? SamplePayloadUrl { get; set; }

        [Input("sourceAlgorithmSpecification")]
        public Input<Inputs.ModelPackageSourceAlgorithmSpecificationArgs>? SourceAlgorithmSpecification { get; set; }

        [Input("tags")]
        private InputList<Inputs.ModelPackageTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.ModelPackageTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ModelPackageTagArgs>());
            set => _tags = value;
        }

        [Input("task")]
        public Input<string>? Task { get; set; }

        [Input("validationSpecification")]
        public Input<Inputs.ModelPackageValidationSpecificationArgs>? ValidationSpecification { get; set; }

        public ModelPackageArgs()
        {
        }
        public static new ModelPackageArgs Empty => new ModelPackageArgs();
    }
}
