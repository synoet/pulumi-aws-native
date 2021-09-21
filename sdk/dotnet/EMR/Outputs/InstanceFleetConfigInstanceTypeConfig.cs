// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EMR.Outputs
{

    [OutputType]
    public sealed class InstanceFleetConfigInstanceTypeConfig
    {
        public readonly string? BidPrice;
        public readonly double? BidPriceAsPercentageOfOnDemandPrice;
        public readonly ImmutableArray<Outputs.InstanceFleetConfigConfiguration> Configurations;
        public readonly Outputs.InstanceFleetConfigEbsConfiguration? EbsConfiguration;
        public readonly string InstanceType;
        public readonly int? WeightedCapacity;

        [OutputConstructor]
        private InstanceFleetConfigInstanceTypeConfig(
            string? bidPrice,

            double? bidPriceAsPercentageOfOnDemandPrice,

            ImmutableArray<Outputs.InstanceFleetConfigConfiguration> configurations,

            Outputs.InstanceFleetConfigEbsConfiguration? ebsConfiguration,

            string instanceType,

            int? weightedCapacity)
        {
            BidPrice = bidPrice;
            BidPriceAsPercentageOfOnDemandPrice = bidPriceAsPercentageOfOnDemandPrice;
            Configurations = configurations;
            EbsConfiguration = ebsConfiguration;
            InstanceType = instanceType;
            WeightedCapacity = weightedCapacity;
        }
    }
}
