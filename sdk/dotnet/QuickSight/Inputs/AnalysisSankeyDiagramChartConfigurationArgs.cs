// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisSankeyDiagramChartConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("dataLabels")]
        public Input<Inputs.AnalysisDataLabelOptionsArgs>? DataLabels { get; set; }

        [Input("fieldWells")]
        public Input<Inputs.AnalysisSankeyDiagramFieldWellsArgs>? FieldWells { get; set; }

        [Input("sortConfiguration")]
        public Input<Inputs.AnalysisSankeyDiagramSortConfigurationArgs>? SortConfiguration { get; set; }

        public AnalysisSankeyDiagramChartConfigurationArgs()
        {
        }
        public static new AnalysisSankeyDiagramChartConfigurationArgs Empty => new AnalysisSankeyDiagramChartConfigurationArgs();
    }
}
