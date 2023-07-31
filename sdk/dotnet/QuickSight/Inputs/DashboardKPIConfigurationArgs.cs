// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardKPIConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("fieldWells")]
        public Input<Inputs.DashboardKPIFieldWellsArgs>? FieldWells { get; set; }

        [Input("kpiOptions")]
        public Input<Inputs.DashboardKPIOptionsArgs>? KpiOptions { get; set; }

        [Input("sortConfiguration")]
        public Input<Inputs.DashboardKPISortConfigurationArgs>? SortConfiguration { get; set; }

        public DashboardKPIConfigurationArgs()
        {
        }
        public static new DashboardKPIConfigurationArgs Empty => new DashboardKPIConfigurationArgs();
    }
}
