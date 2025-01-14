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
    public sealed class TemplateAxisLabelOptions
    {
        public readonly Outputs.TemplateAxisLabelReferenceOptions? ApplyTo;
        public readonly string? CustomLabel;
        public readonly Outputs.TemplateFontConfiguration? FontConfiguration;

        [OutputConstructor]
        private TemplateAxisLabelOptions(
            Outputs.TemplateAxisLabelReferenceOptions? applyTo,

            string? customLabel,

            Outputs.TemplateFontConfiguration? fontConfiguration)
        {
            ApplyTo = applyTo;
            CustomLabel = customLabel;
            FontConfiguration = fontConfiguration;
        }
    }
}
