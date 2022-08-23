// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SNS
{
    public static class GetTopic
    {
        /// <summary>
        /// Resource Type definition for AWS::SNS::Topic
        /// </summary>
        public static Task<GetTopicResult> InvokeAsync(GetTopicArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetTopicResult>("aws-native:sns:getTopic", args ?? new GetTopicArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::SNS::Topic
        /// </summary>
        public static Output<GetTopicResult> Invoke(GetTopicInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetTopicResult>("aws-native:sns:getTopic", args ?? new GetTopicInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetTopicArgs : global::Pulumi.InvokeArgs
    {
        [Input("topicArn", required: true)]
        public string TopicArn { get; set; } = null!;

        public GetTopicArgs()
        {
        }
        public static new GetTopicArgs Empty => new GetTopicArgs();
    }

    public sealed class GetTopicInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("topicArn", required: true)]
        public Input<string> TopicArn { get; set; } = null!;

        public GetTopicInvokeArgs()
        {
        }
        public static new GetTopicInvokeArgs Empty => new GetTopicInvokeArgs();
    }


    [OutputType]
    public sealed class GetTopicResult
    {
        /// <summary>
        /// Enables content-based deduplication for FIFO topics. By default, ContentBasedDeduplication is set to false. If you create a FIFO topic and this attribute is false, you must specify a value for the MessageDeduplicationId parameter for the Publish action.
        /// 
        /// When you set ContentBasedDeduplication to true, Amazon SNS uses a SHA-256 hash to generate the MessageDeduplicationId using the body of the message (but not the attributes of the message).
        /// 
        /// (Optional) To override the generated value, you can specify a value for the the MessageDeduplicationId parameter for the Publish action.
        /// </summary>
        public readonly bool? ContentBasedDeduplication;
        /// <summary>
        /// The display name to use for an Amazon SNS topic with SMS subscriptions.
        /// </summary>
        public readonly string? DisplayName;
        /// <summary>
        /// The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see Key Terms. For more examples, see KeyId in the AWS Key Management Service API Reference.
        /// 
        /// This property applies only to [server-side-encryption](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html).
        /// </summary>
        public readonly string? KmsMasterKeyId;
        /// <summary>
        /// The SNS subscriptions (endpoints) for this topic.
        /// </summary>
        public readonly ImmutableArray<Outputs.TopicSubscription> Subscription;
        public readonly ImmutableArray<Outputs.TopicTag> Tags;
        public readonly string? TopicArn;

        [OutputConstructor]
        private GetTopicResult(
            bool? contentBasedDeduplication,

            string? displayName,

            string? kmsMasterKeyId,

            ImmutableArray<Outputs.TopicSubscription> subscription,

            ImmutableArray<Outputs.TopicTag> tags,

            string? topicArn)
        {
            ContentBasedDeduplication = contentBasedDeduplication;
            DisplayName = displayName;
            KmsMasterKeyId = kmsMasterKeyId;
            Subscription = subscription;
            Tags = tags;
            TopicArn = topicArn;
        }
    }
}
