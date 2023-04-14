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
    public sealed class DashboardDataFieldSeriesItem
    {
        public readonly Pulumi.AwsNative.QuickSight.DashboardAxisBinding AxisBinding;
        public readonly string FieldId;
        public readonly string? FieldValue;
        public readonly Outputs.DashboardLineChartSeriesSettings? Settings;

        [OutputConstructor]
        private DashboardDataFieldSeriesItem(
            Pulumi.AwsNative.QuickSight.DashboardAxisBinding axisBinding,

            string fieldId,

            string? fieldValue,

            Outputs.DashboardLineChartSeriesSettings? settings)
        {
            AxisBinding = axisBinding;
            FieldId = fieldId;
            FieldValue = fieldValue;
            Settings = settings;
        }
    }
}
