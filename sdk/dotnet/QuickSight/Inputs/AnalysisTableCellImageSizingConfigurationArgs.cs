// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisTableCellImageSizingConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("tableCellImageScalingConfiguration")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisTableCellImageScalingConfiguration>? TableCellImageScalingConfiguration { get; set; }

        public AnalysisTableCellImageSizingConfigurationArgs()
        {
        }
        public static new AnalysisTableCellImageSizingConfigurationArgs Empty => new AnalysisTableCellImageSizingConfigurationArgs();
    }
}
