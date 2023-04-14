// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardExcludePeriodConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("amount", required: true)]
        public Input<double> Amount { get; set; } = null!;

        [Input("granularity", required: true)]
        public Input<Pulumi.AwsNative.QuickSight.DashboardTimeGranularity> Granularity { get; set; } = null!;

        [Input("status")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardWidgetStatus>? Status { get; set; }

        public DashboardExcludePeriodConfigurationArgs()
        {
        }
        public static new DashboardExcludePeriodConfigurationArgs Empty => new DashboardExcludePeriodConfigurationArgs();
    }
}
