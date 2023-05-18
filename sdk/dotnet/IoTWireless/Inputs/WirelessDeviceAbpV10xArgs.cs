// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTWireless.Inputs
{

    public sealed class WirelessDeviceAbpV10xArgs : global::Pulumi.ResourceArgs
    {
        [Input("devAddr", required: true)]
        public Input<string> DevAddr { get; set; } = null!;

        [Input("sessionKeys", required: true)]
        public Input<Inputs.WirelessDeviceSessionKeysAbpV10xArgs> SessionKeys { get; set; } = null!;

        public WirelessDeviceAbpV10xArgs()
        {
        }
        public static new WirelessDeviceAbpV10xArgs Empty => new WirelessDeviceAbpV10xArgs();
    }
}
