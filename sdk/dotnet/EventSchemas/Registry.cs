// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EventSchemas
{
    /// <summary>
    /// Resource Type definition for AWS::EventSchemas::Registry
    /// </summary>
    [Obsolete(@"Registry is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:eventschemas:Registry")]
    public partial class Registry : global::Pulumi.CustomResource
    {
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("registryArn")]
        public Output<string> RegistryArn { get; private set; } = null!;

        [Output("registryName")]
        public Output<string?> RegistryName { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.RegistryTagsEntry>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Registry resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Registry(string name, RegistryArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:eventschemas:Registry", name, args ?? new RegistryArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Registry(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:eventschemas:Registry", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Registry resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Registry Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Registry(name, id, options);
        }
    }

    public sealed class RegistryArgs : global::Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("registryName")]
        public Input<string>? RegistryName { get; set; }

        [Input("tags")]
        private InputList<Inputs.RegistryTagsEntryArgs>? _tags;
        public InputList<Inputs.RegistryTagsEntryArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.RegistryTagsEntryArgs>());
            set => _tags = value;
        }

        public RegistryArgs()
        {
        }
        public static new RegistryArgs Empty => new RegistryArgs();
    }
}
