// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Wisdom
{
    /// <summary>
    /// Definition of AWS::Wisdom::AssistantAssociation Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:wisdom:AssistantAssociation")]
    public partial class AssistantAssociation : global::Pulumi.CustomResource
    {
        [Output("assistantArn")]
        public Output<string> AssistantArn { get; private set; } = null!;

        [Output("assistantAssociationArn")]
        public Output<string> AssistantAssociationArn { get; private set; } = null!;

        [Output("assistantAssociationId")]
        public Output<string> AssistantAssociationId { get; private set; } = null!;

        [Output("assistantId")]
        public Output<string> AssistantId { get; private set; } = null!;

        [Output("association")]
        public Output<Outputs.AssistantAssociationAssociationData> Association { get; private set; } = null!;

        [Output("associationType")]
        public Output<Pulumi.AwsNative.Wisdom.AssistantAssociationAssociationType> AssociationType { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.AssistantAssociationTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a AssistantAssociation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AssistantAssociation(string name, AssistantAssociationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:wisdom:AssistantAssociation", name, args ?? new AssistantAssociationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AssistantAssociation(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:wisdom:AssistantAssociation", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "assistantId",
                    "association",
                    "associationType",
                    "tags[*]",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing AssistantAssociation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AssistantAssociation Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new AssistantAssociation(name, id, options);
        }
    }

    public sealed class AssistantAssociationArgs : global::Pulumi.ResourceArgs
    {
        [Input("assistantId", required: true)]
        public Input<string> AssistantId { get; set; } = null!;

        [Input("association", required: true)]
        public Input<Inputs.AssistantAssociationAssociationDataArgs> Association { get; set; } = null!;

        [Input("associationType", required: true)]
        public Input<Pulumi.AwsNative.Wisdom.AssistantAssociationAssociationType> AssociationType { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.AssistantAssociationTagArgs>? _tags;
        public InputList<Inputs.AssistantAssociationTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.AssistantAssociationTagArgs>());
            set => _tags = value;
        }

        public AssistantAssociationArgs()
        {
        }
        public static new AssistantAssociationArgs Empty => new AssistantAssociationArgs();
    }
}
