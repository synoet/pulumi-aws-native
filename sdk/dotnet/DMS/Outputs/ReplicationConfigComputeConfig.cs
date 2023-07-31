// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DMS.Outputs
{

    /// <summary>
    /// Configuration parameters for provisioning a AWS DMS Serverless replication
    /// </summary>
    [OutputType]
    public sealed class ReplicationConfigComputeConfig
    {
        public readonly string? AvailabilityZone;
        public readonly string? DnsNameServers;
        public readonly string? KmsKeyId;
        public readonly int MaxCapacityUnits;
        public readonly int? MinCapacityUnits;
        public readonly bool? MultiAz;
        public readonly string? PreferredMaintenanceWindow;
        public readonly string? ReplicationSubnetGroupId;
        public readonly ImmutableArray<string> VpcSecurityGroupIds;

        [OutputConstructor]
        private ReplicationConfigComputeConfig(
            string? availabilityZone,

            string? dnsNameServers,

            string? kmsKeyId,

            int maxCapacityUnits,

            int? minCapacityUnits,

            bool? multiAz,

            string? preferredMaintenanceWindow,

            string? replicationSubnetGroupId,

            ImmutableArray<string> vpcSecurityGroupIds)
        {
            AvailabilityZone = availabilityZone;
            DnsNameServers = dnsNameServers;
            KmsKeyId = kmsKeyId;
            MaxCapacityUnits = maxCapacityUnits;
            MinCapacityUnits = minCapacityUnits;
            MultiAz = multiAz;
            PreferredMaintenanceWindow = preferredMaintenanceWindow;
            ReplicationSubnetGroupId = replicationSubnetGroupId;
            VpcSecurityGroupIds = vpcSecurityGroupIds;
        }
    }
}
