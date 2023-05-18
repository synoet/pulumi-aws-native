// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardVisualArgs : global::Pulumi.ResourceArgs
    {
        [Input("barChartVisual")]
        public Input<Inputs.DashboardBarChartVisualArgs>? BarChartVisual { get; set; }

        [Input("boxPlotVisual")]
        public Input<Inputs.DashboardBoxPlotVisualArgs>? BoxPlotVisual { get; set; }

        [Input("comboChartVisual")]
        public Input<Inputs.DashboardComboChartVisualArgs>? ComboChartVisual { get; set; }

        [Input("customContentVisual")]
        public Input<Inputs.DashboardCustomContentVisualArgs>? CustomContentVisual { get; set; }

        [Input("emptyVisual")]
        public Input<Inputs.DashboardEmptyVisualArgs>? EmptyVisual { get; set; }

        [Input("filledMapVisual")]
        public Input<Inputs.DashboardFilledMapVisualArgs>? FilledMapVisual { get; set; }

        [Input("funnelChartVisual")]
        public Input<Inputs.DashboardFunnelChartVisualArgs>? FunnelChartVisual { get; set; }

        [Input("gaugeChartVisual")]
        public Input<Inputs.DashboardGaugeChartVisualArgs>? GaugeChartVisual { get; set; }

        [Input("geospatialMapVisual")]
        public Input<Inputs.DashboardGeospatialMapVisualArgs>? GeospatialMapVisual { get; set; }

        [Input("heatMapVisual")]
        public Input<Inputs.DashboardHeatMapVisualArgs>? HeatMapVisual { get; set; }

        [Input("histogramVisual")]
        public Input<Inputs.DashboardHistogramVisualArgs>? HistogramVisual { get; set; }

        [Input("insightVisual")]
        public Input<Inputs.DashboardInsightVisualArgs>? InsightVisual { get; set; }

        [Input("kPIVisual")]
        public Input<Inputs.DashboardKPIVisualArgs>? KPIVisual { get; set; }

        [Input("lineChartVisual")]
        public Input<Inputs.DashboardLineChartVisualArgs>? LineChartVisual { get; set; }

        [Input("pieChartVisual")]
        public Input<Inputs.DashboardPieChartVisualArgs>? PieChartVisual { get; set; }

        [Input("pivotTableVisual")]
        public Input<Inputs.DashboardPivotTableVisualArgs>? PivotTableVisual { get; set; }

        [Input("radarChartVisual")]
        public Input<Inputs.DashboardRadarChartVisualArgs>? RadarChartVisual { get; set; }

        [Input("sankeyDiagramVisual")]
        public Input<Inputs.DashboardSankeyDiagramVisualArgs>? SankeyDiagramVisual { get; set; }

        [Input("scatterPlotVisual")]
        public Input<Inputs.DashboardScatterPlotVisualArgs>? ScatterPlotVisual { get; set; }

        [Input("tableVisual")]
        public Input<Inputs.DashboardTableVisualArgs>? TableVisual { get; set; }

        [Input("treeMapVisual")]
        public Input<Inputs.DashboardTreeMapVisualArgs>? TreeMapVisual { get; set; }

        [Input("waterfallVisual")]
        public Input<Inputs.DashboardWaterfallVisualArgs>? WaterfallVisual { get; set; }

        [Input("wordCloudVisual")]
        public Input<Inputs.DashboardWordCloudVisualArgs>? WordCloudVisual { get; set; }

        public DashboardVisualArgs()
        {
        }
        public static new DashboardVisualArgs Empty => new DashboardVisualArgs();
    }
}
