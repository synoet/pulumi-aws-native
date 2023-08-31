// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ivs
{
    /// <summary>
    /// Resource Type definition for AWS::IVS::StreamKey
    /// </summary>
    [AwsNativeResourceType("aws-native:ivs:StreamKey")]
    public partial class StreamKey : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Stream Key ARN is automatically generated on creation and assigned as the unique identifier.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Channel ARN for the stream.
        /// </summary>
        [Output("channelArn")]
        public Output<string> ChannelArn { get; private set; } = null!;

        /// <summary>
        /// A list of key-value pairs that contain metadata for the asset model.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.StreamKeyTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// Stream-key value.
        /// </summary>
        [Output("value")]
        public Output<string> Value { get; private set; } = null!;


        /// <summary>
        /// Create a StreamKey resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public StreamKey(string name, StreamKeyArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ivs:StreamKey", name, args ?? new StreamKeyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private StreamKey(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ivs:StreamKey", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "channelArn",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing StreamKey resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static StreamKey Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new StreamKey(name, id, options);
        }
    }

    public sealed class StreamKeyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Channel ARN for the stream.
        /// </summary>
        [Input("channelArn", required: true)]
        public Input<string> ChannelArn { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.StreamKeyTagArgs>? _tags;

        /// <summary>
        /// A list of key-value pairs that contain metadata for the asset model.
        /// </summary>
        public InputList<Inputs.StreamKeyTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.StreamKeyTagArgs>());
            set => _tags = value;
        }

        public StreamKeyArgs()
        {
        }
        public static new StreamKeyArgs Empty => new StreamKeyArgs();
    }
}
