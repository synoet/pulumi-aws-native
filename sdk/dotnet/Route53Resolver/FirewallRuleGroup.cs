// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Route53Resolver
{
    /// <summary>
    /// Resource schema for AWS::Route53Resolver::FirewallRuleGroup.
    /// </summary>
    [AwsNativeResourceType("aws-native:route53resolver:FirewallRuleGroup")]
    public partial class FirewallRuleGroup : Pulumi.CustomResource
    {
        /// <summary>
        /// Arn
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Rfc3339TimeString
        /// </summary>
        [Output("creationTime")]
        public Output<string> CreationTime { get; private set; } = null!;

        /// <summary>
        /// The id of the creator request.
        /// </summary>
        [Output("creatorRequestId")]
        public Output<string> CreatorRequestId { get; private set; } = null!;

        /// <summary>
        /// FirewallRules
        /// </summary>
        [Output("firewallRules")]
        public Output<ImmutableArray<Outputs.FirewallRuleGroupFirewallRule>> FirewallRules { get; private set; } = null!;

        /// <summary>
        /// Rfc3339TimeString
        /// </summary>
        [Output("modificationTime")]
        public Output<string> ModificationTime { get; private set; } = null!;

        /// <summary>
        /// FirewallRuleGroupName
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// AccountId
        /// </summary>
        [Output("ownerId")]
        public Output<string> OwnerId { get; private set; } = null!;

        /// <summary>
        /// Count
        /// </summary>
        [Output("ruleCount")]
        public Output<int> RuleCount { get; private set; } = null!;

        /// <summary>
        /// ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.
        /// </summary>
        [Output("shareStatus")]
        public Output<Pulumi.AwsNative.Route53Resolver.FirewallRuleGroupShareStatus> ShareStatus { get; private set; } = null!;

        /// <summary>
        /// ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
        /// </summary>
        [Output("status")]
        public Output<Pulumi.AwsNative.Route53Resolver.FirewallRuleGroupStatus> Status { get; private set; } = null!;

        /// <summary>
        /// FirewallRuleGroupStatus
        /// </summary>
        [Output("statusMessage")]
        public Output<string> StatusMessage { get; private set; } = null!;

        /// <summary>
        /// Tags
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.FirewallRuleGroupTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a FirewallRuleGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FirewallRuleGroup(string name, FirewallRuleGroupArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:route53resolver:FirewallRuleGroup", name, args ?? new FirewallRuleGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FirewallRuleGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:route53resolver:FirewallRuleGroup", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing FirewallRuleGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FirewallRuleGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new FirewallRuleGroup(name, id, options);
        }
    }

    public sealed class FirewallRuleGroupArgs : Pulumi.ResourceArgs
    {
        [Input("firewallRules")]
        private InputList<Inputs.FirewallRuleGroupFirewallRuleArgs>? _firewallRules;

        /// <summary>
        /// FirewallRules
        /// </summary>
        public InputList<Inputs.FirewallRuleGroupFirewallRuleArgs> FirewallRules
        {
            get => _firewallRules ?? (_firewallRules = new InputList<Inputs.FirewallRuleGroupFirewallRuleArgs>());
            set => _firewallRules = value;
        }

        /// <summary>
        /// FirewallRuleGroupName
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputList<Inputs.FirewallRuleGroupTagArgs>? _tags;

        /// <summary>
        /// Tags
        /// </summary>
        public InputList<Inputs.FirewallRuleGroupTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.FirewallRuleGroupTagArgs>());
            set => _tags = value;
        }

        public FirewallRuleGroupArgs()
        {
        }
    }
}
