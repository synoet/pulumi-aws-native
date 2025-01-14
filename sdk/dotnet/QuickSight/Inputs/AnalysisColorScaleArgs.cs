// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisColorScaleArgs : global::Pulumi.ResourceArgs
    {
        [Input("colorFillType", required: true)]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisColorFillType> ColorFillType { get; set; } = null!;

        [Input("colors", required: true)]
        private InputList<Inputs.AnalysisDataColorArgs>? _colors;
        public InputList<Inputs.AnalysisDataColorArgs> Colors
        {
            get => _colors ?? (_colors = new InputList<Inputs.AnalysisDataColorArgs>());
            set => _colors = value;
        }

        [Input("nullValueColor")]
        public Input<Inputs.AnalysisDataColorArgs>? NullValueColor { get; set; }

        public AnalysisColorScaleArgs()
        {
        }
        public static new AnalysisColorScaleArgs Empty => new AnalysisColorScaleArgs();
    }
}
