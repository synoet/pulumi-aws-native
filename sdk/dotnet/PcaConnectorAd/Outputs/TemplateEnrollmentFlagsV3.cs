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
    public sealed class TemplateEnrollmentFlagsV3
    {
        public readonly bool? EnableKeyReuseOnNtTokenKeysetStorageFull;
        public readonly bool? IncludeSymmetricAlgorithms;
        public readonly bool? NoSecurityExtension;
        public readonly bool? RemoveInvalidCertificateFromPersonalStore;
        public readonly bool? UserInteractionRequired;

        [OutputConstructor]
        private TemplateEnrollmentFlagsV3(
            bool? enableKeyReuseOnNtTokenKeysetStorageFull,

            bool? includeSymmetricAlgorithms,

            bool? noSecurityExtension,

            bool? removeInvalidCertificateFromPersonalStore,

            bool? userInteractionRequired)
        {
            EnableKeyReuseOnNtTokenKeysetStorageFull = enableKeyReuseOnNtTokenKeysetStorageFull;
            IncludeSymmetricAlgorithms = includeSymmetricAlgorithms;
            NoSecurityExtension = noSecurityExtension;
            RemoveInvalidCertificateFromPersonalStore = removeInvalidCertificateFromPersonalStore;
            UserInteractionRequired = userInteractionRequired;
        }
    }
}
