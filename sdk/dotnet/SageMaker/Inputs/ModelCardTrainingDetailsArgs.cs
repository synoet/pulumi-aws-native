// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    /// <summary>
    /// Overview about the training.
    /// </summary>
    public sealed class ModelCardTrainingDetailsArgs : global::Pulumi.ResourceArgs
    {
        [Input("objectiveFunction")]
        public Input<Inputs.ModelCardObjectiveFunctionArgs>? ObjectiveFunction { get; set; }

        [Input("trainingJobDetails")]
        public Input<Inputs.ModelCardTrainingDetailsTrainingJobDetailsPropertiesArgs>? TrainingJobDetails { get; set; }

        [Input("trainingObservations")]
        public Input<string>? TrainingObservations { get; set; }

        public ModelCardTrainingDetailsArgs()
        {
        }
        public static new ModelCardTrainingDetailsArgs Empty => new ModelCardTrainingDetailsArgs();
    }
}
