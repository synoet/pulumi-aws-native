// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateHeaderFooterSectionConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("layout", required: true)]
        public Input<Inputs.TemplateSectionLayoutConfigurationArgs> Layout { get; set; } = null!;

        [Input("sectionId", required: true)]
        public Input<string> SectionId { get; set; } = null!;

        [Input("style")]
        public Input<Inputs.TemplateSectionStyleArgs>? Style { get; set; }

        public TemplateHeaderFooterSectionConfigurationArgs()
        {
        }
        public static new TemplateHeaderFooterSectionConfigurationArgs Empty => new TemplateHeaderFooterSectionConfigurationArgs();
    }
}
