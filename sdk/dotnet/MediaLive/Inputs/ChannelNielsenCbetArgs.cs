// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaLive.Inputs
{

    public sealed class ChannelNielsenCbetArgs : global::Pulumi.ResourceArgs
    {
        [Input("cbetCheckDigitString")]
        public Input<string>? CbetCheckDigitString { get; set; }

        [Input("cbetStepaside")]
        public Input<string>? CbetStepaside { get; set; }

        [Input("csid")]
        public Input<string>? Csid { get; set; }

        public ChannelNielsenCbetArgs()
        {
        }
        public static new ChannelNielsenCbetArgs Empty => new ChannelNielsenCbetArgs();
    }
}
