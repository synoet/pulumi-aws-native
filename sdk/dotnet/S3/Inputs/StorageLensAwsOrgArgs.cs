// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.S3.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-awsorg.html
    /// </summary>
    public sealed class StorageLensAwsOrgArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-awsorg.html#cfn-s3-storagelens-awsorg-arn
        /// </summary>
        [Input("Arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public StorageLensAwsOrgArgs()
        {
        }
    }
}