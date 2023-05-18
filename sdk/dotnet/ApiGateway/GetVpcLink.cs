// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGateway
{
    public static class GetVpcLink
    {
        /// <summary>
        /// Schema for AWS ApiGateway VpcLink
        /// </summary>
        public static Task<GetVpcLinkResult> InvokeAsync(GetVpcLinkArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVpcLinkResult>("aws-native:apigateway:getVpcLink", args ?? new GetVpcLinkArgs(), options.WithDefaults());

        /// <summary>
        /// Schema for AWS ApiGateway VpcLink
        /// </summary>
        public static Output<GetVpcLinkResult> Invoke(GetVpcLinkInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVpcLinkResult>("aws-native:apigateway:getVpcLink", args ?? new GetVpcLinkInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVpcLinkArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the instance that backs VPC link.
        /// </summary>
        [Input("vpcLinkId", required: true)]
        public string VpcLinkId { get; set; } = null!;

        public GetVpcLinkArgs()
        {
        }
        public static new GetVpcLinkArgs Empty => new GetVpcLinkArgs();
    }

    public sealed class GetVpcLinkInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the instance that backs VPC link.
        /// </summary>
        [Input("vpcLinkId", required: true)]
        public Input<string> VpcLinkId { get; set; } = null!;

        public GetVpcLinkInvokeArgs()
        {
        }
        public static new GetVpcLinkInvokeArgs Empty => new GetVpcLinkInvokeArgs();
    }


    [OutputType]
    public sealed class GetVpcLinkResult
    {
        /// <summary>
        /// A description of the VPC link.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// A name for the VPC link.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// An array of arbitrary tags (key-value pairs) to associate with the stage.
        /// </summary>
        public readonly ImmutableArray<Outputs.VpcLinkTag> Tags;
        /// <summary>
        /// The ID of the instance that backs VPC link.
        /// </summary>
        public readonly string? VpcLinkId;

        [OutputConstructor]
        private GetVpcLinkResult(
            string? description,

            string? name,

            ImmutableArray<Outputs.VpcLinkTag> tags,

            string? vpcLinkId)
        {
            Description = description;
            Name = name;
            Tags = tags;
            VpcLinkId = vpcLinkId;
        }
    }
}
