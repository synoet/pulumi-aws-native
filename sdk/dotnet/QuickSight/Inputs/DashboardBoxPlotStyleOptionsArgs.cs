// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardBoxPlotStyleOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("fillStyle")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardBoxPlotFillStyle>? FillStyle { get; set; }

        public DashboardBoxPlotStyleOptionsArgs()
        {
        }
        public static new DashboardBoxPlotStyleOptionsArgs Empty => new DashboardBoxPlotStyleOptionsArgs();
    }
}
