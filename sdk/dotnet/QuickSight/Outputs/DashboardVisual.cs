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
    public sealed class DashboardVisual
    {
        public readonly Outputs.DashboardBarChartVisual? BarChartVisual;
        public readonly Outputs.DashboardBoxPlotVisual? BoxPlotVisual;
        public readonly Outputs.DashboardComboChartVisual? ComboChartVisual;
        public readonly Outputs.DashboardCustomContentVisual? CustomContentVisual;
        public readonly Outputs.DashboardEmptyVisual? EmptyVisual;
        public readonly Outputs.DashboardFilledMapVisual? FilledMapVisual;
        public readonly Outputs.DashboardFunnelChartVisual? FunnelChartVisual;
        public readonly Outputs.DashboardGaugeChartVisual? GaugeChartVisual;
        public readonly Outputs.DashboardGeospatialMapVisual? GeospatialMapVisual;
        public readonly Outputs.DashboardHeatMapVisual? HeatMapVisual;
        public readonly Outputs.DashboardHistogramVisual? HistogramVisual;
        public readonly Outputs.DashboardInsightVisual? InsightVisual;
        public readonly Outputs.DashboardKpiVisual? KpiVisual;
        public readonly Outputs.DashboardLineChartVisual? LineChartVisual;
        public readonly Outputs.DashboardPieChartVisual? PieChartVisual;
        public readonly Outputs.DashboardPivotTableVisual? PivotTableVisual;
        public readonly Outputs.DashboardRadarChartVisual? RadarChartVisual;
        public readonly Outputs.DashboardSankeyDiagramVisual? SankeyDiagramVisual;
        public readonly Outputs.DashboardScatterPlotVisual? ScatterPlotVisual;
        public readonly Outputs.DashboardTableVisual? TableVisual;
        public readonly Outputs.DashboardTreeMapVisual? TreeMapVisual;
        public readonly Outputs.DashboardWaterfallVisual? WaterfallVisual;
        public readonly Outputs.DashboardWordCloudVisual? WordCloudVisual;

        [OutputConstructor]
        private DashboardVisual(
            Outputs.DashboardBarChartVisual? barChartVisual,

            Outputs.DashboardBoxPlotVisual? boxPlotVisual,

            Outputs.DashboardComboChartVisual? comboChartVisual,

            Outputs.DashboardCustomContentVisual? customContentVisual,

            Outputs.DashboardEmptyVisual? emptyVisual,

            Outputs.DashboardFilledMapVisual? filledMapVisual,

            Outputs.DashboardFunnelChartVisual? funnelChartVisual,

            Outputs.DashboardGaugeChartVisual? gaugeChartVisual,

            Outputs.DashboardGeospatialMapVisual? geospatialMapVisual,

            Outputs.DashboardHeatMapVisual? heatMapVisual,

            Outputs.DashboardHistogramVisual? histogramVisual,

            Outputs.DashboardInsightVisual? insightVisual,

            Outputs.DashboardKpiVisual? kpiVisual,

            Outputs.DashboardLineChartVisual? lineChartVisual,

            Outputs.DashboardPieChartVisual? pieChartVisual,

            Outputs.DashboardPivotTableVisual? pivotTableVisual,

            Outputs.DashboardRadarChartVisual? radarChartVisual,

            Outputs.DashboardSankeyDiagramVisual? sankeyDiagramVisual,

            Outputs.DashboardScatterPlotVisual? scatterPlotVisual,

            Outputs.DashboardTableVisual? tableVisual,

            Outputs.DashboardTreeMapVisual? treeMapVisual,

            Outputs.DashboardWaterfallVisual? waterfallVisual,

            Outputs.DashboardWordCloudVisual? wordCloudVisual)
        {
            BarChartVisual = barChartVisual;
            BoxPlotVisual = boxPlotVisual;
            ComboChartVisual = comboChartVisual;
            CustomContentVisual = customContentVisual;
            EmptyVisual = emptyVisual;
            FilledMapVisual = filledMapVisual;
            FunnelChartVisual = funnelChartVisual;
            GaugeChartVisual = gaugeChartVisual;
            GeospatialMapVisual = geospatialMapVisual;
            HeatMapVisual = heatMapVisual;
            HistogramVisual = histogramVisual;
            InsightVisual = insightVisual;
            KpiVisual = kpiVisual;
            LineChartVisual = lineChartVisual;
            PieChartVisual = pieChartVisual;
            PivotTableVisual = pivotTableVisual;
            RadarChartVisual = radarChartVisual;
            SankeyDiagramVisual = sankeyDiagramVisual;
            ScatterPlotVisual = scatterPlotVisual;
            TableVisual = tableVisual;
            TreeMapVisual = treeMapVisual;
            WaterfallVisual = waterfallVisual;
            WordCloudVisual = wordCloudVisual;
        }
    }
}
