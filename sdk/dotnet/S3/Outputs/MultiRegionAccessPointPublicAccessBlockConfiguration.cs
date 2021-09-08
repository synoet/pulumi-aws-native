// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3.Outputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-publicaccessblockconfiguration.html
    /// </summary>
    [OutputType]
    public sealed class MultiRegionAccessPointPublicAccessBlockConfiguration
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-publicaccessblockconfiguration.html#cfn-s3-multiregionaccesspoint-publicaccessblockconfiguration-blockpublicacls
        /// </summary>
        public readonly bool? BlockPublicAcls;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-publicaccessblockconfiguration.html#cfn-s3-multiregionaccesspoint-publicaccessblockconfiguration-blockpublicpolicy
        /// </summary>
        public readonly bool? BlockPublicPolicy;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-publicaccessblockconfiguration.html#cfn-s3-multiregionaccesspoint-publicaccessblockconfiguration-ignorepublicacls
        /// </summary>
        public readonly bool? IgnorePublicAcls;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-publicaccessblockconfiguration.html#cfn-s3-multiregionaccesspoint-publicaccessblockconfiguration-restrictpublicbuckets
        /// </summary>
        public readonly bool? RestrictPublicBuckets;

        [OutputConstructor]
        private MultiRegionAccessPointPublicAccessBlockConfiguration(
            bool? blockPublicAcls,

            bool? blockPublicPolicy,

            bool? ignorePublicAcls,

            bool? restrictPublicBuckets)
        {
            BlockPublicAcls = blockPublicAcls;
            BlockPublicPolicy = blockPublicPolicy;
            IgnorePublicAcls = ignorePublicAcls;
            RestrictPublicBuckets = restrictPublicBuckets;
        }
    }
}
