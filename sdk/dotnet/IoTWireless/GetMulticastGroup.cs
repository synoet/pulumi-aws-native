// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTWireless
{
    public static class GetMulticastGroup
    {
        /// <summary>
        /// Create and manage Multicast groups.
        /// </summary>
        public static Task<GetMulticastGroupResult> InvokeAsync(GetMulticastGroupArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetMulticastGroupResult>("aws-native:iotwireless:getMulticastGroup", args ?? new GetMulticastGroupArgs(), options.WithDefaults());

        /// <summary>
        /// Create and manage Multicast groups.
        /// </summary>
        public static Output<GetMulticastGroupResult> Invoke(GetMulticastGroupInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetMulticastGroupResult>("aws-native:iotwireless:getMulticastGroup", args ?? new GetMulticastGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetMulticastGroupArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Multicast group id. Returned after successful create.
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetMulticastGroupArgs()
        {
        }
        public static new GetMulticastGroupArgs Empty => new GetMulticastGroupArgs();
    }

    public sealed class GetMulticastGroupInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Multicast group id. Returned after successful create.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetMulticastGroupInvokeArgs()
        {
        }
        public static new GetMulticastGroupInvokeArgs Empty => new GetMulticastGroupInvokeArgs();
    }


    [OutputType]
    public sealed class GetMulticastGroupResult
    {
        /// <summary>
        /// Multicast group arn. Returned after successful create.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// Wireless device to associate. Only for update request.
        /// </summary>
        public readonly string? AssociateWirelessDevice;
        /// <summary>
        /// Multicast group description
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// Wireless device to disassociate. Only for update request.
        /// </summary>
        public readonly string? DisassociateWirelessDevice;
        /// <summary>
        /// Multicast group id. Returned after successful create.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// Multicast group LoRaWAN
        /// </summary>
        public readonly Outputs.MulticastGroupLoRaWAN? LoRaWan;
        /// <summary>
        /// Name of Multicast group
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// Multicast group status. Returned after successful read.
        /// </summary>
        public readonly string? Status;
        /// <summary>
        /// A list of key-value pairs that contain metadata for the Multicast group.
        /// </summary>
        public readonly ImmutableArray<Outputs.MulticastGroupTag> Tags;

        [OutputConstructor]
        private GetMulticastGroupResult(
            string? arn,

            string? associateWirelessDevice,

            string? description,

            string? disassociateWirelessDevice,

            string? id,

            Outputs.MulticastGroupLoRaWAN? loRaWan,

            string? name,

            string? status,

            ImmutableArray<Outputs.MulticastGroupTag> tags)
        {
            Arn = arn;
            AssociateWirelessDevice = associateWirelessDevice;
            Description = description;
            DisassociateWirelessDevice = disassociateWirelessDevice;
            Id = id;
            LoRaWan = loRaWan;
            Name = name;
            Status = status;
            Tags = tags;
        }
    }
}
