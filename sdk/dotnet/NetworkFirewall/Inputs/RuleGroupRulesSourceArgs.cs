// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.NetworkFirewall.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html
    /// </summary>
    public sealed class RuleGroupRulesSourceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-rulessourcelist
        /// </summary>
        [Input("RulesSourceList")]
        public Input<Inputs.RuleGroupRulesSourceListArgs>? RulesSourceList { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-rulesstring
        /// </summary>
        [Input("RulesString")]
        public Input<string>? RulesString { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-statefulrules
        /// </summary>
        [Input("StatefulRules")]
        public Input<Inputs.RuleGroupStatefulRulesArgs>? StatefulRules { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-statelessrulesandcustomactions
        /// </summary>
        [Input("StatelessRulesAndCustomActions")]
        public Input<Inputs.RuleGroupStatelessRulesAndCustomActionsArgs>? StatelessRulesAndCustomActions { get; set; }

        public RuleGroupRulesSourceArgs()
        {
        }
    }
}