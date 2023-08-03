// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisFirehose.Inputs
{

    public sealed class DeliveryStreamEncryptionConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("kmsEncryptionConfig")]
        public Input<Inputs.DeliveryStreamKmsEncryptionConfigArgs>? KmsEncryptionConfig { get; set; }

        [Input("noEncryptionConfig")]
        public Input<Pulumi.AwsNative.KinesisFirehose.DeliveryStreamEncryptionConfigurationNoEncryptionConfig>? NoEncryptionConfig { get; set; }

        public DeliveryStreamEncryptionConfigurationArgs()
        {
        }
        public static new DeliveryStreamEncryptionConfigurationArgs Empty => new DeliveryStreamEncryptionConfigurationArgs();
    }
}
