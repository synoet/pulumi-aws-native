// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RolesAnywhere.Outputs
{

    [OutputType]
    public sealed class SourceData0Properties
    {
        public readonly string X509CertificateData;

        [OutputConstructor]
        private SourceData0Properties(string x509CertificateData)
        {
            X509CertificateData = x509CertificateData;
        }
    }
}
