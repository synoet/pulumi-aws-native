// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFront
{
    /// <summary>
    /// Resource Type definition for AWS::CloudFront::Function
    /// </summary>
    [AwsNativeResourceType("aws-native:cloudfront:Function")]
    public partial class Function : Pulumi.CustomResource
    {
        [Output("autoPublish")]
        public Output<bool?> AutoPublish { get; private set; } = null!;

        [Output("functionARN")]
        public Output<string> FunctionARN { get; private set; } = null!;

        [Output("functionCode")]
        public Output<string?> FunctionCode { get; private set; } = null!;

        [Output("functionConfig")]
        public Output<Outputs.FunctionConfig?> FunctionConfig { get; private set; } = null!;

        [Output("functionMetadata")]
        public Output<Outputs.FunctionMetadata?> FunctionMetadata { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("stage")]
        public Output<string> Stage { get; private set; } = null!;


        /// <summary>
        /// Create a Function resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Function(string name, FunctionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:cloudfront:Function", name, args ?? new FunctionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Function(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:cloudfront:Function", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Function resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Function Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Function(name, id, options);
        }
    }

    public sealed class FunctionArgs : Pulumi.ResourceArgs
    {
        [Input("autoPublish")]
        public Input<bool>? AutoPublish { get; set; }

        [Input("functionCode")]
        public Input<string>? FunctionCode { get; set; }

        [Input("functionConfig")]
        public Input<Inputs.FunctionConfigArgs>? FunctionConfig { get; set; }

        [Input("functionMetadata")]
        public Input<Inputs.FunctionMetadataArgs>? FunctionMetadata { get; set; }

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public FunctionArgs()
        {
        }
    }
}
