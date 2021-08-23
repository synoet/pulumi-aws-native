// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SES
{
    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html
    /// </summary>
    [AwsNativeResourceType("aws-native:ses:ContactList")]
    public partial class ContactList : Pulumi.CustomResource
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-contactlistname
        /// </summary>
        [Output("contactListName")]
        public Output<string?> ContactListName { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-description
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-tags
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-topics
        /// </summary>
        [Output("topics")]
        public Output<ImmutableArray<Outputs.ContactListTopic>> Topics { get; private set; } = null!;


        /// <summary>
        /// Create a ContactList resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ContactList(string name, ContactListArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:ses:ContactList", name, args ?? new ContactListArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ContactList(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ses:ContactList", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ContactList resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ContactList Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ContactList(name, id, options);
        }
    }

    public sealed class ContactListArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-contactlistname
        /// </summary>
        [Input("contactListName")]
        public Input<string>? ContactListName { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-description
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-tags
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        [Input("topics")]
        private InputList<Inputs.ContactListTopicArgs>? _topics;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-topics
        /// </summary>
        public InputList<Inputs.ContactListTopicArgs> Topics
        {
            get => _topics ?? (_topics = new InputList<Inputs.ContactListTopicArgs>());
            set => _topics = value;
        }

        public ContactListArgs()
        {
        }
    }
}
