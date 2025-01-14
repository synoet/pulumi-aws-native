// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pipes.Outputs
{

    [OutputType]
    public sealed class PipeCapacityProviderStrategyItem
    {
        public readonly int? Base;
        public readonly string CapacityProvider;
        public readonly int? Weight;

        [OutputConstructor]
        private PipeCapacityProviderStrategyItem(
            int? @base,

            string capacityProvider,

            int? weight)
        {
            Base = @base;
            CapacityProvider = capacityProvider;
            Weight = weight;
        }
    }
}
