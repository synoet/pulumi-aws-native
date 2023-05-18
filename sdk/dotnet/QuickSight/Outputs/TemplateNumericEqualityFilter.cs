// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class TemplateNumericEqualityFilter
    {
        public readonly Outputs.TemplateAggregationFunction? AggregationFunction;
        public readonly Outputs.TemplateColumnIdentifier Column;
        public readonly string FilterId;
        public readonly Pulumi.AwsNative.QuickSight.TemplateNumericEqualityMatchOperator MatchOperator;
        public readonly Pulumi.AwsNative.QuickSight.TemplateFilterNullOption NullOption;
        public readonly string? ParameterName;
        public readonly Pulumi.AwsNative.QuickSight.TemplateNumericFilterSelectAllOptions? SelectAllOptions;
        public readonly double? Value;

        [OutputConstructor]
        private TemplateNumericEqualityFilter(
            Outputs.TemplateAggregationFunction? aggregationFunction,

            Outputs.TemplateColumnIdentifier column,

            string filterId,

            Pulumi.AwsNative.QuickSight.TemplateNumericEqualityMatchOperator matchOperator,

            Pulumi.AwsNative.QuickSight.TemplateFilterNullOption nullOption,

            string? parameterName,

            Pulumi.AwsNative.QuickSight.TemplateNumericFilterSelectAllOptions? selectAllOptions,

            double? value)
        {
            AggregationFunction = aggregationFunction;
            Column = column;
            FilterId = filterId;
            MatchOperator = matchOperator;
            NullOption = nullOption;
            ParameterName = parameterName;
            SelectAllOptions = selectAllOptions;
            Value = value;
        }
    }
}
