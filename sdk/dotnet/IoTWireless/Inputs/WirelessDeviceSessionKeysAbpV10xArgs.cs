// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTWireless.Inputs
{

    public sealed class WirelessDeviceSessionKeysAbpV10xArgs : global::Pulumi.ResourceArgs
    {
        [Input("appSKey", required: true)]
        public Input<string> AppSKey { get; set; } = null!;

        [Input("nwkSKey", required: true)]
        public Input<string> NwkSKey { get; set; } = null!;

        public WirelessDeviceSessionKeysAbpV10xArgs()
        {
        }
        public static new WirelessDeviceSessionKeysAbpV10xArgs Empty => new WirelessDeviceSessionKeysAbpV10xArgs();
    }
}
