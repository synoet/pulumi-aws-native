// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DLM.Inputs
{

    public sealed class LifecyclePolicyEventSourceArgs : global::Pulumi.ResourceArgs
    {
        [Input("parameters")]
        public Input<Inputs.LifecyclePolicyEventParametersArgs>? Parameters { get; set; }

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public LifecyclePolicyEventSourceArgs()
        {
        }
        public static new LifecyclePolicyEventSourceArgs Empty => new LifecyclePolicyEventSourceArgs();
    }
}
