// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.LookoutMetrics.Outputs
{

    [OutputType]
    public sealed class AnomalyDetectorMetricSource
    {
        public readonly Outputs.AnomalyDetectorAppFlowConfig? AppFlowConfig;
        public readonly Outputs.AnomalyDetectorCloudwatchConfig? CloudwatchConfig;
        public readonly Outputs.AnomalyDetectorRdsSourceConfig? RdsSourceConfig;
        public readonly Outputs.AnomalyDetectorRedshiftSourceConfig? RedshiftSourceConfig;
        public readonly Outputs.AnomalyDetectorS3SourceConfig? S3SourceConfig;

        [OutputConstructor]
        private AnomalyDetectorMetricSource(
            Outputs.AnomalyDetectorAppFlowConfig? appFlowConfig,

            Outputs.AnomalyDetectorCloudwatchConfig? cloudwatchConfig,

            Outputs.AnomalyDetectorRdsSourceConfig? rdsSourceConfig,

            Outputs.AnomalyDetectorRedshiftSourceConfig? redshiftSourceConfig,

            Outputs.AnomalyDetectorS3SourceConfig? s3SourceConfig)
        {
            AppFlowConfig = appFlowConfig;
            CloudwatchConfig = cloudwatchConfig;
            RdsSourceConfig = rdsSourceConfig;
            RedshiftSourceConfig = redshiftSourceConfig;
            S3SourceConfig = s3SourceConfig;
        }
    }
}
