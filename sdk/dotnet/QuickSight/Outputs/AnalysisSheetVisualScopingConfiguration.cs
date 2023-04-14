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
    public sealed class AnalysisSheetVisualScopingConfiguration
    {
        public readonly Pulumi.AwsNative.QuickSight.AnalysisFilterVisualScope Scope;
        public readonly string SheetId;
        public readonly ImmutableArray<string> VisualIds;

        [OutputConstructor]
        private AnalysisSheetVisualScopingConfiguration(
            Pulumi.AwsNative.QuickSight.AnalysisFilterVisualScope scope,

            string sheetId,

            ImmutableArray<string> visualIds)
        {
            Scope = scope;
            SheetId = sheetId;
            VisualIds = visualIds;
        }
    }
}
