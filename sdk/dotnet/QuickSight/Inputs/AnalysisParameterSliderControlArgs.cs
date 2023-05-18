// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisParameterSliderControlArgs : global::Pulumi.ResourceArgs
    {
        [Input("displayOptions")]
        public Input<Inputs.AnalysisSliderControlDisplayOptionsArgs>? DisplayOptions { get; set; }

        [Input("maximumValue", required: true)]
        public Input<double> MaximumValue { get; set; } = null!;

        [Input("minimumValue", required: true)]
        public Input<double> MinimumValue { get; set; } = null!;

        [Input("parameterControlId", required: true)]
        public Input<string> ParameterControlId { get; set; } = null!;

        [Input("sourceParameterName", required: true)]
        public Input<string> SourceParameterName { get; set; } = null!;

        [Input("stepSize", required: true)]
        public Input<double> StepSize { get; set; } = null!;

        [Input("title", required: true)]
        public Input<string> Title { get; set; } = null!;

        public AnalysisParameterSliderControlArgs()
        {
        }
        public static new AnalysisParameterSliderControlArgs Empty => new AnalysisParameterSliderControlArgs();
    }
}
