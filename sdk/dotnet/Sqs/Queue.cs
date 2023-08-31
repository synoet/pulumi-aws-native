// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Sqs
{
    /// <summary>
    /// Resource Type definition for AWS::SQS::Queue
    /// </summary>
    [AwsNativeResourceType("aws-native:sqs:Queue")]
    public partial class Queue : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the queue.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// For first-in-first-out (FIFO) queues, specifies whether to enable content-based deduplication. During the deduplication interval, Amazon SQS treats messages that are sent with identical content as duplicates and delivers only one copy of the message.
        /// </summary>
        [Output("contentBasedDeduplication")]
        public Output<bool?> ContentBasedDeduplication { get; private set; } = null!;

        /// <summary>
        /// Specifies whether message deduplication occurs at the message group or queue level. Valid values are messageGroup and queue.
        /// </summary>
        [Output("deduplicationScope")]
        public Output<string?> DeduplicationScope { get; private set; } = null!;

        /// <summary>
        /// The time in seconds for which the delivery of all messages in the queue is delayed. You can specify an integer value of 0 to 900 (15 minutes). The default value is 0.
        /// </summary>
        [Output("delaySeconds")]
        public Output<int?> DelaySeconds { get; private set; } = null!;

        /// <summary>
        /// If set to true, creates a FIFO queue. If you don't specify this property, Amazon SQS creates a standard queue.
        /// </summary>
        [Output("fifoQueue")]
        public Output<bool?> FifoQueue { get; private set; } = null!;

        /// <summary>
        /// Specifies whether the FIFO queue throughput quota applies to the entire queue or per message group. Valid values are perQueue and perMessageGroupId. The perMessageGroupId value is allowed only when the value for DeduplicationScope is messageGroup.
        /// </summary>
        [Output("fifoThroughputLimit")]
        public Output<string?> FifoThroughputLimit { get; private set; } = null!;

        /// <summary>
        /// The length of time in seconds for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. The value must be an integer between 60 (1 minute) and 86,400 (24 hours). The default is 300 (5 minutes).
        /// </summary>
        [Output("kmsDataKeyReusePeriodSeconds")]
        public Output<int?> KmsDataKeyReusePeriodSeconds { get; private set; } = null!;

        /// <summary>
        /// The ID of an AWS managed customer master key (CMK) for Amazon SQS or a custom CMK. To use the AWS managed CMK for Amazon SQS, specify the (default) alias alias/aws/sqs.
        /// </summary>
        [Output("kmsMasterKeyId")]
        public Output<string?> KmsMasterKeyId { get; private set; } = null!;

        /// <summary>
        /// The limit of how many bytes that a message can contain before Amazon SQS rejects it. You can specify an integer value from 1,024 bytes (1 KiB) to 262,144 bytes (256 KiB). The default value is 262,144 (256 KiB).
        /// </summary>
        [Output("maximumMessageSize")]
        public Output<int?> MaximumMessageSize { get; private set; } = null!;

        /// <summary>
        /// The number of seconds that Amazon SQS retains a message. You can specify an integer value from 60 seconds (1 minute) to 1,209,600 seconds (14 days). The default value is 345,600 seconds (4 days).
        /// </summary>
        [Output("messageRetentionPeriod")]
        public Output<int?> MessageRetentionPeriod { get; private set; } = null!;

        /// <summary>
        /// A name for the queue. To create a FIFO queue, the name of your FIFO queue must end with the .fifo suffix.
        /// </summary>
        [Output("queueName")]
        public Output<string?> QueueName { get; private set; } = null!;

        /// <summary>
        /// URL of the source queue.
        /// </summary>
        [Output("queueUrl")]
        public Output<string> QueueUrl { get; private set; } = null!;

        /// <summary>
        /// Specifies the duration, in seconds, that the ReceiveMessage action call waits until a message is in the queue in order to include it in the response, rather than returning an empty response if a message isn't yet available. You can specify an integer from 1 to 20. Short polling is used as the default or when you specify 0 for this property.
        /// </summary>
        [Output("receiveMessageWaitTimeSeconds")]
        public Output<int?> ReceiveMessageWaitTimeSeconds { get; private set; } = null!;

        /// <summary>
        /// The string that includes the parameters for the permissions for the dead-letter queue redrive permission and which source queues can specify dead-letter queues as a JSON object.
        /// </summary>
        [Output("redriveAllowPolicy")]
        public Output<object?> RedriveAllowPolicy { get; private set; } = null!;

        /// <summary>
        /// A string that includes the parameters for the dead-letter queue functionality (redrive policy) of the source queue.
        /// </summary>
        [Output("redrivePolicy")]
        public Output<object?> RedrivePolicy { get; private set; } = null!;

        /// <summary>
        /// Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (e.g. SSE-KMS or SSE-SQS ).
        /// </summary>
        [Output("sqsManagedSseEnabled")]
        public Output<bool?> SqsManagedSseEnabled { get; private set; } = null!;

        /// <summary>
        /// The tags that you attach to this queue.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.QueueTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The length of time during which a message will be unavailable after a message is delivered from the queue. This blocks other components from receiving the same message and gives the initial component time to process and delete the message from the queue. Values must be from 0 to 43,200 seconds (12 hours). If you don't specify a value, AWS CloudFormation uses the default value of 30 seconds.
        /// </summary>
        [Output("visibilityTimeout")]
        public Output<int?> VisibilityTimeout { get; private set; } = null!;


        /// <summary>
        /// Create a Queue resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Queue(string name, QueueArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:sqs:Queue", name, args ?? new QueueArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Queue(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:sqs:Queue", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "fifoQueue",
                    "queueName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Queue resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Queue Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Queue(name, id, options);
        }
    }

    public sealed class QueueArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// For first-in-first-out (FIFO) queues, specifies whether to enable content-based deduplication. During the deduplication interval, Amazon SQS treats messages that are sent with identical content as duplicates and delivers only one copy of the message.
        /// </summary>
        [Input("contentBasedDeduplication")]
        public Input<bool>? ContentBasedDeduplication { get; set; }

        /// <summary>
        /// Specifies whether message deduplication occurs at the message group or queue level. Valid values are messageGroup and queue.
        /// </summary>
        [Input("deduplicationScope")]
        public Input<string>? DeduplicationScope { get; set; }

        /// <summary>
        /// The time in seconds for which the delivery of all messages in the queue is delayed. You can specify an integer value of 0 to 900 (15 minutes). The default value is 0.
        /// </summary>
        [Input("delaySeconds")]
        public Input<int>? DelaySeconds { get; set; }

        /// <summary>
        /// If set to true, creates a FIFO queue. If you don't specify this property, Amazon SQS creates a standard queue.
        /// </summary>
        [Input("fifoQueue")]
        public Input<bool>? FifoQueue { get; set; }

        /// <summary>
        /// Specifies whether the FIFO queue throughput quota applies to the entire queue or per message group. Valid values are perQueue and perMessageGroupId. The perMessageGroupId value is allowed only when the value for DeduplicationScope is messageGroup.
        /// </summary>
        [Input("fifoThroughputLimit")]
        public Input<string>? FifoThroughputLimit { get; set; }

        /// <summary>
        /// The length of time in seconds for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. The value must be an integer between 60 (1 minute) and 86,400 (24 hours). The default is 300 (5 minutes).
        /// </summary>
        [Input("kmsDataKeyReusePeriodSeconds")]
        public Input<int>? KmsDataKeyReusePeriodSeconds { get; set; }

        /// <summary>
        /// The ID of an AWS managed customer master key (CMK) for Amazon SQS or a custom CMK. To use the AWS managed CMK for Amazon SQS, specify the (default) alias alias/aws/sqs.
        /// </summary>
        [Input("kmsMasterKeyId")]
        public Input<string>? KmsMasterKeyId { get; set; }

        /// <summary>
        /// The limit of how many bytes that a message can contain before Amazon SQS rejects it. You can specify an integer value from 1,024 bytes (1 KiB) to 262,144 bytes (256 KiB). The default value is 262,144 (256 KiB).
        /// </summary>
        [Input("maximumMessageSize")]
        public Input<int>? MaximumMessageSize { get; set; }

        /// <summary>
        /// The number of seconds that Amazon SQS retains a message. You can specify an integer value from 60 seconds (1 minute) to 1,209,600 seconds (14 days). The default value is 345,600 seconds (4 days).
        /// </summary>
        [Input("messageRetentionPeriod")]
        public Input<int>? MessageRetentionPeriod { get; set; }

        /// <summary>
        /// A name for the queue. To create a FIFO queue, the name of your FIFO queue must end with the .fifo suffix.
        /// </summary>
        [Input("queueName")]
        public Input<string>? QueueName { get; set; }

        /// <summary>
        /// Specifies the duration, in seconds, that the ReceiveMessage action call waits until a message is in the queue in order to include it in the response, rather than returning an empty response if a message isn't yet available. You can specify an integer from 1 to 20. Short polling is used as the default or when you specify 0 for this property.
        /// </summary>
        [Input("receiveMessageWaitTimeSeconds")]
        public Input<int>? ReceiveMessageWaitTimeSeconds { get; set; }

        /// <summary>
        /// The string that includes the parameters for the permissions for the dead-letter queue redrive permission and which source queues can specify dead-letter queues as a JSON object.
        /// </summary>
        [Input("redriveAllowPolicy")]
        public Input<object>? RedriveAllowPolicy { get; set; }

        /// <summary>
        /// A string that includes the parameters for the dead-letter queue functionality (redrive policy) of the source queue.
        /// </summary>
        [Input("redrivePolicy")]
        public Input<object>? RedrivePolicy { get; set; }

        /// <summary>
        /// Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (e.g. SSE-KMS or SSE-SQS ).
        /// </summary>
        [Input("sqsManagedSseEnabled")]
        public Input<bool>? SqsManagedSseEnabled { get; set; }

        [Input("tags")]
        private InputList<Inputs.QueueTagArgs>? _tags;

        /// <summary>
        /// The tags that you attach to this queue.
        /// </summary>
        public InputList<Inputs.QueueTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.QueueTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The length of time during which a message will be unavailable after a message is delivered from the queue. This blocks other components from receiving the same message and gives the initial component time to process and delete the message from the queue. Values must be from 0 to 43,200 seconds (12 hours). If you don't specify a value, AWS CloudFormation uses the default value of 30 seconds.
        /// </summary>
        [Input("visibilityTimeout")]
        public Input<int>? VisibilityTimeout { get; set; }

        public QueueArgs()
        {
        }
        public static new QueueArgs Empty => new QueueArgs();
    }
}
