// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApplicationInsights.Inputs
{

    /// <summary>
    /// The HANA DB Prometheus Exporter settings.
    /// </summary>
    public sealed class ApplicationHanaPrometheusExporterArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A flag which indicates agreeing to install SAP HANA DB client.
        /// </summary>
        [Input("agreeToInstallHanadbClient", required: true)]
        public Input<bool> AgreeToInstallHanadbClient { get; set; } = null!;

        /// <summary>
        /// The HANA DB port.
        /// </summary>
        [Input("hanaPort", required: true)]
        public Input<string> HanaPort { get; set; } = null!;

        /// <summary>
        /// The secret name which manages the HANA DB credentials e.g. {
        ///   "username": "&lt;&gt;",
        ///   "password": "&lt;&gt;"
        /// }.
        /// </summary>
        [Input("hanaSecretName", required: true)]
        public Input<string> HanaSecretName { get; set; } = null!;

        /// <summary>
        /// HANA DB SID.
        /// </summary>
        [Input("hanasid", required: true)]
        public Input<string> Hanasid { get; set; } = null!;

        /// <summary>
        /// Prometheus exporter port.
        /// </summary>
        [Input("prometheusPort")]
        public Input<string>? PrometheusPort { get; set; }

        public ApplicationHanaPrometheusExporterArgs()
        {
        }
        public static new ApplicationHanaPrometheusExporterArgs Empty => new ApplicationHanaPrometheusExporterArgs();
    }
}
