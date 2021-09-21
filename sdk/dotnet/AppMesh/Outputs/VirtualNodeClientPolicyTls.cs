// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppMesh.Outputs
{

    [OutputType]
    public sealed class VirtualNodeClientPolicyTls
    {
        public readonly Outputs.VirtualNodeClientTlsCertificate? Certificate;
        public readonly bool? Enforce;
        public readonly ImmutableArray<int> Ports;
        public readonly Outputs.VirtualNodeTlsValidationContext Validation;

        [OutputConstructor]
        private VirtualNodeClientPolicyTls(
            Outputs.VirtualNodeClientTlsCertificate? certificate,

            bool? enforce,

            ImmutableArray<int> ports,

            Outputs.VirtualNodeTlsValidationContext validation)
        {
            Certificate = certificate;
            Enforce = enforce;
            Ports = ports;
            Validation = validation;
        }
    }
}
