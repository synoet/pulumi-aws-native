// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardBodySectionContentArgs : global::Pulumi.ResourceArgs
    {
        [Input("layout")]
        public Input<Inputs.DashboardSectionLayoutConfigurationArgs>? Layout { get; set; }

        public DashboardBodySectionContentArgs()
        {
        }
        public static new DashboardBodySectionContentArgs Empty => new DashboardBodySectionContentArgs();
    }
}
