// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisShapeConditionalFormatArgs : global::Pulumi.ResourceArgs
    {
        [Input("backgroundColor", required: true)]
        public Input<Inputs.AnalysisConditionalFormattingColorArgs> BackgroundColor { get; set; } = null!;

        public AnalysisShapeConditionalFormatArgs()
        {
        }
        public static new AnalysisShapeConditionalFormatArgs Empty => new AnalysisShapeConditionalFormatArgs();
    }
}
