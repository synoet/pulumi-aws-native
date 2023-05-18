// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GameLift.Outputs
{

    /// <summary>
    /// Configuration for Anywhere fleet.
    /// </summary>
    [OutputType]
    public sealed class FleetAnywhereConfiguration
    {
        /// <summary>
        /// Cost of compute can be specified on Anywhere Fleets to prioritize placement across Queue destinations based on Cost.
        /// </summary>
        public readonly string Cost;

        [OutputConstructor]
        private FleetAnywhereConfiguration(string cost)
        {
            Cost = cost;
        }
    }
}
