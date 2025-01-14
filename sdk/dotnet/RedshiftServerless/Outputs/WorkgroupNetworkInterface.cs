// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RedshiftServerless.Outputs
{

    [OutputType]
    public sealed class WorkgroupNetworkInterface
    {
        public readonly string? AvailabilityZone;
        public readonly string? NetworkInterfaceId;
        public readonly string? PrivateIpAddress;
        public readonly string? SubnetId;

        [OutputConstructor]
        private WorkgroupNetworkInterface(
            string? availabilityZone,

            string? networkInterfaceId,

            string? privateIpAddress,

            string? subnetId)
        {
            AvailabilityZone = availabilityZone;
            NetworkInterfaceId = networkInterfaceId;
            PrivateIpAddress = privateIpAddress;
            SubnetId = subnetId;
        }
    }
}
