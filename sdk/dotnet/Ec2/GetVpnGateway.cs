// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    public static class GetVpnGateway
    {
        /// <summary>
        /// Schema for EC2 VPN Gateway
        /// </summary>
        public static Task<GetVpnGatewayResult> InvokeAsync(GetVpnGatewayArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVpnGatewayResult>("aws-native:ec2:getVpnGateway", args ?? new GetVpnGatewayArgs(), options.WithDefaults());

        /// <summary>
        /// Schema for EC2 VPN Gateway
        /// </summary>
        public static Output<GetVpnGatewayResult> Invoke(GetVpnGatewayInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVpnGatewayResult>("aws-native:ec2:getVpnGateway", args ?? new GetVpnGatewayInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVpnGatewayArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// VPN Gateway ID generated by service
        /// </summary>
        [Input("vpnGatewayId", required: true)]
        public string VpnGatewayId { get; set; } = null!;

        public GetVpnGatewayArgs()
        {
        }
        public static new GetVpnGatewayArgs Empty => new GetVpnGatewayArgs();
    }

    public sealed class GetVpnGatewayInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// VPN Gateway ID generated by service
        /// </summary>
        [Input("vpnGatewayId", required: true)]
        public Input<string> VpnGatewayId { get; set; } = null!;

        public GetVpnGatewayInvokeArgs()
        {
        }
        public static new GetVpnGatewayInvokeArgs Empty => new GetVpnGatewayInvokeArgs();
    }


    [OutputType]
    public sealed class GetVpnGatewayResult
    {
        /// <summary>
        /// Any tags assigned to the virtual private gateway.
        /// </summary>
        public readonly ImmutableArray<Outputs.VpnGatewayTag> Tags;
        /// <summary>
        /// VPN Gateway ID generated by service
        /// </summary>
        public readonly string? VpnGatewayId;

        [OutputConstructor]
        private GetVpnGatewayResult(
            ImmutableArray<Outputs.VpnGatewayTag> tags,

            string? vpnGatewayId)
        {
            Tags = tags;
            VpnGatewayId = vpnGatewayId;
        }
    }
}
