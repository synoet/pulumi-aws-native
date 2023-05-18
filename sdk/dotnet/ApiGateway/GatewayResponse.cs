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
    /// Resource Type definition for AWS::ApiGateway::GatewayResponse
    /// </summary>
    [Obsolete(@"GatewayResponse is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:apigateway:GatewayResponse")]
    public partial class GatewayResponse : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The response parameters (paths, query strings, and headers) for the response.
        /// </summary>
        [Output("responseParameters")]
        public Output<object?> ResponseParameters { get; private set; } = null!;

        /// <summary>
        /// The response templates for the response.
        /// </summary>
        [Output("responseTemplates")]
        public Output<object?> ResponseTemplates { get; private set; } = null!;

        /// <summary>
        /// The type of the Gateway Response.
        /// </summary>
        [Output("responseType")]
        public Output<string> ResponseType { get; private set; } = null!;

        /// <summary>
        /// The identifier of the API.
        /// </summary>
        [Output("restApiId")]
        public Output<string> RestApiId { get; private set; } = null!;

        /// <summary>
        /// The HTTP status code for the response.
        /// </summary>
        [Output("statusCode")]
        public Output<string?> StatusCode { get; private set; } = null!;


        /// <summary>
        /// Create a GatewayResponse resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public GatewayResponse(string name, GatewayResponseArgs args, CustomResourceOptions? options = null)
            : base("aws-native:apigateway:GatewayResponse", name, args ?? new GatewayResponseArgs(), MakeResourceOptions(options, ""))
        {
        }

        private GatewayResponse(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:apigateway:GatewayResponse", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing GatewayResponse resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static GatewayResponse Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new GatewayResponse(name, id, options);
        }
    }

    public sealed class GatewayResponseArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The response parameters (paths, query strings, and headers) for the response.
        /// </summary>
        [Input("responseParameters")]
        public Input<object>? ResponseParameters { get; set; }

        /// <summary>
        /// The response templates for the response.
        /// </summary>
        [Input("responseTemplates")]
        public Input<object>? ResponseTemplates { get; set; }

        /// <summary>
        /// The type of the Gateway Response.
        /// </summary>
        [Input("responseType", required: true)]
        public Input<string> ResponseType { get; set; } = null!;

        /// <summary>
        /// The identifier of the API.
        /// </summary>
        [Input("restApiId", required: true)]
        public Input<string> RestApiId { get; set; } = null!;

        /// <summary>
        /// The HTTP status code for the response.
        /// </summary>
        [Input("statusCode")]
        public Input<string>? StatusCode { get; set; }

        public GatewayResponseArgs()
        {
        }
        public static new GatewayResponseArgs Empty => new GatewayResponseArgs();
    }
}
