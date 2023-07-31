// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppMesh.Inputs
{

    public sealed class VirtualGatewayTlsValidationContextTrustArgs : global::Pulumi.ResourceArgs
    {
        [Input("acm")]
        public Input<Inputs.VirtualGatewayTlsValidationContextAcmTrustArgs>? Acm { get; set; }

        [Input("file")]
        public Input<Inputs.VirtualGatewayTlsValidationContextFileTrustArgs>? File { get; set; }

        [Input("sds")]
        public Input<Inputs.VirtualGatewayTlsValidationContextSdsTrustArgs>? Sds { get; set; }

        public VirtualGatewayTlsValidationContextTrustArgs()
        {
        }
        public static new VirtualGatewayTlsValidationContextTrustArgs Empty => new VirtualGatewayTlsValidationContextTrustArgs();
    }
}
