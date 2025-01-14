// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Inputs
{

    /// <summary>
    /// Specifies an elastic inference accelerator.
    /// </summary>
    public sealed class LaunchTemplateElasticInferenceAcceleratorArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The number of elastic inference accelerators to attach to the instance.
        /// </summary>
        [Input("count")]
        public Input<int>? Count { get; set; }

        /// <summary>
        /// The type of elastic inference accelerator.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public LaunchTemplateElasticInferenceAcceleratorArgs()
        {
        }
        public static new LaunchTemplateElasticInferenceAcceleratorArgs Empty => new LaunchTemplateElasticInferenceAcceleratorArgs();
    }
}
