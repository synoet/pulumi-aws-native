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
    public sealed class AnalysisCustomFilterConfiguration
    {
        public readonly string? CategoryValue;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisCategoryFilterMatchOperator MatchOperator;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisFilterNullOption NullOption;
        public readonly string? ParameterName;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisCategoryFilterSelectAllOptions? SelectAllOptions;

        [OutputConstructor]
        private AnalysisCustomFilterConfiguration(
            string? categoryValue,

            Pulumi.AwsNative.QuickSight.AnalysisCategoryFilterMatchOperator matchOperator,

            Pulumi.AwsNative.QuickSight.AnalysisFilterNullOption nullOption,

            string? parameterName,

            Pulumi.AwsNative.QuickSight.AnalysisCategoryFilterSelectAllOptions? selectAllOptions)
        {
            CategoryValue = categoryValue;
            MatchOperator = matchOperator;
            NullOption = nullOption;
            ParameterName = parameterName;
            SelectAllOptions = selectAllOptions;
        }
    }
}
