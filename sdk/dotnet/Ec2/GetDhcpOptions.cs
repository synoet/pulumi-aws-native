// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    public static class GetDhcpOptions
    {
        /// <summary>
        /// Resource Type definition for AWS::EC2::DHCPOptions
        /// </summary>
        public static Task<GetDhcpOptionsResult> InvokeAsync(GetDhcpOptionsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDhcpOptionsResult>("aws-native:ec2:getDhcpOptions", args ?? new GetDhcpOptionsArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::EC2::DHCPOptions
        /// </summary>
        public static Output<GetDhcpOptionsResult> Invoke(GetDhcpOptionsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDhcpOptionsResult>("aws-native:ec2:getDhcpOptions", args ?? new GetDhcpOptionsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDhcpOptionsArgs : global::Pulumi.InvokeArgs
    {
        [Input("dhcpOptionsId", required: true)]
        public string DhcpOptionsId { get; set; } = null!;

        public GetDhcpOptionsArgs()
        {
        }
        public static new GetDhcpOptionsArgs Empty => new GetDhcpOptionsArgs();
    }

    public sealed class GetDhcpOptionsInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("dhcpOptionsId", required: true)]
        public Input<string> DhcpOptionsId { get; set; } = null!;

        public GetDhcpOptionsInvokeArgs()
        {
        }
        public static new GetDhcpOptionsInvokeArgs Empty => new GetDhcpOptionsInvokeArgs();
    }


    [OutputType]
    public sealed class GetDhcpOptionsResult
    {
        public readonly string? DhcpOptionsId;
        /// <summary>
        /// Any tags assigned to the DHCP options set.
        /// </summary>
        public readonly ImmutableArray<Outputs.DhcpOptionsTag> Tags;

        [OutputConstructor]
        private GetDhcpOptionsResult(
            string? dhcpOptionsId,

            ImmutableArray<Outputs.DhcpOptionsTag> tags)
        {
            DhcpOptionsId = dhcpOptionsId;
            Tags = tags;
        }
    }
}
