// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaLive.Outputs
{

    [OutputType]
    public sealed class ChannelNielsenConfiguration
    {
        public readonly string? DistributorId;
        public readonly string? NielsenPcmToId3Tagging;

        [OutputConstructor]
        private ChannelNielsenConfiguration(
            string? distributorId,

            string? nielsenPcmToId3Tagging)
        {
            DistributorId = distributorId;
            NielsenPcmToId3Tagging = nielsenPcmToId3Tagging;
        }
    }
}
