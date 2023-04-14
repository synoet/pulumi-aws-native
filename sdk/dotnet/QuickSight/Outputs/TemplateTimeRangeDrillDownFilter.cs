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
    public sealed class TemplateTimeRangeDrillDownFilter
    {
        public readonly Outputs.TemplateColumnIdentifier Column;
        public readonly string RangeMaximum;
        public readonly string RangeMinimum;
        public readonly Pulumi.AwsNative.QuickSight.TemplateTimeGranularity TimeGranularity;

        [OutputConstructor]
        private TemplateTimeRangeDrillDownFilter(
            Outputs.TemplateColumnIdentifier column,

            string rangeMaximum,

            string rangeMinimum,

            Pulumi.AwsNative.QuickSight.TemplateTimeGranularity timeGranularity)
        {
            Column = column;
            RangeMaximum = rangeMaximum;
            RangeMinimum = rangeMinimum;
            TimeGranularity = timeGranularity;
        }
    }
}
