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
    public sealed class DashboardSheetDefinition
    {
        public readonly Pulumi.AwsNative.QuickSight.DashboardSheetContentType? ContentType;
        public readonly string? Description;
        public readonly ImmutableArray<Outputs.DashboardFilterControl> FilterControls;
        public readonly ImmutableArray<Outputs.DashboardLayout> Layouts;
        public readonly string? Name;
        public readonly ImmutableArray<Outputs.DashboardParameterControl> ParameterControls;
        public readonly ImmutableArray<Outputs.DashboardSheetControlLayout> SheetControlLayouts;
        public readonly string SheetId;
        public readonly ImmutableArray<Outputs.DashboardSheetTextBox> TextBoxes;
        public readonly string? Title;
        public readonly ImmutableArray<Outputs.DashboardVisual> Visuals;

        [OutputConstructor]
        private DashboardSheetDefinition(
            Pulumi.AwsNative.QuickSight.DashboardSheetContentType? contentType,

            string? description,

            ImmutableArray<Outputs.DashboardFilterControl> filterControls,

            ImmutableArray<Outputs.DashboardLayout> layouts,

            string? name,

            ImmutableArray<Outputs.DashboardParameterControl> parameterControls,

            ImmutableArray<Outputs.DashboardSheetControlLayout> sheetControlLayouts,

            string sheetId,

            ImmutableArray<Outputs.DashboardSheetTextBox> textBoxes,

            string? title,

            ImmutableArray<Outputs.DashboardVisual> visuals)
        {
            ContentType = contentType;
            Description = description;
            FilterControls = filterControls;
            Layouts = layouts;
            Name = name;
            ParameterControls = parameterControls;
            SheetControlLayouts = sheetControlLayouts;
            SheetId = sheetId;
            TextBoxes = textBoxes;
            Title = title;
            Visuals = visuals;
        }
    }
}
