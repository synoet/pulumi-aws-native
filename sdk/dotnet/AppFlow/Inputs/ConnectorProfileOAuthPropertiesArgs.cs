// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Inputs
{

    public sealed class ConnectorProfileOAuthPropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("authCodeUrl")]
        public Input<string>? AuthCodeUrl { get; set; }

        [Input("oAuthScopes")]
        private InputList<string>? _oAuthScopes;
        public InputList<string> OAuthScopes
        {
            get => _oAuthScopes ?? (_oAuthScopes = new InputList<string>());
            set => _oAuthScopes = value;
        }

        [Input("tokenUrl")]
        public Input<string>? TokenUrl { get; set; }

        public ConnectorProfileOAuthPropertiesArgs()
        {
        }
        public static new ConnectorProfileOAuthPropertiesArgs Empty => new ConnectorProfileOAuthPropertiesArgs();
    }
}
