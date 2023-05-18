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
    public sealed class DashboardPeriodOverPeriodComputation
    {
        public readonly string ComputationId;
        public readonly string? Name;
        public readonly Outputs.DashboardDimensionField Time;
        public readonly Outputs.DashboardMeasureField? Value;

        [OutputConstructor]
        private DashboardPeriodOverPeriodComputation(
            string computationId,

            string? name,

            Outputs.DashboardDimensionField time,

            Outputs.DashboardMeasureField? value)
        {
            ComputationId = computationId;
            Name = name;
            Time = time;
            Value = value;
        }
    }
}
