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
    /// Represents the drift check bias baselines that can be used when the model monitor is set using the model package.
    /// </summary>
    public sealed class ModelPackageDriftCheckBiasArgs : global::Pulumi.ResourceArgs
    {
        [Input("configFile")]
        public Input<Inputs.ModelPackageFileSourceArgs>? ConfigFile { get; set; }

        [Input("postTrainingConstraints")]
        public Input<Inputs.ModelPackageMetricsSourceArgs>? PostTrainingConstraints { get; set; }

        [Input("preTrainingConstraints")]
        public Input<Inputs.ModelPackageMetricsSourceArgs>? PreTrainingConstraints { get; set; }

        public ModelPackageDriftCheckBiasArgs()
        {
        }
        public static new ModelPackageDriftCheckBiasArgs Empty => new ModelPackageDriftCheckBiasArgs();
    }
}
