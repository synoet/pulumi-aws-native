// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Personalize.Inputs
{

    /// <summary>
    /// The configuration to use with the solution. When performAutoML is set to true, Amazon Personalize only evaluates the autoMLConfig section of the solution configuration.
    /// </summary>
    public sealed class SolutionConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Lists the hyperparameter names and ranges.
        /// </summary>
        [Input("algorithmHyperParameters")]
        public Input<object>? AlgorithmHyperParameters { get; set; }

        /// <summary>
        /// The AutoMLConfig object containing a list of recipes to search when AutoML is performed.
        /// </summary>
        [Input("autoMlConfig")]
        public Input<Inputs.SolutionConfigAutoMLConfigPropertiesArgs>? AutoMlConfig { get; set; }

        /// <summary>
        /// Only events with a value greater than or equal to this threshold are used for training a model.
        /// </summary>
        [Input("eventValueThreshold")]
        public Input<string>? EventValueThreshold { get; set; }

        /// <summary>
        /// Lists the feature transformation parameters.
        /// </summary>
        [Input("featureTransformationParameters")]
        public Input<object>? FeatureTransformationParameters { get; set; }

        /// <summary>
        /// Describes the properties for hyperparameter optimization (HPO)
        /// </summary>
        [Input("hpoConfig")]
        public Input<Inputs.SolutionConfigHpoConfigPropertiesArgs>? HpoConfig { get; set; }

        public SolutionConfigArgs()
        {
        }
        public static new SolutionConfigArgs Empty => new SolutionConfigArgs();
    }
}
