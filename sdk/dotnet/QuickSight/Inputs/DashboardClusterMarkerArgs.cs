// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardClusterMarkerArgs : global::Pulumi.ResourceArgs
    {
        [Input("simpleClusterMarker")]
        public Input<Inputs.DashboardSimpleClusterMarkerArgs>? SimpleClusterMarker { get; set; }

        public DashboardClusterMarkerArgs()
        {
        }
        public static new DashboardClusterMarkerArgs Empty => new DashboardClusterMarkerArgs();
    }
}
