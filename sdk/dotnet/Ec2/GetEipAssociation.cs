// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    public static class GetEipAssociation
    {
        /// <summary>
        /// Resource schema for EC2 EIP association.
        /// </summary>
        public static Task<GetEipAssociationResult> InvokeAsync(GetEipAssociationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetEipAssociationResult>("aws-native:ec2:getEipAssociation", args ?? new GetEipAssociationArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for EC2 EIP association.
        /// </summary>
        public static Output<GetEipAssociationResult> Invoke(GetEipAssociationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetEipAssociationResult>("aws-native:ec2:getEipAssociation", args ?? new GetEipAssociationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetEipAssociationArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Composite ID of non-empty properties, to determine the identification.
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetEipAssociationArgs()
        {
        }
        public static new GetEipAssociationArgs Empty => new GetEipAssociationArgs();
    }

    public sealed class GetEipAssociationInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Composite ID of non-empty properties, to determine the identification.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetEipAssociationInvokeArgs()
        {
        }
        public static new GetEipAssociationInvokeArgs Empty => new GetEipAssociationInvokeArgs();
    }


    [OutputType]
    public sealed class GetEipAssociationResult
    {
        /// <summary>
        /// Composite ID of non-empty properties, to determine the identification.
        /// </summary>
        public readonly string? Id;

        [OutputConstructor]
        private GetEipAssociationResult(string? id)
        {
            Id = id;
        }
    }
}
