// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.PcaConnectorAd.Inputs
{

    public sealed class TemplateKeyUsagePropertyFlagsArgs : global::Pulumi.ResourceArgs
    {
        [Input("decrypt")]
        public Input<bool>? Decrypt { get; set; }

        [Input("keyAgreement")]
        public Input<bool>? KeyAgreement { get; set; }

        [Input("sign")]
        public Input<bool>? Sign { get; set; }

        public TemplateKeyUsagePropertyFlagsArgs()
        {
        }
        public static new TemplateKeyUsagePropertyFlagsArgs Empty => new TemplateKeyUsagePropertyFlagsArgs();
    }
}
