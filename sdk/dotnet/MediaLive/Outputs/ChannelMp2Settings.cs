// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.MediaLive.Outputs
{

    [OutputType]
    public sealed class ChannelMp2Settings
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html#cfn-medialive-channel-mp2settings-bitrate
        /// </summary>
        public readonly double? Bitrate;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html#cfn-medialive-channel-mp2settings-codingmode
        /// </summary>
        public readonly string? CodingMode;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html#cfn-medialive-channel-mp2settings-samplerate
        /// </summary>
        public readonly double? SampleRate;

        [OutputConstructor]
        private ChannelMp2Settings(
            double? Bitrate,

            string? CodingMode,

            double? SampleRate)
        {
            this.Bitrate = Bitrate;
            this.CodingMode = CodingMode;
            this.SampleRate = SampleRate;
        }
    }
}