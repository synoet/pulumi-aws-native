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
    /// AWS::NetworkManager::VpcAttachment Resoruce Type
    /// </summary>
    [AwsNativeResourceType("aws-native:networkmanager:VpcAttachment")]
    public partial class VpcAttachment : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Id of the attachment.
        /// </summary>
        [Output("attachmentId")]
        public Output<string> AttachmentId { get; private set; } = null!;

        /// <summary>
        /// The policy rule number associated with the attachment.
        /// </summary>
        [Output("attachmentPolicyRuleNumber")]
        public Output<int> AttachmentPolicyRuleNumber { get; private set; } = null!;

        /// <summary>
        /// Attachment type.
        /// </summary>
        [Output("attachmentType")]
        public Output<string> AttachmentType { get; private set; } = null!;

        /// <summary>
        /// The ARN of a core network for the VPC attachment.
        /// </summary>
        [Output("coreNetworkArn")]
        public Output<string> CoreNetworkArn { get; private set; } = null!;

        /// <summary>
        /// The ID of a core network for the VPC attachment.
        /// </summary>
        [Output("coreNetworkId")]
        public Output<string> CoreNetworkId { get; private set; } = null!;

        /// <summary>
        /// Creation time of the attachment.
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The Region where the edge is located.
        /// </summary>
        [Output("edgeLocation")]
        public Output<string> EdgeLocation { get; private set; } = null!;

        /// <summary>
        /// Vpc options of the attachment.
        /// </summary>
        [Output("options")]
        public Output<Outputs.VpcAttachmentVpcOptions?> Options { get; private set; } = null!;

        /// <summary>
        /// Owner account of the attachment.
        /// </summary>
        [Output("ownerAccountId")]
        public Output<string> OwnerAccountId { get; private set; } = null!;

        /// <summary>
        /// The attachment to move from one segment to another.
        /// </summary>
        [Output("proposedSegmentChange")]
        public Output<Outputs.VpcAttachmentProposedSegmentChange> ProposedSegmentChange { get; private set; } = null!;

        /// <summary>
        /// The ARN of the Resource.
        /// </summary>
        [Output("resourceArn")]
        public Output<string> ResourceArn { get; private set; } = null!;

        /// <summary>
        /// The name of the segment attachment..
        /// </summary>
        [Output("segmentName")]
        public Output<string> SegmentName { get; private set; } = null!;

        /// <summary>
        /// State of the attachment.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// Subnet Arn list
        /// </summary>
        [Output("subnetArns")]
        public Output<ImmutableArray<string>> SubnetArns { get; private set; } = null!;

        /// <summary>
        /// Tags for the attachment.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.VpcAttachmentTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// Last update time of the attachment.
        /// </summary>
        [Output("updatedAt")]
        public Output<string> UpdatedAt { get; private set; } = null!;

        /// <summary>
        /// The ARN of the VPC.
        /// </summary>
        [Output("vpcArn")]
        public Output<string> VpcArn { get; private set; } = null!;


        /// <summary>
        /// Create a VpcAttachment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VpcAttachment(string name, VpcAttachmentArgs args, CustomResourceOptions? options = null)
            : base("aws-native:networkmanager:VpcAttachment", name, args ?? new VpcAttachmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VpcAttachment(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:networkmanager:VpcAttachment", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing VpcAttachment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VpcAttachment Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new VpcAttachment(name, id, options);
        }
    }

    public sealed class VpcAttachmentArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of a core network for the VPC attachment.
        /// </summary>
        [Input("coreNetworkId", required: true)]
        public Input<string> CoreNetworkId { get; set; } = null!;

        /// <summary>
        /// Vpc options of the attachment.
        /// </summary>
        [Input("options")]
        public Input<Inputs.VpcAttachmentVpcOptionsArgs>? Options { get; set; }

        [Input("subnetArns", required: true)]
        private InputList<string>? _subnetArns;

        /// <summary>
        /// Subnet Arn list
        /// </summary>
        public InputList<string> SubnetArns
        {
            get => _subnetArns ?? (_subnetArns = new InputList<string>());
            set => _subnetArns = value;
        }

        [Input("tags")]
        private InputList<Inputs.VpcAttachmentTagArgs>? _tags;

        /// <summary>
        /// Tags for the attachment.
        /// </summary>
        public InputList<Inputs.VpcAttachmentTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.VpcAttachmentTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The ARN of the VPC.
        /// </summary>
        [Input("vpcArn", required: true)]
        public Input<string> VpcArn { get; set; } = null!;

        public VpcAttachmentArgs()
        {
        }
        public static new VpcAttachmentArgs Empty => new VpcAttachmentArgs();
    }
}
