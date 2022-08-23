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
    /// Source connector details required to query a connector
    /// </summary>
    public sealed class FlowSourceConnectorPropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("amplitude")]
        public Input<Inputs.FlowAmplitudeSourcePropertiesArgs>? Amplitude { get; set; }

        [Input("customConnector")]
        public Input<Inputs.FlowCustomConnectorSourcePropertiesArgs>? CustomConnector { get; set; }

        [Input("datadog")]
        public Input<Inputs.FlowDatadogSourcePropertiesArgs>? Datadog { get; set; }

        [Input("dynatrace")]
        public Input<Inputs.FlowDynatraceSourcePropertiesArgs>? Dynatrace { get; set; }

        [Input("googleAnalytics")]
        public Input<Inputs.FlowGoogleAnalyticsSourcePropertiesArgs>? GoogleAnalytics { get; set; }

        [Input("inforNexus")]
        public Input<Inputs.FlowInforNexusSourcePropertiesArgs>? InforNexus { get; set; }

        [Input("marketo")]
        public Input<Inputs.FlowMarketoSourcePropertiesArgs>? Marketo { get; set; }

        [Input("s3")]
        public Input<Inputs.FlowS3SourcePropertiesArgs>? S3 { get; set; }

        [Input("sAPOData")]
        public Input<Inputs.FlowSAPODataSourcePropertiesArgs>? SAPOData { get; set; }

        [Input("salesforce")]
        public Input<Inputs.FlowSalesforceSourcePropertiesArgs>? Salesforce { get; set; }

        [Input("serviceNow")]
        public Input<Inputs.FlowServiceNowSourcePropertiesArgs>? ServiceNow { get; set; }

        [Input("singular")]
        public Input<Inputs.FlowSingularSourcePropertiesArgs>? Singular { get; set; }

        [Input("slack")]
        public Input<Inputs.FlowSlackSourcePropertiesArgs>? Slack { get; set; }

        [Input("trendmicro")]
        public Input<Inputs.FlowTrendmicroSourcePropertiesArgs>? Trendmicro { get; set; }

        [Input("veeva")]
        public Input<Inputs.FlowVeevaSourcePropertiesArgs>? Veeva { get; set; }

        [Input("zendesk")]
        public Input<Inputs.FlowZendeskSourcePropertiesArgs>? Zendesk { get; set; }

        public FlowSourceConnectorPropertiesArgs()
        {
        }
        public static new FlowSourceConnectorPropertiesArgs Empty => new FlowSourceConnectorPropertiesArgs();
    }
}
