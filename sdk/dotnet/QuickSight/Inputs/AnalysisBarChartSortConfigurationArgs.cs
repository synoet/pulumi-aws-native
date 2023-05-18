// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisBarChartSortConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("categoryItemsLimit")]
        public Input<Inputs.AnalysisItemsLimitConfigurationArgs>? CategoryItemsLimit { get; set; }

        [Input("categorySort")]
        private InputList<Inputs.AnalysisFieldSortOptionsArgs>? _categorySort;
        public InputList<Inputs.AnalysisFieldSortOptionsArgs> CategorySort
        {
            get => _categorySort ?? (_categorySort = new InputList<Inputs.AnalysisFieldSortOptionsArgs>());
            set => _categorySort = value;
        }

        [Input("colorItemsLimit")]
        public Input<Inputs.AnalysisItemsLimitConfigurationArgs>? ColorItemsLimit { get; set; }

        [Input("colorSort")]
        private InputList<Inputs.AnalysisFieldSortOptionsArgs>? _colorSort;
        public InputList<Inputs.AnalysisFieldSortOptionsArgs> ColorSort
        {
            get => _colorSort ?? (_colorSort = new InputList<Inputs.AnalysisFieldSortOptionsArgs>());
            set => _colorSort = value;
        }

        [Input("smallMultiplesLimitConfiguration")]
        public Input<Inputs.AnalysisItemsLimitConfigurationArgs>? SmallMultiplesLimitConfiguration { get; set; }

        [Input("smallMultiplesSort")]
        private InputList<Inputs.AnalysisFieldSortOptionsArgs>? _smallMultiplesSort;
        public InputList<Inputs.AnalysisFieldSortOptionsArgs> SmallMultiplesSort
        {
            get => _smallMultiplesSort ?? (_smallMultiplesSort = new InputList<Inputs.AnalysisFieldSortOptionsArgs>());
            set => _smallMultiplesSort = value;
        }

        public AnalysisBarChartSortConfigurationArgs()
        {
        }
        public static new AnalysisBarChartSortConfigurationArgs Empty => new AnalysisBarChartSortConfigurationArgs();
    }
}
