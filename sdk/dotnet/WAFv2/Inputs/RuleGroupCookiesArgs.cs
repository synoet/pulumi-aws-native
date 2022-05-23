// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFv2.Inputs
{

    /// <summary>
    /// Includes headers of a web request.
    /// </summary>
    public sealed class RuleGroupCookiesArgs : Pulumi.ResourceArgs
    {
        [Input("matchPattern", required: true)]
        public Input<Inputs.RuleGroupCookieMatchPatternArgs> MatchPattern { get; set; } = null!;

        [Input("matchScope", required: true)]
        public Input<Pulumi.AwsNative.WAFv2.RuleGroupMapMatchScope> MatchScope { get; set; } = null!;

        [Input("oversizeHandling", required: true)]
        public Input<Pulumi.AwsNative.WAFv2.RuleGroupOversizeHandling> OversizeHandling { get; set; } = null!;

        public RuleGroupCookiesArgs()
        {
        }
    }
}
