// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DeviceFarm
{
    public static class GetNetworkProfile
    {
        /// <summary>
        /// AWS::DeviceFarm::NetworkProfile creates a new DF Network Profile
        /// </summary>
        public static Task<GetNetworkProfileResult> InvokeAsync(GetNetworkProfileArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetNetworkProfileResult>("aws-native:devicefarm:getNetworkProfile", args ?? new GetNetworkProfileArgs(), options.WithDefaults());

        /// <summary>
        /// AWS::DeviceFarm::NetworkProfile creates a new DF Network Profile
        /// </summary>
        public static Output<GetNetworkProfileResult> Invoke(GetNetworkProfileInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetNetworkProfileResult>("aws-native:devicefarm:getNetworkProfile", args ?? new GetNetworkProfileInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNetworkProfileArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetNetworkProfileArgs()
        {
        }
        public static new GetNetworkProfileArgs Empty => new GetNetworkProfileArgs();
    }

    public sealed class GetNetworkProfileInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetNetworkProfileInvokeArgs()
        {
        }
        public static new GetNetworkProfileInvokeArgs Empty => new GetNetworkProfileInvokeArgs();
    }


    [OutputType]
    public sealed class GetNetworkProfileResult
    {
        public readonly string? Arn;
        public readonly string? Description;
        public readonly int? DownlinkBandwidthBits;
        public readonly int? DownlinkDelayMs;
        public readonly int? DownlinkJitterMs;
        public readonly int? DownlinkLossPercent;
        public readonly string? Name;
        public readonly ImmutableArray<Outputs.NetworkProfileTag> Tags;
        public readonly int? UplinkBandwidthBits;
        public readonly int? UplinkDelayMs;
        public readonly int? UplinkJitterMs;
        public readonly int? UplinkLossPercent;

        [OutputConstructor]
        private GetNetworkProfileResult(
            string? arn,

            string? description,

            int? downlinkBandwidthBits,

            int? downlinkDelayMs,

            int? downlinkJitterMs,

            int? downlinkLossPercent,

            string? name,

            ImmutableArray<Outputs.NetworkProfileTag> tags,

            int? uplinkBandwidthBits,

            int? uplinkDelayMs,

            int? uplinkJitterMs,

            int? uplinkLossPercent)
        {
            Arn = arn;
            Description = description;
            DownlinkBandwidthBits = downlinkBandwidthBits;
            DownlinkDelayMs = downlinkDelayMs;
            DownlinkJitterMs = downlinkJitterMs;
            DownlinkLossPercent = downlinkLossPercent;
            Name = name;
            Tags = tags;
            UplinkBandwidthBits = uplinkBandwidthBits;
            UplinkDelayMs = uplinkDelayMs;
            UplinkJitterMs = uplinkJitterMs;
            UplinkLossPercent = uplinkLossPercent;
        }
    }
}
