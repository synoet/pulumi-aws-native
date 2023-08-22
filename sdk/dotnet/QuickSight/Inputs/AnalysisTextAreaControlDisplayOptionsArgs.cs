// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisTextAreaControlDisplayOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("infoIconLabelOptions")]
        public Input<Inputs.AnalysisSheetControlInfoIconLabelOptionsArgs>? InfoIconLabelOptions { get; set; }

        [Input("placeholderOptions")]
        public Input<Inputs.AnalysisTextControlPlaceholderOptionsArgs>? PlaceholderOptions { get; set; }

        [Input("titleOptions")]
        public Input<Inputs.AnalysisLabelOptionsArgs>? TitleOptions { get; set; }

        public AnalysisTextAreaControlDisplayOptionsArgs()
        {
        }
        public static new AnalysisTextAreaControlDisplayOptionsArgs Empty => new AnalysisTextAreaControlDisplayOptionsArgs();
    }
}
