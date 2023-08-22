// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Emr.Inputs
{

    public sealed class ClusterVolumeSpecificationArgs : global::Pulumi.ResourceArgs
    {
        [Input("iops")]
        public Input<int>? Iops { get; set; }

        [Input("sizeInGb", required: true)]
        public Input<int> SizeInGb { get; set; } = null!;

        [Input("throughput")]
        public Input<int>? Throughput { get; set; }

        [Input("volumeType", required: true)]
        public Input<string> VolumeType { get; set; } = null!;

        public ClusterVolumeSpecificationArgs()
        {
        }
        public static new ClusterVolumeSpecificationArgs Empty => new ClusterVolumeSpecificationArgs();
    }
}
