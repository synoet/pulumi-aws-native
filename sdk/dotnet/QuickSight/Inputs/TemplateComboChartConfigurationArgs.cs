// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateComboChartConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("barDataLabels")]
        public Input<Inputs.TemplateDataLabelOptionsArgs>? BarDataLabels { get; set; }

        [Input("barsArrangement")]
        public Input<Pulumi.AwsNative.QuickSight.TemplateBarsArrangement>? BarsArrangement { get; set; }

        [Input("categoryAxis")]
        public Input<Inputs.TemplateAxisDisplayOptionsArgs>? CategoryAxis { get; set; }

        [Input("categoryLabelOptions")]
        public Input<Inputs.TemplateChartAxisLabelOptionsArgs>? CategoryLabelOptions { get; set; }

        [Input("colorLabelOptions")]
        public Input<Inputs.TemplateChartAxisLabelOptionsArgs>? ColorLabelOptions { get; set; }

        [Input("fieldWells")]
        public Input<Inputs.TemplateComboChartFieldWellsArgs>? FieldWells { get; set; }

        [Input("legend")]
        public Input<Inputs.TemplateLegendOptionsArgs>? Legend { get; set; }

        [Input("lineDataLabels")]
        public Input<Inputs.TemplateDataLabelOptionsArgs>? LineDataLabels { get; set; }

        [Input("primaryYAxisDisplayOptions")]
        public Input<Inputs.TemplateAxisDisplayOptionsArgs>? PrimaryYAxisDisplayOptions { get; set; }

        [Input("primaryYAxisLabelOptions")]
        public Input<Inputs.TemplateChartAxisLabelOptionsArgs>? PrimaryYAxisLabelOptions { get; set; }

        [Input("referenceLines")]
        private InputList<Inputs.TemplateReferenceLineArgs>? _referenceLines;
        public InputList<Inputs.TemplateReferenceLineArgs> ReferenceLines
        {
            get => _referenceLines ?? (_referenceLines = new InputList<Inputs.TemplateReferenceLineArgs>());
            set => _referenceLines = value;
        }

        [Input("secondaryYAxisDisplayOptions")]
        public Input<Inputs.TemplateAxisDisplayOptionsArgs>? SecondaryYAxisDisplayOptions { get; set; }

        [Input("secondaryYAxisLabelOptions")]
        public Input<Inputs.TemplateChartAxisLabelOptionsArgs>? SecondaryYAxisLabelOptions { get; set; }

        [Input("sortConfiguration")]
        public Input<Inputs.TemplateComboChartSortConfigurationArgs>? SortConfiguration { get; set; }

        [Input("tooltip")]
        public Input<Inputs.TemplateTooltipOptionsArgs>? Tooltip { get; set; }

        [Input("visualPalette")]
        public Input<Inputs.TemplateVisualPaletteArgs>? VisualPalette { get; set; }

        public TemplateComboChartConfigurationArgs()
        {
        }
        public static new TemplateComboChartConfigurationArgs Empty => new TemplateComboChartConfigurationArgs();
    }
}
