// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.LookoutMetrics.Outputs
{

    [OutputType]
    public sealed class AnomalyDetectorMetric
    {
        /// <summary>
        /// Operator used to aggregate metric values
        /// </summary>
        public readonly Pulumi.AwsNative.LookoutMetrics.AnomalyDetectorMetricAggregationFunction AggregationFunction;
        public readonly string MetricName;
        public readonly string? Namespace;

        [OutputConstructor]
        private AnomalyDetectorMetric(
            Pulumi.AwsNative.LookoutMetrics.AnomalyDetectorMetricAggregationFunction aggregationFunction,

            string metricName,

            string? @namespace)
        {
            AggregationFunction = aggregationFunction;
            MetricName = metricName;
            Namespace = @namespace;
        }
    }
}
