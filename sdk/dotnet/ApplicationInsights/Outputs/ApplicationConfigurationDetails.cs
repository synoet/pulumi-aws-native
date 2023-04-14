// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApplicationInsights.Outputs
{

    /// <summary>
    /// The configuration settings.
    /// </summary>
    [OutputType]
    public sealed class ApplicationConfigurationDetails
    {
        /// <summary>
        /// A list of metrics to monitor for the component.
        /// </summary>
        public readonly ImmutableArray<Outputs.ApplicationAlarmMetric> AlarmMetrics;
        /// <summary>
        /// A list of alarms to monitor for the component.
        /// </summary>
        public readonly ImmutableArray<Outputs.ApplicationAlarm> Alarms;
        /// <summary>
        /// The HA cluster Prometheus Exporter settings.
        /// </summary>
        public readonly Outputs.ApplicationHAClusterPrometheusExporter? HAClusterPrometheusExporter;
        /// <summary>
        /// The HANA DB Prometheus Exporter settings.
        /// </summary>
        public readonly Outputs.ApplicationHANAPrometheusExporter? HANAPrometheusExporter;
        /// <summary>
        /// The JMX Prometheus Exporter settings.
        /// </summary>
        public readonly Outputs.ApplicationJMXPrometheusExporter? JMXPrometheusExporter;
        /// <summary>
        /// A list of logs to monitor for the component.
        /// </summary>
        public readonly ImmutableArray<Outputs.ApplicationLog> Logs;
        /// <summary>
        /// A list of Windows Events to log.
        /// </summary>
        public readonly ImmutableArray<Outputs.ApplicationWindowsEvent> WindowsEvents;

        [OutputConstructor]
        private ApplicationConfigurationDetails(
            ImmutableArray<Outputs.ApplicationAlarmMetric> alarmMetrics,

            ImmutableArray<Outputs.ApplicationAlarm> alarms,

            Outputs.ApplicationHAClusterPrometheusExporter? hAClusterPrometheusExporter,

            Outputs.ApplicationHANAPrometheusExporter? hANAPrometheusExporter,

            Outputs.ApplicationJMXPrometheusExporter? jMXPrometheusExporter,

            ImmutableArray<Outputs.ApplicationLog> logs,

            ImmutableArray<Outputs.ApplicationWindowsEvent> windowsEvents)
        {
            AlarmMetrics = alarmMetrics;
            Alarms = alarms;
            HAClusterPrometheusExporter = hAClusterPrometheusExporter;
            HANAPrometheusExporter = hANAPrometheusExporter;
            JMXPrometheusExporter = jMXPrometheusExporter;
            Logs = logs;
            WindowsEvents = windowsEvents;
        }
    }
}
