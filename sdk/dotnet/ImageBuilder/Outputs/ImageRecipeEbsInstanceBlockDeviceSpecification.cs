// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ImageBuilder.Outputs
{

    /// <summary>
    /// Amazon EBS-specific block device mapping specifications. 
    /// </summary>
    [OutputType]
    public sealed class ImageRecipeEbsInstanceBlockDeviceSpecification
    {
        /// <summary>
        /// Use to configure delete on termination of the associated device.
        /// </summary>
        public readonly bool? DeleteOnTermination;
        /// <summary>
        /// Use to configure device encryption.
        /// </summary>
        public readonly bool? Encrypted;
        /// <summary>
        /// Use to configure device IOPS.
        /// </summary>
        public readonly int? Iops;
        /// <summary>
        /// Use to configure the KMS key to use when encrypting the device.
        /// </summary>
        public readonly string? KmsKeyId;
        /// <summary>
        /// The snapshot that defines the device contents.
        /// </summary>
        public readonly string? SnapshotId;
        /// <summary>
        /// Use to override the device's volume size.
        /// </summary>
        public readonly int? VolumeSize;
        /// <summary>
        /// Use to override the device's volume type.
        /// </summary>
        public readonly Pulumi.AwsNative.ImageBuilder.ImageRecipeEbsInstanceBlockDeviceSpecificationVolumeType? VolumeType;

        [OutputConstructor]
        private ImageRecipeEbsInstanceBlockDeviceSpecification(
            bool? deleteOnTermination,

            bool? encrypted,

            int? iops,

            string? kmsKeyId,

            string? snapshotId,

            int? volumeSize,

            Pulumi.AwsNative.ImageBuilder.ImageRecipeEbsInstanceBlockDeviceSpecificationVolumeType? volumeType)
        {
            DeleteOnTermination = deleteOnTermination;
            Encrypted = encrypted;
            Iops = iops;
            KmsKeyId = kmsKeyId;
            SnapshotId = snapshotId;
            VolumeSize = volumeSize;
            VolumeType = volumeType;
        }
    }
}
