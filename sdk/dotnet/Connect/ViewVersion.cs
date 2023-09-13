// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect
{
    /// <summary>
    /// Resource Type definition for AWS::Connect::ViewVersion
    /// </summary>
    [AwsNativeResourceType("aws-native:connect:ViewVersion")]
    public partial class ViewVersion : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The version of the view.
        /// </summary>
        [Output("version")]
        public Output<int> Version { get; private set; } = null!;

        /// <summary>
        /// The description for the view version.
        /// </summary>
        [Output("versionDescription")]
        public Output<string?> VersionDescription { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the view for which a version is being created.
        /// </summary>
        [Output("viewArn")]
        public Output<string> ViewArn { get; private set; } = null!;

        /// <summary>
        /// The view content hash to be checked.
        /// </summary>
        [Output("viewContentSha256")]
        public Output<string?> ViewContentSha256 { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the created view version.
        /// </summary>
        [Output("viewVersionArn")]
        public Output<string> ViewVersionArn { get; private set; } = null!;


        /// <summary>
        /// Create a ViewVersion resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ViewVersion(string name, ViewVersionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:connect:ViewVersion", name, args ?? new ViewVersionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ViewVersion(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:connect:ViewVersion", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "versionDescription",
                    "viewArn",
                    "viewContentSha256",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ViewVersion resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ViewVersion Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ViewVersion(name, id, options);
        }
    }

    public sealed class ViewVersionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description for the view version.
        /// </summary>
        [Input("versionDescription")]
        public Input<string>? VersionDescription { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the view for which a version is being created.
        /// </summary>
        [Input("viewArn", required: true)]
        public Input<string> ViewArn { get; set; } = null!;

        /// <summary>
        /// The view content hash to be checked.
        /// </summary>
        [Input("viewContentSha256")]
        public Input<string>? ViewContentSha256 { get; set; }

        public ViewVersionArgs()
        {
        }
        public static new ViewVersionArgs Empty => new ViewVersionArgs();
    }
}
