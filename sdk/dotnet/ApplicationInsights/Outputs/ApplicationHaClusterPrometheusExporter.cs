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
    /// The HA cluster Prometheus Exporter settings.
    /// </summary>
    [OutputType]
    public sealed class ApplicationHaClusterPrometheusExporter
    {
        /// <summary>
        /// Prometheus exporter port.
        /// </summary>
        public readonly string? PrometheusPort;

        [OutputConstructor]
        private ApplicationHaClusterPrometheusExporter(string? prometheusPort)
        {
            PrometheusPort = prometheusPort;
        }
    }
}
