// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ServiceCatalog
{
    /// <summary>
    /// Resource Type definition for AWS::ServiceCatalog::TagOption
    /// </summary>
    [Obsolete(@"TagOption is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:servicecatalog:TagOption")]
    public partial class TagOption : global::Pulumi.CustomResource
    {
        [Output("active")]
        public Output<bool?> Active { get; private set; } = null!;

        [Output("key")]
        public Output<string> Key { get; private set; } = null!;

        [Output("value")]
        public Output<string> Value { get; private set; } = null!;


        /// <summary>
        /// Create a TagOption resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TagOption(string name, TagOptionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:servicecatalog:TagOption", name, args ?? new TagOptionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TagOption(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:servicecatalog:TagOption", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "key",
                    "value",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing TagOption resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TagOption Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new TagOption(name, id, options);
        }
    }

    public sealed class TagOptionArgs : global::Pulumi.ResourceArgs
    {
        [Input("active")]
        public Input<bool>? Active { get; set; }

        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public TagOptionArgs()
        {
        }
        public static new TagOptionArgs Empty => new TagOptionArgs();
    }
}
