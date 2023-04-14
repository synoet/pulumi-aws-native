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
    public sealed class DashboardFieldSortOptions
    {
        public readonly Outputs.DashboardColumnSort? ColumnSort;
        public readonly Outputs.DashboardFieldSort? FieldSort;

        [OutputConstructor]
        private DashboardFieldSortOptions(
            Outputs.DashboardColumnSort? columnSort,

            Outputs.DashboardFieldSort? fieldSort)
        {
            ColumnSort = columnSort;
            FieldSort = fieldSort;
        }
    }
}
