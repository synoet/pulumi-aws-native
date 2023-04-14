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
    public sealed class TemplateHistogramVisual
    {
        public readonly ImmutableArray<Outputs.TemplateVisualCustomAction> Actions;
        public readonly Outputs.TemplateHistogramConfiguration? ChartConfiguration;
        public readonly Outputs.TemplateVisualSubtitleLabelOptions? Subtitle;
        public readonly Outputs.TemplateVisualTitleLabelOptions? Title;
        public readonly string VisualId;

        [OutputConstructor]
        private TemplateHistogramVisual(
            ImmutableArray<Outputs.TemplateVisualCustomAction> actions,

            Outputs.TemplateHistogramConfiguration? chartConfiguration,

            Outputs.TemplateVisualSubtitleLabelOptions? subtitle,

            Outputs.TemplateVisualTitleLabelOptions? title,

            string visualId)
        {
            Actions = actions;
            ChartConfiguration = chartConfiguration;
            Subtitle = subtitle;
            Title = title;
            VisualId = visualId;
        }
    }
}
