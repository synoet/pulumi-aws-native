// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardFilterArgs : global::Pulumi.ResourceArgs
    {
        [Input("categoryFilter")]
        public Input<Inputs.DashboardCategoryFilterArgs>? CategoryFilter { get; set; }

        [Input("numericEqualityFilter")]
        public Input<Inputs.DashboardNumericEqualityFilterArgs>? NumericEqualityFilter { get; set; }

        [Input("numericRangeFilter")]
        public Input<Inputs.DashboardNumericRangeFilterArgs>? NumericRangeFilter { get; set; }

        [Input("relativeDatesFilter")]
        public Input<Inputs.DashboardRelativeDatesFilterArgs>? RelativeDatesFilter { get; set; }

        [Input("timeEqualityFilter")]
        public Input<Inputs.DashboardTimeEqualityFilterArgs>? TimeEqualityFilter { get; set; }

        [Input("timeRangeFilter")]
        public Input<Inputs.DashboardTimeRangeFilterArgs>? TimeRangeFilter { get; set; }

        [Input("topBottomFilter")]
        public Input<Inputs.DashboardTopBottomFilterArgs>? TopBottomFilter { get; set; }

        public DashboardFilterArgs()
        {
        }
        public static new DashboardFilterArgs Empty => new DashboardFilterArgs();
    }
}
