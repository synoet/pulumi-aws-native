// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardGrowthRateComputationArgs : global::Pulumi.ResourceArgs
    {
        [Input("computationId", required: true)]
        public Input<string> ComputationId { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("periodSize")]
        public Input<double>? PeriodSize { get; set; }

        [Input("time", required: true)]
        public Input<Inputs.DashboardDimensionFieldArgs> Time { get; set; } = null!;

        [Input("value")]
        public Input<Inputs.DashboardMeasureFieldArgs>? Value { get; set; }

        public DashboardGrowthRateComputationArgs()
        {
        }
        public static new DashboardGrowthRateComputationArgs Empty => new DashboardGrowthRateComputationArgs();
    }
}
