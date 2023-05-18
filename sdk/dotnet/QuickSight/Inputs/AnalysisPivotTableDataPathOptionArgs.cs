// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisPivotTableDataPathOptionArgs : global::Pulumi.ResourceArgs
    {
        [Input("dataPathList", required: true)]
        private InputList<Inputs.AnalysisDataPathValueArgs>? _dataPathList;
        public InputList<Inputs.AnalysisDataPathValueArgs> DataPathList
        {
            get => _dataPathList ?? (_dataPathList = new InputList<Inputs.AnalysisDataPathValueArgs>());
            set => _dataPathList = value;
        }

        /// <summary>
        /// String based length that is composed of value and unit in px
        /// </summary>
        [Input("width")]
        public Input<string>? Width { get; set; }

        public AnalysisPivotTableDataPathOptionArgs()
        {
        }
        public static new AnalysisPivotTableDataPathOptionArgs Empty => new AnalysisPivotTableDataPathOptionArgs();
    }
}
