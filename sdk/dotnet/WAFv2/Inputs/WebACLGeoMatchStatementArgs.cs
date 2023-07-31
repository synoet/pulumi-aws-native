// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFv2.Inputs
{

    public sealed class WebACLGeoMatchStatementArgs : global::Pulumi.ResourceArgs
    {
        [Input("countryCodes")]
        private InputList<string>? _countryCodes;
        public InputList<string> CountryCodes
        {
            get => _countryCodes ?? (_countryCodes = new InputList<string>());
            set => _countryCodes = value;
        }

        [Input("forwardedIpConfig")]
        public Input<Inputs.WebACLForwardedIPConfigurationArgs>? ForwardedIpConfig { get; set; }

        public WebACLGeoMatchStatementArgs()
        {
        }
        public static new WebACLGeoMatchStatementArgs Empty => new WebACLGeoMatchStatementArgs();
    }
}
