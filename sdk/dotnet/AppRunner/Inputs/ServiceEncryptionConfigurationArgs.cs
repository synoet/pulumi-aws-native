// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppRunner.Inputs
{

    /// <summary>
    /// Encryption configuration (KMS key)
    /// </summary>
    public sealed class ServiceEncryptionConfigurationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The KMS Key
        /// </summary>
        [Input("kmsKey", required: true)]
        public Input<string> KmsKey { get; set; } = null!;

        public ServiceEncryptionConfigurationArgs()
        {
        }
        public static new ServiceEncryptionConfigurationArgs Empty => new ServiceEncryptionConfigurationArgs();
    }
}
