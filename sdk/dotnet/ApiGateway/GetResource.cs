// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGateway
{
    public static class GetResource
    {
        /// <summary>
        /// The ``AWS::ApiGateway::Resource`` resource creates a resource in an API.
        /// </summary>
        public static Task<GetResourceResult> InvokeAsync(GetResourceArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetResourceResult>("aws-native:apigateway:getResource", args ?? new GetResourceArgs(), options.WithDefaults());

        /// <summary>
        /// The ``AWS::ApiGateway::Resource`` resource creates a resource in an API.
        /// </summary>
        public static Output<GetResourceResult> Invoke(GetResourceInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetResourceResult>("aws-native:apigateway:getResource", args ?? new GetResourceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetResourceArgs : global::Pulumi.InvokeArgs
    {
        [Input("resourceId", required: true)]
        public string ResourceId { get; set; } = null!;

        /// <summary>
        /// The string identifier of the associated RestApi.
        /// </summary>
        [Input("restApiId", required: true)]
        public string RestApiId { get; set; } = null!;

        public GetResourceArgs()
        {
        }
        public static new GetResourceArgs Empty => new GetResourceArgs();
    }

    public sealed class GetResourceInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("resourceId", required: true)]
        public Input<string> ResourceId { get; set; } = null!;

        /// <summary>
        /// The string identifier of the associated RestApi.
        /// </summary>
        [Input("restApiId", required: true)]
        public Input<string> RestApiId { get; set; } = null!;

        public GetResourceInvokeArgs()
        {
        }
        public static new GetResourceInvokeArgs Empty => new GetResourceInvokeArgs();
    }


    [OutputType]
    public sealed class GetResourceResult
    {
        public readonly string? ResourceId;

        [OutputConstructor]
        private GetResourceResult(string? resourceId)
        {
            ResourceId = resourceId;
        }
    }
}
