// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisNumericEqualityFilterArgs : global::Pulumi.ResourceArgs
    {
        [Input("aggregationFunction")]
        public Input<Inputs.AnalysisAggregationFunctionArgs>? AggregationFunction { get; set; }

        [Input("column", required: true)]
        public Input<Inputs.AnalysisColumnIdentifierArgs> Column { get; set; } = null!;

        [Input("filterId", required: true)]
        public Input<string> FilterId { get; set; } = null!;

        [Input("matchOperator", required: true)]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisNumericEqualityMatchOperator> MatchOperator { get; set; } = null!;

        [Input("nullOption", required: true)]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisFilterNullOption> NullOption { get; set; } = null!;

        [Input("parameterName")]
        public Input<string>? ParameterName { get; set; }

        [Input("selectAllOptions")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisNumericFilterSelectAllOptions>? SelectAllOptions { get; set; }

        [Input("value")]
        public Input<double>? Value { get; set; }

        public AnalysisNumericEqualityFilterArgs()
        {
        }
        public static new AnalysisNumericEqualityFilterArgs Empty => new AnalysisNumericEqualityFilterArgs();
    }
}
