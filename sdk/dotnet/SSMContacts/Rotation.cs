// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SSMContacts
{
    /// <summary>
    /// Resource Type definition for AWS::SSMContacts::Rotation.
    /// </summary>
    [AwsNativeResourceType("aws-native:ssmcontacts:Rotation")]
    public partial class Rotation : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the rotation.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Members of the rotation
        /// </summary>
        [Output("contactIds")]
        public Output<ImmutableArray<string>> ContactIds { get; private set; } = null!;

        /// <summary>
        /// Name of the Rotation
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("recurrence")]
        public Output<Outputs.RotationRecurrenceSettings> Recurrence { get; private set; } = null!;

        /// <summary>
        /// Start time of the first shift of Oncall Schedule
        /// </summary>
        [Output("startTime")]
        public Output<string> StartTime { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.RotationTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// TimeZone Identifier for the Oncall Schedule
        /// </summary>
        [Output("timeZoneId")]
        public Output<string> TimeZoneId { get; private set; } = null!;


        /// <summary>
        /// Create a Rotation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Rotation(string name, RotationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ssmcontacts:Rotation", name, args ?? new RotationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Rotation(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ssmcontacts:Rotation", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Rotation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Rotation Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Rotation(name, id, options);
        }
    }

    public sealed class RotationArgs : global::Pulumi.ResourceArgs
    {
        [Input("contactIds", required: true)]
        private InputList<string>? _contactIds;

        /// <summary>
        /// Members of the rotation
        /// </summary>
        public InputList<string> ContactIds
        {
            get => _contactIds ?? (_contactIds = new InputList<string>());
            set => _contactIds = value;
        }

        /// <summary>
        /// Name of the Rotation
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("recurrence", required: true)]
        public Input<Inputs.RotationRecurrenceSettingsArgs> Recurrence { get; set; } = null!;

        /// <summary>
        /// Start time of the first shift of Oncall Schedule
        /// </summary>
        [Input("startTime", required: true)]
        public Input<string> StartTime { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.RotationTagArgs>? _tags;
        public InputList<Inputs.RotationTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.RotationTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// TimeZone Identifier for the Oncall Schedule
        /// </summary>
        [Input("timeZoneId", required: true)]
        public Input<string> TimeZoneId { get; set; } = null!;

        public RotationArgs()
        {
        }
        public static new RotationArgs Empty => new RotationArgs();
    }
}
