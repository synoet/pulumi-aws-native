// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.VpcLattice.Outputs
{

    [OutputType]
    public sealed class TargetGroupHealthCheckConfig
    {
        public readonly bool? Enabled;
        public readonly int? HealthCheckIntervalSeconds;
        public readonly int? HealthCheckTimeoutSeconds;
        public readonly int? HealthyThresholdCount;
        public readonly Outputs.TargetGroupMatcher? Matcher;
        public readonly string? Path;
        public readonly int? Port;
        public readonly Pulumi.AwsNative.VpcLattice.TargetGroupHealthCheckConfigProtocol? Protocol;
        public readonly int? UnhealthyThresholdCount;

        [OutputConstructor]
        private TargetGroupHealthCheckConfig(
            bool? enabled,

            int? healthCheckIntervalSeconds,

            int? healthCheckTimeoutSeconds,

            int? healthyThresholdCount,

            Outputs.TargetGroupMatcher? matcher,

            string? path,

            int? port,

            Pulumi.AwsNative.VpcLattice.TargetGroupHealthCheckConfigProtocol? protocol,

            int? unhealthyThresholdCount)
        {
            Enabled = enabled;
            HealthCheckIntervalSeconds = healthCheckIntervalSeconds;
            HealthCheckTimeoutSeconds = healthCheckTimeoutSeconds;
            HealthyThresholdCount = healthyThresholdCount;
            Matcher = matcher;
            Path = path;
            Port = port;
            Protocol = protocol;
            UnhealthyThresholdCount = unhealthyThresholdCount;
        }
    }
}
