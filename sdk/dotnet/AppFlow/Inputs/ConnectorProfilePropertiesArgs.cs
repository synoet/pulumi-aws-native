// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Inputs
{

    /// <summary>
    /// Connector specific properties needed to create connector profile - currently not needed for Amplitude, Trendmicro, Googleanalytics and Singular
    /// </summary>
    public sealed class ConnectorProfilePropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("customConnector")]
        public Input<Inputs.ConnectorProfileCustomConnectorProfilePropertiesArgs>? CustomConnector { get; set; }

        [Input("datadog")]
        public Input<Inputs.ConnectorProfileDatadogConnectorProfilePropertiesArgs>? Datadog { get; set; }

        [Input("dynatrace")]
        public Input<Inputs.ConnectorProfileDynatraceConnectorProfilePropertiesArgs>? Dynatrace { get; set; }

        [Input("inforNexus")]
        public Input<Inputs.ConnectorProfileInforNexusConnectorProfilePropertiesArgs>? InforNexus { get; set; }

        [Input("marketo")]
        public Input<Inputs.ConnectorProfileMarketoConnectorProfilePropertiesArgs>? Marketo { get; set; }

        [Input("pardot")]
        public Input<Inputs.ConnectorProfilePardotConnectorProfilePropertiesArgs>? Pardot { get; set; }

        [Input("redshift")]
        public Input<Inputs.ConnectorProfileRedshiftConnectorProfilePropertiesArgs>? Redshift { get; set; }

        [Input("salesforce")]
        public Input<Inputs.ConnectorProfileSalesforceConnectorProfilePropertiesArgs>? Salesforce { get; set; }

        [Input("sapoData")]
        public Input<Inputs.ConnectorProfileSapoDataConnectorProfilePropertiesArgs>? SapoData { get; set; }

        [Input("serviceNow")]
        public Input<Inputs.ConnectorProfileServiceNowConnectorProfilePropertiesArgs>? ServiceNow { get; set; }

        [Input("slack")]
        public Input<Inputs.ConnectorProfileSlackConnectorProfilePropertiesArgs>? Slack { get; set; }

        [Input("snowflake")]
        public Input<Inputs.ConnectorProfileSnowflakeConnectorProfilePropertiesArgs>? Snowflake { get; set; }

        [Input("veeva")]
        public Input<Inputs.ConnectorProfileVeevaConnectorProfilePropertiesArgs>? Veeva { get; set; }

        [Input("zendesk")]
        public Input<Inputs.ConnectorProfileZendeskConnectorProfilePropertiesArgs>? Zendesk { get; set; }

        public ConnectorProfilePropertiesArgs()
        {
        }
        public static new ConnectorProfilePropertiesArgs Empty => new ConnectorProfilePropertiesArgs();
    }
}
