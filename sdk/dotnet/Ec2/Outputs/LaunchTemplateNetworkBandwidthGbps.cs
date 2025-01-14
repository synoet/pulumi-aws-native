// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Outputs
{

    /// <summary>
    /// The minimum and maximum amount of network bandwidth, in gigabits per second (Gbps).
    /// </summary>
    [OutputType]
    public sealed class LaunchTemplateNetworkBandwidthGbps
    {
        /// <summary>
        /// The maximum amount of network bandwidth, in Gbps.
        /// </summary>
        public readonly double? Max;
        /// <summary>
        /// The minimum amount of network bandwidth, in Gbps.
        /// </summary>
        public readonly double? Min;

        [OutputConstructor]
        private LaunchTemplateNetworkBandwidthGbps(
            double? max,

            double? min)
        {
            Max = max;
            Min = min;
        }
    }
}
