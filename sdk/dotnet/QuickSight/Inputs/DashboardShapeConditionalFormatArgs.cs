// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardShapeConditionalFormatArgs : global::Pulumi.ResourceArgs
    {
        [Input("backgroundColor", required: true)]
        public Input<Inputs.DashboardConditionalFormattingColorArgs> BackgroundColor { get; set; } = null!;

        public DashboardShapeConditionalFormatArgs()
        {
        }
        public static new DashboardShapeConditionalFormatArgs Empty => new DashboardShapeConditionalFormatArgs();
    }
}
