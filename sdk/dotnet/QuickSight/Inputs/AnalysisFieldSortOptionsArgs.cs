// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisFieldSortOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("columnSort")]
        public Input<Inputs.AnalysisColumnSortArgs>? ColumnSort { get; set; }

        [Input("fieldSort")]
        public Input<Inputs.AnalysisFieldSortArgs>? FieldSort { get; set; }

        public AnalysisFieldSortOptionsArgs()
        {
        }
        public static new AnalysisFieldSortOptionsArgs Empty => new AnalysisFieldSortOptionsArgs();
    }
}
