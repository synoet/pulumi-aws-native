// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    public sealed class EndpointConfigAsyncInferenceClientConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("maxConcurrentInvocationsPerInstance")]
        public Input<int>? MaxConcurrentInvocationsPerInstance { get; set; }

        public EndpointConfigAsyncInferenceClientConfigArgs()
        {
        }
        public static new EndpointConfigAsyncInferenceClientConfigArgs Empty => new EndpointConfigAsyncInferenceClientConfigArgs();
    }
}
