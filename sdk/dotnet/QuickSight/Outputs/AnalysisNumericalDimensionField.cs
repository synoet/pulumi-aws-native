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
    public sealed class AnalysisNumericalDimensionField
    {
        public readonly Outputs.AnalysisColumnIdentifier Column;
        public readonly string FieldId;
        public readonly Outputs.AnalysisNumberFormatConfiguration? FormatConfiguration;
        public readonly string? HierarchyId;

        [OutputConstructor]
        private AnalysisNumericalDimensionField(
            Outputs.AnalysisColumnIdentifier column,

            string fieldId,

            Outputs.AnalysisNumberFormatConfiguration? formatConfiguration,

            string? hierarchyId)
        {
            Column = column;
            FieldId = fieldId;
            FormatConfiguration = formatConfiguration;
            HierarchyId = hierarchyId;
        }
    }
}
