// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.PcaConnectorAd.Outputs
{

    [OutputType]
    public sealed class TemplatePrivateKeyAttributesV2
    {
        public readonly ImmutableArray<string> CryptoProviders;
        public readonly Pulumi.AwsNative.PcaConnectorAd.TemplateKeySpec KeySpec;
        public readonly double MinimalKeyLength;

        [OutputConstructor]
        private TemplatePrivateKeyAttributesV2(
            ImmutableArray<string> cryptoProviders,

            Pulumi.AwsNative.PcaConnectorAd.TemplateKeySpec keySpec,

            double minimalKeyLength)
        {
            CryptoProviders = cryptoProviders;
            KeySpec = keySpec;
            MinimalKeyLength = minimalKeyLength;
        }
    }
}
