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
    public sealed class WebAclRuleGroupReferenceStatement
    {
        public readonly string Arn;
        public readonly ImmutableArray<Outputs.WebAclExcludedRule> ExcludedRules;
        /// <summary>
        /// Action overrides for rules in the rule group.
        /// </summary>
        public readonly ImmutableArray<Outputs.WebAclRuleActionOverride> RuleActionOverrides;

        [OutputConstructor]
        private WebAclRuleGroupReferenceStatement(
            string arn,

            ImmutableArray<Outputs.WebAclExcludedRule> excludedRules,

            ImmutableArray<Outputs.WebAclRuleActionOverride> ruleActionOverrides)
        {
            Arn = arn;
            ExcludedRules = excludedRules;
            RuleActionOverrides = ruleActionOverrides;
        }
    }
}
