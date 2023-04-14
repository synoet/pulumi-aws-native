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
    /// A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    /// </summary>
    public sealed class PackagingConfigurationSpekeKeyProviderArgs : global::Pulumi.ResourceArgs
    {
        [Input("encryptionContractConfiguration")]
        public Input<Inputs.PackagingConfigurationEncryptionContractConfigurationArgs>? EncryptionContractConfiguration { get; set; }

        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

        [Input("systemIds", required: true)]
        private InputList<string>? _systemIds;

        /// <summary>
        /// The system IDs to include in key requests.
        /// </summary>
        public InputList<string> SystemIds
        {
            get => _systemIds ?? (_systemIds = new InputList<string>());
            set => _systemIds = value;
        }

        /// <summary>
        /// The URL of the external key provider service.
        /// </summary>
        [Input("url", required: true)]
        public Input<string> Url { get; set; } = null!;

        public PackagingConfigurationSpekeKeyProviderArgs()
        {
        }
        public static new PackagingConfigurationSpekeKeyProviderArgs Empty => new PackagingConfigurationSpekeKeyProviderArgs();
    }
}
