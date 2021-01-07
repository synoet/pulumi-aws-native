// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.S3.Outputs
{

    [OutputType]
    public sealed class BucketNotificationConfiguration
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig.html#cfn-s3-bucket-notificationconfig-lambdaconfig
        /// </summary>
        public readonly ImmutableArray<Outputs.BucketLambdaConfiguration> LambdaConfigurations;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig.html#cfn-s3-bucket-notificationconfig-queueconfig
        /// </summary>
        public readonly ImmutableArray<Outputs.BucketQueueConfiguration> QueueConfigurations;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig.html#cfn-s3-bucket-notificationconfig-topicconfig
        /// </summary>
        public readonly ImmutableArray<Outputs.BucketTopicConfiguration> TopicConfigurations;

        [OutputConstructor]
        private BucketNotificationConfiguration(
            ImmutableArray<Outputs.BucketLambdaConfiguration> LambdaConfigurations,

            ImmutableArray<Outputs.BucketQueueConfiguration> QueueConfigurations,

            ImmutableArray<Outputs.BucketTopicConfiguration> TopicConfigurations)
        {
            this.LambdaConfigurations = LambdaConfigurations;
            this.QueueConfigurations = QueueConfigurations;
            this.TopicConfigurations = TopicConfigurations;
        }
    }
}