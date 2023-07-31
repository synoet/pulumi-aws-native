// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFront.Inputs
{

    public sealed class DistributionLegacyCustomOriginArgs : global::Pulumi.ResourceArgs
    {
        [Input("dnsName", required: true)]
        public Input<string> DnsName { get; set; } = null!;

        [Input("httpPort")]
        public Input<int>? HttpPort { get; set; }

        [Input("httpsPort")]
        public Input<int>? HttpsPort { get; set; }

        [Input("originProtocolPolicy", required: true)]
        public Input<string> OriginProtocolPolicy { get; set; } = null!;

        [Input("originSslProtocols", required: true)]
        private InputList<string>? _originSslProtocols;
        public InputList<string> OriginSslProtocols
        {
            get => _originSslProtocols ?? (_originSslProtocols = new InputList<string>());
            set => _originSslProtocols = value;
        }

        public DistributionLegacyCustomOriginArgs()
        {
        }
        public static new DistributionLegacyCustomOriginArgs Empty => new DistributionLegacyCustomOriginArgs();
    }
}
