// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisRadarChartSeriesSettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("areaStyleSettings")]
        public Input<Inputs.AnalysisRadarChartAreaStyleSettingsArgs>? AreaStyleSettings { get; set; }

        public AnalysisRadarChartSeriesSettingsArgs()
        {
        }
        public static new AnalysisRadarChartSeriesSettingsArgs Empty => new AnalysisRadarChartSeriesSettingsArgs();
    }
}
