// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.VpcLattice
{
    public static class GetServiceNetworkVpcAssociation
    {
        /// <summary>
        /// Associates a VPC with a service network.
        /// </summary>
        public static Task<GetServiceNetworkVpcAssociationResult> InvokeAsync(GetServiceNetworkVpcAssociationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetServiceNetworkVpcAssociationResult>("aws-native:vpclattice:getServiceNetworkVpcAssociation", args ?? new GetServiceNetworkVpcAssociationArgs(), options.WithDefaults());

        /// <summary>
        /// Associates a VPC with a service network.
        /// </summary>
        public static Output<GetServiceNetworkVpcAssociationResult> Invoke(GetServiceNetworkVpcAssociationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetServiceNetworkVpcAssociationResult>("aws-native:vpclattice:getServiceNetworkVpcAssociation", args ?? new GetServiceNetworkVpcAssociationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetServiceNetworkVpcAssociationArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetServiceNetworkVpcAssociationArgs()
        {
        }
        public static new GetServiceNetworkVpcAssociationArgs Empty => new GetServiceNetworkVpcAssociationArgs();
    }

    public sealed class GetServiceNetworkVpcAssociationInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetServiceNetworkVpcAssociationInvokeArgs()
        {
        }
        public static new GetServiceNetworkVpcAssociationInvokeArgs Empty => new GetServiceNetworkVpcAssociationInvokeArgs();
    }


    [OutputType]
    public sealed class GetServiceNetworkVpcAssociationResult
    {
        public readonly string? Arn;
        public readonly string? CreatedAt;
        public readonly string? Id;
        public readonly ImmutableArray<string> SecurityGroupIds;
        public readonly string? ServiceNetworkArn;
        public readonly string? ServiceNetworkId;
        public readonly string? ServiceNetworkName;
        public readonly Pulumi.AwsNative.VpcLattice.ServiceNetworkVpcAssociationStatus? Status;
        public readonly ImmutableArray<Outputs.ServiceNetworkVpcAssociationTag> Tags;
        public readonly string? VpcId;

        [OutputConstructor]
        private GetServiceNetworkVpcAssociationResult(
            string? arn,

            string? createdAt,

            string? id,

            ImmutableArray<string> securityGroupIds,

            string? serviceNetworkArn,

            string? serviceNetworkId,

            string? serviceNetworkName,

            Pulumi.AwsNative.VpcLattice.ServiceNetworkVpcAssociationStatus? status,

            ImmutableArray<Outputs.ServiceNetworkVpcAssociationTag> tags,

            string? vpcId)
        {
            Arn = arn;
            CreatedAt = createdAt;
            Id = id;
            SecurityGroupIds = securityGroupIds;
            ServiceNetworkArn = serviceNetworkArn;
            ServiceNetworkId = serviceNetworkId;
            ServiceNetworkName = serviceNetworkName;
            Status = status;
            Tags = tags;
            VpcId = vpcId;
        }
    }
}
