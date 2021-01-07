// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.CloudTrail.Outputs
{

    [OutputType]
    public sealed class TrailProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsloggrouparn
        /// </summary>
        public readonly string? CloudWatchLogsLogGroupArn;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsrolearn
        /// </summary>
        public readonly string? CloudWatchLogsRoleArn;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-enablelogfilevalidation
        /// </summary>
        public readonly bool? EnableLogFileValidation;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-eventselectors
        /// </summary>
        public readonly ImmutableArray<Outputs.TrailEventSelector> EventSelectors;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-includeglobalserviceevents
        /// </summary>
        public readonly bool? IncludeGlobalServiceEvents;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-islogging
        /// </summary>
        public readonly bool IsLogging;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-ismultiregiontrail
        /// </summary>
        public readonly bool? IsMultiRegionTrail;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-kmskeyid
        /// </summary>
        public readonly string? KMSKeyId;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3bucketname
        /// </summary>
        public readonly string S3BucketName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3keyprefix
        /// </summary>
        public readonly string? S3KeyPrefix;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-snstopicname
        /// </summary>
        public readonly string? SnsTopicName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-tags
        /// </summary>
        public readonly ImmutableArray<Pulumi.Cloudformation.Outputs.Tag> Tags;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-trailname
        /// </summary>
        public readonly string? TrailName;

        [OutputConstructor]
        private TrailProperties(
            string? CloudWatchLogsLogGroupArn,

            string? CloudWatchLogsRoleArn,

            bool? EnableLogFileValidation,

            ImmutableArray<Outputs.TrailEventSelector> EventSelectors,

            bool? IncludeGlobalServiceEvents,

            bool IsLogging,

            bool? IsMultiRegionTrail,

            string? KMSKeyId,

            string S3BucketName,

            string? S3KeyPrefix,

            string? SnsTopicName,

            ImmutableArray<Pulumi.Cloudformation.Outputs.Tag> Tags,

            string? TrailName)
        {
            this.CloudWatchLogsLogGroupArn = CloudWatchLogsLogGroupArn;
            this.CloudWatchLogsRoleArn = CloudWatchLogsRoleArn;
            this.EnableLogFileValidation = EnableLogFileValidation;
            this.EventSelectors = EventSelectors;
            this.IncludeGlobalServiceEvents = IncludeGlobalServiceEvents;
            this.IsLogging = IsLogging;
            this.IsMultiRegionTrail = IsMultiRegionTrail;
            this.KMSKeyId = KMSKeyId;
            this.S3BucketName = S3BucketName;
            this.S3KeyPrefix = S3KeyPrefix;
            this.SnsTopicName = SnsTopicName;
            this.Tags = Tags;
            this.TrailName = TrailName;
        }
    }
}