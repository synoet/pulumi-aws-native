// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WaFv2.Inputs
{

    public sealed class RuleGroupForwardedIpConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("fallbackBehavior", required: true)]
        public Input<Pulumi.AwsNative.WaFv2.RuleGroupForwardedIpConfigurationFallbackBehavior> FallbackBehavior { get; set; } = null!;

        [Input("headerName", required: true)]
        public Input<string> HeaderName { get; set; } = null!;

        public RuleGroupForwardedIpConfigurationArgs()
        {
        }
        public static new RuleGroupForwardedIpConfigurationArgs Empty => new RuleGroupForwardedIpConfigurationArgs();
    }
}
