// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IvsChat
{
    /// <summary>
    /// Resource type definition for AWS::IVSChat::LoggingConfiguration.
    /// </summary>
    [AwsNativeResourceType("aws-native:ivschat:LoggingConfiguration")]
    public partial class LoggingConfiguration : global::Pulumi.CustomResource
    {
        /// <summary>
        /// LoggingConfiguration ARN is automatically generated on creation and assigned as the unique identifier.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("destinationConfiguration")]
        public Output<Outputs.LoggingConfigurationDestinationConfiguration> DestinationConfiguration { get; private set; } = null!;

        /// <summary>
        /// The name of the logging configuration. The value does not need to be unique.
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// The state of the logging configuration. When the state is ACTIVE, the configuration is ready to log chat content.
        /// </summary>
        [Output("state")]
        public Output<Pulumi.AwsNative.IvsChat.LoggingConfigurationState> State { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.LoggingConfigurationTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a LoggingConfiguration resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LoggingConfiguration(string name, LoggingConfigurationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ivschat:LoggingConfiguration", name, args ?? new LoggingConfigurationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LoggingConfiguration(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ivschat:LoggingConfiguration", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing LoggingConfiguration resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LoggingConfiguration Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new LoggingConfiguration(name, id, options);
        }
    }

    public sealed class LoggingConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("destinationConfiguration", required: true)]
        public Input<Inputs.LoggingConfigurationDestinationConfigurationArgs> DestinationConfiguration { get; set; } = null!;

        /// <summary>
        /// The name of the logging configuration. The value does not need to be unique.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputList<Inputs.LoggingConfigurationTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.LoggingConfigurationTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.LoggingConfigurationTagArgs>());
            set => _tags = value;
        }

        public LoggingConfigurationArgs()
        {
        }
        public static new LoggingConfigurationArgs Empty => new LoggingConfigurationArgs();
    }
}
