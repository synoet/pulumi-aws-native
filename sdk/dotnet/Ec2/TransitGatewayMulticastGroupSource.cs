// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    /// <summary>
    /// The AWS::EC2::TransitGatewayMulticastGroupSource registers and deregisters members and sources (network interfaces) with the transit gateway multicast group
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:TransitGatewayMulticastGroupSource")]
    public partial class TransitGatewayMulticastGroupSource : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The IP address assigned to the transit gateway multicast group.
        /// </summary>
        [Output("groupIpAddress")]
        public Output<string> GroupIpAddress { get; private set; } = null!;

        /// <summary>
        /// Indicates that the resource is a transit gateway multicast group member.
        /// </summary>
        [Output("groupMember")]
        public Output<bool> GroupMember { get; private set; } = null!;

        /// <summary>
        /// Indicates that the resource is a transit gateway multicast group member.
        /// </summary>
        [Output("groupSource")]
        public Output<bool> GroupSource { get; private set; } = null!;

        /// <summary>
        /// The member type (for example, static).
        /// </summary>
        [Output("memberType")]
        public Output<string> MemberType { get; private set; } = null!;

        /// <summary>
        /// The ID of the transit gateway attachment.
        /// </summary>
        [Output("networkInterfaceId")]
        public Output<string> NetworkInterfaceId { get; private set; } = null!;

        /// <summary>
        /// The ID of the resource.
        /// </summary>
        [Output("resourceId")]
        public Output<string> ResourceId { get; private set; } = null!;

        /// <summary>
        /// The type of resource, for example a VPC attachment.
        /// </summary>
        [Output("resourceType")]
        public Output<string> ResourceType { get; private set; } = null!;

        /// <summary>
        /// The source type.
        /// </summary>
        [Output("sourceType")]
        public Output<string> SourceType { get; private set; } = null!;

        /// <summary>
        /// The ID of the subnet.
        /// </summary>
        [Output("subnetId")]
        public Output<string> SubnetId { get; private set; } = null!;

        /// <summary>
        /// The ID of the transit gateway attachment.
        /// </summary>
        [Output("transitGatewayAttachmentId")]
        public Output<string> TransitGatewayAttachmentId { get; private set; } = null!;

        /// <summary>
        /// The ID of the transit gateway multicast domain.
        /// </summary>
        [Output("transitGatewayMulticastDomainId")]
        public Output<string> TransitGatewayMulticastDomainId { get; private set; } = null!;


        /// <summary>
        /// Create a TransitGatewayMulticastGroupSource resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TransitGatewayMulticastGroupSource(string name, TransitGatewayMulticastGroupSourceArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:TransitGatewayMulticastGroupSource", name, args ?? new TransitGatewayMulticastGroupSourceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TransitGatewayMulticastGroupSource(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:TransitGatewayMulticastGroupSource", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "groupIpAddress",
                    "networkInterfaceId",
                    "transitGatewayMulticastDomainId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing TransitGatewayMulticastGroupSource resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TransitGatewayMulticastGroupSource Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new TransitGatewayMulticastGroupSource(name, id, options);
        }
    }

    public sealed class TransitGatewayMulticastGroupSourceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IP address assigned to the transit gateway multicast group.
        /// </summary>
        [Input("groupIpAddress", required: true)]
        public Input<string> GroupIpAddress { get; set; } = null!;

        /// <summary>
        /// The ID of the transit gateway attachment.
        /// </summary>
        [Input("networkInterfaceId", required: true)]
        public Input<string> NetworkInterfaceId { get; set; } = null!;

        /// <summary>
        /// The ID of the transit gateway multicast domain.
        /// </summary>
        [Input("transitGatewayMulticastDomainId", required: true)]
        public Input<string> TransitGatewayMulticastDomainId { get; set; } = null!;

        public TransitGatewayMulticastGroupSourceArgs()
        {
        }
        public static new TransitGatewayMulticastGroupSourceArgs Empty => new TransitGatewayMulticastGroupSourceArgs();
    }
}
