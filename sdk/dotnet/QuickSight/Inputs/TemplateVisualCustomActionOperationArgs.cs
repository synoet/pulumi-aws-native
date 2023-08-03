// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateVisualCustomActionOperationArgs : global::Pulumi.ResourceArgs
    {
        [Input("filterOperation")]
        public Input<Inputs.TemplateCustomActionFilterOperationArgs>? FilterOperation { get; set; }

        [Input("navigationOperation")]
        public Input<Inputs.TemplateCustomActionNavigationOperationArgs>? NavigationOperation { get; set; }

        [Input("setParametersOperation")]
        public Input<Inputs.TemplateCustomActionSetParametersOperationArgs>? SetParametersOperation { get; set; }

        [Input("urlOperation")]
        public Input<Inputs.TemplateCustomActionUrlOperationArgs>? UrlOperation { get; set; }

        public TemplateVisualCustomActionOperationArgs()
        {
        }
        public static new TemplateVisualCustomActionOperationArgs Empty => new TemplateVisualCustomActionOperationArgs();
    }
}
