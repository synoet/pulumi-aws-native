// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.NetworkFirewall.Outputs
{

    [OutputType]
    public sealed class FirewallPolicyStatefulRuleGroupReferences
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreferences.html#cfn-networkfirewall-firewallpolicy-statefulrulegroupreferences-statefulrulegroupreferences
        /// </summary>
        public readonly ImmutableArray<Outputs.FirewallPolicyStatefulRuleGroupReference> StatefulRuleGroupReferences;

        [OutputConstructor]
        private FirewallPolicyStatefulRuleGroupReferences(ImmutableArray<Outputs.FirewallPolicyStatefulRuleGroupReference> StatefulRuleGroupReferences)
        {
            this.StatefulRuleGroupReferences = StatefulRuleGroupReferences;
        }
    }
}