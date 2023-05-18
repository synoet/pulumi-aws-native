// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateGeospatialMapVisualArgs : global::Pulumi.ResourceArgs
    {
        [Input("actions")]
        private InputList<Inputs.TemplateVisualCustomActionArgs>? _actions;
        public InputList<Inputs.TemplateVisualCustomActionArgs> Actions
        {
            get => _actions ?? (_actions = new InputList<Inputs.TemplateVisualCustomActionArgs>());
            set => _actions = value;
        }

        [Input("chartConfiguration")]
        public Input<Inputs.TemplateGeospatialMapConfigurationArgs>? ChartConfiguration { get; set; }

        [Input("columnHierarchies")]
        private InputList<Inputs.TemplateColumnHierarchyArgs>? _columnHierarchies;
        public InputList<Inputs.TemplateColumnHierarchyArgs> ColumnHierarchies
        {
            get => _columnHierarchies ?? (_columnHierarchies = new InputList<Inputs.TemplateColumnHierarchyArgs>());
            set => _columnHierarchies = value;
        }

        [Input("subtitle")]
        public Input<Inputs.TemplateVisualSubtitleLabelOptionsArgs>? Subtitle { get; set; }

        [Input("title")]
        public Input<Inputs.TemplateVisualTitleLabelOptionsArgs>? Title { get; set; }

        [Input("visualId", required: true)]
        public Input<string> VisualId { get; set; } = null!;

        public TemplateGeospatialMapVisualArgs()
        {
        }
        public static new TemplateGeospatialMapVisualArgs Empty => new TemplateGeospatialMapVisualArgs();
    }
}
