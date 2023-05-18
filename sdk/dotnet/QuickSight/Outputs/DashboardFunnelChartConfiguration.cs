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
    public sealed class DashboardFunnelChartConfiguration
    {
        public readonly Outputs.DashboardChartAxisLabelOptions? CategoryLabelOptions;
        public readonly Outputs.DashboardFunnelChartDataLabelOptions? DataLabelOptions;
        public readonly Outputs.DashboardFunnelChartFieldWells? FieldWells;
        public readonly Outputs.DashboardFunnelChartSortConfiguration? SortConfiguration;
        public readonly Outputs.DashboardTooltipOptions? Tooltip;
        public readonly Outputs.DashboardChartAxisLabelOptions? ValueLabelOptions;
        public readonly Outputs.DashboardVisualPalette? VisualPalette;

        [OutputConstructor]
        private DashboardFunnelChartConfiguration(
            Outputs.DashboardChartAxisLabelOptions? categoryLabelOptions,

            Outputs.DashboardFunnelChartDataLabelOptions? dataLabelOptions,

            Outputs.DashboardFunnelChartFieldWells? fieldWells,

            Outputs.DashboardFunnelChartSortConfiguration? sortConfiguration,

            Outputs.DashboardTooltipOptions? tooltip,

            Outputs.DashboardChartAxisLabelOptions? valueLabelOptions,

            Outputs.DashboardVisualPalette? visualPalette)
        {
            CategoryLabelOptions = categoryLabelOptions;
            DataLabelOptions = dataLabelOptions;
            FieldWells = fieldWells;
            SortConfiguration = sortConfiguration;
            Tooltip = tooltip;
            ValueLabelOptions = valueLabelOptions;
            VisualPalette = visualPalette;
        }
    }
}
