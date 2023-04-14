// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SecurityHub
{
    public static class GetHub
    {
        /// <summary>
        /// Resource Type definition for AWS::SecurityHub::Hub
        /// </summary>
        public static Task<GetHubResult> InvokeAsync(GetHubArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetHubResult>("aws-native:securityhub:getHub", args ?? new GetHubArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::SecurityHub::Hub
        /// </summary>
        public static Output<GetHubResult> Invoke(GetHubInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetHubResult>("aws-native:securityhub:getHub", args ?? new GetHubInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetHubArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetHubArgs()
        {
        }
        public static new GetHubArgs Empty => new GetHubArgs();
    }

    public sealed class GetHubInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetHubInvokeArgs()
        {
        }
        public static new GetHubInvokeArgs Empty => new GetHubInvokeArgs();
    }


    [OutputType]
    public sealed class GetHubResult
    {
        public readonly string? Id;
        public readonly object? Tags;

        [OutputConstructor]
        private GetHubResult(
            string? id,

            object? tags)
        {
            Id = id;
            Tags = tags;
        }
    }
}
