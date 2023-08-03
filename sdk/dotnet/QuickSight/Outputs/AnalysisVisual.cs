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
    public sealed class AnalysisVisual
    {
        public readonly Outputs.AnalysisBarChartVisual? BarChartVisual;
        public readonly Outputs.AnalysisBoxPlotVisual? BoxPlotVisual;
        public readonly Outputs.AnalysisComboChartVisual? ComboChartVisual;
        public readonly Outputs.AnalysisCustomContentVisual? CustomContentVisual;
        public readonly Outputs.AnalysisEmptyVisual? EmptyVisual;
        public readonly Outputs.AnalysisFilledMapVisual? FilledMapVisual;
        public readonly Outputs.AnalysisFunnelChartVisual? FunnelChartVisual;
        public readonly Outputs.AnalysisGaugeChartVisual? GaugeChartVisual;
        public readonly Outputs.AnalysisGeospatialMapVisual? GeospatialMapVisual;
        public readonly Outputs.AnalysisHeatMapVisual? HeatMapVisual;
        public readonly Outputs.AnalysisHistogramVisual? HistogramVisual;
        public readonly Outputs.AnalysisInsightVisual? InsightVisual;
        public readonly Outputs.AnalysisKpiVisual? KpiVisual;
        public readonly Outputs.AnalysisLineChartVisual? LineChartVisual;
        public readonly Outputs.AnalysisPieChartVisual? PieChartVisual;
        public readonly Outputs.AnalysisPivotTableVisual? PivotTableVisual;
        public readonly Outputs.AnalysisRadarChartVisual? RadarChartVisual;
        public readonly Outputs.AnalysisSankeyDiagramVisual? SankeyDiagramVisual;
        public readonly Outputs.AnalysisScatterPlotVisual? ScatterPlotVisual;
        public readonly Outputs.AnalysisTableVisual? TableVisual;
        public readonly Outputs.AnalysisTreeMapVisual? TreeMapVisual;
        public readonly Outputs.AnalysisWaterfallVisual? WaterfallVisual;
        public readonly Outputs.AnalysisWordCloudVisual? WordCloudVisual;

        [OutputConstructor]
        private AnalysisVisual(
            Outputs.AnalysisBarChartVisual? barChartVisual,

            Outputs.AnalysisBoxPlotVisual? boxPlotVisual,

            Outputs.AnalysisComboChartVisual? comboChartVisual,

            Outputs.AnalysisCustomContentVisual? customContentVisual,

            Outputs.AnalysisEmptyVisual? emptyVisual,

            Outputs.AnalysisFilledMapVisual? filledMapVisual,

            Outputs.AnalysisFunnelChartVisual? funnelChartVisual,

            Outputs.AnalysisGaugeChartVisual? gaugeChartVisual,

            Outputs.AnalysisGeospatialMapVisual? geospatialMapVisual,

            Outputs.AnalysisHeatMapVisual? heatMapVisual,

            Outputs.AnalysisHistogramVisual? histogramVisual,

            Outputs.AnalysisInsightVisual? insightVisual,

            Outputs.AnalysisKpiVisual? kpiVisual,

            Outputs.AnalysisLineChartVisual? lineChartVisual,

            Outputs.AnalysisPieChartVisual? pieChartVisual,

            Outputs.AnalysisPivotTableVisual? pivotTableVisual,

            Outputs.AnalysisRadarChartVisual? radarChartVisual,

            Outputs.AnalysisSankeyDiagramVisual? sankeyDiagramVisual,

            Outputs.AnalysisScatterPlotVisual? scatterPlotVisual,

            Outputs.AnalysisTableVisual? tableVisual,

            Outputs.AnalysisTreeMapVisual? treeMapVisual,

            Outputs.AnalysisWaterfallVisual? waterfallVisual,

            Outputs.AnalysisWordCloudVisual? wordCloudVisual)
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
