// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lex.Inputs
{

    /// <summary>
    /// Specifies an Amazon S3 bucket for logging audio conversations
    /// </summary>
    public sealed class BotS3BucketLogDestinationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of an AWS Key Management Service (KMS) key for encrypting audio log files stored in an S3 bucket.
        /// </summary>
        [Input("kmsKeyArn")]
        public Input<string>? KmsKeyArn { get; set; }

        /// <summary>
        /// The Amazon S3 key of the deployment package.
        /// </summary>
        [Input("logPrefix", required: true)]
        public Input<string> LogPrefix { get; set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of an Amazon S3 bucket where audio log files are stored.
        /// </summary>
        [Input("s3BucketArn", required: true)]
        public Input<string> S3BucketArn { get; set; } = null!;

        public BotS3BucketLogDestinationArgs()
        {
        }
        public static new BotS3BucketLogDestinationArgs Empty => new BotS3BucketLogDestinationArgs();
    }
}
