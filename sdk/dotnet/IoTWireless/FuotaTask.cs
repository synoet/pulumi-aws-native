// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTWireless
{
    /// <summary>
    /// Create and manage FUOTA tasks.
    /// </summary>
    [Obsolete(@"FuotaTask is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:iotwireless:FuotaTask")]
    public partial class FuotaTask : Pulumi.CustomResource
    {
        /// <summary>
        /// FUOTA task arn. Returned after successful create.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Multicast group to associate. Only for update request.
        /// </summary>
        [Output("associateMulticastGroup")]
        public Output<string?> AssociateMulticastGroup { get; private set; } = null!;

        /// <summary>
        /// Wireless device to associate. Only for update request.
        /// </summary>
        [Output("associateWirelessDevice")]
        public Output<string?> AssociateWirelessDevice { get; private set; } = null!;

        /// <summary>
        /// FUOTA task description
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Multicast group to disassociate. Only for update request.
        /// </summary>
        [Output("disassociateMulticastGroup")]
        public Output<string?> DisassociateMulticastGroup { get; private set; } = null!;

        /// <summary>
        /// Wireless device to disassociate. Only for update request.
        /// </summary>
        [Output("disassociateWirelessDevice")]
        public Output<string?> DisassociateWirelessDevice { get; private set; } = null!;

        /// <summary>
        /// FUOTA task firmware update image binary S3 link
        /// </summary>
        [Output("firmwareUpdateImage")]
        public Output<string> FirmwareUpdateImage { get; private set; } = null!;

        /// <summary>
        /// FUOTA task firmware IAM role for reading S3
        /// </summary>
        [Output("firmwareUpdateRole")]
        public Output<string> FirmwareUpdateRole { get; private set; } = null!;

        /// <summary>
        /// FUOTA task status. Returned after successful read.
        /// </summary>
        [Output("fuotaTaskStatus")]
        public Output<string> FuotaTaskStatus { get; private set; } = null!;

        /// <summary>
        /// FUOTA task LoRaWAN
        /// </summary>
        [Output("loRaWAN")]
        public Output<Outputs.FuotaTaskLoRaWAN> LoRaWAN { get; private set; } = null!;

        /// <summary>
        /// Name of FUOTA task
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// A list of key-value pairs that contain metadata for the FUOTA task.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.FuotaTaskTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a FuotaTask resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FuotaTask(string name, FuotaTaskArgs args, CustomResourceOptions? options = null)
            : base("aws-native:iotwireless:FuotaTask", name, args ?? new FuotaTaskArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FuotaTask(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iotwireless:FuotaTask", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing FuotaTask resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FuotaTask Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new FuotaTask(name, id, options);
        }
    }

    public sealed class FuotaTaskArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Multicast group to associate. Only for update request.
        /// </summary>
        [Input("associateMulticastGroup")]
        public Input<string>? AssociateMulticastGroup { get; set; }

        /// <summary>
        /// Wireless device to associate. Only for update request.
        /// </summary>
        [Input("associateWirelessDevice")]
        public Input<string>? AssociateWirelessDevice { get; set; }

        /// <summary>
        /// FUOTA task description
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Multicast group to disassociate. Only for update request.
        /// </summary>
        [Input("disassociateMulticastGroup")]
        public Input<string>? DisassociateMulticastGroup { get; set; }

        /// <summary>
        /// Wireless device to disassociate. Only for update request.
        /// </summary>
        [Input("disassociateWirelessDevice")]
        public Input<string>? DisassociateWirelessDevice { get; set; }

        /// <summary>
        /// FUOTA task firmware update image binary S3 link
        /// </summary>
        [Input("firmwareUpdateImage", required: true)]
        public Input<string> FirmwareUpdateImage { get; set; } = null!;

        /// <summary>
        /// FUOTA task firmware IAM role for reading S3
        /// </summary>
        [Input("firmwareUpdateRole", required: true)]
        public Input<string> FirmwareUpdateRole { get; set; } = null!;

        /// <summary>
        /// FUOTA task LoRaWAN
        /// </summary>
        [Input("loRaWAN", required: true)]
        public Input<Inputs.FuotaTaskLoRaWANArgs> LoRaWAN { get; set; } = null!;

        /// <summary>
        /// Name of FUOTA task
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputList<Inputs.FuotaTaskTagArgs>? _tags;

        /// <summary>
        /// A list of key-value pairs that contain metadata for the FUOTA task.
        /// </summary>
        public InputList<Inputs.FuotaTaskTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.FuotaTaskTagArgs>());
            set => _tags = value;
        }

        public FuotaTaskArgs()
        {
        }
    }
}
