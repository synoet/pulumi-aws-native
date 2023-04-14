// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardTooltipItemArgs : global::Pulumi.ResourceArgs
    {
        [Input("columnTooltipItem")]
        public Input<Inputs.DashboardColumnTooltipItemArgs>? ColumnTooltipItem { get; set; }

        [Input("fieldTooltipItem")]
        public Input<Inputs.DashboardFieldTooltipItemArgs>? FieldTooltipItem { get; set; }

        public DashboardTooltipItemArgs()
        {
        }
        public static new DashboardTooltipItemArgs Empty => new DashboardTooltipItemArgs();
    }
}
