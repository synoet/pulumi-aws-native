// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2.Outputs
{

    [OutputType]
    public sealed class SpotFleetSpotFleetRequestConfigData
    {
        public readonly Pulumi.AwsNative.EC2.SpotFleetSpotFleetRequestConfigDataAllocationStrategy? AllocationStrategy;
        public readonly string? Context;
        public readonly Pulumi.AwsNative.EC2.SpotFleetSpotFleetRequestConfigDataExcessCapacityTerminationPolicy? ExcessCapacityTerminationPolicy;
        public readonly string IamFleetRole;
        public readonly Pulumi.AwsNative.EC2.SpotFleetSpotFleetRequestConfigDataInstanceInterruptionBehavior? InstanceInterruptionBehavior;
        public readonly int? InstancePoolsToUseCount;
        public readonly ImmutableArray<Outputs.SpotFleetSpotFleetLaunchSpecification> LaunchSpecifications;
        public readonly ImmutableArray<Outputs.SpotFleetLaunchTemplateConfig> LaunchTemplateConfigs;
        public readonly Outputs.SpotFleetLoadBalancersConfig? LoadBalancersConfig;
        public readonly string? OnDemandAllocationStrategy;
        public readonly string? OnDemandMaxTotalPrice;
        public readonly int? OnDemandTargetCapacity;
        public readonly bool? ReplaceUnhealthyInstances;
        public readonly Outputs.SpotFleetSpotMaintenanceStrategies? SpotMaintenanceStrategies;
        public readonly string? SpotMaxTotalPrice;
        public readonly string? SpotPrice;
        public readonly int TargetCapacity;
        public readonly bool? TerminateInstancesWithExpiration;
        public readonly Pulumi.AwsNative.EC2.SpotFleetSpotFleetRequestConfigDataType? Type;
        public readonly string? ValidFrom;
        public readonly string? ValidUntil;

        [OutputConstructor]
        private SpotFleetSpotFleetRequestConfigData(
            Pulumi.AwsNative.EC2.SpotFleetSpotFleetRequestConfigDataAllocationStrategy? allocationStrategy,

            string? context,

            Pulumi.AwsNative.EC2.SpotFleetSpotFleetRequestConfigDataExcessCapacityTerminationPolicy? excessCapacityTerminationPolicy,

            string iamFleetRole,

            Pulumi.AwsNative.EC2.SpotFleetSpotFleetRequestConfigDataInstanceInterruptionBehavior? instanceInterruptionBehavior,

            int? instancePoolsToUseCount,

            ImmutableArray<Outputs.SpotFleetSpotFleetLaunchSpecification> launchSpecifications,

            ImmutableArray<Outputs.SpotFleetLaunchTemplateConfig> launchTemplateConfigs,

            Outputs.SpotFleetLoadBalancersConfig? loadBalancersConfig,

            string? onDemandAllocationStrategy,

            string? onDemandMaxTotalPrice,

            int? onDemandTargetCapacity,

            bool? replaceUnhealthyInstances,

            Outputs.SpotFleetSpotMaintenanceStrategies? spotMaintenanceStrategies,

            string? spotMaxTotalPrice,

            string? spotPrice,

            int targetCapacity,

            bool? terminateInstancesWithExpiration,

            Pulumi.AwsNative.EC2.SpotFleetSpotFleetRequestConfigDataType? type,

            string? validFrom,

            string? validUntil)
        {
            AllocationStrategy = allocationStrategy;
            Context = context;
            ExcessCapacityTerminationPolicy = excessCapacityTerminationPolicy;
            IamFleetRole = iamFleetRole;
            InstanceInterruptionBehavior = instanceInterruptionBehavior;
            InstancePoolsToUseCount = instancePoolsToUseCount;
            LaunchSpecifications = launchSpecifications;
            LaunchTemplateConfigs = launchTemplateConfigs;
            LoadBalancersConfig = loadBalancersConfig;
            OnDemandAllocationStrategy = onDemandAllocationStrategy;
            OnDemandMaxTotalPrice = onDemandMaxTotalPrice;
            OnDemandTargetCapacity = onDemandTargetCapacity;
            ReplaceUnhealthyInstances = replaceUnhealthyInstances;
            SpotMaintenanceStrategies = spotMaintenanceStrategies;
            SpotMaxTotalPrice = spotMaxTotalPrice;
            SpotPrice = spotPrice;
            TargetCapacity = targetCapacity;
            TerminateInstancesWithExpiration = terminateInstancesWithExpiration;
            Type = type;
            ValidFrom = validFrom;
            ValidUntil = validUntil;
        }
    }
}
