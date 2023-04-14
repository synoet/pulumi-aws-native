// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.M2
{
    public static class GetApplication
    {
        /// <summary>
        /// Represents an application that runs on an AWS Mainframe Modernization Environment
        /// </summary>
        public static Task<GetApplicationResult> InvokeAsync(GetApplicationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetApplicationResult>("aws-native:m2:getApplication", args ?? new GetApplicationArgs(), options.WithDefaults());

        /// <summary>
        /// Represents an application that runs on an AWS Mainframe Modernization Environment
        /// </summary>
        public static Output<GetApplicationResult> Invoke(GetApplicationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetApplicationResult>("aws-native:m2:getApplication", args ?? new GetApplicationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetApplicationArgs : global::Pulumi.InvokeArgs
    {
        [Input("applicationArn", required: true)]
        public string ApplicationArn { get; set; } = null!;

        public GetApplicationArgs()
        {
        }
        public static new GetApplicationArgs Empty => new GetApplicationArgs();
    }

    public sealed class GetApplicationInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("applicationArn", required: true)]
        public Input<string> ApplicationArn { get; set; } = null!;

        public GetApplicationInvokeArgs()
        {
        }
        public static new GetApplicationInvokeArgs Empty => new GetApplicationInvokeArgs();
    }


    [OutputType]
    public sealed class GetApplicationResult
    {
        public readonly string? ApplicationArn;
        public readonly string? ApplicationId;
        public readonly string? Description;
        public readonly Outputs.ApplicationTagMap? Tags;

        [OutputConstructor]
        private GetApplicationResult(
            string? applicationArn,

            string? applicationId,

            string? description,

            Outputs.ApplicationTagMap? tags)
        {
            ApplicationArn = applicationArn;
            ApplicationId = applicationId;
            Description = description;
            Tags = tags;
        }
    }
}
