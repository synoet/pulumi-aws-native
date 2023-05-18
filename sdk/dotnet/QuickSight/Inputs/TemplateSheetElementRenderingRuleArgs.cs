// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateSheetElementRenderingRuleArgs : global::Pulumi.ResourceArgs
    {
        [Input("configurationOverrides", required: true)]
        public Input<Inputs.TemplateSheetElementConfigurationOverridesArgs> ConfigurationOverrides { get; set; } = null!;

        [Input("expression", required: true)]
        public Input<string> Expression { get; set; } = null!;

        public TemplateSheetElementRenderingRuleArgs()
        {
        }
        public static new TemplateSheetElementRenderingRuleArgs Empty => new TemplateSheetElementRenderingRuleArgs();
    }
}
