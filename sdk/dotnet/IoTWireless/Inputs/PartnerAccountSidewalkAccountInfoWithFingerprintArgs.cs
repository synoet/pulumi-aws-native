// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTWireless.Inputs
{

    public sealed class PartnerAccountSidewalkAccountInfoWithFingerprintArgs : global::Pulumi.ResourceArgs
    {
        [Input("amazonId")]
        public Input<string>? AmazonId { get; set; }

        [Input("arn")]
        public Input<string>? Arn { get; set; }

        [Input("fingerprint")]
        public Input<string>? Fingerprint { get; set; }

        public PartnerAccountSidewalkAccountInfoWithFingerprintArgs()
        {
        }
        public static new PartnerAccountSidewalkAccountInfoWithFingerprintArgs Empty => new PartnerAccountSidewalkAccountInfoWithFingerprintArgs();
    }
}
