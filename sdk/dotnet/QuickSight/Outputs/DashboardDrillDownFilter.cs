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
    public sealed class DashboardDrillDownFilter
    {
        public readonly Outputs.DashboardCategoryDrillDownFilter? CategoryFilter;
        public readonly Outputs.DashboardNumericEqualityDrillDownFilter? NumericEqualityFilter;
        public readonly Outputs.DashboardTimeRangeDrillDownFilter? TimeRangeFilter;

        [OutputConstructor]
        private DashboardDrillDownFilter(
            Outputs.DashboardCategoryDrillDownFilter? categoryFilter,

            Outputs.DashboardNumericEqualityDrillDownFilter? numericEqualityFilter,

            Outputs.DashboardTimeRangeDrillDownFilter? timeRangeFilter)
        {
            CategoryFilter = categoryFilter;
            NumericEqualityFilter = numericEqualityFilter;
            TimeRangeFilter = timeRangeFilter;
        }
    }
}
