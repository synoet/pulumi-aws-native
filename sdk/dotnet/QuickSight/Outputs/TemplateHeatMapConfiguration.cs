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
    public sealed class TemplateHeatMapConfiguration
    {
        public readonly Outputs.TemplateColorScale? ColorScale;
        public readonly Outputs.TemplateChartAxisLabelOptions? ColumnLabelOptions;
        public readonly Outputs.TemplateDataLabelOptions? DataLabels;
        public readonly Outputs.TemplateHeatMapFieldWells? FieldWells;
        public readonly Outputs.TemplateLegendOptions? Legend;
        public readonly Outputs.TemplateChartAxisLabelOptions? RowLabelOptions;
        public readonly Outputs.TemplateHeatMapSortConfiguration? SortConfiguration;
        public readonly Outputs.TemplateTooltipOptions? Tooltip;

        [OutputConstructor]
        private TemplateHeatMapConfiguration(
            Outputs.TemplateColorScale? colorScale,

            Outputs.TemplateChartAxisLabelOptions? columnLabelOptions,

            Outputs.TemplateDataLabelOptions? dataLabels,

            Outputs.TemplateHeatMapFieldWells? fieldWells,

            Outputs.TemplateLegendOptions? legend,

            Outputs.TemplateChartAxisLabelOptions? rowLabelOptions,

            Outputs.TemplateHeatMapSortConfiguration? sortConfiguration,

            Outputs.TemplateTooltipOptions? tooltip)
        {
            ColorScale = colorScale;
            ColumnLabelOptions = columnLabelOptions;
            DataLabels = dataLabels;
            FieldWells = fieldWells;
            Legend = legend;
            RowLabelOptions = rowLabelOptions;
            SortConfiguration = sortConfiguration;
            Tooltip = tooltip;
        }
    }
}
