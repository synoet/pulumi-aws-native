// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Macie
{
    /// <summary>
    /// Macie CustomDataIdentifier resource schema
    /// </summary>
    [AwsNativeResourceType("aws-native:macie:CustomDataIdentifier")]
    public partial class CustomDataIdentifier : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Custom data identifier ARN.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Description of custom data identifier.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Words to be ignored.
        /// </summary>
        [Output("ignoreWords")]
        public Output<ImmutableArray<string>> IgnoreWords { get; private set; } = null!;

        /// <summary>
        /// Keywords to be matched against.
        /// </summary>
        [Output("keywords")]
        public Output<ImmutableArray<string>> Keywords { get; private set; } = null!;

        /// <summary>
        /// Maximum match distance.
        /// </summary>
        [Output("maximumMatchDistance")]
        public Output<int?> MaximumMatchDistance { get; private set; } = null!;

        /// <summary>
        /// Name of custom data identifier.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Regular expression for custom data identifier.
        /// </summary>
        [Output("regex")]
        public Output<string> Regex { get; private set; } = null!;


        /// <summary>
        /// Create a CustomDataIdentifier resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CustomDataIdentifier(string name, CustomDataIdentifierArgs args, CustomResourceOptions? options = null)
            : base("aws-native:macie:CustomDataIdentifier", name, args ?? new CustomDataIdentifierArgs(), MakeResourceOptions(options, ""))
        {
        }

        private CustomDataIdentifier(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:macie:CustomDataIdentifier", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "description",
                    "ignoreWords[*]",
                    "keywords[*]",
                    "maximumMatchDistance",
                    "name",
                    "regex",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing CustomDataIdentifier resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CustomDataIdentifier Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new CustomDataIdentifier(name, id, options);
        }
    }

    public sealed class CustomDataIdentifierArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Description of custom data identifier.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("ignoreWords")]
        private InputList<string>? _ignoreWords;

        /// <summary>
        /// Words to be ignored.
        /// </summary>
        public InputList<string> IgnoreWords
        {
            get => _ignoreWords ?? (_ignoreWords = new InputList<string>());
            set => _ignoreWords = value;
        }

        [Input("keywords")]
        private InputList<string>? _keywords;

        /// <summary>
        /// Keywords to be matched against.
        /// </summary>
        public InputList<string> Keywords
        {
            get => _keywords ?? (_keywords = new InputList<string>());
            set => _keywords = value;
        }

        /// <summary>
        /// Maximum match distance.
        /// </summary>
        [Input("maximumMatchDistance")]
        public Input<int>? MaximumMatchDistance { get; set; }

        /// <summary>
        /// Name of custom data identifier.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Regular expression for custom data identifier.
        /// </summary>
        [Input("regex", required: true)]
        public Input<string> Regex { get; set; } = null!;

        public CustomDataIdentifierArgs()
        {
        }
        public static new CustomDataIdentifierArgs Empty => new CustomDataIdentifierArgs();
    }
}
