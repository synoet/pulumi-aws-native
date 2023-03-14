// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.VpcLattice
{
    /// <summary>
    /// A unit of configuration defining how Mercury routes incoming requests for a Service to its Target Groups
    /// </summary>
    [AwsNativeResourceType("aws-native:vpclattice:Rule")]
    public partial class Rule : global::Pulumi.CustomResource
    {
        [Output("action")]
        public Output<Outputs.RuleAction> Action { get; private set; } = null!;

        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("listenerIdentifier")]
        public Output<string?> ListenerIdentifier { get; private set; } = null!;

        [Output("match")]
        public Output<Outputs.RuleMatch> Match { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("priority")]
        public Output<int> Priority { get; private set; } = null!;

        [Output("serviceIdentifier")]
        public Output<string?> ServiceIdentifier { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.RuleTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Rule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Rule(string name, RuleArgs args, CustomResourceOptions? options = null)
            : base("aws-native:vpclattice:Rule", name, args ?? new RuleArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Rule(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:vpclattice:Rule", name, null, MakeResourceOptions(options, id))
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
        [Input("action", required: true)]
        public Input<Inputs.RuleActionArgs> Action { get; set; } = null!;

        [Input("listenerIdentifier")]
        public Input<string>? ListenerIdentifier { get; set; }

        [Input("match", required: true)]
        public Input<Inputs.RuleMatchArgs> Match { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("priority", required: true)]
        public Input<int> Priority { get; set; } = null!;

        [Input("serviceIdentifier")]
        public Input<string>? ServiceIdentifier { get; set; }

        [Input("tags")]
        private InputList<Inputs.RuleTagArgs>? _tags;
        public InputList<Inputs.RuleTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.RuleTagArgs>());
            set => _tags = value;
        }

        public RuleArgs()
        {
        }
        public static new RuleArgs Empty => new RuleArgs();
    }
}
