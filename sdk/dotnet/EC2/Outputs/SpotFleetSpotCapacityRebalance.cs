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
    public sealed class SpotFleetSpotCapacityRebalance
    {
        public readonly Pulumi.AwsNative.EC2.SpotFleetSpotCapacityRebalanceReplacementStrategy? ReplacementStrategy;
        public readonly int? TerminationDelay;

        [OutputConstructor]
        private SpotFleetSpotCapacityRebalance(
            Pulumi.AwsNative.EC2.SpotFleetSpotCapacityRebalanceReplacementStrategy? replacementStrategy,

            int? terminationDelay)
        {
            ReplacementStrategy = replacementStrategy;
            TerminationDelay = terminationDelay;
        }
    }
}
