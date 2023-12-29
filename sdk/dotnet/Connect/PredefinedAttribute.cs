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
    /// Resource Type definition for AWS::Connect::PredefinedAttribute
    /// </summary>
    [AwsNativeResourceType("aws-native:connect:PredefinedAttribute")]
    public partial class PredefinedAttribute : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The identifier of the Amazon Connect instance.
        /// </summary>
        [Output("instanceArn")]
        public Output<string> InstanceArn { get; private set; } = null!;

        /// <summary>
        /// The name of the predefined attribute.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The values of a predefined attribute.
        /// </summary>
        [Output("values")]
        public Output<Outputs.ValuesProperties> Values { get; private set; } = null!;


        /// <summary>
        /// Create a PredefinedAttribute resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PredefinedAttribute(string name, PredefinedAttributeArgs args, CustomResourceOptions? options = null)
            : base("aws-native:connect:PredefinedAttribute", name, args ?? new PredefinedAttributeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private PredefinedAttribute(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:connect:PredefinedAttribute", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "instanceArn",
                    "name",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing PredefinedAttribute resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PredefinedAttribute Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new PredefinedAttribute(name, id, options);
        }
    }

    public sealed class PredefinedAttributeArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The identifier of the Amazon Connect instance.
        /// </summary>
        [Input("instanceArn", required: true)]
        public Input<string> InstanceArn { get; set; } = null!;

        /// <summary>
        /// The name of the predefined attribute.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The values of a predefined attribute.
        /// </summary>
        [Input("values", required: true)]
        public Input<Inputs.ValuesPropertiesArgs> Values { get; set; } = null!;

        public PredefinedAttributeArgs()
        {
        }
        public static new PredefinedAttributeArgs Empty => new PredefinedAttributeArgs();
    }
}
