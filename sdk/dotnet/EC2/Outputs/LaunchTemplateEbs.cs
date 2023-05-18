// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2.Outputs
{

    [OutputType]
    public sealed class LaunchTemplateEbs
    {
        public readonly bool? DeleteOnTermination;
        public readonly bool? Encrypted;
        public readonly int? Iops;
        public readonly string? KmsKeyId;
        public readonly string? SnapshotId;
        public readonly int? Throughput;
        public readonly int? VolumeSize;
        public readonly string? VolumeType;

        [OutputConstructor]
        private LaunchTemplateEbs(
            bool? deleteOnTermination,

            bool? encrypted,

            int? iops,

            string? kmsKeyId,

            string? snapshotId,

            int? throughput,

            int? volumeSize,

            string? volumeType)
        {
            DeleteOnTermination = deleteOnTermination;
            Encrypted = encrypted;
            Iops = iops;
            KmsKeyId = kmsKeyId;
            SnapshotId = snapshotId;
            Throughput = throughput;
            VolumeSize = volumeSize;
            VolumeType = volumeType;
        }
    }
}
