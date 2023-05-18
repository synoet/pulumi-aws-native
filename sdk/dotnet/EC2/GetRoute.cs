// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    public static class GetRoute
    {
        /// <summary>
        /// Resource Type definition for AWS::EC2::Route
        /// </summary>
        public static Task<GetRouteResult> InvokeAsync(GetRouteArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetRouteResult>("aws-native:ec2:getRoute", args ?? new GetRouteArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::EC2::Route
        /// </summary>
        public static Output<GetRouteResult> Invoke(GetRouteInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetRouteResult>("aws-native:ec2:getRoute", args ?? new GetRouteInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetRouteArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetRouteArgs()
        {
        }
        public static new GetRouteArgs Empty => new GetRouteArgs();
    }

    public sealed class GetRouteInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetRouteInvokeArgs()
        {
        }
        public static new GetRouteInvokeArgs Empty => new GetRouteInvokeArgs();
    }


    [OutputType]
    public sealed class GetRouteResult
    {
        public readonly string? CarrierGatewayId;
        public readonly string? DestinationIpv6CidrBlock;
        public readonly string? EgressOnlyInternetGatewayId;
        public readonly string? GatewayId;
        public readonly string? Id;
        public readonly string? InstanceId;
        public readonly string? LocalGatewayId;
        public readonly string? NatGatewayId;
        public readonly string? NetworkInterfaceId;
        public readonly string? TransitGatewayId;
        public readonly string? VpcEndpointId;
        public readonly string? VpcPeeringConnectionId;

        [OutputConstructor]
        private GetRouteResult(
            string? carrierGatewayId,

            string? destinationIpv6CidrBlock,

            string? egressOnlyInternetGatewayId,

            string? gatewayId,

            string? id,

            string? instanceId,

            string? localGatewayId,

            string? natGatewayId,

            string? networkInterfaceId,

            string? transitGatewayId,

            string? vpcEndpointId,

            string? vpcPeeringConnectionId)
        {
            CarrierGatewayId = carrierGatewayId;
            DestinationIpv6CidrBlock = destinationIpv6CidrBlock;
            EgressOnlyInternetGatewayId = egressOnlyInternetGatewayId;
            GatewayId = gatewayId;
            Id = id;
            InstanceId = instanceId;
            LocalGatewayId = localGatewayId;
            NatGatewayId = natGatewayId;
            NetworkInterfaceId = networkInterfaceId;
            TransitGatewayId = transitGatewayId;
            VpcEndpointId = vpcEndpointId;
            VpcPeeringConnectionId = vpcPeeringConnectionId;
        }
    }
}
