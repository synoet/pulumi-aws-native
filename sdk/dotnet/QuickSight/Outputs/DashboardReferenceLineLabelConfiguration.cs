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
    public sealed class DashboardReferenceLineLabelConfiguration
    {
        public readonly Outputs.DashboardReferenceLineCustomLabelConfiguration? CustomLabelConfiguration;
        public readonly string? FontColor;
        public readonly Outputs.DashboardFontConfiguration? FontConfiguration;
        public readonly Pulumi.AwsNative.QuickSight.DashboardReferenceLineLabelHorizontalPosition? HorizontalPosition;
        public readonly Outputs.DashboardReferenceLineValueLabelConfiguration? ValueLabelConfiguration;
        public readonly Pulumi.AwsNative.QuickSight.DashboardReferenceLineLabelVerticalPosition? VerticalPosition;

        [OutputConstructor]
        private DashboardReferenceLineLabelConfiguration(
            Outputs.DashboardReferenceLineCustomLabelConfiguration? customLabelConfiguration,

            string? fontColor,

            Outputs.DashboardFontConfiguration? fontConfiguration,

            Pulumi.AwsNative.QuickSight.DashboardReferenceLineLabelHorizontalPosition? horizontalPosition,

            Outputs.DashboardReferenceLineValueLabelConfiguration? valueLabelConfiguration,

            Pulumi.AwsNative.QuickSight.DashboardReferenceLineLabelVerticalPosition? verticalPosition)
        {
            CustomLabelConfiguration = customLabelConfiguration;
            FontColor = fontColor;
            FontConfiguration = fontConfiguration;
            HorizontalPosition = horizontalPosition;
            ValueLabelConfiguration = valueLabelConfiguration;
            VerticalPosition = verticalPosition;
        }
    }
}
