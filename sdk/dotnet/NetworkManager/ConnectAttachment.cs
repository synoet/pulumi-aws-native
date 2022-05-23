// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NetworkManager
{
    /// <summary>
    /// AWS::NetworkManager::ConnectAttachment Resource Type Definition
    /// </summary>
    [Obsolete(@"ConnectAttachment is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:networkmanager:ConnectAttachment")]
    public partial class ConnectAttachment : Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the attachment.
        /// </summary>
        [Output("attachmentId")]
        public Output<string> AttachmentId { get; private set; } = null!;

        /// <summary>
        /// The policy rule number associated with the attachment.
        /// </summary>
        [Output("attachmentPolicyRuleNumber")]
        public Output<int> AttachmentPolicyRuleNumber { get; private set; } = null!;

        /// <summary>
        /// The type of attachment.
        /// </summary>
        [Output("attachmentType")]
        public Output<string> AttachmentType { get; private set; } = null!;

        /// <summary>
        /// The ARN of a core network for the VPC attachment.
        /// </summary>
        [Output("coreNetworkArn")]
        public Output<string> CoreNetworkArn { get; private set; } = null!;

        /// <summary>
        /// ID of the CoreNetwork that the attachment will be attached to.
        /// </summary>
        [Output("coreNetworkId")]
        public Output<string?> CoreNetworkId { get; private set; } = null!;

        /// <summary>
        /// Creation time of the attachment.
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// Edge location of the attachment.
        /// </summary>
        [Output("edgeLocation")]
        public Output<string?> EdgeLocation { get; private set; } = null!;

        /// <summary>
        /// Protocol options for connect attachment
        /// </summary>
        [Output("options")]
        public Output<Outputs.ConnectAttachmentOptions?> Options { get; private set; } = null!;

        /// <summary>
        /// The ID of the attachment account owner.
        /// </summary>
        [Output("ownerAccountId")]
        public Output<string> OwnerAccountId { get; private set; } = null!;

        /// <summary>
        /// The attachment to move from one segment to another.
        /// </summary>
        [Output("proposedSegmentChange")]
        public Output<Outputs.ConnectAttachmentProposedSegmentChange> ProposedSegmentChange { get; private set; } = null!;

        /// <summary>
        /// The attachment resource ARN.
        /// </summary>
        [Output("resourceArn")]
        public Output<string> ResourceArn { get; private set; } = null!;

        /// <summary>
        /// The name of the segment attachment.
        /// </summary>
        [Output("segmentName")]
        public Output<string> SegmentName { get; private set; } = null!;

        /// <summary>
        /// State of the attachment.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// Tags for the attachment.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ConnectAttachmentTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// Id of transport attachment
        /// </summary>
        [Output("transportAttachmentId")]
        public Output<string?> TransportAttachmentId { get; private set; } = null!;

        /// <summary>
        /// Last update time of the attachment.
        /// </summary>
        [Output("updatedAt")]
        public Output<string> UpdatedAt { get; private set; } = null!;


        /// <summary>
        /// Create a ConnectAttachment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ConnectAttachment(string name, ConnectAttachmentArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:networkmanager:ConnectAttachment", name, args ?? new ConnectAttachmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ConnectAttachment(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:networkmanager:ConnectAttachment", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ConnectAttachment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ConnectAttachment Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ConnectAttachment(name, id, options);
        }
    }

    public sealed class ConnectAttachmentArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the CoreNetwork that the attachment will be attached to.
        /// </summary>
        [Input("coreNetworkId")]
        public Input<string>? CoreNetworkId { get; set; }

        /// <summary>
        /// Edge location of the attachment.
        /// </summary>
        [Input("edgeLocation")]
        public Input<string>? EdgeLocation { get; set; }

        /// <summary>
        /// Protocol options for connect attachment
        /// </summary>
        [Input("options")]
        public Input<Inputs.ConnectAttachmentOptionsArgs>? Options { get; set; }

        [Input("tags")]
        private InputList<Inputs.ConnectAttachmentTagArgs>? _tags;

        /// <summary>
        /// Tags for the attachment.
        /// </summary>
        public InputList<Inputs.ConnectAttachmentTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ConnectAttachmentTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// Id of transport attachment
        /// </summary>
        [Input("transportAttachmentId")]
        public Input<string>? TransportAttachmentId { get; set; }

        public ConnectAttachmentArgs()
        {
        }
    }
}
