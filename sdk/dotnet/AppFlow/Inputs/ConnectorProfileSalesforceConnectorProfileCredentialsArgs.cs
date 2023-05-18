// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Inputs
{

    public sealed class ConnectorProfileSalesforceConnectorProfileCredentialsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The credentials used to access protected resources.
        /// </summary>
        [Input("accessToken")]
        public Input<string>? AccessToken { get; set; }

        /// <summary>
        /// The client credentials to fetch access token and refresh token.
        /// </summary>
        [Input("clientCredentialsArn")]
        public Input<string>? ClientCredentialsArn { get; set; }

        /// <summary>
        /// The oauth needed to request security tokens from the connector endpoint.
        /// </summary>
        [Input("connectorOAuthRequest")]
        public Input<Inputs.ConnectorProfileConnectorOAuthRequestArgs>? ConnectorOAuthRequest { get; set; }

        /// <summary>
        /// The credentials used to access your Salesforce records
        /// </summary>
        [Input("jwtToken")]
        public Input<string>? JwtToken { get; set; }

        /// <summary>
        /// The grant types to fetch an access token
        /// </summary>
        [Input("oAuth2GrantType")]
        public Input<Pulumi.AwsNative.AppFlow.ConnectorProfileOAuth2GrantType>? OAuth2GrantType { get; set; }

        /// <summary>
        /// The credentials used to acquire new access tokens.
        /// </summary>
        [Input("refreshToken")]
        public Input<string>? RefreshToken { get; set; }

        public ConnectorProfileSalesforceConnectorProfileCredentialsArgs()
        {
        }
        public static new ConnectorProfileSalesforceConnectorProfileCredentialsArgs Empty => new ConnectorProfileSalesforceConnectorProfileCredentialsArgs();
    }
}
