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
    public sealed class TemplateFilterScopeConfiguration
    {
        public readonly Outputs.TemplateAllSheetsFilterScopeConfiguration? AllSheets;
        public readonly Outputs.TemplateSelectedSheetsFilterScopeConfiguration? SelectedSheets;

        [OutputConstructor]
        private TemplateFilterScopeConfiguration(
            Outputs.TemplateAllSheetsFilterScopeConfiguration? allSheets,

            Outputs.TemplateSelectedSheetsFilterScopeConfiguration? selectedSheets)
        {
            AllSheets = allSheets;
            SelectedSheets = selectedSheets;
        }
    }
}
