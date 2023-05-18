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
    public sealed class TemplateWordCloudAggregatedFieldWells
    {
        public readonly ImmutableArray<Outputs.TemplateDimensionField> GroupBy;
        public readonly ImmutableArray<Outputs.TemplateMeasureField> Size;

        [OutputConstructor]
        private TemplateWordCloudAggregatedFieldWells(
            ImmutableArray<Outputs.TemplateDimensionField> groupBy,

            ImmutableArray<Outputs.TemplateMeasureField> size)
        {
            GroupBy = groupBy;
            Size = size;
        }
    }
}
