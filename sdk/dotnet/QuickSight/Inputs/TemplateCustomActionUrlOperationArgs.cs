// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateCustomActionUrlOperationArgs : global::Pulumi.ResourceArgs
    {
        [Input("urlTarget", required: true)]
        public Input<Pulumi.AwsNative.QuickSight.TemplateUrlTargetConfiguration> UrlTarget { get; set; } = null!;

        [Input("urlTemplate", required: true)]
        public Input<string> UrlTemplate { get; set; } = null!;

        public TemplateCustomActionUrlOperationArgs()
        {
        }
        public static new TemplateCustomActionUrlOperationArgs Empty => new TemplateCustomActionUrlOperationArgs();
    }
}
