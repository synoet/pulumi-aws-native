// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.LakeFormation
{
    /// <summary>
    /// A resource schema representing a Lake Formation Tag.
    /// </summary>
    [AwsNativeResourceType("aws-native:lakeformation:Tag")]
    public partial class Tag : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
        /// </summary>
        [Output("catalogId")]
        public Output<string?> CatalogId { get; private set; } = null!;

        /// <summary>
        /// The key-name for the LF-tag.
        /// </summary>
        [Output("tagKey")]
        public Output<string> TagKey { get; private set; } = null!;

        /// <summary>
        /// A list of possible values an attribute can take.
        /// </summary>
        [Output("tagValues")]
        public Output<ImmutableArray<string>> TagValues { get; private set; } = null!;


        /// <summary>
        /// Create a Tag resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Tag(string name, TagArgs args, CustomResourceOptions? options = null)
            : base("aws-native:lakeformation:Tag", name, args ?? new TagArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Tag(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:lakeformation:Tag", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "catalogId",
                    "tagKey",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Tag resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Tag Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Tag(name, id, options);
        }
    }

    public sealed class TagArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
        /// </summary>
        [Input("catalogId")]
        public Input<string>? CatalogId { get; set; }

        /// <summary>
        /// The key-name for the LF-tag.
        /// </summary>
        [Input("tagKey", required: true)]
        public Input<string> TagKey { get; set; } = null!;

        [Input("tagValues", required: true)]
        private InputList<string>? _tagValues;

        /// <summary>
        /// A list of possible values an attribute can take.
        /// </summary>
        public InputList<string> TagValues
        {
            get => _tagValues ?? (_tagValues = new InputList<string>());
            set => _tagValues = value;
        }

        public TagArgs()
        {
        }
        public static new TagArgs Empty => new TagArgs();
    }
}
