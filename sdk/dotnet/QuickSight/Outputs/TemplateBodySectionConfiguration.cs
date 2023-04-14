// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class TemplateBodySectionConfiguration
    {
        public readonly Outputs.TemplateBodySectionContent Content;
        public readonly Outputs.TemplateSectionPageBreakConfiguration? PageBreakConfiguration;
        public readonly string SectionId;
        public readonly Outputs.TemplateSectionStyle? Style;

        [OutputConstructor]
        private TemplateBodySectionConfiguration(
            Outputs.TemplateBodySectionContent content,

            Outputs.TemplateSectionPageBreakConfiguration? pageBreakConfiguration,

            string sectionId,

            Outputs.TemplateSectionStyle? style)
        {
            Content = content;
            PageBreakConfiguration = pageBreakConfiguration;
            SectionId = sectionId;
            Style = style;
        }
    }
}
