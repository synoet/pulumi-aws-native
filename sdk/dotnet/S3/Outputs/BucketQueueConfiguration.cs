// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3.Outputs
{

    /// <summary>
    /// The Amazon Simple Queue Service queues to publish messages to and the events for which to publish messages.
    /// </summary>
    [OutputType]
    public sealed class BucketQueueConfiguration
    {
        /// <summary>
        /// The Amazon S3 bucket event about which you want to publish messages to Amazon SQS.
        /// </summary>
        public readonly string Event;
        /// <summary>
        /// The filtering rules that determine which objects trigger notifications.
        /// </summary>
        public readonly Outputs.BucketNotificationFilter? Filter;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a message when it detects events of the specified type.
        /// </summary>
        public readonly string Queue;

        [OutputConstructor]
        private BucketQueueConfiguration(
            string @event,

            Outputs.BucketNotificationFilter? filter,

            string queue)
        {
            Event = @event;
            Filter = filter;
            Queue = queue;
        }
    }
}
