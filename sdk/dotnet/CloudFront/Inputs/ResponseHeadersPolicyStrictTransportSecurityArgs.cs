// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFront.Inputs
{

    public sealed class ResponseHeadersPolicyStrictTransportSecurityArgs : global::Pulumi.ResourceArgs
    {
        [Input("accessControlMaxAgeSec", required: true)]
        public Input<int> AccessControlMaxAgeSec { get; set; } = null!;

        [Input("includeSubdomains")]
        public Input<bool>? IncludeSubdomains { get; set; }

        [Input("override", required: true)]
        public Input<bool> Override { get; set; } = null!;

        [Input("preload")]
        public Input<bool>? Preload { get; set; }

        public ResponseHeadersPolicyStrictTransportSecurityArgs()
        {
        }
        public static new ResponseHeadersPolicyStrictTransportSecurityArgs Empty => new ResponseHeadersPolicyStrictTransportSecurityArgs();
    }
}
