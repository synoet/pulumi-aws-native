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
    public sealed class TemplateGeospatialMapFieldWells
    {
        public readonly Outputs.TemplateGeospatialMapAggregatedFieldWells? GeospatialMapAggregatedFieldWells;

        [OutputConstructor]
        private TemplateGeospatialMapFieldWells(Outputs.TemplateGeospatialMapAggregatedFieldWells? geospatialMapAggregatedFieldWells)
        {
            GeospatialMapAggregatedFieldWells = geospatialMapAggregatedFieldWells;
        }
    }
}
