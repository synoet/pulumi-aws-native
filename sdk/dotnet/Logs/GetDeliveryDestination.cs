// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Logs
{
    public static class GetDeliveryDestination
    {
        /// <summary>
        /// This structure contains information about one delivery destination in your account.
        /// 
        /// A delivery destination is an AWS resource that represents an AWS service that logs can be sent to CloudWatch Logs, Amazon S3, are supported as Kinesis Data Firehose delivery destinations.
        /// </summary>
        public static Task<GetDeliveryDestinationResult> InvokeAsync(GetDeliveryDestinationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDeliveryDestinationResult>("aws-native:logs:getDeliveryDestination", args ?? new GetDeliveryDestinationArgs(), options.WithDefaults());

        /// <summary>
        /// This structure contains information about one delivery destination in your account.
        /// 
        /// A delivery destination is an AWS resource that represents an AWS service that logs can be sent to CloudWatch Logs, Amazon S3, are supported as Kinesis Data Firehose delivery destinations.
        /// </summary>
        public static Output<GetDeliveryDestinationResult> Invoke(GetDeliveryDestinationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDeliveryDestinationResult>("aws-native:logs:getDeliveryDestination", args ?? new GetDeliveryDestinationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDeliveryDestinationArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of this delivery destination.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetDeliveryDestinationArgs()
        {
        }
        public static new GetDeliveryDestinationArgs Empty => new GetDeliveryDestinationArgs();
    }

    public sealed class GetDeliveryDestinationInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of this delivery destination.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetDeliveryDestinationInvokeArgs()
        {
        }
        public static new GetDeliveryDestinationInvokeArgs Empty => new GetDeliveryDestinationInvokeArgs();
    }


    [OutputType]
    public sealed class GetDeliveryDestinationResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) that uniquely identifies this delivery destination.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account.
        /// 
        /// The policy must be in JSON string format.
        /// 
        /// Length Constraints: Maximum length of 51200
        /// </summary>
        public readonly object? DeliveryDestinationPolicy;
        /// <summary>
        /// Displays whether this delivery destination is CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.
        /// </summary>
        public readonly string? DeliveryDestinationType;
        /// <summary>
        /// The tags that have been assigned to this delivery destination.
        /// </summary>
        public readonly ImmutableArray<Outputs.DeliveryDestinationTag> Tags;

        [OutputConstructor]
        private GetDeliveryDestinationResult(
            string? arn,

            object? deliveryDestinationPolicy,

            string? deliveryDestinationType,

            ImmutableArray<Outputs.DeliveryDestinationTag> tags)
        {
            Arn = arn;
            DeliveryDestinationPolicy = deliveryDestinationPolicy;
            DeliveryDestinationType = deliveryDestinationType;
            Tags = tags;
        }
    }
}
