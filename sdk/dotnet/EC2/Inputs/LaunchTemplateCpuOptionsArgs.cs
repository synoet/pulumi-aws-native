// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2.Inputs
{

    public sealed class LaunchTemplateCpuOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("coreCount")]
        public Input<int>? CoreCount { get; set; }

        [Input("threadsPerCore")]
        public Input<int>? ThreadsPerCore { get; set; }

        public LaunchTemplateCpuOptionsArgs()
        {
        }
        public static new LaunchTemplateCpuOptionsArgs Empty => new LaunchTemplateCpuOptionsArgs();
    }
}
