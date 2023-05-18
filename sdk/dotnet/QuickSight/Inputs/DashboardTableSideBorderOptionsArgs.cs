// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardTableSideBorderOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("bottom")]
        public Input<Inputs.DashboardTableBorderOptionsArgs>? Bottom { get; set; }

        [Input("innerHorizontal")]
        public Input<Inputs.DashboardTableBorderOptionsArgs>? InnerHorizontal { get; set; }

        [Input("innerVertical")]
        public Input<Inputs.DashboardTableBorderOptionsArgs>? InnerVertical { get; set; }

        [Input("left")]
        public Input<Inputs.DashboardTableBorderOptionsArgs>? Left { get; set; }

        [Input("right")]
        public Input<Inputs.DashboardTableBorderOptionsArgs>? Right { get; set; }

        [Input("top")]
        public Input<Inputs.DashboardTableBorderOptionsArgs>? Top { get; set; }

        public DashboardTableSideBorderOptionsArgs()
        {
        }
        public static new DashboardTableSideBorderOptionsArgs Empty => new DashboardTableSideBorderOptionsArgs();
    }
}
