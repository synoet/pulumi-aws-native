// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NetworkFirewall.Outputs
{

    [OutputType]
    public sealed class RuleGroup
    {
        public readonly Outputs.RuleGroupReferenceSets? ReferenceSets;
        public readonly Outputs.RuleGroupRuleVariables? RuleVariables;
        public readonly Outputs.RuleGroupRulesSource RulesSource;
        public readonly Outputs.RuleGroupStatefulRuleOptions? StatefulRuleOptions;

        [OutputConstructor]
        private RuleGroup(
            Outputs.RuleGroupReferenceSets? referenceSets,

            Outputs.RuleGroupRuleVariables? ruleVariables,

            Outputs.RuleGroupRulesSource rulesSource,

            Outputs.RuleGroupStatefulRuleOptions? statefulRuleOptions)
        {
            ReferenceSets = referenceSets;
            RuleVariables = ruleVariables;
            RulesSource = rulesSource;
            StatefulRuleOptions = statefulRuleOptions;
        }
    }
}
