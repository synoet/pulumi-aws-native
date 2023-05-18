// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateBoxPlotSortConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("categorySort")]
        private InputList<Inputs.TemplateFieldSortOptionsArgs>? _categorySort;
        public InputList<Inputs.TemplateFieldSortOptionsArgs> CategorySort
        {
            get => _categorySort ?? (_categorySort = new InputList<Inputs.TemplateFieldSortOptionsArgs>());
            set => _categorySort = value;
        }

        [Input("paginationConfiguration")]
        public Input<Inputs.TemplatePaginationConfigurationArgs>? PaginationConfiguration { get; set; }

        public TemplateBoxPlotSortConfigurationArgs()
        {
        }
        public static new TemplateBoxPlotSortConfigurationArgs Empty => new TemplateBoxPlotSortConfigurationArgs();
    }
}
