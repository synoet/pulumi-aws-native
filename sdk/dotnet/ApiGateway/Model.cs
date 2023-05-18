// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGateway
{
    /// <summary>
    /// Resource Type definition for AWS::ApiGateway::Model
    /// </summary>
    [AwsNativeResourceType("aws-native:apigateway:Model")]
    public partial class Model : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The content type for the model.
        /// </summary>
        [Output("contentType")]
        public Output<string?> ContentType { get; private set; } = null!;

        /// <summary>
        /// A description that identifies this model.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// A name for the model. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the model name.
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of a REST API with which to associate this model.
        /// </summary>
        [Output("restApiId")]
        public Output<string> RestApiId { get; private set; } = null!;

        /// <summary>
        /// The schema to use to transform data to one or more output formats. Specify null ({}) if you don't want to specify a schema.
        /// </summary>
        [Output("schema")]
        public Output<object?> Schema { get; private set; } = null!;


        /// <summary>
        /// Create a Model resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Model(string name, ModelArgs args, CustomResourceOptions? options = null)
            : base("aws-native:apigateway:Model", name, args ?? new ModelArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Model(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:apigateway:Model", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Model resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Model Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Model(name, id, options);
        }
    }

    public sealed class ModelArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The content type for the model.
        /// </summary>
        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        /// <summary>
        /// A description that identifies this model.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// A name for the model. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the model name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of a REST API with which to associate this model.
        /// </summary>
        [Input("restApiId", required: true)]
        public Input<string> RestApiId { get; set; } = null!;

        /// <summary>
        /// The schema to use to transform data to one or more output formats. Specify null ({}) if you don't want to specify a schema.
        /// </summary>
        [Input("schema")]
        public Input<object>? Schema { get; set; }

        public ModelArgs()
        {
        }
        public static new ModelArgs Empty => new ModelArgs();
    }
}
