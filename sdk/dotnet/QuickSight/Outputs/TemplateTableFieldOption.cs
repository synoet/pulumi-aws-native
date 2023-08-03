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
    public sealed class TemplateTableFieldOption
    {
        public readonly string? CustomLabel;
        public readonly string FieldId;
        public readonly Outputs.TemplateTableFieldUrlConfiguration? UrlStyling;
        public readonly Pulumi.AwsNative.QuickSight.TemplateVisibility? Visibility;
        /// <summary>
        /// String based length that is composed of value and unit in px
        /// </summary>
        public readonly string? Width;

        [OutputConstructor]
        private TemplateTableFieldOption(
            string? customLabel,

            string fieldId,

            Outputs.TemplateTableFieldUrlConfiguration? urlStyling,

            Pulumi.AwsNative.QuickSight.TemplateVisibility? visibility,

            string? width)
        {
            CustomLabel = customLabel;
            FieldId = fieldId;
            UrlStyling = urlStyling;
            Visibility = visibility;
            Width = width;
        }
    }
}
