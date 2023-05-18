// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaPackage.Inputs
{

    /// <summary>
    /// An HTTP Live Streaming (HLS) encryption configuration.
    /// </summary>
    public sealed class PackagingConfigurationHlsEncryptionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// An HTTP Live Streaming (HLS) encryption configuration.
        /// </summary>
        [Input("constantInitializationVector")]
        public Input<string>? ConstantInitializationVector { get; set; }

        /// <summary>
        /// The encryption method to use.
        /// </summary>
        [Input("encryptionMethod")]
        public Input<Pulumi.AwsNative.MediaPackage.PackagingConfigurationHlsEncryptionEncryptionMethod>? EncryptionMethod { get; set; }

        [Input("spekeKeyProvider", required: true)]
        public Input<Inputs.PackagingConfigurationSpekeKeyProviderArgs> SpekeKeyProvider { get; set; } = null!;

        public PackagingConfigurationHlsEncryptionArgs()
        {
        }
        public static new PackagingConfigurationHlsEncryptionArgs Empty => new PackagingConfigurationHlsEncryptionArgs();
    }
}
