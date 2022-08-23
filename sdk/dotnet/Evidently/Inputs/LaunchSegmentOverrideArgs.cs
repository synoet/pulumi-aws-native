// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Evidently.Inputs
{

    public sealed class LaunchSegmentOverrideArgs : global::Pulumi.ResourceArgs
    {
        [Input("evaluationOrder", required: true)]
        public Input<int> EvaluationOrder { get; set; } = null!;

        [Input("segment", required: true)]
        public Input<string> Segment { get; set; } = null!;

        [Input("weights", required: true)]
        private InputList<Inputs.LaunchGroupToWeightArgs>? _weights;
        public InputList<Inputs.LaunchGroupToWeightArgs> Weights
        {
            get => _weights ?? (_weights = new InputList<Inputs.LaunchGroupToWeightArgs>());
            set => _weights = value;
        }

        public LaunchSegmentOverrideArgs()
        {
        }
        public static new LaunchSegmentOverrideArgs Empty => new LaunchSegmentOverrideArgs();
    }
}
