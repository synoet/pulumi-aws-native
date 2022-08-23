// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Outputs
{

    /// <summary>
    /// Source connector details required to query a connector
    /// </summary>
    [OutputType]
    public sealed class FlowSourceConnectorProperties
    {
        public readonly Outputs.FlowAmplitudeSourceProperties? Amplitude;
        public readonly Outputs.FlowCustomConnectorSourceProperties? CustomConnector;
        public readonly Outputs.FlowDatadogSourceProperties? Datadog;
        public readonly Outputs.FlowDynatraceSourceProperties? Dynatrace;
        public readonly Outputs.FlowGoogleAnalyticsSourceProperties? GoogleAnalytics;
        public readonly Outputs.FlowInforNexusSourceProperties? InforNexus;
        public readonly Outputs.FlowMarketoSourceProperties? Marketo;
        public readonly Outputs.FlowS3SourceProperties? S3;
        public readonly Outputs.FlowSAPODataSourceProperties? SAPOData;
        public readonly Outputs.FlowSalesforceSourceProperties? Salesforce;
        public readonly Outputs.FlowServiceNowSourceProperties? ServiceNow;
        public readonly Outputs.FlowSingularSourceProperties? Singular;
        public readonly Outputs.FlowSlackSourceProperties? Slack;
        public readonly Outputs.FlowTrendmicroSourceProperties? Trendmicro;
        public readonly Outputs.FlowVeevaSourceProperties? Veeva;
        public readonly Outputs.FlowZendeskSourceProperties? Zendesk;

        [OutputConstructor]
        private FlowSourceConnectorProperties(
            Outputs.FlowAmplitudeSourceProperties? amplitude,

            Outputs.FlowCustomConnectorSourceProperties? customConnector,

            Outputs.FlowDatadogSourceProperties? datadog,

            Outputs.FlowDynatraceSourceProperties? dynatrace,

            Outputs.FlowGoogleAnalyticsSourceProperties? googleAnalytics,

            Outputs.FlowInforNexusSourceProperties? inforNexus,

            Outputs.FlowMarketoSourceProperties? marketo,

            Outputs.FlowS3SourceProperties? s3,

            Outputs.FlowSAPODataSourceProperties? sAPOData,

            Outputs.FlowSalesforceSourceProperties? salesforce,

            Outputs.FlowServiceNowSourceProperties? serviceNow,

            Outputs.FlowSingularSourceProperties? singular,

            Outputs.FlowSlackSourceProperties? slack,

            Outputs.FlowTrendmicroSourceProperties? trendmicro,

            Outputs.FlowVeevaSourceProperties? veeva,

            Outputs.FlowZendeskSourceProperties? zendesk)
        {
            Amplitude = amplitude;
            CustomConnector = customConnector;
            Datadog = datadog;
            Dynatrace = dynatrace;
            GoogleAnalytics = googleAnalytics;
            InforNexus = inforNexus;
            Marketo = marketo;
            S3 = s3;
            SAPOData = sAPOData;
            Salesforce = salesforce;
            ServiceNow = serviceNow;
            Singular = singular;
            Slack = slack;
            Trendmicro = trendmicro;
            Veeva = veeva;
            Zendesk = zendesk;
        }
    }
}
