// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardDefaultSectionBasedLayoutConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("canvasSizeOptions", required: true)]
        public Input<Inputs.DashboardSectionBasedLayoutCanvasSizeOptionsArgs> CanvasSizeOptions { get; set; } = null!;

        public DashboardDefaultSectionBasedLayoutConfigurationArgs()
        {
        }
        public static new DashboardDefaultSectionBasedLayoutConfigurationArgs Empty => new DashboardDefaultSectionBasedLayoutConfigurationArgs();
    }
}
