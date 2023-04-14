// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Evidently.Inputs
{

    public sealed class ExperimentOnlineAbConfigObjectArgs : global::Pulumi.ResourceArgs
    {
        [Input("controlTreatmentName")]
        public Input<string>? ControlTreatmentName { get; set; }

        [Input("treatmentWeights")]
        private InputList<Inputs.ExperimentTreatmentToWeightArgs>? _treatmentWeights;
        public InputList<Inputs.ExperimentTreatmentToWeightArgs> TreatmentWeights
        {
            get => _treatmentWeights ?? (_treatmentWeights = new InputList<Inputs.ExperimentTreatmentToWeightArgs>());
            set => _treatmentWeights = value;
        }

        public ExperimentOnlineAbConfigObjectArgs()
        {
        }
        public static new ExperimentOnlineAbConfigObjectArgs Empty => new ExperimentOnlineAbConfigObjectArgs();
    }
}
