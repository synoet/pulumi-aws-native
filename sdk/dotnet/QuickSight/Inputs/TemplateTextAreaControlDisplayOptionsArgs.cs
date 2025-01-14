// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateTextAreaControlDisplayOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("infoIconLabelOptions")]
        public Input<Inputs.TemplateSheetControlInfoIconLabelOptionsArgs>? InfoIconLabelOptions { get; set; }

        [Input("placeholderOptions")]
        public Input<Inputs.TemplateTextControlPlaceholderOptionsArgs>? PlaceholderOptions { get; set; }

        [Input("titleOptions")]
        public Input<Inputs.TemplateLabelOptionsArgs>? TitleOptions { get; set; }

        public TemplateTextAreaControlDisplayOptionsArgs()
        {
        }
        public static new TemplateTextAreaControlDisplayOptionsArgs Empty => new TemplateTextAreaControlDisplayOptionsArgs();
    }
}
