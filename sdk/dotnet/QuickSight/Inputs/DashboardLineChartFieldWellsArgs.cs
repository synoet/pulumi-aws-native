// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardLineChartFieldWellsArgs : global::Pulumi.ResourceArgs
    {
        [Input("lineChartAggregatedFieldWells")]
        public Input<Inputs.DashboardLineChartAggregatedFieldWellsArgs>? LineChartAggregatedFieldWells { get; set; }

        public DashboardLineChartFieldWellsArgs()
        {
        }
        public static new DashboardLineChartFieldWellsArgs Empty => new DashboardLineChartFieldWellsArgs();
    }
}
