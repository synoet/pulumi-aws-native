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
    public sealed class AnomalyDetectorAnomalyDetectorConfig
    {
        /// <summary>
        /// Frequency of anomaly detection
        /// </summary>
        public readonly Pulumi.AwsNative.LookoutMetrics.AnomalyDetectorAnomalyDetectorFrequency AnomalyDetectorFrequency;

        [OutputConstructor]
        private AnomalyDetectorAnomalyDetectorConfig(Pulumi.AwsNative.LookoutMetrics.AnomalyDetectorAnomalyDetectorFrequency anomalyDetectorFrequency)
        {
            AnomalyDetectorFrequency = anomalyDetectorFrequency;
        }
    }
}
