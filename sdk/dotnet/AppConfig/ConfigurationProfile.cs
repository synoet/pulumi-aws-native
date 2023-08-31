// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppConfig
{
    /// <summary>
    /// Resource Type definition for AWS::AppConfig::ConfigurationProfile
    /// </summary>
    [Obsolete(@"ConfigurationProfile is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:appconfig:ConfigurationProfile")]
    public partial class ConfigurationProfile : global::Pulumi.CustomResource
    {
        [Output("applicationId")]
        public Output<string> ApplicationId { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("locationUri")]
        public Output<string> LocationUri { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("retrievalRoleArn")]
        public Output<string?> RetrievalRoleArn { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.ConfigurationProfileTags>> Tags { get; private set; } = null!;

        [Output("type")]
        public Output<string?> Type { get; private set; } = null!;

        [Output("validators")]
        public Output<ImmutableArray<Outputs.ConfigurationProfileValidators>> Validators { get; private set; } = null!;


        /// <summary>
        /// Create a ConfigurationProfile resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ConfigurationProfile(string name, ConfigurationProfileArgs args, CustomResourceOptions? options = null)
            : base("aws-native:appconfig:ConfigurationProfile", name, args ?? new ConfigurationProfileArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ConfigurationProfile(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:appconfig:ConfigurationProfile", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "applicationId",
                    "locationUri",
                    "type",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ConfigurationProfile resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ConfigurationProfile Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ConfigurationProfile(name, id, options);
        }
    }

    public sealed class ConfigurationProfileArgs : global::Pulumi.ResourceArgs
    {
        [Input("applicationId", required: true)]
        public Input<string> ApplicationId { get; set; } = null!;

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("locationUri", required: true)]
        public Input<string> LocationUri { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("retrievalRoleArn")]
        public Input<string>? RetrievalRoleArn { get; set; }

        [Input("tags")]
        private InputList<Inputs.ConfigurationProfileTagsArgs>? _tags;
        public InputList<Inputs.ConfigurationProfileTagsArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ConfigurationProfileTagsArgs>());
            set => _tags = value;
        }

        [Input("type")]
        public Input<string>? Type { get; set; }

        [Input("validators")]
        private InputList<Inputs.ConfigurationProfileValidatorsArgs>? _validators;
        public InputList<Inputs.ConfigurationProfileValidatorsArgs> Validators
        {
            get => _validators ?? (_validators = new InputList<Inputs.ConfigurationProfileValidatorsArgs>());
            set => _validators = value;
        }

        public ConfigurationProfileArgs()
        {
        }
        public static new ConfigurationProfileArgs Empty => new ConfigurationProfileArgs();
    }
}
