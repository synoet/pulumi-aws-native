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
    public sealed class DashboardTableOptions
    {
        public readonly Outputs.DashboardTableCellStyle? CellStyle;
        public readonly Outputs.DashboardTableCellStyle? HeaderStyle;
        public readonly Pulumi.AwsNative.QuickSight.DashboardTableOrientation? Orientation;
        public readonly Outputs.DashboardRowAlternateColorOptions? RowAlternateColorOptions;

        [OutputConstructor]
        private DashboardTableOptions(
            Outputs.DashboardTableCellStyle? cellStyle,

            Outputs.DashboardTableCellStyle? headerStyle,

            Pulumi.AwsNative.QuickSight.DashboardTableOrientation? orientation,

            Outputs.DashboardRowAlternateColorOptions? rowAlternateColorOptions)
        {
            CellStyle = cellStyle;
            HeaderStyle = headerStyle;
            Orientation = orientation;
            RowAlternateColorOptions = rowAlternateColorOptions;
        }
    }
}
