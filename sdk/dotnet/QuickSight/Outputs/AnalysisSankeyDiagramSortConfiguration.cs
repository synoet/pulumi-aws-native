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
    public sealed class AnalysisSankeyDiagramSortConfiguration
    {
        public readonly Outputs.AnalysisItemsLimitConfiguration? DestinationItemsLimit;
        public readonly Outputs.AnalysisItemsLimitConfiguration? SourceItemsLimit;
        public readonly ImmutableArray<Outputs.AnalysisFieldSortOptions> WeightSort;

        [OutputConstructor]
        private AnalysisSankeyDiagramSortConfiguration(
            Outputs.AnalysisItemsLimitConfiguration? destinationItemsLimit,

            Outputs.AnalysisItemsLimitConfiguration? sourceItemsLimit,

            ImmutableArray<Outputs.AnalysisFieldSortOptions> weightSort)
        {
            DestinationItemsLimit = destinationItemsLimit;
            SourceItemsLimit = sourceItemsLimit;
            WeightSort = weightSort;
        }
    }
}
