// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Greengrass
{
    /// <summary>
    /// Resource Type definition for AWS::Greengrass::FunctionDefinition
    /// </summary>
    [Obsolete(@"FunctionDefinition is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:greengrass:FunctionDefinition")]
    public partial class FunctionDefinition : Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("initialVersion")]
        public Output<Outputs.FunctionDefinitionFunctionDefinitionVersion?> InitialVersion { get; private set; } = null!;

        [Output("latestVersionArn")]
        public Output<string> LatestVersionArn { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("tags")]
        public Output<object?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a FunctionDefinition resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FunctionDefinition(string name, FunctionDefinitionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:greengrass:FunctionDefinition", name, args ?? new FunctionDefinitionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FunctionDefinition(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:greengrass:FunctionDefinition", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing FunctionDefinition resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FunctionDefinition Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new FunctionDefinition(name, id, options);
        }
    }

    public sealed class FunctionDefinitionArgs : Pulumi.ResourceArgs
    {
        [Input("initialVersion")]
        public Input<Inputs.FunctionDefinitionFunctionDefinitionVersionArgs>? InitialVersion { get; set; }

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("tags")]
        public Input<object>? Tags { get; set; }

        public FunctionDefinitionArgs()
        {
        }
    }
}
