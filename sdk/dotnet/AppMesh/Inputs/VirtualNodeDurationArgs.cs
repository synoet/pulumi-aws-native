// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppMesh.Inputs
{

    public sealed class VirtualNodeDurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("unit", required: true)]
        public Input<string> Unit { get; set; } = null!;

        [Input("value", required: true)]
        public Input<int> Value { get; set; } = null!;

        public VirtualNodeDurationArgs()
        {
        }
        public static new VirtualNodeDurationArgs Empty => new VirtualNodeDurationArgs();
    }
}
