// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisFilterControlArgs : global::Pulumi.ResourceArgs
    {
        [Input("dateTimePicker")]
        public Input<Inputs.AnalysisFilterDateTimePickerControlArgs>? DateTimePicker { get; set; }

        [Input("dropdown")]
        public Input<Inputs.AnalysisFilterDropDownControlArgs>? Dropdown { get; set; }

        [Input("list")]
        public Input<Inputs.AnalysisFilterListControlArgs>? List { get; set; }

        [Input("relativeDateTime")]
        public Input<Inputs.AnalysisFilterRelativeDateTimeControlArgs>? RelativeDateTime { get; set; }

        [Input("slider")]
        public Input<Inputs.AnalysisFilterSliderControlArgs>? Slider { get; set; }

        [Input("textArea")]
        public Input<Inputs.AnalysisFilterTextAreaControlArgs>? TextArea { get; set; }

        [Input("textField")]
        public Input<Inputs.AnalysisFilterTextFieldControlArgs>? TextField { get; set; }

        public AnalysisFilterControlArgs()
        {
        }
        public static new AnalysisFilterControlArgs Empty => new AnalysisFilterControlArgs();
    }
}
