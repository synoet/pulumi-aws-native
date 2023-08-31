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
    /// Resource Type definition for AWS::ApiGateway::Stage
    /// </summary>
    [AwsNativeResourceType("aws-native:apigateway:Stage")]
    public partial class Stage : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Specifies settings for logging access in this stage.
        /// </summary>
        [Output("accessLogSetting")]
        public Output<Outputs.StageAccessLogSetting?> AccessLogSetting { get; private set; } = null!;

        /// <summary>
        /// Indicates whether cache clustering is enabled for the stage.
        /// </summary>
        [Output("cacheClusterEnabled")]
        public Output<bool?> CacheClusterEnabled { get; private set; } = null!;

        /// <summary>
        /// The stage's cache cluster size.
        /// </summary>
        [Output("cacheClusterSize")]
        public Output<string?> CacheClusterSize { get; private set; } = null!;

        /// <summary>
        /// Specifies settings for the canary deployment in this stage.
        /// </summary>
        [Output("canarySetting")]
        public Output<Outputs.StageCanarySetting?> CanarySetting { get; private set; } = null!;

        /// <summary>
        /// The ID of the client certificate that API Gateway uses to call your integration endpoints in the stage. 
        /// </summary>
        [Output("clientCertificateId")]
        public Output<string?> ClientCertificateId { get; private set; } = null!;

        /// <summary>
        /// The ID of the deployment that the stage is associated with. This parameter is required to create a stage. 
        /// </summary>
        [Output("deploymentId")]
        public Output<string?> DeploymentId { get; private set; } = null!;

        /// <summary>
        /// A description of the stage.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The version ID of the API documentation snapshot.
        /// </summary>
        [Output("documentationVersion")]
        public Output<string?> DocumentationVersion { get; private set; } = null!;

        /// <summary>
        /// Settings for all methods in the stage.
        /// </summary>
        [Output("methodSettings")]
        public Output<ImmutableArray<Outputs.StageMethodSetting>> MethodSettings { get; private set; } = null!;

        /// <summary>
        /// The ID of the RestApi resource that you're deploying with this stage.
        /// </summary>
        [Output("restApiId")]
        public Output<string> RestApiId { get; private set; } = null!;

        /// <summary>
        /// The name of the stage, which API Gateway uses as the first path segment in the invoked Uniform Resource Identifier (URI).
        /// </summary>
        [Output("stageName")]
        public Output<string?> StageName { get; private set; } = null!;

        /// <summary>
        /// An array of arbitrary tags (key-value pairs) to associate with the stage.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.StageTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// Specifies whether active X-Ray tracing is enabled for this stage.
        /// </summary>
        [Output("tracingEnabled")]
        public Output<bool?> TracingEnabled { get; private set; } = null!;

        /// <summary>
        /// A map (string-to-string map) that defines the stage variables, where the variable name is the key and the variable value is the value.
        /// </summary>
        [Output("variables")]
        public Output<object?> Variables { get; private set; } = null!;


        /// <summary>
        /// Create a Stage resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Stage(string name, StageArgs args, CustomResourceOptions? options = null)
            : base("aws-native:apigateway:Stage", name, args ?? new StageArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Stage(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:apigateway:Stage", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "restApiId",
                    "stageName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Stage resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Stage Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Stage(name, id, options);
        }
    }

    public sealed class StageArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies settings for logging access in this stage.
        /// </summary>
        [Input("accessLogSetting")]
        public Input<Inputs.StageAccessLogSettingArgs>? AccessLogSetting { get; set; }

        /// <summary>
        /// Indicates whether cache clustering is enabled for the stage.
        /// </summary>
        [Input("cacheClusterEnabled")]
        public Input<bool>? CacheClusterEnabled { get; set; }

        /// <summary>
        /// The stage's cache cluster size.
        /// </summary>
        [Input("cacheClusterSize")]
        public Input<string>? CacheClusterSize { get; set; }

        /// <summary>
        /// Specifies settings for the canary deployment in this stage.
        /// </summary>
        [Input("canarySetting")]
        public Input<Inputs.StageCanarySettingArgs>? CanarySetting { get; set; }

        /// <summary>
        /// The ID of the client certificate that API Gateway uses to call your integration endpoints in the stage. 
        /// </summary>
        [Input("clientCertificateId")]
        public Input<string>? ClientCertificateId { get; set; }

        /// <summary>
        /// The ID of the deployment that the stage is associated with. This parameter is required to create a stage. 
        /// </summary>
        [Input("deploymentId")]
        public Input<string>? DeploymentId { get; set; }

        /// <summary>
        /// A description of the stage.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The version ID of the API documentation snapshot.
        /// </summary>
        [Input("documentationVersion")]
        public Input<string>? DocumentationVersion { get; set; }

        [Input("methodSettings")]
        private InputList<Inputs.StageMethodSettingArgs>? _methodSettings;

        /// <summary>
        /// Settings for all methods in the stage.
        /// </summary>
        public InputList<Inputs.StageMethodSettingArgs> MethodSettings
        {
            get => _methodSettings ?? (_methodSettings = new InputList<Inputs.StageMethodSettingArgs>());
            set => _methodSettings = value;
        }

        /// <summary>
        /// The ID of the RestApi resource that you're deploying with this stage.
        /// </summary>
        [Input("restApiId", required: true)]
        public Input<string> RestApiId { get; set; } = null!;

        /// <summary>
        /// The name of the stage, which API Gateway uses as the first path segment in the invoked Uniform Resource Identifier (URI).
        /// </summary>
        [Input("stageName")]
        public Input<string>? StageName { get; set; }

        [Input("tags")]
        private InputList<Inputs.StageTagArgs>? _tags;

        /// <summary>
        /// An array of arbitrary tags (key-value pairs) to associate with the stage.
        /// </summary>
        public InputList<Inputs.StageTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.StageTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// Specifies whether active X-Ray tracing is enabled for this stage.
        /// </summary>
        [Input("tracingEnabled")]
        public Input<bool>? TracingEnabled { get; set; }

        /// <summary>
        /// A map (string-to-string map) that defines the stage variables, where the variable name is the key and the variable value is the value.
        /// </summary>
        [Input("variables")]
        public Input<object>? Variables { get; set; }

        public StageArgs()
        {
        }
        public static new StageArgs Empty => new StageArgs();
    }
}
