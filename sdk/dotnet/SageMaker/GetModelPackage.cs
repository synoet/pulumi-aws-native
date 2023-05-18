// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker
{
    public static class GetModelPackage
    {
        /// <summary>
        /// Resource Type definition for AWS::SageMaker::ModelPackage
        /// </summary>
        public static Task<GetModelPackageResult> InvokeAsync(GetModelPackageArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetModelPackageResult>("aws-native:sagemaker:getModelPackage", args ?? new GetModelPackageArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::SageMaker::ModelPackage
        /// </summary>
        public static Output<GetModelPackageResult> Invoke(GetModelPackageInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetModelPackageResult>("aws-native:sagemaker:getModelPackage", args ?? new GetModelPackageInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetModelPackageArgs : global::Pulumi.InvokeArgs
    {
        [Input("modelPackageArn", required: true)]
        public string ModelPackageArn { get; set; } = null!;

        public GetModelPackageArgs()
        {
        }
        public static new GetModelPackageArgs Empty => new GetModelPackageArgs();
    }

    public sealed class GetModelPackageInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("modelPackageArn", required: true)]
        public Input<string> ModelPackageArn { get; set; } = null!;

        public GetModelPackageInvokeArgs()
        {
        }
        public static new GetModelPackageInvokeArgs Empty => new GetModelPackageInvokeArgs();
    }


    [OutputType]
    public sealed class GetModelPackageResult
    {
        public readonly Outputs.ModelPackageAdditionalInferenceSpecificationDefinition? AdditionalInferenceSpecificationDefinition;
        public readonly ImmutableArray<Outputs.ModelPackageAdditionalInferenceSpecificationDefinition> AdditionalInferenceSpecifications;
        public readonly ImmutableArray<Outputs.ModelPackageAdditionalInferenceSpecificationDefinition> AdditionalInferenceSpecificationsToAdd;
        public readonly string? ApprovalDescription;
        public readonly bool? CertifyForMarketplace;
        public readonly Outputs.ModelPackageCreatedBy? CreatedBy;
        public readonly string? CreationTime;
        public readonly Outputs.ModelPackageCustomerMetadataProperties? CustomerMetadataProperties;
        public readonly Outputs.ModelPackageEnvironment? Environment;
        public readonly Outputs.ModelPackageLastModifiedBy? LastModifiedBy;
        public readonly string? LastModifiedTime;
        public readonly Pulumi.AwsNative.SageMaker.ModelPackageModelApprovalStatus? ModelApprovalStatus;
        public readonly string? ModelPackageArn;
        public readonly string? ModelPackageName;
        public readonly Pulumi.AwsNative.SageMaker.ModelPackageStatus? ModelPackageStatus;
        public readonly Outputs.ModelPackageStatusDetails? ModelPackageStatusDetails;
        public readonly Outputs.ModelPackageStatusItem? ModelPackageStatusItem;
        public readonly int? ModelPackageVersion;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.ModelPackageTag> Tags;

        [OutputConstructor]
        private GetModelPackageResult(
            Outputs.ModelPackageAdditionalInferenceSpecificationDefinition? additionalInferenceSpecificationDefinition,

            ImmutableArray<Outputs.ModelPackageAdditionalInferenceSpecificationDefinition> additionalInferenceSpecifications,

            ImmutableArray<Outputs.ModelPackageAdditionalInferenceSpecificationDefinition> additionalInferenceSpecificationsToAdd,

            string? approvalDescription,

            bool? certifyForMarketplace,

            Outputs.ModelPackageCreatedBy? createdBy,

            string? creationTime,

            Outputs.ModelPackageCustomerMetadataProperties? customerMetadataProperties,

            Outputs.ModelPackageEnvironment? environment,

            Outputs.ModelPackageLastModifiedBy? lastModifiedBy,

            string? lastModifiedTime,

            Pulumi.AwsNative.SageMaker.ModelPackageModelApprovalStatus? modelApprovalStatus,

            string? modelPackageArn,

            string? modelPackageName,

            Pulumi.AwsNative.SageMaker.ModelPackageStatus? modelPackageStatus,

            Outputs.ModelPackageStatusDetails? modelPackageStatusDetails,

            Outputs.ModelPackageStatusItem? modelPackageStatusItem,

            int? modelPackageVersion,

            ImmutableArray<Outputs.ModelPackageTag> tags)
        {
            AdditionalInferenceSpecificationDefinition = additionalInferenceSpecificationDefinition;
            AdditionalInferenceSpecifications = additionalInferenceSpecifications;
            AdditionalInferenceSpecificationsToAdd = additionalInferenceSpecificationsToAdd;
            ApprovalDescription = approvalDescription;
            CertifyForMarketplace = certifyForMarketplace;
            CreatedBy = createdBy;
            CreationTime = creationTime;
            CustomerMetadataProperties = customerMetadataProperties;
            Environment = environment;
            LastModifiedBy = lastModifiedBy;
            LastModifiedTime = lastModifiedTime;
            ModelApprovalStatus = modelApprovalStatus;
            ModelPackageArn = modelPackageArn;
            ModelPackageName = modelPackageName;
            ModelPackageStatus = modelPackageStatus;
            ModelPackageStatusDetails = modelPackageStatusDetails;
            ModelPackageStatusItem = modelPackageStatusItem;
            ModelPackageVersion = modelPackageVersion;
            Tags = tags;
        }
    }
}
