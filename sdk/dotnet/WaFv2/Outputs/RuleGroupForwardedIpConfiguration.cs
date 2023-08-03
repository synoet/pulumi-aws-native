// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WaFv2.Outputs
{

    [OutputType]
    public sealed class RuleGroupForwardedIpConfiguration
    {
        public readonly Pulumi.AwsNative.WaFv2.RuleGroupForwardedIpConfigurationFallbackBehavior FallbackBehavior;
        public readonly string HeaderName;

        [OutputConstructor]
        private RuleGroupForwardedIpConfiguration(
            Pulumi.AwsNative.WaFv2.RuleGroupForwardedIpConfigurationFallbackBehavior fallbackBehavior,

            string headerName)
        {
            FallbackBehavior = fallbackBehavior;
            HeaderName = headerName;
        }
    }
}
