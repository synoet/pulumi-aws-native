// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisConditionalFormattingCustomIconConditionArgs : global::Pulumi.ResourceArgs
    {
        [Input("color")]
        public Input<string>? Color { get; set; }

        [Input("displayConfiguration")]
        public Input<Inputs.AnalysisConditionalFormattingIconDisplayConfigurationArgs>? DisplayConfiguration { get; set; }

        [Input("expression", required: true)]
        public Input<string> Expression { get; set; } = null!;

        [Input("iconOptions", required: true)]
        public Input<Inputs.AnalysisConditionalFormattingCustomIconOptionsArgs> IconOptions { get; set; } = null!;

        public AnalysisConditionalFormattingCustomIconConditionArgs()
        {
        }
        public static new AnalysisConditionalFormattingCustomIconConditionArgs Empty => new AnalysisConditionalFormattingCustomIconConditionArgs();
    }
}
