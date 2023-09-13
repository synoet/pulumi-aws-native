// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaLive.Inputs
{

    public sealed class ChannelAc3SettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("attenuationControl")]
        public Input<string>? AttenuationControl { get; set; }

        [Input("bitrate")]
        public Input<double>? Bitrate { get; set; }

        [Input("bitstreamMode")]
        public Input<string>? BitstreamMode { get; set; }

        [Input("codingMode")]
        public Input<string>? CodingMode { get; set; }

        [Input("dialnorm")]
        public Input<int>? Dialnorm { get; set; }

        [Input("drcProfile")]
        public Input<string>? DrcProfile { get; set; }

        [Input("lfeFilter")]
        public Input<string>? LfeFilter { get; set; }

        [Input("metadataControl")]
        public Input<string>? MetadataControl { get; set; }

        public ChannelAc3SettingsArgs()
        {
        }
        public static new ChannelAc3SettingsArgs Empty => new ChannelAc3SettingsArgs();
    }
}
