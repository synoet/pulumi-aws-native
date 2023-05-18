// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardTopBottomMoversComputationArgs : global::Pulumi.ResourceArgs
    {
        [Input("category", required: true)]
        public Input<Inputs.DashboardDimensionFieldArgs> Category { get; set; } = null!;

        [Input("computationId", required: true)]
        public Input<string> ComputationId { get; set; } = null!;

        [Input("moverSize")]
        public Input<double>? MoverSize { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("sortOrder")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardTopBottomSortOrder>? SortOrder { get; set; }

        [Input("time", required: true)]
        public Input<Inputs.DashboardDimensionFieldArgs> Time { get; set; } = null!;

        [Input("type", required: true)]
        public Input<Pulumi.AwsNative.QuickSight.DashboardTopBottomComputationType> Type { get; set; } = null!;

        [Input("value")]
        public Input<Inputs.DashboardMeasureFieldArgs>? Value { get; set; }

        public DashboardTopBottomMoversComputationArgs()
        {
        }
        public static new DashboardTopBottomMoversComputationArgs Empty => new DashboardTopBottomMoversComputationArgs();
    }
}
