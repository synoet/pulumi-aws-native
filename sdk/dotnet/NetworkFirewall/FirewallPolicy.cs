// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NetworkFirewall
{
    /// <summary>
    /// Resource type definition for AWS::NetworkFirewall::FirewallPolicy
    /// </summary>
    [AwsNativeResourceType("aws-native:networkfirewall:FirewallPolicy")]
    public partial class FirewallPolicy : global::Pulumi.CustomResource
    {
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("firewallPolicy")]
        public Output<Outputs.FirewallPolicy> FirewallPolicyValue { get; private set; } = null!;

        [Output("firewallPolicyArn")]
        public Output<string> FirewallPolicyArn { get; private set; } = null!;

        [Output("firewallPolicyId")]
        public Output<string> FirewallPolicyId { get; private set; } = null!;

        [Output("firewallPolicyName")]
        public Output<string> FirewallPolicyName { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.FirewallPolicyTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a FirewallPolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FirewallPolicy(string name, FirewallPolicyArgs args, CustomResourceOptions? options = null)
            : base("aws-native:networkfirewall:FirewallPolicy", name, args ?? new FirewallPolicyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FirewallPolicy(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:networkfirewall:FirewallPolicy", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "firewallPolicyName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing FirewallPolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FirewallPolicy Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new FirewallPolicy(name, id, options);
        }
    }

    public sealed class FirewallPolicyArgs : global::Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("firewallPolicy", required: true)]
        public Input<Inputs.FirewallPolicyArgs> FirewallPolicyValue { get; set; } = null!;

        [Input("firewallPolicyName")]
        public Input<string>? FirewallPolicyName { get; set; }

        [Input("tags")]
        private InputList<Inputs.FirewallPolicyTagArgs>? _tags;
        public InputList<Inputs.FirewallPolicyTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.FirewallPolicyTagArgs>());
            set => _tags = value;
        }

        public FirewallPolicyArgs()
        {
        }
        public static new FirewallPolicyArgs Empty => new FirewallPolicyArgs();
    }
}
