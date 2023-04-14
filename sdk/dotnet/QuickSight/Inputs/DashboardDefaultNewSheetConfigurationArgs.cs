// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardDefaultNewSheetConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("interactiveLayoutConfiguration")]
        public Input<Inputs.DashboardDefaultInteractiveLayoutConfigurationArgs>? InteractiveLayoutConfiguration { get; set; }

        [Input("paginatedLayoutConfiguration")]
        public Input<Inputs.DashboardDefaultPaginatedLayoutConfigurationArgs>? PaginatedLayoutConfiguration { get; set; }

        [Input("sheetContentType")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardSheetContentType>? SheetContentType { get; set; }

        public DashboardDefaultNewSheetConfigurationArgs()
        {
        }
        public static new DashboardDefaultNewSheetConfigurationArgs Empty => new DashboardDefaultNewSheetConfigurationArgs();
    }
}
