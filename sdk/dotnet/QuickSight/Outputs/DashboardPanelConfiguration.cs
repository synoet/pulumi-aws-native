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
    public sealed class DashboardPanelConfiguration
    {
        public readonly string? BackgroundColor;
        public readonly Pulumi.AwsNative.QuickSight.DashboardVisibility? BackgroundVisibility;
        public readonly string? BorderColor;
        public readonly Pulumi.AwsNative.QuickSight.DashboardPanelBorderStyle? BorderStyle;
        /// <summary>
        /// String based length that is composed of value and unit in px
        /// </summary>
        public readonly string? BorderThickness;
        public readonly Pulumi.AwsNative.QuickSight.DashboardVisibility? BorderVisibility;
        /// <summary>
        /// String based length that is composed of value and unit in px
        /// </summary>
        public readonly string? GutterSpacing;
        public readonly Pulumi.AwsNative.QuickSight.DashboardVisibility? GutterVisibility;
        public readonly Outputs.DashboardPanelTitleOptions? Title;

        [OutputConstructor]
        private DashboardPanelConfiguration(
            string? backgroundColor,

            Pulumi.AwsNative.QuickSight.DashboardVisibility? backgroundVisibility,

            string? borderColor,

            Pulumi.AwsNative.QuickSight.DashboardPanelBorderStyle? borderStyle,

            string? borderThickness,

            Pulumi.AwsNative.QuickSight.DashboardVisibility? borderVisibility,

            string? gutterSpacing,

            Pulumi.AwsNative.QuickSight.DashboardVisibility? gutterVisibility,

            Outputs.DashboardPanelTitleOptions? title)
        {
            BackgroundColor = backgroundColor;
            BackgroundVisibility = backgroundVisibility;
            BorderColor = borderColor;
            BorderStyle = borderStyle;
            BorderThickness = borderThickness;
            BorderVisibility = borderVisibility;
            GutterSpacing = gutterSpacing;
            GutterVisibility = gutterVisibility;
            Title = title;
        }
    }
}
