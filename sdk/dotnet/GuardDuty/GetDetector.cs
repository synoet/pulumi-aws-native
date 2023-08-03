// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GuardDuty
{
    public static class GetDetector
    {
        /// <summary>
        /// Resource Type definition for AWS::GuardDuty::Detector
        /// </summary>
        public static Task<GetDetectorResult> InvokeAsync(GetDetectorArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDetectorResult>("aws-native:guardduty:getDetector", args ?? new GetDetectorArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::GuardDuty::Detector
        /// </summary>
        public static Output<GetDetectorResult> Invoke(GetDetectorInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDetectorResult>("aws-native:guardduty:getDetector", args ?? new GetDetectorInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDetectorArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetDetectorArgs()
        {
        }
        public static new GetDetectorArgs Empty => new GetDetectorArgs();
    }

    public sealed class GetDetectorInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetDetectorInvokeArgs()
        {
        }
        public static new GetDetectorInvokeArgs Empty => new GetDetectorInvokeArgs();
    }


    [OutputType]
    public sealed class GetDetectorResult
    {
        public readonly Outputs.DetectorCfnDataSourceConfigurations? DataSources;
        public readonly bool? Enable;
        public readonly ImmutableArray<Outputs.DetectorFeatureConfigurations> Features;
        public readonly string? FindingPublishingFrequency;
        public readonly string? Id;
        public readonly ImmutableArray<Outputs.DetectorTag> Tags;

        [OutputConstructor]
        private GetDetectorResult(
            Outputs.DetectorCfnDataSourceConfigurations? dataSources,

            bool? enable,

            ImmutableArray<Outputs.DetectorFeatureConfigurations> features,

            string? findingPublishingFrequency,

            string? id,

            ImmutableArray<Outputs.DetectorTag> tags)
        {
            DataSources = dataSources;
            Enable = enable;
            Features = features;
            FindingPublishingFrequency = findingPublishingFrequency;
            Id = id;
            Tags = tags;
        }
    }
}
