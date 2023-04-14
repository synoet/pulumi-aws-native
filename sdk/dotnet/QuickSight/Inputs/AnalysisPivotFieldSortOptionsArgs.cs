// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisPivotFieldSortOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("fieldId", required: true)]
        public Input<string> FieldId { get; set; } = null!;

        [Input("sortBy", required: true)]
        public Input<Inputs.AnalysisPivotTableSortByArgs> SortBy { get; set; } = null!;

        public AnalysisPivotFieldSortOptionsArgs()
        {
        }
        public static new AnalysisPivotFieldSortOptionsArgs Empty => new AnalysisPivotFieldSortOptionsArgs();
    }
}
