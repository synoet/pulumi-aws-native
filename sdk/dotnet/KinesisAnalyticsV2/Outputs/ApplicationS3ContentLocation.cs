// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisAnalyticsV2.Outputs
{

    [OutputType]
    public sealed class ApplicationS3ContentLocation
    {
        public readonly string BucketARN;
        public readonly string FileKey;
        public readonly string? ObjectVersion;

        [OutputConstructor]
        private ApplicationS3ContentLocation(
            string bucketARN,

            string fileKey,

            string? objectVersion)
        {
            BucketARN = bucketARN;
            FileKey = fileKey;
            ObjectVersion = objectVersion;
        }
    }
}
