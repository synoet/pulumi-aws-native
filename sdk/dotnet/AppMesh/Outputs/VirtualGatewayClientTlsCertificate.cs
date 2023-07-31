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
    public sealed class VirtualGatewayClientTlsCertificate
    {
        public readonly Outputs.VirtualGatewayListenerTlsFileCertificate? File;
        public readonly Outputs.VirtualGatewayListenerTlsSdsCertificate? Sds;

        [OutputConstructor]
        private VirtualGatewayClientTlsCertificate(
            Outputs.VirtualGatewayListenerTlsFileCertificate? file,

            Outputs.VirtualGatewayListenerTlsSdsCertificate? sds)
        {
            File = file;
            Sds = sds;
        }
    }
}
