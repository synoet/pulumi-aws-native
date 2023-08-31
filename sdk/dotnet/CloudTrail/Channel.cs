// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudTrail
{
    /// <summary>
    /// A channel receives events from a specific source (such as an on-premises storage solution or application, or a partner event data source), and delivers the events to one or more event data stores. You use channels to ingest events into CloudTrail from sources outside AWS.
    /// </summary>
    [AwsNativeResourceType("aws-native:cloudtrail:Channel")]
    public partial class Channel : global::Pulumi.CustomResource
    {
        [Output("channelArn")]
        public Output<string> ChannelArn { get; private set; } = null!;

        /// <summary>
        /// One or more resources to which events arriving through a channel are logged and stored.
        /// </summary>
        [Output("destinations")]
        public Output<ImmutableArray<Outputs.ChannelDestination>> Destinations { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// The ARN of an on-premises storage solution or application, or a partner event source.
        /// </summary>
        [Output("source")]
        public Output<string?> Source { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ChannelTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Channel resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Channel(string name, ChannelArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:cloudtrail:Channel", name, args ?? new ChannelArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Channel(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:cloudtrail:Channel", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "source",
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
        [Input("destinations")]
        private InputList<Inputs.ChannelDestinationArgs>? _destinations;

        /// <summary>
        /// One or more resources to which events arriving through a channel are logged and stored.
        /// </summary>
        public InputList<Inputs.ChannelDestinationArgs> Destinations
        {
            get => _destinations ?? (_destinations = new InputList<Inputs.ChannelDestinationArgs>());
            set => _destinations = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ARN of an on-premises storage solution or application, or a partner event source.
        /// </summary>
        [Input("source")]
        public Input<string>? Source { get; set; }

        [Input("tags")]
        private InputList<Inputs.ChannelTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.ChannelTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ChannelTagArgs>());
            set => _tags = value;
        }

        public ChannelArgs()
        {
        }
        public static new ChannelArgs Empty => new ChannelArgs();
    }
}
