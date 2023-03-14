// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.VpcLattice
{
    public static class GetAccessLogSubscription
    {
        /// <summary>
        /// Delivers logs from a Mesh or Service to the provided destination
        /// </summary>
        public static Task<GetAccessLogSubscriptionResult> InvokeAsync(GetAccessLogSubscriptionArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetAccessLogSubscriptionResult>("aws-native:vpclattice:getAccessLogSubscription", args ?? new GetAccessLogSubscriptionArgs(), options.WithDefaults());

        /// <summary>
        /// Delivers logs from a Mesh or Service to the provided destination
        /// </summary>
        public static Output<GetAccessLogSubscriptionResult> Invoke(GetAccessLogSubscriptionInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetAccessLogSubscriptionResult>("aws-native:vpclattice:getAccessLogSubscription", args ?? new GetAccessLogSubscriptionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAccessLogSubscriptionArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetAccessLogSubscriptionArgs()
        {
        }
        public static new GetAccessLogSubscriptionArgs Empty => new GetAccessLogSubscriptionArgs();
    }

    public sealed class GetAccessLogSubscriptionInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetAccessLogSubscriptionInvokeArgs()
        {
        }
        public static new GetAccessLogSubscriptionInvokeArgs Empty => new GetAccessLogSubscriptionInvokeArgs();
    }


    [OutputType]
    public sealed class GetAccessLogSubscriptionResult
    {
        public readonly string? Arn;
        public readonly string? DestinationArn;
        public readonly string? Id;
        public readonly string? ResourceArn;
        public readonly string? ResourceId;
        public readonly ImmutableArray<Outputs.AccessLogSubscriptionTag> Tags;

        [OutputConstructor]
        private GetAccessLogSubscriptionResult(
            string? arn,

            string? destinationArn,

            string? id,

            string? resourceArn,

            string? resourceId,

            ImmutableArray<Outputs.AccessLogSubscriptionTag> tags)
        {
            Arn = arn;
            DestinationArn = destinationArn;
            Id = id;
            ResourceArn = resourceArn;
            ResourceId = resourceId;
            Tags = tags;
        }
    }
}
