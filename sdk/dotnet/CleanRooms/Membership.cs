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
    /// Represents an AWS account that is a part of a collaboration
    /// </summary>
    [AwsNativeResourceType("aws-native:cleanrooms:Membership")]
    public partial class Membership : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("collaborationArn")]
        public Output<string> CollaborationArn { get; private set; } = null!;

        [Output("collaborationCreatorAccountId")]
        public Output<string> CollaborationCreatorAccountId { get; private set; } = null!;

        [Output("collaborationIdentifier")]
        public Output<string> CollaborationIdentifier { get; private set; } = null!;

        [Output("membershipIdentifier")]
        public Output<string> MembershipIdentifier { get; private set; } = null!;

        [Output("queryLogStatus")]
        public Output<Pulumi.AwsNative.CleanRooms.MembershipQueryLogStatus> QueryLogStatus { get; private set; } = null!;

        /// <summary>
        /// An arbitrary set of tags (key-value pairs) for this cleanrooms membership.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.MembershipTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Membership resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Membership(string name, MembershipArgs args, CustomResourceOptions? options = null)
            : base("aws-native:cleanrooms:Membership", name, args ?? new MembershipArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Membership(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:cleanrooms:Membership", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "collaborationIdentifier",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Membership resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Membership Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Membership(name, id, options);
        }
    }

    public sealed class MembershipArgs : global::Pulumi.ResourceArgs
    {
        [Input("collaborationIdentifier", required: true)]
        public Input<string> CollaborationIdentifier { get; set; } = null!;

        [Input("queryLogStatus", required: true)]
        public Input<Pulumi.AwsNative.CleanRooms.MembershipQueryLogStatus> QueryLogStatus { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.MembershipTagArgs>? _tags;

        /// <summary>
        /// An arbitrary set of tags (key-value pairs) for this cleanrooms membership.
        /// </summary>
        public InputList<Inputs.MembershipTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.MembershipTagArgs>());
            set => _tags = value;
        }

        public MembershipArgs()
        {
        }
        public static new MembershipArgs Empty => new MembershipArgs();
    }
}
