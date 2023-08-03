// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.FSx
{
    public static class GetVolume
    {
        /// <summary>
        /// Resource Type definition for AWS::FSx::Volume
        /// </summary>
        public static Task<GetVolumeResult> InvokeAsync(GetVolumeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVolumeResult>("aws-native:fsx:getVolume", args ?? new GetVolumeArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::FSx::Volume
        /// </summary>
        public static Output<GetVolumeResult> Invoke(GetVolumeInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVolumeResult>("aws-native:fsx:getVolume", args ?? new GetVolumeInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVolumeArgs : global::Pulumi.InvokeArgs
    {
        [Input("volumeId", required: true)]
        public string VolumeId { get; set; } = null!;

        public GetVolumeArgs()
        {
        }
        public static new GetVolumeArgs Empty => new GetVolumeArgs();
    }

    public sealed class GetVolumeInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("volumeId", required: true)]
        public Input<string> VolumeId { get; set; } = null!;

        public GetVolumeInvokeArgs()
        {
        }
        public static new GetVolumeInvokeArgs Empty => new GetVolumeInvokeArgs();
    }


    [OutputType]
    public sealed class GetVolumeResult
    {
        public readonly string? Name;
        public readonly Outputs.VolumeOntapConfiguration? OntapConfiguration;
        public readonly Outputs.VolumeOpenZfsConfiguration? OpenZfsConfiguration;
        public readonly string? ResourceArn;
        public readonly ImmutableArray<Outputs.VolumeTag> Tags;
        public readonly string? Uuid;
        public readonly string? VolumeId;

        [OutputConstructor]
        private GetVolumeResult(
            string? name,

            Outputs.VolumeOntapConfiguration? ontapConfiguration,

            Outputs.VolumeOpenZfsConfiguration? openZfsConfiguration,

            string? resourceArn,

            ImmutableArray<Outputs.VolumeTag> tags,

            string? uuid,

            string? volumeId)
        {
            Name = name;
            OntapConfiguration = ontapConfiguration;
            OpenZfsConfiguration = openZfsConfiguration;
            ResourceArn = resourceArn;
            Tags = tags;
            Uuid = uuid;
            VolumeId = volumeId;
        }
    }
}
