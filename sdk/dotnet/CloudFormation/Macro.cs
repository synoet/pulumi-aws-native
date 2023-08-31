// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFormation
{
    /// <summary>
    /// Resource Type definition for AWS::CloudFormation::Macro
    /// </summary>
    [Obsolete(@"Macro is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:cloudformation:Macro")]
    public partial class Macro : global::Pulumi.CustomResource
    {
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("functionName")]
        public Output<string> FunctionName { get; private set; } = null!;

        [Output("logGroupName")]
        public Output<string?> LogGroupName { get; private set; } = null!;

        [Output("logRoleArn")]
        public Output<string?> LogRoleArn { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a Macro resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Macro(string name, MacroArgs args, CustomResourceOptions? options = null)
            : base("aws-native:cloudformation:Macro", name, args ?? new MacroArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Macro(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:cloudformation:Macro", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "name",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Macro resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Macro Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Macro(name, id, options);
        }
    }

    public sealed class MacroArgs : global::Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("functionName", required: true)]
        public Input<string> FunctionName { get; set; } = null!;

        [Input("logGroupName")]
        public Input<string>? LogGroupName { get; set; }

        [Input("logRoleArn")]
        public Input<string>? LogRoleArn { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        public MacroArgs()
        {
        }
        public static new MacroArgs Empty => new MacroArgs();
    }
}
