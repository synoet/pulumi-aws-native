// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker
{
    public static class GetImageVersion
    {
        /// <summary>
        /// Resource Type definition for AWS::SageMaker::ImageVersion
        /// </summary>
        public static Task<GetImageVersionResult> InvokeAsync(GetImageVersionArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetImageVersionResult>("aws-native:sagemaker:getImageVersion", args ?? new GetImageVersionArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::SageMaker::ImageVersion
        /// </summary>
        public static Output<GetImageVersionResult> Invoke(GetImageVersionInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetImageVersionResult>("aws-native:sagemaker:getImageVersion", args ?? new GetImageVersionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetImageVersionArgs : global::Pulumi.InvokeArgs
    {
        [Input("imageVersionArn", required: true)]
        public string ImageVersionArn { get; set; } = null!;

        public GetImageVersionArgs()
        {
        }
        public static new GetImageVersionArgs Empty => new GetImageVersionArgs();
    }

    public sealed class GetImageVersionInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("imageVersionArn", required: true)]
        public Input<string> ImageVersionArn { get; set; } = null!;

        public GetImageVersionInvokeArgs()
        {
        }
        public static new GetImageVersionInvokeArgs Empty => new GetImageVersionInvokeArgs();
    }


    [OutputType]
    public sealed class GetImageVersionResult
    {
        public readonly string? ContainerImage;
        public readonly bool? Horovod;
        public readonly string? ImageArn;
        public readonly string? ImageVersionArn;
        public readonly Pulumi.AwsNative.SageMaker.ImageVersionJobType? JobType;
        public readonly string? MlFramework;
        public readonly Pulumi.AwsNative.SageMaker.ImageVersionProcessor? Processor;
        public readonly string? ProgrammingLang;
        public readonly string? ReleaseNotes;
        public readonly Pulumi.AwsNative.SageMaker.ImageVersionVendorGuidance? VendorGuidance;
        public readonly int? Version;

        [OutputConstructor]
        private GetImageVersionResult(
            string? containerImage,

            bool? horovod,

            string? imageArn,

            string? imageVersionArn,

            Pulumi.AwsNative.SageMaker.ImageVersionJobType? jobType,

            string? mlFramework,

            Pulumi.AwsNative.SageMaker.ImageVersionProcessor? processor,

            string? programmingLang,

            string? releaseNotes,

            Pulumi.AwsNative.SageMaker.ImageVersionVendorGuidance? vendorGuidance,

            int? version)
        {
            ContainerImage = containerImage;
            Horovod = horovod;
            ImageArn = imageArn;
            ImageVersionArn = imageVersionArn;
            JobType = jobType;
            MlFramework = mlFramework;
            Processor = processor;
            ProgrammingLang = programmingLang;
            ReleaseNotes = releaseNotes;
            VendorGuidance = vendorGuidance;
            Version = version;
        }
    }
}
