// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisBarChartConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("barsArrangement")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisBarsArrangement>? BarsArrangement { get; set; }

        [Input("categoryAxis")]
        public Input<Inputs.AnalysisAxisDisplayOptionsArgs>? CategoryAxis { get; set; }

        [Input("categoryLabelOptions")]
        public Input<Inputs.AnalysisChartAxisLabelOptionsArgs>? CategoryLabelOptions { get; set; }

        [Input("colorLabelOptions")]
        public Input<Inputs.AnalysisChartAxisLabelOptionsArgs>? ColorLabelOptions { get; set; }

        [Input("contributionAnalysisDefaults")]
        private InputList<Inputs.AnalysisContributionAnalysisDefaultArgs>? _contributionAnalysisDefaults;
        public InputList<Inputs.AnalysisContributionAnalysisDefaultArgs> ContributionAnalysisDefaults
        {
            get => _contributionAnalysisDefaults ?? (_contributionAnalysisDefaults = new InputList<Inputs.AnalysisContributionAnalysisDefaultArgs>());
            set => _contributionAnalysisDefaults = value;
        }

        [Input("dataLabels")]
        public Input<Inputs.AnalysisDataLabelOptionsArgs>? DataLabels { get; set; }

        [Input("fieldWells")]
        public Input<Inputs.AnalysisBarChartFieldWellsArgs>? FieldWells { get; set; }

        [Input("legend")]
        public Input<Inputs.AnalysisLegendOptionsArgs>? Legend { get; set; }

        [Input("orientation")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisBarChartOrientation>? Orientation { get; set; }

        [Input("referenceLines")]
        private InputList<Inputs.AnalysisReferenceLineArgs>? _referenceLines;
        public InputList<Inputs.AnalysisReferenceLineArgs> ReferenceLines
        {
            get => _referenceLines ?? (_referenceLines = new InputList<Inputs.AnalysisReferenceLineArgs>());
            set => _referenceLines = value;
        }

        [Input("smallMultiplesOptions")]
        public Input<Inputs.AnalysisSmallMultiplesOptionsArgs>? SmallMultiplesOptions { get; set; }

        [Input("sortConfiguration")]
        public Input<Inputs.AnalysisBarChartSortConfigurationArgs>? SortConfiguration { get; set; }

        [Input("tooltip")]
        public Input<Inputs.AnalysisTooltipOptionsArgs>? Tooltip { get; set; }

        [Input("valueAxis")]
        public Input<Inputs.AnalysisAxisDisplayOptionsArgs>? ValueAxis { get; set; }

        [Input("valueLabelOptions")]
        public Input<Inputs.AnalysisChartAxisLabelOptionsArgs>? ValueLabelOptions { get; set; }

        [Input("visualPalette")]
        public Input<Inputs.AnalysisVisualPaletteArgs>? VisualPalette { get; set; }

        public AnalysisBarChartConfigurationArgs()
        {
        }
        public static new AnalysisBarChartConfigurationArgs Empty => new AnalysisBarChartConfigurationArgs();
    }
}
