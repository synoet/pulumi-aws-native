// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    public static class GetIpamResourceDiscoveryAssociation
    {
        /// <summary>
        /// Resource Schema of AWS::EC2::IPAMResourceDiscoveryAssociation Type
        /// </summary>
        public static Task<GetIpamResourceDiscoveryAssociationResult> InvokeAsync(GetIpamResourceDiscoveryAssociationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetIpamResourceDiscoveryAssociationResult>("aws-native:ec2:getIpamResourceDiscoveryAssociation", args ?? new GetIpamResourceDiscoveryAssociationArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Schema of AWS::EC2::IPAMResourceDiscoveryAssociation Type
        /// </summary>
        public static Output<GetIpamResourceDiscoveryAssociationResult> Invoke(GetIpamResourceDiscoveryAssociationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetIpamResourceDiscoveryAssociationResult>("aws-native:ec2:getIpamResourceDiscoveryAssociation", args ?? new GetIpamResourceDiscoveryAssociationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetIpamResourceDiscoveryAssociationArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Id of the IPAM Resource Discovery Association.
        /// </summary>
        [Input("ipamResourceDiscoveryAssociationId", required: true)]
        public string IpamResourceDiscoveryAssociationId { get; set; } = null!;

        public GetIpamResourceDiscoveryAssociationArgs()
        {
        }
        public static new GetIpamResourceDiscoveryAssociationArgs Empty => new GetIpamResourceDiscoveryAssociationArgs();
    }

    public sealed class GetIpamResourceDiscoveryAssociationInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Id of the IPAM Resource Discovery Association.
        /// </summary>
        [Input("ipamResourceDiscoveryAssociationId", required: true)]
        public Input<string> IpamResourceDiscoveryAssociationId { get; set; } = null!;

        public GetIpamResourceDiscoveryAssociationInvokeArgs()
        {
        }
        public static new GetIpamResourceDiscoveryAssociationInvokeArgs Empty => new GetIpamResourceDiscoveryAssociationInvokeArgs();
    }


    [OutputType]
    public sealed class GetIpamResourceDiscoveryAssociationResult
    {
        /// <summary>
        /// Arn of the IPAM.
        /// </summary>
        public readonly string? IpamArn;
        /// <summary>
        /// The home region of the IPAM.
        /// </summary>
        public readonly string? IpamRegion;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the resource discovery association is a part of.
        /// </summary>
        public readonly string? IpamResourceDiscoveryAssociationArn;
        /// <summary>
        /// Id of the IPAM Resource Discovery Association.
        /// </summary>
        public readonly string? IpamResourceDiscoveryAssociationId;
        /// <summary>
        /// If the Resource Discovery Association exists due as part of CreateIpam.
        /// </summary>
        public readonly bool? IsDefault;
        /// <summary>
        /// The AWS Account ID for the account where the shared IPAM exists.
        /// </summary>
        public readonly string? OwnerId;
        /// <summary>
        /// The status of the resource discovery.
        /// </summary>
        public readonly string? ResourceDiscoveryStatus;
        /// <summary>
        /// The operational state of the Resource Discovery Association. Related to Create/Delete activities.
        /// </summary>
        public readonly string? State;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.IpamResourceDiscoveryAssociationTag> Tags;

        [OutputConstructor]
        private GetIpamResourceDiscoveryAssociationResult(
            string? ipamArn,

            string? ipamRegion,

            string? ipamResourceDiscoveryAssociationArn,

            string? ipamResourceDiscoveryAssociationId,

            bool? isDefault,

            string? ownerId,

            string? resourceDiscoveryStatus,

            string? state,

            ImmutableArray<Outputs.IpamResourceDiscoveryAssociationTag> tags)
        {
            IpamArn = ipamArn;
            IpamRegion = ipamRegion;
            IpamResourceDiscoveryAssociationArn = ipamResourceDiscoveryAssociationArn;
            IpamResourceDiscoveryAssociationId = ipamResourceDiscoveryAssociationId;
            IsDefault = isDefault;
            OwnerId = ownerId;
            ResourceDiscoveryStatus = resourceDiscoveryStatus;
            State = state;
            Tags = tags;
        }
    }
}
