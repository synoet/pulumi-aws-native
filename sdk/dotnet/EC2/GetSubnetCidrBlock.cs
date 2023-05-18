// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    public static class GetSubnetCidrBlock
    {
        /// <summary>
        /// The AWS::EC2::SubnetCidrBlock resource creates association between subnet and IPv6 CIDR
        /// </summary>
        public static Task<GetSubnetCidrBlockResult> InvokeAsync(GetSubnetCidrBlockArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSubnetCidrBlockResult>("aws-native:ec2:getSubnetCidrBlock", args ?? new GetSubnetCidrBlockArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS::EC2::SubnetCidrBlock resource creates association between subnet and IPv6 CIDR
        /// </summary>
        public static Output<GetSubnetCidrBlockResult> Invoke(GetSubnetCidrBlockInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSubnetCidrBlockResult>("aws-native:ec2:getSubnetCidrBlock", args ?? new GetSubnetCidrBlockInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSubnetCidrBlockArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Information about the IPv6 association.
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetSubnetCidrBlockArgs()
        {
        }
        public static new GetSubnetCidrBlockArgs Empty => new GetSubnetCidrBlockArgs();
    }

    public sealed class GetSubnetCidrBlockInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Information about the IPv6 association.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetSubnetCidrBlockInvokeArgs()
        {
        }
        public static new GetSubnetCidrBlockInvokeArgs Empty => new GetSubnetCidrBlockInvokeArgs();
    }


    [OutputType]
    public sealed class GetSubnetCidrBlockResult
    {
        /// <summary>
        /// Information about the IPv6 association.
        /// </summary>
        public readonly string? Id;

        [OutputConstructor]
        private GetSubnetCidrBlockResult(string? id)
        {
            Id = id;
        }
    }
}
