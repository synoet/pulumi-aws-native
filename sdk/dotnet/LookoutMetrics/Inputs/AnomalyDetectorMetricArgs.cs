// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.LookoutMetrics.Inputs
{

    public sealed class AnomalyDetectorMetricArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Operator used to aggregate metric values
        /// </summary>
        [Input("aggregationFunction", required: true)]
        public Input<Pulumi.AwsNative.LookoutMetrics.AnomalyDetectorMetricAggregationFunction> AggregationFunction { get; set; } = null!;

        [Input("metricName", required: true)]
        public Input<string> MetricName { get; set; } = null!;

        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        public AnomalyDetectorMetricArgs()
        {
        }
        public static new AnomalyDetectorMetricArgs Empty => new AnomalyDetectorMetricArgs();
    }
}
