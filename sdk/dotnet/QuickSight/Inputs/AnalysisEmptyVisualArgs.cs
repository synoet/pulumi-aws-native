// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisEmptyVisualArgs : global::Pulumi.ResourceArgs
    {
        [Input("actions")]
        private InputList<Inputs.AnalysisVisualCustomActionArgs>? _actions;
        public InputList<Inputs.AnalysisVisualCustomActionArgs> Actions
        {
            get => _actions ?? (_actions = new InputList<Inputs.AnalysisVisualCustomActionArgs>());
            set => _actions = value;
        }

        [Input("dataSetIdentifier", required: true)]
        public Input<string> DataSetIdentifier { get; set; } = null!;

        [Input("visualId", required: true)]
        public Input<string> VisualId { get; set; } = null!;

        public AnalysisEmptyVisualArgs()
        {
        }
        public static new AnalysisEmptyVisualArgs Empty => new AnalysisEmptyVisualArgs();
    }
}
