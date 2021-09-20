// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFormation.Outputs
{

    /// <summary>
    /// The user-specified preferences for how AWS CloudFormation performs a stack set operation.
    /// </summary>
    [OutputType]
    public sealed class StackSetOperationPreferences
    {
        public readonly int? FailureToleranceCount;
        public readonly int? FailureTolerancePercentage;
        public readonly int? MaxConcurrentCount;
        public readonly int? MaxConcurrentPercentage;
        public readonly Pulumi.AwsNative.CloudFormation.StackSetRegionConcurrencyType? RegionConcurrencyType;
        public readonly ImmutableArray<string> RegionOrder;

        [OutputConstructor]
        private StackSetOperationPreferences(
            int? failureToleranceCount,

            int? failureTolerancePercentage,

            int? maxConcurrentCount,

            int? maxConcurrentPercentage,

            Pulumi.AwsNative.CloudFormation.StackSetRegionConcurrencyType? regionConcurrencyType,

            ImmutableArray<string> regionOrder)
        {
            FailureToleranceCount = failureToleranceCount;
            FailureTolerancePercentage = failureTolerancePercentage;
            MaxConcurrentCount = maxConcurrentCount;
            MaxConcurrentPercentage = maxConcurrentPercentage;
            RegionConcurrencyType = regionConcurrencyType;
            RegionOrder = regionOrder;
        }
    }
}
