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
    public sealed class ChannelNielsenWatermarksSettings
    {
        public readonly Outputs.ChannelNielsenCbet? NielsenCbetSettings;
        public readonly string? NielsenDistributionType;
        public readonly Outputs.ChannelNielsenNaesIiNw? NielsenNaesIiNwSettings;

        [OutputConstructor]
        private ChannelNielsenWatermarksSettings(
            Outputs.ChannelNielsenCbet? nielsenCbetSettings,

            string? nielsenDistributionType,

            Outputs.ChannelNielsenNaesIiNw? nielsenNaesIiNwSettings)
        {
            NielsenCbetSettings = nielsenCbetSettings;
            NielsenDistributionType = nielsenDistributionType;
            NielsenNaesIiNwSettings = nielsenNaesIiNwSettings;
        }
    }
}
