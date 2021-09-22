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
    public sealed class LaunchTemplateLaunchTemplateData
    {
        public readonly ImmutableArray<Outputs.LaunchTemplateBlockDeviceMapping> BlockDeviceMappings;
        public readonly Outputs.LaunchTemplateCapacityReservationSpecification? CapacityReservationSpecification;
        public readonly Outputs.LaunchTemplateCpuOptions? CpuOptions;
        public readonly Outputs.LaunchTemplateCreditSpecification? CreditSpecification;
        public readonly bool? DisableApiTermination;
        public readonly bool? EbsOptimized;
        public readonly ImmutableArray<Outputs.LaunchTemplateElasticGpuSpecification> ElasticGpuSpecifications;
        public readonly ImmutableArray<Outputs.LaunchTemplateLaunchTemplateElasticInferenceAccelerator> ElasticInferenceAccelerators;
        public readonly Outputs.LaunchTemplateEnclaveOptions? EnclaveOptions;
        public readonly Outputs.LaunchTemplateHibernationOptions? HibernationOptions;
        public readonly Outputs.LaunchTemplateIamInstanceProfile? IamInstanceProfile;
        public readonly string? ImageId;
        public readonly string? InstanceInitiatedShutdownBehavior;
        public readonly Outputs.LaunchTemplateInstanceMarketOptions? InstanceMarketOptions;
        public readonly string? InstanceType;
        public readonly string? KernelId;
        public readonly string? KeyName;
        public readonly ImmutableArray<Outputs.LaunchTemplateLicenseSpecification> LicenseSpecifications;
        public readonly Outputs.LaunchTemplateMetadataOptions? MetadataOptions;
        public readonly Outputs.LaunchTemplateMonitoring? Monitoring;
        public readonly ImmutableArray<Outputs.LaunchTemplateNetworkInterface> NetworkInterfaces;
        public readonly Outputs.LaunchTemplatePlacement? Placement;
        public readonly string? RamDiskId;
        public readonly ImmutableArray<string> SecurityGroupIds;
        public readonly ImmutableArray<string> SecurityGroups;
        public readonly ImmutableArray<Outputs.LaunchTemplateTagSpecification> TagSpecifications;
        public readonly string? UserData;

        [OutputConstructor]
        private LaunchTemplateLaunchTemplateData(
            ImmutableArray<Outputs.LaunchTemplateBlockDeviceMapping> blockDeviceMappings,

            Outputs.LaunchTemplateCapacityReservationSpecification? capacityReservationSpecification,

            Outputs.LaunchTemplateCpuOptions? cpuOptions,

            Outputs.LaunchTemplateCreditSpecification? creditSpecification,

            bool? disableApiTermination,

            bool? ebsOptimized,

            ImmutableArray<Outputs.LaunchTemplateElasticGpuSpecification> elasticGpuSpecifications,

            ImmutableArray<Outputs.LaunchTemplateLaunchTemplateElasticInferenceAccelerator> elasticInferenceAccelerators,

            Outputs.LaunchTemplateEnclaveOptions? enclaveOptions,

            Outputs.LaunchTemplateHibernationOptions? hibernationOptions,

            Outputs.LaunchTemplateIamInstanceProfile? iamInstanceProfile,

            string? imageId,

            string? instanceInitiatedShutdownBehavior,

            Outputs.LaunchTemplateInstanceMarketOptions? instanceMarketOptions,

            string? instanceType,

            string? kernelId,

            string? keyName,

            ImmutableArray<Outputs.LaunchTemplateLicenseSpecification> licenseSpecifications,

            Outputs.LaunchTemplateMetadataOptions? metadataOptions,

            Outputs.LaunchTemplateMonitoring? monitoring,

            ImmutableArray<Outputs.LaunchTemplateNetworkInterface> networkInterfaces,

            Outputs.LaunchTemplatePlacement? placement,

            string? ramDiskId,

            ImmutableArray<string> securityGroupIds,

            ImmutableArray<string> securityGroups,

            ImmutableArray<Outputs.LaunchTemplateTagSpecification> tagSpecifications,

            string? userData)
        {
            BlockDeviceMappings = blockDeviceMappings;
            CapacityReservationSpecification = capacityReservationSpecification;
            CpuOptions = cpuOptions;
            CreditSpecification = creditSpecification;
            DisableApiTermination = disableApiTermination;
            EbsOptimized = ebsOptimized;
            ElasticGpuSpecifications = elasticGpuSpecifications;
            ElasticInferenceAccelerators = elasticInferenceAccelerators;
            EnclaveOptions = enclaveOptions;
            HibernationOptions = hibernationOptions;
            IamInstanceProfile = iamInstanceProfile;
            ImageId = imageId;
            InstanceInitiatedShutdownBehavior = instanceInitiatedShutdownBehavior;
            InstanceMarketOptions = instanceMarketOptions;
            InstanceType = instanceType;
            KernelId = kernelId;
            KeyName = keyName;
            LicenseSpecifications = licenseSpecifications;
            MetadataOptions = metadataOptions;
            Monitoring = monitoring;
            NetworkInterfaces = networkInterfaces;
            Placement = placement;
            RamDiskId = ramDiskId;
            SecurityGroupIds = securityGroupIds;
            SecurityGroups = securityGroups;
            TagSpecifications = tagSpecifications;
            UserData = userData;
        }
    }
}
