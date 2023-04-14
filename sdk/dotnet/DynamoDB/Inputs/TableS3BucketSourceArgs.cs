// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DynamoDB.Inputs
{

    public sealed class TableS3BucketSourceArgs : global::Pulumi.ResourceArgs
    {
        [Input("s3Bucket", required: true)]
        public Input<string> S3Bucket { get; set; } = null!;

        [Input("s3BucketOwner")]
        public Input<string>? S3BucketOwner { get; set; }

        [Input("s3KeyPrefix")]
        public Input<string>? S3KeyPrefix { get; set; }

        public TableS3BucketSourceArgs()
        {
        }
        public static new TableS3BucketSourceArgs Empty => new TableS3BucketSourceArgs();
    }
}
