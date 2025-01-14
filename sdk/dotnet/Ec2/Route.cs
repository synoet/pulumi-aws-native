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
    /// Resource Type definition for AWS::EC2::Route
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:Route")]
    public partial class Route : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the carrier gateway.
        /// </summary>
        [Output("carrierGatewayId")]
        public Output<string?> CarrierGatewayId { get; private set; } = null!;

        /// <summary>
        /// The primary identifier of the resource generated by the service.
        /// </summary>
        [Output("cidrBlock")]
        public Output<string> CidrBlock { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the core network.
        /// </summary>
        [Output("coreNetworkArn")]
        public Output<string?> CoreNetworkArn { get; private set; } = null!;

        /// <summary>
        /// The IPv4 CIDR block used for the destination match.
        /// </summary>
        [Output("destinationCidrBlock")]
        public Output<string?> DestinationCidrBlock { get; private set; } = null!;

        /// <summary>
        /// The IPv6 CIDR block used for the destination match.
        /// </summary>
        [Output("destinationIpv6CidrBlock")]
        public Output<string?> DestinationIpv6CidrBlock { get; private set; } = null!;

        /// <summary>
        /// The ID of managed prefix list, it's a set of one or more CIDR blocks.
        /// </summary>
        [Output("destinationPrefixListId")]
        public Output<string?> DestinationPrefixListId { get; private set; } = null!;

        /// <summary>
        /// The ID of the egress-only internet gateway.
        /// </summary>
        [Output("egressOnlyInternetGatewayId")]
        public Output<string?> EgressOnlyInternetGatewayId { get; private set; } = null!;

        /// <summary>
        /// The ID of an internet gateway or virtual private gateway attached to your VPC.
        /// </summary>
        [Output("gatewayId")]
        public Output<string?> GatewayId { get; private set; } = null!;

        /// <summary>
        /// The ID of a NAT instance in your VPC.
        /// </summary>
        [Output("instanceId")]
        public Output<string?> InstanceId { get; private set; } = null!;

        /// <summary>
        /// The ID of the local gateway.
        /// </summary>
        [Output("localGatewayId")]
        public Output<string?> LocalGatewayId { get; private set; } = null!;

        /// <summary>
        /// The ID of a NAT gateway.
        /// </summary>
        [Output("natGatewayId")]
        public Output<string?> NatGatewayId { get; private set; } = null!;

        /// <summary>
        /// The ID of the network interface.
        /// </summary>
        [Output("networkInterfaceId")]
        public Output<string?> NetworkInterfaceId { get; private set; } = null!;

        /// <summary>
        /// The ID of the route table. The routing table must be associated with the same VPC that the virtual private gateway is attached to.
        /// </summary>
        [Output("routeTableId")]
        public Output<string> RouteTableId { get; private set; } = null!;

        /// <summary>
        /// The ID of a transit gateway.
        /// </summary>
        [Output("transitGatewayId")]
        public Output<string?> TransitGatewayId { get; private set; } = null!;

        /// <summary>
        /// The ID of a VPC endpoint. Supported for Gateway Load Balancer endpoints only.
        /// </summary>
        [Output("vpcEndpointId")]
        public Output<string?> VpcEndpointId { get; private set; } = null!;

        /// <summary>
        /// The ID of a VPC peering connection.
        /// </summary>
        [Output("vpcPeeringConnectionId")]
        public Output<string?> VpcPeeringConnectionId { get; private set; } = null!;


        /// <summary>
        /// Create a Route resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Route(string name, RouteArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:Route", name, args ?? new RouteArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Route(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:Route", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "destinationCidrBlock",
                    "destinationIpv6CidrBlock",
                    "destinationPrefixListId",
                    "routeTableId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Route resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Route Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Route(name, id, options);
        }
    }

    public sealed class RouteArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the carrier gateway.
        /// </summary>
        [Input("carrierGatewayId")]
        public Input<string>? CarrierGatewayId { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the core network.
        /// </summary>
        [Input("coreNetworkArn")]
        public Input<string>? CoreNetworkArn { get; set; }

        /// <summary>
        /// The IPv4 CIDR block used for the destination match.
        /// </summary>
        [Input("destinationCidrBlock")]
        public Input<string>? DestinationCidrBlock { get; set; }

        /// <summary>
        /// The IPv6 CIDR block used for the destination match.
        /// </summary>
        [Input("destinationIpv6CidrBlock")]
        public Input<string>? DestinationIpv6CidrBlock { get; set; }

        /// <summary>
        /// The ID of managed prefix list, it's a set of one or more CIDR blocks.
        /// </summary>
        [Input("destinationPrefixListId")]
        public Input<string>? DestinationPrefixListId { get; set; }

        /// <summary>
        /// The ID of the egress-only internet gateway.
        /// </summary>
        [Input("egressOnlyInternetGatewayId")]
        public Input<string>? EgressOnlyInternetGatewayId { get; set; }

        /// <summary>
        /// The ID of an internet gateway or virtual private gateway attached to your VPC.
        /// </summary>
        [Input("gatewayId")]
        public Input<string>? GatewayId { get; set; }

        /// <summary>
        /// The ID of a NAT instance in your VPC.
        /// </summary>
        [Input("instanceId")]
        public Input<string>? InstanceId { get; set; }

        /// <summary>
        /// The ID of the local gateway.
        /// </summary>
        [Input("localGatewayId")]
        public Input<string>? LocalGatewayId { get; set; }

        /// <summary>
        /// The ID of a NAT gateway.
        /// </summary>
        [Input("natGatewayId")]
        public Input<string>? NatGatewayId { get; set; }

        /// <summary>
        /// The ID of the network interface.
        /// </summary>
        [Input("networkInterfaceId")]
        public Input<string>? NetworkInterfaceId { get; set; }

        /// <summary>
        /// The ID of the route table. The routing table must be associated with the same VPC that the virtual private gateway is attached to.
        /// </summary>
        [Input("routeTableId", required: true)]
        public Input<string> RouteTableId { get; set; } = null!;

        /// <summary>
        /// The ID of a transit gateway.
        /// </summary>
        [Input("transitGatewayId")]
        public Input<string>? TransitGatewayId { get; set; }

        /// <summary>
        /// The ID of a VPC endpoint. Supported for Gateway Load Balancer endpoints only.
        /// </summary>
        [Input("vpcEndpointId")]
        public Input<string>? VpcEndpointId { get; set; }

        /// <summary>
        /// The ID of a VPC peering connection.
        /// </summary>
        [Input("vpcPeeringConnectionId")]
        public Input<string>? VpcPeeringConnectionId { get; set; }

        public RouteArgs()
        {
        }
        public static new RouteArgs Empty => new RouteArgs();
    }
}
