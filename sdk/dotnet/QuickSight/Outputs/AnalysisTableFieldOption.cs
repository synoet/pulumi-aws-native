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
    public sealed class AnalysisTableFieldOption
    {
        public readonly string? CustomLabel;
        public readonly string FieldId;
        public readonly Outputs.AnalysisTableFieldUrlConfiguration? UrlStyling;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisVisibility? Visibility;
        /// <summary>
        /// String based length that is composed of value and unit in px
        /// </summary>
        public readonly string? Width;

        [OutputConstructor]
        private AnalysisTableFieldOption(
            string? customLabel,

            string fieldId,

            Outputs.AnalysisTableFieldUrlConfiguration? urlStyling,

            Pulumi.AwsNative.QuickSight.AnalysisVisibility? visibility,

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
