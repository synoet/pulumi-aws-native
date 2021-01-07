// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.KinesisFirehose.Outputs
{

    [OutputType]
    public sealed class DeliveryStreamKMSEncryptionConfig
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig.html#cfn-kinesisfirehose-deliverystream-kmsencryptionconfig-awskmskeyarn
        /// </summary>
        public readonly string AWSKMSKeyARN;

        [OutputConstructor]
        private DeliveryStreamKMSEncryptionConfig(string AWSKMSKeyARN)
        {
            this.AWSKMSKeyARN = AWSKMSKeyARN;
        }
    }
}