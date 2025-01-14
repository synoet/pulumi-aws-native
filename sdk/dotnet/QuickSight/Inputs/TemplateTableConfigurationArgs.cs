// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateTableConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("fieldOptions")]
        public Input<Inputs.TemplateTableFieldOptionsArgs>? FieldOptions { get; set; }

        [Input("fieldWells")]
        public Input<Inputs.TemplateTableFieldWellsArgs>? FieldWells { get; set; }

        [Input("paginatedReportOptions")]
        public Input<Inputs.TemplateTablePaginatedReportOptionsArgs>? PaginatedReportOptions { get; set; }

        [Input("sortConfiguration")]
        public Input<Inputs.TemplateTableSortConfigurationArgs>? SortConfiguration { get; set; }

        [Input("tableInlineVisualizations")]
        private InputList<Inputs.TemplateTableInlineVisualizationArgs>? _tableInlineVisualizations;
        public InputList<Inputs.TemplateTableInlineVisualizationArgs> TableInlineVisualizations
        {
            get => _tableInlineVisualizations ?? (_tableInlineVisualizations = new InputList<Inputs.TemplateTableInlineVisualizationArgs>());
            set => _tableInlineVisualizations = value;
        }

        [Input("tableOptions")]
        public Input<Inputs.TemplateTableOptionsArgs>? TableOptions { get; set; }

        [Input("totalOptions")]
        public Input<Inputs.TemplateTotalOptionsArgs>? TotalOptions { get; set; }

        public TemplateTableConfigurationArgs()
        {
        }
        public static new TemplateTableConfigurationArgs Empty => new TemplateTableConfigurationArgs();
    }
}
