// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaLive
{
    /// <summary>
    /// Resource Type definition for AWS::MediaLive::Channel
    /// </summary>
    [Obsolete(@"Channel is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:medialive:Channel")]
    public partial class Channel : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("cdiInputSpecification")]
        public Output<Outputs.ChannelCdiInputSpecification?> CdiInputSpecification { get; private set; } = null!;

        [Output("channelClass")]
        public Output<string?> ChannelClass { get; private set; } = null!;

        [Output("destinations")]
        public Output<ImmutableArray<Outputs.ChannelOutputDestination>> Destinations { get; private set; } = null!;

        [Output("encoderSettings")]
        public Output<Outputs.ChannelEncoderSettings?> EncoderSettings { get; private set; } = null!;

        [Output("inputAttachments")]
        public Output<ImmutableArray<Outputs.ChannelInputAttachment>> InputAttachments { get; private set; } = null!;

        [Output("inputSpecification")]
        public Output<Outputs.ChannelInputSpecification?> InputSpecification { get; private set; } = null!;

        [Output("inputs")]
        public Output<ImmutableArray<string>> Inputs { get; private set; } = null!;

        [Output("logLevel")]
        public Output<string?> LogLevel { get; private set; } = null!;

        [Output("maintenance")]
        public Output<Outputs.ChannelMaintenanceCreateSettings?> Maintenance { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("roleArn")]
        public Output<string?> RoleArn { get; private set; } = null!;

        [Output("tags")]
        public Output<object?> Tags { get; private set; } = null!;

        [Output("vpc")]
        public Output<Outputs.ChannelVpcOutputSettings?> Vpc { get; private set; } = null!;


        /// <summary>
        /// Create a Channel resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Channel(string name, ChannelArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:medialive:Channel", name, args ?? new ChannelArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Channel(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:medialive:Channel", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "vpc",
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
        [Input("cdiInputSpecification")]
        public Input<Inputs.ChannelCdiInputSpecificationArgs>? CdiInputSpecification { get; set; }

        [Input("channelClass")]
        public Input<string>? ChannelClass { get; set; }

        [Input("destinations")]
        private InputList<Inputs.ChannelOutputDestinationArgs>? _destinations;
        public InputList<Inputs.ChannelOutputDestinationArgs> Destinations
        {
            get => _destinations ?? (_destinations = new InputList<Inputs.ChannelOutputDestinationArgs>());
            set => _destinations = value;
        }

        [Input("encoderSettings")]
        public Input<Inputs.ChannelEncoderSettingsArgs>? EncoderSettings { get; set; }

        [Input("inputAttachments")]
        private InputList<Inputs.ChannelInputAttachmentArgs>? _inputAttachments;
        public InputList<Inputs.ChannelInputAttachmentArgs> InputAttachments
        {
            get => _inputAttachments ?? (_inputAttachments = new InputList<Inputs.ChannelInputAttachmentArgs>());
            set => _inputAttachments = value;
        }

        [Input("inputSpecification")]
        public Input<Inputs.ChannelInputSpecificationArgs>? InputSpecification { get; set; }

        [Input("logLevel")]
        public Input<string>? LogLevel { get; set; }

        [Input("maintenance")]
        public Input<Inputs.ChannelMaintenanceCreateSettingsArgs>? Maintenance { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("roleArn")]
        public Input<string>? RoleArn { get; set; }

        [Input("tags")]
        public Input<object>? Tags { get; set; }

        [Input("vpc")]
        public Input<Inputs.ChannelVpcOutputSettingsArgs>? Vpc { get; set; }

        public ChannelArgs()
        {
        }
        public static new ChannelArgs Empty => new ChannelArgs();
    }
}
