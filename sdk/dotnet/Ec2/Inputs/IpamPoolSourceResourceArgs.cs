// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Inputs
{

    /// <summary>
    /// The resource associated with this pool's space. Depending on the ResourceType, setting a SourceResource changes which space can be provisioned in this pool and which types of resources can receive allocations
    /// </summary>
    public sealed class IpamPoolSourceResourceArgs : global::Pulumi.ResourceArgs
    {
        [Input("resourceId", required: true)]
        public Input<string> ResourceId { get; set; } = null!;

        [Input("resourceOwner", required: true)]
        public Input<string> ResourceOwner { get; set; } = null!;

        [Input("resourceRegion", required: true)]
        public Input<string> ResourceRegion { get; set; } = null!;

        [Input("resourceType", required: true)]
        public Input<string> ResourceType { get; set; } = null!;

        public IpamPoolSourceResourceArgs()
        {
        }
        public static new IpamPoolSourceResourceArgs Empty => new IpamPoolSourceResourceArgs();
    }
}
