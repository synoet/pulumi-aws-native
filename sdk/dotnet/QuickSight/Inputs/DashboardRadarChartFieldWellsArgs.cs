// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardRadarChartFieldWellsArgs : global::Pulumi.ResourceArgs
    {
        [Input("radarChartAggregatedFieldWells")]
        public Input<Inputs.DashboardRadarChartAggregatedFieldWellsArgs>? RadarChartAggregatedFieldWells { get; set; }

        public DashboardRadarChartFieldWellsArgs()
        {
        }
        public static new DashboardRadarChartFieldWellsArgs Empty => new DashboardRadarChartFieldWellsArgs();
    }
}
