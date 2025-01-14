// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisTooltipOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("fieldBasedTooltip")]
        public Input<Inputs.AnalysisFieldBasedTooltipArgs>? FieldBasedTooltip { get; set; }

        [Input("selectedTooltipType")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisSelectedTooltipType>? SelectedTooltipType { get; set; }

        [Input("tooltipVisibility")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisVisibility>? TooltipVisibility { get; set; }

        public AnalysisTooltipOptionsArgs()
        {
        }
        public static new AnalysisTooltipOptionsArgs Empty => new AnalysisTooltipOptionsArgs();
    }
}
