// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue
{
    /// <summary>
    /// Resource Type definition for AWS::Glue::Trigger
    /// </summary>
    [Obsolete(@"Trigger is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:glue:Trigger")]
    public partial class Trigger : Pulumi.CustomResource
    {
        [Output("actions")]
        public Output<ImmutableArray<Outputs.TriggerAction>> Actions { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("predicate")]
        public Output<Outputs.TriggerPredicate?> Predicate { get; private set; } = null!;

        [Output("schedule")]
        public Output<string?> Schedule { get; private set; } = null!;

        [Output("startOnCreation")]
        public Output<bool?> StartOnCreation { get; private set; } = null!;

        [Output("tags")]
        public Output<object?> Tags { get; private set; } = null!;

        [Output("type")]
        public Output<string> Type { get; private set; } = null!;

        [Output("workflowName")]
        public Output<string?> WorkflowName { get; private set; } = null!;


        /// <summary>
        /// Create a Trigger resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Trigger(string name, TriggerArgs args, CustomResourceOptions? options = null)
            : base("aws-native:glue:Trigger", name, args ?? new TriggerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Trigger(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:glue:Trigger", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Trigger resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Trigger Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Trigger(name, id, options);
        }
    }

    public sealed class TriggerArgs : Pulumi.ResourceArgs
    {
        [Input("actions", required: true)]
        private InputList<Inputs.TriggerActionArgs>? _actions;
        public InputList<Inputs.TriggerActionArgs> Actions
        {
            get => _actions ?? (_actions = new InputList<Inputs.TriggerActionArgs>());
            set => _actions = value;
        }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("predicate")]
        public Input<Inputs.TriggerPredicateArgs>? Predicate { get; set; }

        [Input("schedule")]
        public Input<string>? Schedule { get; set; }

        [Input("startOnCreation")]
        public Input<bool>? StartOnCreation { get; set; }

        [Input("tags")]
        public Input<object>? Tags { get; set; }

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        [Input("workflowName")]
        public Input<string>? WorkflowName { get; set; }

        public TriggerArgs()
        {
        }
    }
}
