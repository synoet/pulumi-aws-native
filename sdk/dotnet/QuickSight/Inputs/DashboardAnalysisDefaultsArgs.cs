// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardAnalysisDefaultsArgs : global::Pulumi.ResourceArgs
    {
        [Input("defaultNewSheetConfiguration", required: true)]
        public Input<Inputs.DashboardDefaultNewSheetConfigurationArgs> DefaultNewSheetConfiguration { get; set; } = null!;

        public DashboardAnalysisDefaultsArgs()
        {
        }
        public static new DashboardAnalysisDefaultsArgs Empty => new DashboardAnalysisDefaultsArgs();
    }
}
