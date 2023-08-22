// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Inputs
{

    public sealed class ConnectorProfileSapoDataConnectorProfilePropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("applicationHostUrl")]
        public Input<string>? ApplicationHostUrl { get; set; }

        [Input("applicationServicePath")]
        public Input<string>? ApplicationServicePath { get; set; }

        [Input("clientNumber")]
        public Input<string>? ClientNumber { get; set; }

        /// <summary>
        /// If you set this parameter to true, Amazon AppFlow bypasses the single sign-on (SSO) settings in your SAP account when it accesses your SAP OData instance.
        /// </summary>
        [Input("disableSso")]
        public Input<bool>? DisableSso { get; set; }

        [Input("logonLanguage")]
        public Input<string>? LogonLanguage { get; set; }

        [Input("oAuthProperties")]
        public Input<Inputs.ConnectorProfileOAuthPropertiesArgs>? OAuthProperties { get; set; }

        [Input("portNumber")]
        public Input<int>? PortNumber { get; set; }

        [Input("privateLinkServiceName")]
        public Input<string>? PrivateLinkServiceName { get; set; }

        public ConnectorProfileSapoDataConnectorProfilePropertiesArgs()
        {
        }
        public static new ConnectorProfileSapoDataConnectorProfilePropertiesArgs Empty => new ConnectorProfileSapoDataConnectorProfilePropertiesArgs();
    }
}
