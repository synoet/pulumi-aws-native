// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardSmallMultiplesAxisPropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("placement")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardSmallMultiplesAxisPlacement>? Placement { get; set; }

        [Input("scale")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardSmallMultiplesAxisScale>? Scale { get; set; }

        public DashboardSmallMultiplesAxisPropertiesArgs()
        {
        }
        public static new DashboardSmallMultiplesAxisPropertiesArgs Empty => new DashboardSmallMultiplesAxisPropertiesArgs();
    }
}
