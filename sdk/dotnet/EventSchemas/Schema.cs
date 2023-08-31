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
    /// Resource Type definition for AWS::EventSchemas::Schema
    /// </summary>
    [Obsolete(@"Schema is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:eventschemas:Schema")]
    public partial class Schema : global::Pulumi.CustomResource
    {
        [Output("content")]
        public Output<string> Content { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("registryName")]
        public Output<string> RegistryName { get; private set; } = null!;

        [Output("schemaArn")]
        public Output<string> SchemaArn { get; private set; } = null!;

        [Output("schemaName")]
        public Output<string?> SchemaName { get; private set; } = null!;

        [Output("schemaVersion")]
        public Output<string> SchemaVersion { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.SchemaTagsEntry>> Tags { get; private set; } = null!;

        [Output("type")]
        public Output<string> Type { get; private set; } = null!;


        /// <summary>
        /// Create a Schema resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Schema(string name, SchemaArgs args, CustomResourceOptions? options = null)
            : base("aws-native:eventschemas:Schema", name, args ?? new SchemaArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Schema(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:eventschemas:Schema", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "registryName",
                    "schemaName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Schema resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Schema Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Schema(name, id, options);
        }
    }

    public sealed class SchemaArgs : global::Pulumi.ResourceArgs
    {
        [Input("content", required: true)]
        public Input<string> Content { get; set; } = null!;

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("registryName", required: true)]
        public Input<string> RegistryName { get; set; } = null!;

        [Input("schemaName")]
        public Input<string>? SchemaName { get; set; }

        [Input("tags")]
        private InputList<Inputs.SchemaTagsEntryArgs>? _tags;
        public InputList<Inputs.SchemaTagsEntryArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.SchemaTagsEntryArgs>());
            set => _tags = value;
        }

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public SchemaArgs()
        {
        }
        public static new SchemaArgs Empty => new SchemaArgs();
    }
}
