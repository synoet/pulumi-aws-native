// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ecs.Inputs
{

    /// <summary>
    /// The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.
    /// </summary>
    public sealed class ClusterTagArgs : global::Pulumi.ResourceArgs
    {
        [Input("key")]
        public Input<string>? Key { get; set; }

        [Input("value")]
        public Input<string>? Value { get; set; }

        public ClusterTagArgs()
        {
        }
        public static new ClusterTagArgs Empty => new ClusterTagArgs();
    }
}
