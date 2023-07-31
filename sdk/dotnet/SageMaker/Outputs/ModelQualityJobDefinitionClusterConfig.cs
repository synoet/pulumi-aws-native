// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Outputs
{

    /// <summary>
    /// Configuration for the cluster used to run model monitoring jobs.
    /// </summary>
    [OutputType]
    public sealed class ModelQualityJobDefinitionClusterConfig
    {
        /// <summary>
        /// The number of ML compute instances to use in the model monitoring job. For distributed processing jobs, specify a value greater than 1. The default value is 1.
        /// </summary>
        public readonly int InstanceCount;
        /// <summary>
        /// The ML compute instance type for the processing job.
        /// </summary>
        public readonly string InstanceType;
        /// <summary>
        /// The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the model monitoring job.
        /// </summary>
        public readonly string? VolumeKmsKeyId;
        /// <summary>
        /// The size of the ML storage volume, in gigabytes, that you want to provision. You must specify sufficient ML storage for your scenario.
        /// </summary>
        public readonly int VolumeSizeInGb;

        [OutputConstructor]
        private ModelQualityJobDefinitionClusterConfig(
            int instanceCount,

            string instanceType,

            string? volumeKmsKeyId,

            int volumeSizeInGb)
        {
            InstanceCount = instanceCount;
            InstanceType = instanceType;
            VolumeKmsKeyId = volumeKmsKeyId;
            VolumeSizeInGb = volumeSizeInGb;
        }
    }
}
