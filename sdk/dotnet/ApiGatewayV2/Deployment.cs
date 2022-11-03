// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGatewayV2
{
    /// <summary>
    /// Resource Type definition for AWS::ApiGatewayV2::Deployment
    /// </summary>
    [AwsNativeResourceType("aws-native:apigatewayv2:Deployment")]
    public partial class Deployment : global::Pulumi.CustomResource
    {
        [Output("apiId")]
        public Output<string> ApiId { get; private set; } = null!;

        [Output("deploymentId")]
        public Output<string> DeploymentId { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("stageName")]
        public Output<string?> StageName { get; private set; } = null!;


        /// <summary>
        /// Create a Deployment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Deployment(string name, DeploymentArgs args, CustomResourceOptions? options = null)
            : base("aws-native:apigatewayv2:Deployment", name, args ?? new DeploymentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Deployment(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:apigatewayv2:Deployment", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Deployment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Deployment Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Deployment(name, id, options);
        }
    }

    public sealed class DeploymentArgs : global::Pulumi.ResourceArgs
    {
        [Input("apiId", required: true)]
        public Input<string> ApiId { get; set; } = null!;

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("stageName")]
        public Input<string>? StageName { get; set; }

        public DeploymentArgs()
        {
        }
        public static new DeploymentArgs Empty => new DeploymentArgs();
    }
}
