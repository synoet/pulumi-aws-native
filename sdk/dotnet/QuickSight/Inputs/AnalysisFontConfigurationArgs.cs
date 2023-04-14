// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisFontConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("fontColor")]
        public Input<string>? FontColor { get; set; }

        [Input("fontDecoration")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisFontDecoration>? FontDecoration { get; set; }

        [Input("fontSize")]
        public Input<Inputs.AnalysisFontSizeArgs>? FontSize { get; set; }

        [Input("fontStyle")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisFontStyle>? FontStyle { get; set; }

        [Input("fontWeight")]
        public Input<Inputs.AnalysisFontWeightArgs>? FontWeight { get; set; }

        public AnalysisFontConfigurationArgs()
        {
        }
        public static new AnalysisFontConfigurationArgs Empty => new AnalysisFontConfigurationArgs();
    }
}
