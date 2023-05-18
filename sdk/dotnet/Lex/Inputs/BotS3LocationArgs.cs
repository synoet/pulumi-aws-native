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
    /// S3 location of bot definitions zip file, if it's not defined inline in CloudFormation.
    /// </summary>
    public sealed class BotS3LocationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// An Amazon S3 bucket in the same AWS Region as your function. The bucket can be in a different AWS account.
        /// </summary>
        [Input("s3Bucket", required: true)]
        public Input<string> S3Bucket { get; set; } = null!;

        /// <summary>
        /// The Amazon S3 key of the deployment package.
        /// </summary>
        [Input("s3ObjectKey", required: true)]
        public Input<string> S3ObjectKey { get; set; } = null!;

        /// <summary>
        /// For versioned objects, the version of the deployment package object to use. If not specified, the current object version will be used.
        /// </summary>
        [Input("s3ObjectVersion")]
        public Input<string>? S3ObjectVersion { get; set; }

        public BotS3LocationArgs()
        {
        }
        public static new BotS3LocationArgs Empty => new BotS3LocationArgs();
    }
}
