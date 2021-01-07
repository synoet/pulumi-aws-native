// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.RoboMaker.Outputs
{

    [OutputType]
    public sealed class RobotApplicationSourceConfig
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-sourceconfig.html#cfn-robomaker-robotapplication-sourceconfig-architecture
        /// </summary>
        public readonly string Architecture;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-sourceconfig.html#cfn-robomaker-robotapplication-sourceconfig-s3bucket
        /// </summary>
        public readonly string S3Bucket;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-sourceconfig.html#cfn-robomaker-robotapplication-sourceconfig-s3key
        /// </summary>
        public readonly string S3Key;

        [OutputConstructor]
        private RobotApplicationSourceConfig(
            string Architecture,

            string S3Bucket,

            string S3Key)
        {
            this.Architecture = Architecture;
            this.S3Bucket = S3Bucket;
            this.S3Key = S3Key;
        }
    }
}