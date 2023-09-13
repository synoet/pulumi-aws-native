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
    public sealed class TemplatePrivateKeyFlagsV4
    {
        public readonly Pulumi.AwsNative.PcaConnectorAd.TemplateClientCompatibilityV4 ClientVersion;
        public readonly bool? ExportableKey;
        public readonly bool? RequireAlternateSignatureAlgorithm;
        public readonly bool? RequireSameKeyRenewal;
        public readonly bool? StrongKeyProtectionRequired;
        public readonly bool? UseLegacyProvider;

        [OutputConstructor]
        private TemplatePrivateKeyFlagsV4(
            Pulumi.AwsNative.PcaConnectorAd.TemplateClientCompatibilityV4 clientVersion,

            bool? exportableKey,

            bool? requireAlternateSignatureAlgorithm,

            bool? requireSameKeyRenewal,

            bool? strongKeyProtectionRequired,

            bool? useLegacyProvider)
        {
            ClientVersion = clientVersion;
            ExportableKey = exportableKey;
            RequireAlternateSignatureAlgorithm = requireAlternateSignatureAlgorithm;
            RequireSameKeyRenewal = requireSameKeyRenewal;
            StrongKeyProtectionRequired = strongKeyProtectionRequired;
            UseLegacyProvider = useLegacyProvider;
        }
    }
}
