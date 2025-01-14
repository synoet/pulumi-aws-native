// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Sns.Outputs
{

    [OutputType]
    public sealed class TopicLoggingConfig
    {
        /// <summary>
        /// The IAM role ARN to be used when logging failed message deliveries in Amazon CloudWatch
        /// </summary>
        public readonly string? FailureFeedbackRoleArn;
        /// <summary>
        /// Indicates one of the supported protocols for the SNS topic
        /// </summary>
        public readonly Pulumi.AwsNative.Sns.TopicLoggingConfigProtocol Protocol;
        /// <summary>
        /// The IAM role ARN to be used when logging successful message deliveries in Amazon CloudWatch
        /// </summary>
        public readonly string? SuccessFeedbackRoleArn;
        /// <summary>
        /// The percentage of successful message deliveries to be logged in Amazon CloudWatch. Valid percentage values range from 0 to 100
        /// </summary>
        public readonly string? SuccessFeedbackSampleRate;

        [OutputConstructor]
        private TopicLoggingConfig(
            string? failureFeedbackRoleArn,

            Pulumi.AwsNative.Sns.TopicLoggingConfigProtocol protocol,

            string? successFeedbackRoleArn,

            string? successFeedbackSampleRate)
        {
            FailureFeedbackRoleArn = failureFeedbackRoleArn;
            Protocol = protocol;
            SuccessFeedbackRoleArn = successFeedbackRoleArn;
            SuccessFeedbackSampleRate = successFeedbackSampleRate;
        }
    }
}
