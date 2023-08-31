// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaTailor
{
    /// <summary>
    /// Definition of AWS::MediaTailor::Channel Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:mediatailor:Channel")]
    public partial class Channel : global::Pulumi.CustomResource
    {
        /// <summary>
        /// &lt;p&gt;The ARN of the channel.&lt;/p&gt;
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("channelName")]
        public Output<string> ChannelName { get; private set; } = null!;

        [Output("fillerSlate")]
        public Output<Outputs.ChannelSlateSource?> FillerSlate { get; private set; } = null!;

        [Output("logConfiguration")]
        public Output<Outputs.ChannelLogConfigurationForChannel?> LogConfiguration { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;The channel's output properties.&lt;/p&gt;
        /// </summary>
        [Output("outputs")]
        public Output<ImmutableArray<Outputs.ChannelRequestOutputItem>> Outputs { get; private set; } = null!;

        [Output("playbackMode")]
        public Output<Pulumi.AwsNative.MediaTailor.ChannelPlaybackMode> PlaybackMode { get; private set; } = null!;

        /// <summary>
        /// The tags to assign to the channel.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ChannelTag>> Tags { get; private set; } = null!;

        [Output("tier")]
        public Output<Pulumi.AwsNative.MediaTailor.ChannelTier?> Tier { get; private set; } = null!;


        /// <summary>
        /// Create a Channel resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Channel(string name, ChannelArgs args, CustomResourceOptions? options = null)
            : base("aws-native:mediatailor:Channel", name, args ?? new ChannelArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Channel(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:mediatailor:Channel", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "channelName",
                    "tier",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Channel resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Channel Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Channel(name, id, options);
        }
    }

    public sealed class ChannelArgs : global::Pulumi.ResourceArgs
    {
        [Input("channelName")]
        public Input<string>? ChannelName { get; set; }

        [Input("fillerSlate")]
        public Input<Inputs.ChannelSlateSourceArgs>? FillerSlate { get; set; }

        [Input("logConfiguration")]
        public Input<Inputs.ChannelLogConfigurationForChannelArgs>? LogConfiguration { get; set; }

        [Input("outputs", required: true)]
        private InputList<Inputs.ChannelRequestOutputItemArgs>? _outputs;

        /// <summary>
        /// &lt;p&gt;The channel's output properties.&lt;/p&gt;
        /// </summary>
        public InputList<Inputs.ChannelRequestOutputItemArgs> Outputs
        {
            get => _outputs ?? (_outputs = new InputList<Inputs.ChannelRequestOutputItemArgs>());
            set => _outputs = value;
        }

        [Input("playbackMode", required: true)]
        public Input<Pulumi.AwsNative.MediaTailor.ChannelPlaybackMode> PlaybackMode { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.ChannelTagArgs>? _tags;

        /// <summary>
        /// The tags to assign to the channel.
        /// </summary>
        public InputList<Inputs.ChannelTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ChannelTagArgs>());
            set => _tags = value;
        }

        [Input("tier")]
        public Input<Pulumi.AwsNative.MediaTailor.ChannelTier>? Tier { get; set; }

        public ChannelArgs()
        {
        }
        public static new ChannelArgs Empty => new ChannelArgs();
    }
}
