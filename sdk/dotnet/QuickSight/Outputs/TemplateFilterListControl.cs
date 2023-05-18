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
    public sealed class TemplateFilterListControl
    {
        public readonly Outputs.TemplateCascadingControlConfiguration? CascadingControlConfiguration;
        public readonly Outputs.TemplateListControlDisplayOptions? DisplayOptions;
        public readonly string FilterControlId;
        public readonly Outputs.TemplateFilterSelectableValues? SelectableValues;
        public readonly string SourceFilterId;
        public readonly string Title;
        public readonly Pulumi.AwsNative.QuickSight.TemplateSheetControlListType? Type;

        [OutputConstructor]
        private TemplateFilterListControl(
            Outputs.TemplateCascadingControlConfiguration? cascadingControlConfiguration,

            Outputs.TemplateListControlDisplayOptions? displayOptions,

            string filterControlId,

            Outputs.TemplateFilterSelectableValues? selectableValues,

            string sourceFilterId,

            string title,

            Pulumi.AwsNative.QuickSight.TemplateSheetControlListType? type)
        {
            CascadingControlConfiguration = cascadingControlConfiguration;
            DisplayOptions = displayOptions;
            FilterControlId = filterControlId;
            SelectableValues = selectableValues;
            SourceFilterId = sourceFilterId;
            Title = title;
            Type = type;
        }
    }
}
