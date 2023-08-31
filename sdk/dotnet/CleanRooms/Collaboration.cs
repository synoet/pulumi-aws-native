// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CleanRooms
{
    /// <summary>
    /// Represents a collaboration between AWS accounts that allows for secure data collaboration
    /// </summary>
    [AwsNativeResourceType("aws-native:cleanrooms:Collaboration")]
    public partial class Collaboration : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("collaborationIdentifier")]
        public Output<string> CollaborationIdentifier { get; private set; } = null!;

        [Output("creatorDisplayName")]
        public Output<string> CreatorDisplayName { get; private set; } = null!;

        [Output("creatorMemberAbilities")]
        public Output<ImmutableArray<Pulumi.AwsNative.CleanRooms.CollaborationMemberAbility>> CreatorMemberAbilities { get; private set; } = null!;

        [Output("dataEncryptionMetadata")]
        public Output<Outputs.CollaborationDataEncryptionMetadata?> DataEncryptionMetadata { get; private set; } = null!;

        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        [Output("members")]
        public Output<ImmutableArray<Outputs.CollaborationMemberSpecification>> Members { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("queryLogStatus")]
        public Output<Pulumi.AwsNative.CleanRooms.CollaborationQueryLogStatus> QueryLogStatus { get; private set; } = null!;

        /// <summary>
        /// An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.CollaborationTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Collaboration resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Collaboration(string name, CollaborationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:cleanrooms:Collaboration", name, args ?? new CollaborationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Collaboration(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:cleanrooms:Collaboration", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "creatorDisplayName",
                    "creatorMemberAbilities[*]",
                    "dataEncryptionMetadata",
                    "members[*]",
                    "queryLogStatus",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Collaboration resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Collaboration Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Collaboration(name, id, options);
        }
    }

    public sealed class CollaborationArgs : global::Pulumi.ResourceArgs
    {
        [Input("creatorDisplayName", required: true)]
        public Input<string> CreatorDisplayName { get; set; } = null!;

        [Input("creatorMemberAbilities", required: true)]
        private InputList<Pulumi.AwsNative.CleanRooms.CollaborationMemberAbility>? _creatorMemberAbilities;
        public InputList<Pulumi.AwsNative.CleanRooms.CollaborationMemberAbility> CreatorMemberAbilities
        {
            get => _creatorMemberAbilities ?? (_creatorMemberAbilities = new InputList<Pulumi.AwsNative.CleanRooms.CollaborationMemberAbility>());
            set => _creatorMemberAbilities = value;
        }

        [Input("dataEncryptionMetadata")]
        public Input<Inputs.CollaborationDataEncryptionMetadataArgs>? DataEncryptionMetadata { get; set; }

        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        [Input("members", required: true)]
        private InputList<Inputs.CollaborationMemberSpecificationArgs>? _members;
        public InputList<Inputs.CollaborationMemberSpecificationArgs> Members
        {
            get => _members ?? (_members = new InputList<Inputs.CollaborationMemberSpecificationArgs>());
            set => _members = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("queryLogStatus", required: true)]
        public Input<Pulumi.AwsNative.CleanRooms.CollaborationQueryLogStatus> QueryLogStatus { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.CollaborationTagArgs>? _tags;

        /// <summary>
        /// An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
        /// </summary>
        public InputList<Inputs.CollaborationTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.CollaborationTagArgs>());
            set => _tags = value;
        }

        public CollaborationArgs()
        {
        }
        public static new CollaborationArgs Empty => new CollaborationArgs();
    }
}
