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
    /// Resource Type definition for AWS::ApiGatewayV2::Stage
    /// </summary>
    [Obsolete(@"Stage is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:apigatewayv2:Stage")]
    public partial class Stage : global::Pulumi.CustomResource
    {
        [Output("accessLogSettings")]
        public Output<Outputs.StageAccessLogSettings?> AccessLogSettings { get; private set; } = null!;

        [Output("accessPolicyId")]
        public Output<string?> AccessPolicyId { get; private set; } = null!;

        [Output("apiId")]
        public Output<string> ApiId { get; private set; } = null!;

        [Output("autoDeploy")]
        public Output<bool?> AutoDeploy { get; private set; } = null!;

        [Output("clientCertificateId")]
        public Output<string?> ClientCertificateId { get; private set; } = null!;

        [Output("defaultRouteSettings")]
        public Output<Outputs.StageRouteSettings?> DefaultRouteSettings { get; private set; } = null!;

        [Output("deploymentId")]
        public Output<string?> DeploymentId { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("routeSettings")]
        public Output<object?> RouteSettings { get; private set; } = null!;

        [Output("stageName")]
        public Output<string> StageName { get; private set; } = null!;

        [Output("stageVariables")]
        public Output<object?> StageVariables { get; private set; } = null!;

        [Output("tags")]
        public Output<object?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Stage resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Stage(string name, StageArgs args, CustomResourceOptions? options = null)
            : base("aws-native:apigatewayv2:Stage", name, args ?? new StageArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Stage(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:apigatewayv2:Stage", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "apiId",
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
        [Input("accessLogSettings")]
        public Input<Inputs.StageAccessLogSettingsArgs>? AccessLogSettings { get; set; }

        [Input("accessPolicyId")]
        public Input<string>? AccessPolicyId { get; set; }

        [Input("apiId", required: true)]
        public Input<string> ApiId { get; set; } = null!;

        [Input("autoDeploy")]
        public Input<bool>? AutoDeploy { get; set; }

        [Input("clientCertificateId")]
        public Input<string>? ClientCertificateId { get; set; }

        [Input("defaultRouteSettings")]
        public Input<Inputs.StageRouteSettingsArgs>? DefaultRouteSettings { get; set; }

        [Input("deploymentId")]
        public Input<string>? DeploymentId { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("routeSettings")]
        public Input<object>? RouteSettings { get; set; }

        [Input("stageName")]
        public Input<string>? StageName { get; set; }

        [Input("stageVariables")]
        public Input<object>? StageVariables { get; set; }

        [Input("tags")]
        public Input<object>? Tags { get; set; }

        public StageArgs()
        {
        }
        public static new StageArgs Empty => new StageArgs();
    }
}
