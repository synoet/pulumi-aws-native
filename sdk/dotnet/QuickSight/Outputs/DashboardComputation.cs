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
    public sealed class DashboardComputation
    {
        public readonly Outputs.DashboardForecastComputation? Forecast;
        public readonly Outputs.DashboardGrowthRateComputation? GrowthRate;
        public readonly Outputs.DashboardMaximumMinimumComputation? MaximumMinimum;
        public readonly Outputs.DashboardMetricComparisonComputation? MetricComparison;
        public readonly Outputs.DashboardPeriodOverPeriodComputation? PeriodOverPeriod;
        public readonly Outputs.DashboardPeriodToDateComputation? PeriodToDate;
        public readonly Outputs.DashboardTopBottomMoversComputation? TopBottomMovers;
        public readonly Outputs.DashboardTopBottomRankedComputation? TopBottomRanked;
        public readonly Outputs.DashboardTotalAggregationComputation? TotalAggregation;
        public readonly Outputs.DashboardUniqueValuesComputation? UniqueValues;

        [OutputConstructor]
        private DashboardComputation(
            Outputs.DashboardForecastComputation? forecast,

            Outputs.DashboardGrowthRateComputation? growthRate,

            Outputs.DashboardMaximumMinimumComputation? maximumMinimum,

            Outputs.DashboardMetricComparisonComputation? metricComparison,

            Outputs.DashboardPeriodOverPeriodComputation? periodOverPeriod,

            Outputs.DashboardPeriodToDateComputation? periodToDate,

            Outputs.DashboardTopBottomMoversComputation? topBottomMovers,

            Outputs.DashboardTopBottomRankedComputation? topBottomRanked,

            Outputs.DashboardTotalAggregationComputation? totalAggregation,

            Outputs.DashboardUniqueValuesComputation? uniqueValues)
        {
            Forecast = forecast;
            GrowthRate = growthRate;
            MaximumMinimum = maximumMinimum;
            MetricComparison = metricComparison;
            PeriodOverPeriod = periodOverPeriod;
            PeriodToDate = periodToDate;
            TopBottomMovers = topBottomMovers;
            TopBottomRanked = topBottomRanked;
            TotalAggregation = totalAggregation;
            UniqueValues = uniqueValues;
        }
    }
}
