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
    public sealed class BucketInventoryConfiguration
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-inventoryconfiguration.html#cfn-s3-bucket-inventoryconfiguration-destination
        /// </summary>
        public readonly Outputs.BucketDestination Destination;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-inventoryconfiguration.html#cfn-s3-bucket-inventoryconfiguration-enabled
        /// </summary>
        public readonly bool Enabled;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-inventoryconfiguration.html#cfn-s3-bucket-inventoryconfiguration-id
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-inventoryconfiguration.html#cfn-s3-bucket-inventoryconfiguration-includedobjectversions
        /// </summary>
        public readonly string IncludedObjectVersions;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-inventoryconfiguration.html#cfn-s3-bucket-inventoryconfiguration-optionalfields
        /// </summary>
        public readonly ImmutableArray<string> OptionalFields;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-inventoryconfiguration.html#cfn-s3-bucket-inventoryconfiguration-prefix
        /// </summary>
        public readonly string? Prefix;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-inventoryconfiguration.html#cfn-s3-bucket-inventoryconfiguration-schedulefrequency
        /// </summary>
        public readonly string ScheduleFrequency;

        [OutputConstructor]
        private BucketInventoryConfiguration(
            Outputs.BucketDestination Destination,

            bool Enabled,

            string Id,

            string IncludedObjectVersions,

            ImmutableArray<string> OptionalFields,

            string? Prefix,

            string ScheduleFrequency)
        {
            this.Destination = Destination;
            this.Enabled = Enabled;
            this.Id = Id;
            this.IncludedObjectVersions = IncludedObjectVersions;
            this.OptionalFields = OptionalFields;
            this.Prefix = Prefix;
            this.ScheduleFrequency = ScheduleFrequency;
        }
    }
}