// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardBarChartSortConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("categoryItemsLimit")]
        public Input<Inputs.DashboardItemsLimitConfigurationArgs>? CategoryItemsLimit { get; set; }

        [Input("categorySort")]
        private InputList<Inputs.DashboardFieldSortOptionsArgs>? _categorySort;
        public InputList<Inputs.DashboardFieldSortOptionsArgs> CategorySort
        {
            get => _categorySort ?? (_categorySort = new InputList<Inputs.DashboardFieldSortOptionsArgs>());
            set => _categorySort = value;
        }

        [Input("colorItemsLimit")]
        public Input<Inputs.DashboardItemsLimitConfigurationArgs>? ColorItemsLimit { get; set; }

        [Input("colorSort")]
        private InputList<Inputs.DashboardFieldSortOptionsArgs>? _colorSort;
        public InputList<Inputs.DashboardFieldSortOptionsArgs> ColorSort
        {
            get => _colorSort ?? (_colorSort = new InputList<Inputs.DashboardFieldSortOptionsArgs>());
            set => _colorSort = value;
        }

        [Input("smallMultiplesLimitConfiguration")]
        public Input<Inputs.DashboardItemsLimitConfigurationArgs>? SmallMultiplesLimitConfiguration { get; set; }

        [Input("smallMultiplesSort")]
        private InputList<Inputs.DashboardFieldSortOptionsArgs>? _smallMultiplesSort;
        public InputList<Inputs.DashboardFieldSortOptionsArgs> SmallMultiplesSort
        {
            get => _smallMultiplesSort ?? (_smallMultiplesSort = new InputList<Inputs.DashboardFieldSortOptionsArgs>());
            set => _smallMultiplesSort = value;
        }

        public DashboardBarChartSortConfigurationArgs()
        {
        }
        public static new DashboardBarChartSortConfigurationArgs Empty => new DashboardBarChartSortConfigurationArgs();
    }
}
