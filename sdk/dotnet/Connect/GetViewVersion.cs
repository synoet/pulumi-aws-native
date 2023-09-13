// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect
{
    public static class GetViewVersion
    {
        /// <summary>
        /// Resource Type definition for AWS::Connect::ViewVersion
        /// </summary>
        public static Task<GetViewVersionResult> InvokeAsync(GetViewVersionArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetViewVersionResult>("aws-native:connect:getViewVersion", args ?? new GetViewVersionArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Connect::ViewVersion
        /// </summary>
        public static Output<GetViewVersionResult> Invoke(GetViewVersionInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetViewVersionResult>("aws-native:connect:getViewVersion", args ?? new GetViewVersionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetViewVersionArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the created view version.
        /// </summary>
        [Input("viewVersionArn", required: true)]
        public string ViewVersionArn { get; set; } = null!;

        public GetViewVersionArgs()
        {
        }
        public static new GetViewVersionArgs Empty => new GetViewVersionArgs();
    }

    public sealed class GetViewVersionInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the created view version.
        /// </summary>
        [Input("viewVersionArn", required: true)]
        public Input<string> ViewVersionArn { get; set; } = null!;

        public GetViewVersionInvokeArgs()
        {
        }
        public static new GetViewVersionInvokeArgs Empty => new GetViewVersionInvokeArgs();
    }


    [OutputType]
    public sealed class GetViewVersionResult
    {
        /// <summary>
        /// The version of the view.
        /// </summary>
        public readonly int? Version;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the created view version.
        /// </summary>
        public readonly string? ViewVersionArn;

        [OutputConstructor]
        private GetViewVersionResult(
            int? version,

            string? viewVersionArn)
        {
            Version = version;
            ViewVersionArn = viewVersionArn;
        }
    }
}
