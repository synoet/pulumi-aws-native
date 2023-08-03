// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WafRegional
{
    /// <summary>
    /// Resource Type definition for AWS::WAFRegional::Rule
    /// </summary>
    [Obsolete(@"Rule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:wafregional:Rule")]
    public partial class Rule : global::Pulumi.CustomResource
    {
        [Output("metricName")]
        public Output<string> MetricName { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("predicates")]
        public Output<ImmutableArray<Outputs.RulePredicate>> Predicates { get; private set; } = null!;


        /// <summary>
        /// Create a Rule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Rule(string name, RuleArgs args, CustomResourceOptions? options = null)
            : base("aws-native:wafregional:Rule", name, args ?? new RuleArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Rule(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:wafregional:Rule", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Rule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Rule Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Rule(name, id, options);
        }
    }

    public sealed class RuleArgs : global::Pulumi.ResourceArgs
    {
        [Input("metricName", required: true)]
        public Input<string> MetricName { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("predicates")]
        private InputList<Inputs.RulePredicateArgs>? _predicates;
        public InputList<Inputs.RulePredicateArgs> Predicates
        {
            get => _predicates ?? (_predicates = new InputList<Inputs.RulePredicateArgs>());
            set => _predicates = value;
        }

        public RuleArgs()
        {
        }
        public static new RuleArgs Empty => new RuleArgs();
    }
}
