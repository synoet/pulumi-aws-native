// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class AnalysisGeospatialPointStyleOptions
    {
        public readonly Outputs.AnalysisClusterMarkerConfiguration? ClusterMarkerConfiguration;
        public readonly Outputs.AnalysisGeospatialHeatmapConfiguration? HeatmapConfiguration;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisGeospatialSelectedPointStyle? SelectedPointStyle;

        [OutputConstructor]
        private AnalysisGeospatialPointStyleOptions(
            Outputs.AnalysisClusterMarkerConfiguration? clusterMarkerConfiguration,

            Outputs.AnalysisGeospatialHeatmapConfiguration? heatmapConfiguration,

            Pulumi.AwsNative.QuickSight.AnalysisGeospatialSelectedPointStyle? selectedPointStyle)
        {
            ClusterMarkerConfiguration = clusterMarkerConfiguration;
            HeatmapConfiguration = heatmapConfiguration;
            SelectedPointStyle = selectedPointStyle;
        }
    }
}
