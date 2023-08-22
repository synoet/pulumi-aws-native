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
    public sealed class AnalysisTopBottomRankedComputation
    {
        public readonly Outputs.AnalysisDimensionField? Category;
        public readonly string ComputationId;
        public readonly string? Name;
        public readonly double? ResultSize;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisTopBottomComputationType Type;
        public readonly Outputs.AnalysisMeasureField? Value;

        [OutputConstructor]
        private AnalysisTopBottomRankedComputation(
            Outputs.AnalysisDimensionField? category,

            string computationId,

            string? name,

            double? resultSize,

            Pulumi.AwsNative.QuickSight.AnalysisTopBottomComputationType type,

            Outputs.AnalysisMeasureField? value)
        {
            Category = category;
            ComputationId = computationId;
            Name = name;
            ResultSize = resultSize;
            Type = type;
            Value = value;
        }
    }
}
