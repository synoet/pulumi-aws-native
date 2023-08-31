// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AmplifyUiBuilder
{
    /// <summary>
    /// Definition of AWS::AmplifyUIBuilder::Theme Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:amplifyuibuilder:Theme")]
    public partial class Theme : global::Pulumi.CustomResource
    {
        [Output("appId")]
        public Output<string?> AppId { get; private set; } = null!;

        [Output("environmentName")]
        public Output<string?> EnvironmentName { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("overrides")]
        public Output<ImmutableArray<Outputs.ThemeValues>> Overrides { get; private set; } = null!;

        [Output("tags")]
        public Output<Outputs.ThemeTags?> Tags { get; private set; } = null!;

        [Output("values")]
        public Output<ImmutableArray<Outputs.ThemeValues>> Values { get; private set; } = null!;


        /// <summary>
        /// Create a Theme resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Theme(string name, ThemeArgs args, CustomResourceOptions? options = null)
            : base("aws-native:amplifyuibuilder:Theme", name, args ?? new ThemeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Theme(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:amplifyuibuilder:Theme", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "tags",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Theme resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Theme Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Theme(name, id, options);
        }
    }

    public sealed class ThemeArgs : global::Pulumi.ResourceArgs
    {
        [Input("appId")]
        public Input<string>? AppId { get; set; }

        [Input("environmentName")]
        public Input<string>? EnvironmentName { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("overrides")]
        private InputList<Inputs.ThemeValuesArgs>? _overrides;
        public InputList<Inputs.ThemeValuesArgs> Overrides
        {
            get => _overrides ?? (_overrides = new InputList<Inputs.ThemeValuesArgs>());
            set => _overrides = value;
        }

        [Input("tags")]
        public Input<Inputs.ThemeTagsArgs>? Tags { get; set; }

        [Input("values", required: true)]
        private InputList<Inputs.ThemeValuesArgs>? _values;
        public InputList<Inputs.ThemeValuesArgs> Values
        {
            get => _values ?? (_values = new InputList<Inputs.ThemeValuesArgs>());
            set => _values = value;
        }

        public ThemeArgs()
        {
        }
        public static new ThemeArgs Empty => new ThemeArgs();
    }
}
