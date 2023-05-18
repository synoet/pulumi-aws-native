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
    public sealed class TemplatePivotTableFieldOptions
    {
        public readonly ImmutableArray<Outputs.TemplatePivotTableDataPathOption> DataPathOptions;
        public readonly ImmutableArray<Outputs.TemplatePivotTableFieldOption> SelectedFieldOptions;

        [OutputConstructor]
        private TemplatePivotTableFieldOptions(
            ImmutableArray<Outputs.TemplatePivotTableDataPathOption> dataPathOptions,

            ImmutableArray<Outputs.TemplatePivotTableFieldOption> selectedFieldOptions)
        {
            DataPathOptions = dataPathOptions;
            SelectedFieldOptions = selectedFieldOptions;
        }
    }
}
