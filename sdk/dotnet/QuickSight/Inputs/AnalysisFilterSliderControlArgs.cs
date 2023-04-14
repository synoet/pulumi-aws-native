// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisFilterSliderControlArgs : global::Pulumi.ResourceArgs
    {
        [Input("displayOptions")]
        public Input<Inputs.AnalysisSliderControlDisplayOptionsArgs>? DisplayOptions { get; set; }

        [Input("filterControlId", required: true)]
        public Input<string> FilterControlId { get; set; } = null!;

        [Input("maximumValue", required: true)]
        public Input<double> MaximumValue { get; set; } = null!;

        [Input("minimumValue", required: true)]
        public Input<double> MinimumValue { get; set; } = null!;

        [Input("sourceFilterId", required: true)]
        public Input<string> SourceFilterId { get; set; } = null!;

        [Input("stepSize", required: true)]
        public Input<double> StepSize { get; set; } = null!;

        [Input("title", required: true)]
        public Input<string> Title { get; set; } = null!;

        [Input("type")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisSheetControlSliderType>? Type { get; set; }

        public AnalysisFilterSliderControlArgs()
        {
        }
        public static new AnalysisFilterSliderControlArgs Empty => new AnalysisFilterSliderControlArgs();
    }
}
