// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Outputs
{

    [OutputType]
    public sealed class Ec2FleetSpotOptionsRequest
    {
        public readonly Pulumi.AwsNative.Ec2.Ec2FleetSpotOptionsRequestAllocationStrategy? AllocationStrategy;
        public readonly Pulumi.AwsNative.Ec2.Ec2FleetSpotOptionsRequestInstanceInterruptionBehavior? InstanceInterruptionBehavior;
        public readonly int? InstancePoolsToUseCount;
        public readonly Outputs.Ec2FleetMaintenanceStrategies? MaintenanceStrategies;
        public readonly string? MaxTotalPrice;
        public readonly int? MinTargetCapacity;
        public readonly bool? SingleAvailabilityZone;
        public readonly bool? SingleInstanceType;

        [OutputConstructor]
        private Ec2FleetSpotOptionsRequest(
            Pulumi.AwsNative.Ec2.Ec2FleetSpotOptionsRequestAllocationStrategy? allocationStrategy,

            Pulumi.AwsNative.Ec2.Ec2FleetSpotOptionsRequestInstanceInterruptionBehavior? instanceInterruptionBehavior,

            int? instancePoolsToUseCount,

            Outputs.Ec2FleetMaintenanceStrategies? maintenanceStrategies,

            string? maxTotalPrice,

            int? minTargetCapacity,

            bool? singleAvailabilityZone,

            bool? singleInstanceType)
        {
            AllocationStrategy = allocationStrategy;
            InstanceInterruptionBehavior = instanceInterruptionBehavior;
            InstancePoolsToUseCount = instancePoolsToUseCount;
            MaintenanceStrategies = maintenanceStrategies;
            MaxTotalPrice = maxTotalPrice;
            MinTargetCapacity = minTargetCapacity;
            SingleAvailabilityZone = singleAvailabilityZone;
            SingleInstanceType = singleInstanceType;
        }
    }
}
