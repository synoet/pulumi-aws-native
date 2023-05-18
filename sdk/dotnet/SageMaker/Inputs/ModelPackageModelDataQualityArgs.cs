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
    /// Metrics that measure the quality of the input data for a model.
    /// </summary>
    public sealed class ModelPackageModelDataQualityArgs : global::Pulumi.ResourceArgs
    {
        [Input("constraints")]
        public Input<Inputs.ModelPackageMetricsSourceArgs>? Constraints { get; set; }

        [Input("statistics")]
        public Input<Inputs.ModelPackageMetricsSourceArgs>? Statistics { get; set; }

        public ModelPackageModelDataQualityArgs()
        {
        }
        public static new ModelPackageModelDataQualityArgs Empty => new ModelPackageModelDataQualityArgs();
    }
}
