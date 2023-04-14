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
    public sealed class AnalysisPivotTableCellConditionalFormatting
    {
        public readonly string FieldId;
        public readonly Outputs.AnalysisPivotTableConditionalFormattingScope? Scope;
        public readonly Outputs.AnalysisTextConditionalFormat? TextFormat;

        [OutputConstructor]
        private AnalysisPivotTableCellConditionalFormatting(
            string fieldId,

            Outputs.AnalysisPivotTableConditionalFormattingScope? scope,

            Outputs.AnalysisTextConditionalFormat? textFormat)
        {
            FieldId = fieldId;
            Scope = scope;
            TextFormat = textFormat;
        }
    }
}
