// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Oam
{
    public static class GetSink
    {
        /// <summary>
        /// Resource Type definition for AWS::Oam::Sink
        /// </summary>
        public static Task<GetSinkResult> InvokeAsync(GetSinkArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSinkResult>("aws-native:oam:getSink", args ?? new GetSinkArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Oam::Sink
        /// </summary>
        public static Output<GetSinkResult> Invoke(GetSinkInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSinkResult>("aws-native:oam:getSink", args ?? new GetSinkInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSinkArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon resource name (ARN) of the ObservabilityAccessManager Sink
        /// </summary>
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetSinkArgs()
        {
        }
        public static new GetSinkArgs Empty => new GetSinkArgs();
    }

    public sealed class GetSinkInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon resource name (ARN) of the ObservabilityAccessManager Sink
        /// </summary>
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetSinkInvokeArgs()
        {
        }
        public static new GetSinkInvokeArgs Empty => new GetSinkInvokeArgs();
    }


    [OutputType]
    public sealed class GetSinkResult
    {
        /// <summary>
        /// The Amazon resource name (ARN) of the ObservabilityAccessManager Sink
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// The policy of this ObservabilityAccessManager Sink.
        /// </summary>
        public readonly object? Policy;
        /// <summary>
        /// Tags to apply to the sink
        /// </summary>
        public readonly object? Tags;

        [OutputConstructor]
        private GetSinkResult(
            string? arn,

            object? policy,

            object? tags)
        {
            Arn = arn;
            Policy = policy;
            Tags = tags;
        }
    }
}
