// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardGeospatialPointStyleOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("clusterMarkerConfiguration")]
        public Input<Inputs.DashboardClusterMarkerConfigurationArgs>? ClusterMarkerConfiguration { get; set; }

        [Input("selectedPointStyle")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardGeospatialSelectedPointStyle>? SelectedPointStyle { get; set; }

        public DashboardGeospatialPointStyleOptionsArgs()
        {
        }
        public static new DashboardGeospatialPointStyleOptionsArgs Empty => new DashboardGeospatialPointStyleOptionsArgs();
    }
}
