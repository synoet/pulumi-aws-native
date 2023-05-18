// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.HealthLake.Inputs
{

    /// <summary>
    /// The server-side encryption key configuration for a customer provided encryption key.
    /// </summary>
    public sealed class FHIRDatastoreSseConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("kmsEncryptionConfig", required: true)]
        public Input<Inputs.FHIRDatastoreKmsEncryptionConfigArgs> KmsEncryptionConfig { get; set; } = null!;

        public FHIRDatastoreSseConfigurationArgs()
        {
        }
        public static new FHIRDatastoreSseConfigurationArgs Empty => new FHIRDatastoreSseConfigurationArgs();
    }
}
