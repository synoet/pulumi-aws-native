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
    public sealed class DashboardComparisonConfiguration
    {
        public readonly Outputs.DashboardComparisonFormatConfiguration? ComparisonFormat;
        public readonly Pulumi.AwsNative.QuickSight.DashboardComparisonMethod? ComparisonMethod;

        [OutputConstructor]
        private DashboardComparisonConfiguration(
            Outputs.DashboardComparisonFormatConfiguration? comparisonFormat,

            Pulumi.AwsNative.QuickSight.DashboardComparisonMethod? comparisonMethod)
        {
            ComparisonFormat = comparisonFormat;
            ComparisonMethod = comparisonMethod;
        }
    }
}
