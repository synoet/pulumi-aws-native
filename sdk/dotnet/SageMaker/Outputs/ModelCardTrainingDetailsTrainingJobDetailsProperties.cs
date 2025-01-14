// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Outputs
{

    [OutputType]
    public sealed class ModelCardTrainingDetailsTrainingJobDetailsProperties
    {
        public readonly ImmutableArray<Outputs.ModelCardTrainingHyperParameter> HyperParameters;
        /// <summary>
        /// SageMaker Training job arn.
        /// </summary>
        public readonly string? TrainingArn;
        /// <summary>
        /// Location of the model datasets.
        /// </summary>
        public readonly ImmutableArray<string> TrainingDatasets;
        public readonly Outputs.ModelCardTrainingDetailsTrainingJobDetailsPropertiesTrainingEnvironmentProperties? TrainingEnvironment;
        public readonly ImmutableArray<Outputs.ModelCardTrainingMetric> TrainingMetrics;
        public readonly ImmutableArray<Outputs.ModelCardTrainingHyperParameter> UserProvidedHyperParameters;
        public readonly ImmutableArray<Outputs.ModelCardTrainingMetric> UserProvidedTrainingMetrics;

        [OutputConstructor]
        private ModelCardTrainingDetailsTrainingJobDetailsProperties(
            ImmutableArray<Outputs.ModelCardTrainingHyperParameter> hyperParameters,

            string? trainingArn,

            ImmutableArray<string> trainingDatasets,

            Outputs.ModelCardTrainingDetailsTrainingJobDetailsPropertiesTrainingEnvironmentProperties? trainingEnvironment,

            ImmutableArray<Outputs.ModelCardTrainingMetric> trainingMetrics,

            ImmutableArray<Outputs.ModelCardTrainingHyperParameter> userProvidedHyperParameters,

            ImmutableArray<Outputs.ModelCardTrainingMetric> userProvidedTrainingMetrics)
        {
            HyperParameters = hyperParameters;
            TrainingArn = trainingArn;
            TrainingDatasets = trainingDatasets;
            TrainingEnvironment = trainingEnvironment;
            TrainingMetrics = trainingMetrics;
            UserProvidedHyperParameters = userProvidedHyperParameters;
            UserProvidedTrainingMetrics = userProvidedTrainingMetrics;
        }
    }
}
