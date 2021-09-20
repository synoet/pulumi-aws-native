// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTWireless
{
    /// <summary>
    /// Create and manage wireless gateways, including LoRa gateways.
    /// </summary>
    [AwsNativeResourceType("aws-native:iotwireless:WirelessDevice")]
    public partial class WirelessDevice : Pulumi.CustomResource
    {
        /// <summary>
        /// Wireless device arn. Returned after successful create.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Wireless device description
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Wireless device destination name
        /// </summary>
        [Output("destinationName")]
        public Output<string> DestinationName { get; private set; } = null!;

        /// <summary>
        /// The date and time when the most recent uplink was received.
        /// </summary>
        [Output("lastUplinkReceivedAt")]
        public Output<string?> LastUplinkReceivedAt { get; private set; } = null!;

        /// <summary>
        /// The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Device.
        /// </summary>
        [Output("loRaWAN")]
        public Output<Outputs.WirelessDeviceLoRaWANDevice?> LoRaWAN { get; private set; } = null!;

        /// <summary>
        /// Wireless device name
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// A list of key-value pairs that contain metadata for the device. Currently not supported, will not create if tags are passed.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.WirelessDeviceTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// Thing arn. Passed into update to associate Thing with Wireless device.
        /// </summary>
        [Output("thingArn")]
        public Output<string?> ThingArn { get; private set; } = null!;

        /// <summary>
        /// Thing Arn. If there is a Thing created, this can be returned with a Get call.
        /// </summary>
        [Output("thingName")]
        public Output<string> ThingName { get; private set; } = null!;

        /// <summary>
        /// Wireless device type, currently only Sidewalk and LoRa
        /// </summary>
        [Output("type")]
        public Output<Pulumi.AwsNative.IoTWireless.WirelessDeviceType> Type { get; private set; } = null!;


        /// <summary>
        /// Create a WirelessDevice resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public WirelessDevice(string name, WirelessDeviceArgs args, CustomResourceOptions? options = null)
            : base("aws-native:iotwireless:WirelessDevice", name, args ?? new WirelessDeviceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private WirelessDevice(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iotwireless:WirelessDevice", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing WirelessDevice resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static WirelessDevice Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new WirelessDevice(name, id, options);
        }
    }

    public sealed class WirelessDeviceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Wireless device description
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Wireless device destination name
        /// </summary>
        [Input("destinationName", required: true)]
        public Input<string> DestinationName { get; set; } = null!;

        /// <summary>
        /// The date and time when the most recent uplink was received.
        /// </summary>
        [Input("lastUplinkReceivedAt")]
        public Input<string>? LastUplinkReceivedAt { get; set; }

        /// <summary>
        /// The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Device.
        /// </summary>
        [Input("loRaWAN")]
        public Input<Inputs.WirelessDeviceLoRaWANDeviceArgs>? LoRaWAN { get; set; }

        /// <summary>
        /// Wireless device name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputList<Inputs.WirelessDeviceTagArgs>? _tags;

        /// <summary>
        /// A list of key-value pairs that contain metadata for the device. Currently not supported, will not create if tags are passed.
        /// </summary>
        public InputList<Inputs.WirelessDeviceTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.WirelessDeviceTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// Thing arn. Passed into update to associate Thing with Wireless device.
        /// </summary>
        [Input("thingArn")]
        public Input<string>? ThingArn { get; set; }

        /// <summary>
        /// Wireless device type, currently only Sidewalk and LoRa
        /// </summary>
        [Input("type", required: true)]
        public Input<Pulumi.AwsNative.IoTWireless.WirelessDeviceType> Type { get; set; } = null!;

        public WirelessDeviceArgs()
        {
        }
    }
}
