// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lambda
{
    /// <summary>
    /// Resource Type definition for AWS::Lambda::Version
    /// </summary>
    [Obsolete(@"Version is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:lambda:Version")]
    public partial class Version : global::Pulumi.CustomResource
    {
        [Output("codeSha256")]
        public Output<string?> CodeSha256 { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("functionName")]
        public Output<string> FunctionName { get; private set; } = null!;

        [Output("provisionedConcurrencyConfig")]
        public Output<Outputs.VersionProvisionedConcurrencyConfiguration?> ProvisionedConcurrencyConfig { get; private set; } = null!;

        [Output("version")]
        public Output<string> VersionValue { get; private set; } = null!;


        /// <summary>
        /// Create a Version resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Version(string name, VersionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:lambda:Version", name, args ?? new VersionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Version(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:lambda:Version", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "functionName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Version resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Version Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Version(name, id, options);
        }
    }

    public sealed class VersionArgs : global::Pulumi.ResourceArgs
    {
        [Input("codeSha256")]
        public Input<string>? CodeSha256 { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("functionName", required: true)]
        public Input<string> FunctionName { get; set; } = null!;

        [Input("provisionedConcurrencyConfig")]
        public Input<Inputs.VersionProvisionedConcurrencyConfigurationArgs>? ProvisionedConcurrencyConfig { get; set; }

        public VersionArgs()
        {
        }
        public static new VersionArgs Empty => new VersionArgs();
    }
}
