// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CleanRooms.Outputs
{

    [OutputType]
    public sealed class ConfiguredTableAnalysisRuleAggregation
    {
        public readonly ImmutableArray<Outputs.ConfiguredTableAggregateColumn> AggregateColumns;
        public readonly ImmutableArray<Pulumi.AwsNative.CleanRooms.ConfiguredTableJoinOperator> AllowedJoinOperators;
        public readonly ImmutableArray<string> DimensionColumns;
        public readonly ImmutableArray<string> JoinColumns;
        public readonly Pulumi.AwsNative.CleanRooms.ConfiguredTableJoinRequiredOption? JoinRequired;
        public readonly ImmutableArray<Outputs.ConfiguredTableAggregationConstraint> OutputConstraints;
        public readonly ImmutableArray<Pulumi.AwsNative.CleanRooms.ConfiguredTableScalarFunctions> ScalarFunctions;

        [OutputConstructor]
        private ConfiguredTableAnalysisRuleAggregation(
            ImmutableArray<Outputs.ConfiguredTableAggregateColumn> aggregateColumns,

            ImmutableArray<Pulumi.AwsNative.CleanRooms.ConfiguredTableJoinOperator> allowedJoinOperators,

            ImmutableArray<string> dimensionColumns,

            ImmutableArray<string> joinColumns,

            Pulumi.AwsNative.CleanRooms.ConfiguredTableJoinRequiredOption? joinRequired,

            ImmutableArray<Outputs.ConfiguredTableAggregationConstraint> outputConstraints,

            ImmutableArray<Pulumi.AwsNative.CleanRooms.ConfiguredTableScalarFunctions> scalarFunctions)
        {
            AggregateColumns = aggregateColumns;
            AllowedJoinOperators = allowedJoinOperators;
            DimensionColumns = dimensionColumns;
            JoinColumns = joinColumns;
            JoinRequired = joinRequired;
            OutputConstraints = outputConstraints;
            ScalarFunctions = scalarFunctions;
        }
    }
}
