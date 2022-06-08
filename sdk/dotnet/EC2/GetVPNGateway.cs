// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    public static class GetVPNGateway
    {
        /// <summary>
        /// Schema for EC2 VPN Gateway
        /// </summary>
        public static Task<GetVPNGatewayResult> InvokeAsync(GetVPNGatewayArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetVPNGatewayResult>("aws-native:ec2:getVPNGateway", args ?? new GetVPNGatewayArgs(), options.WithDefaults());

        /// <summary>
        /// Schema for EC2 VPN Gateway
        /// </summary>
        public static Output<GetVPNGatewayResult> Invoke(GetVPNGatewayInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetVPNGatewayResult>("aws-native:ec2:getVPNGateway", args ?? new GetVPNGatewayInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVPNGatewayArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// VPN Gateway ID generated by service
        /// </summary>
        [Input("vPNGatewayId", required: true)]
        public string VPNGatewayId { get; set; } = null!;

        public GetVPNGatewayArgs()
        {
        }
    }

    public sealed class GetVPNGatewayInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// VPN Gateway ID generated by service
        /// </summary>
        [Input("vPNGatewayId", required: true)]
        public Input<string> VPNGatewayId { get; set; } = null!;

        public GetVPNGatewayInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetVPNGatewayResult
    {
        /// <summary>
        /// Any tags assigned to the virtual private gateway.
        /// </summary>
        public readonly ImmutableArray<Outputs.VPNGatewayTag> Tags;
        /// <summary>
        /// VPN Gateway ID generated by service
        /// </summary>
        public readonly string? VPNGatewayId;

        [OutputConstructor]
        private GetVPNGatewayResult(
            ImmutableArray<Outputs.VPNGatewayTag> tags,

            string? vPNGatewayId)
        {
            Tags = tags;
            VPNGatewayId = vPNGatewayId;
        }
    }
}
