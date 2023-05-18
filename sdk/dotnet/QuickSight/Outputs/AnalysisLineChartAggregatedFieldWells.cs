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
    public sealed class AnalysisLineChartAggregatedFieldWells
    {
        public readonly ImmutableArray<Outputs.AnalysisDimensionField> Category;
        public readonly ImmutableArray<Outputs.AnalysisDimensionField> Colors;
        public readonly ImmutableArray<Outputs.AnalysisDimensionField> SmallMultiples;
        public readonly ImmutableArray<Outputs.AnalysisMeasureField> Values;

        [OutputConstructor]
        private AnalysisLineChartAggregatedFieldWells(
            ImmutableArray<Outputs.AnalysisDimensionField> category,

            ImmutableArray<Outputs.AnalysisDimensionField> colors,

            ImmutableArray<Outputs.AnalysisDimensionField> smallMultiples,

            ImmutableArray<Outputs.AnalysisMeasureField> values)
        {
            Category = category;
            Colors = colors;
            SmallMultiples = smallMultiples;
            Values = values;
        }
    }
}
