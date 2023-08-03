// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardVisualCustomActionOperationArgs : global::Pulumi.ResourceArgs
    {
        [Input("filterOperation")]
        public Input<Inputs.DashboardCustomActionFilterOperationArgs>? FilterOperation { get; set; }

        [Input("navigationOperation")]
        public Input<Inputs.DashboardCustomActionNavigationOperationArgs>? NavigationOperation { get; set; }

        [Input("setParametersOperation")]
        public Input<Inputs.DashboardCustomActionSetParametersOperationArgs>? SetParametersOperation { get; set; }

        [Input("urlOperation")]
        public Input<Inputs.DashboardCustomActionUrlOperationArgs>? UrlOperation { get; set; }

        public DashboardVisualCustomActionOperationArgs()
        {
        }
        public static new DashboardVisualCustomActionOperationArgs Empty => new DashboardVisualCustomActionOperationArgs();
    }
}
