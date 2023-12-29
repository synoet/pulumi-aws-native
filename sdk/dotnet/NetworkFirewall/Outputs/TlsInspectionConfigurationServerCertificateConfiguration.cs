// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NetworkFirewall.Outputs
{

    [OutputType]
    public sealed class TlsInspectionConfigurationServerCertificateConfiguration
    {
        public readonly string? CertificateAuthorityArn;
        public readonly Outputs.TlsInspectionConfigurationServerCertificateConfigurationCheckCertificateRevocationStatusProperties? CheckCertificateRevocationStatus;
        public readonly ImmutableArray<Outputs.TlsInspectionConfigurationServerCertificateScope> Scopes;
        public readonly ImmutableArray<Outputs.TlsInspectionConfigurationServerCertificate> ServerCertificates;

        [OutputConstructor]
        private TlsInspectionConfigurationServerCertificateConfiguration(
            string? certificateAuthorityArn,

            Outputs.TlsInspectionConfigurationServerCertificateConfigurationCheckCertificateRevocationStatusProperties? checkCertificateRevocationStatus,

            ImmutableArray<Outputs.TlsInspectionConfigurationServerCertificateScope> scopes,

            ImmutableArray<Outputs.TlsInspectionConfigurationServerCertificate> serverCertificates)
        {
            CertificateAuthorityArn = certificateAuthorityArn;
            CheckCertificateRevocationStatus = checkCertificateRevocationStatus;
            Scopes = scopes;
            ServerCertificates = serverCertificates;
        }
    }
}
