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
    /// Resource Type definition for AWS::ApiGateway::Deployment
    /// </summary>
    [AwsNativeResourceType("aws-native:apigateway:Deployment")]
    public partial class Deployment : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Specifies settings for the canary deployment.
        /// </summary>
        [Output("deploymentCanarySettings")]
        public Output<Outputs.DeploymentCanarySettings?> DeploymentCanarySettings { get; private set; } = null!;

        /// <summary>
        /// Primary Id for this resource
        /// </summary>
        [Output("deploymentId")]
        public Output<string> DeploymentId { get; private set; } = null!;

        /// <summary>
        /// A description of the purpose of the API Gateway deployment.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The ID of the RestApi resource to deploy. 
        /// </summary>
        [Output("restApiId")]
        public Output<string> RestApiId { get; private set; } = null!;

        /// <summary>
        /// Configures the stage that API Gateway creates with this deployment.
        /// </summary>
        [Output("stageDescription")]
        public Output<Outputs.DeploymentStageDescription?> StageDescription { get; private set; } = null!;

        /// <summary>
        /// A name for the stage that API Gateway creates with this deployment. Use only alphanumeric characters.
        /// </summary>
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
            : base("aws-native:apigateway:Deployment", name, args ?? new DeploymentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Deployment(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:apigateway:Deployment", name, null, MakeResourceOptions(options, id))
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
        /// <summary>
        /// Specifies settings for the canary deployment.
        /// </summary>
        [Input("deploymentCanarySettings")]
        public Input<Inputs.DeploymentCanarySettingsArgs>? DeploymentCanarySettings { get; set; }

        /// <summary>
        /// A description of the purpose of the API Gateway deployment.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The ID of the RestApi resource to deploy. 
        /// </summary>
        [Input("restApiId", required: true)]
        public Input<string> RestApiId { get; set; } = null!;

        /// <summary>
        /// Configures the stage that API Gateway creates with this deployment.
        /// </summary>
        [Input("stageDescription")]
        public Input<Inputs.DeploymentStageDescriptionArgs>? StageDescription { get; set; }

        /// <summary>
        /// A name for the stage that API Gateway creates with this deployment. Use only alphanumeric characters.
        /// </summary>
        [Input("stageName")]
        public Input<string>? StageName { get; set; }

        public DeploymentArgs()
        {
        }
        public static new DeploymentArgs Empty => new DeploymentArgs();
    }
}
