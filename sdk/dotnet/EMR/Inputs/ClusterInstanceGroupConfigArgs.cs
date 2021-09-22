// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EMR.Inputs
{

    public sealed class ClusterInstanceGroupConfigArgs : Pulumi.ResourceArgs
    {
        [Input("autoScalingPolicy")]
        public Input<Inputs.ClusterAutoScalingPolicyArgs>? AutoScalingPolicy { get; set; }

        [Input("bidPrice")]
        public Input<string>? BidPrice { get; set; }

        [Input("configurations")]
        private InputList<Inputs.ClusterConfigurationArgs>? _configurations;
        public InputList<Inputs.ClusterConfigurationArgs> Configurations
        {
            get => _configurations ?? (_configurations = new InputList<Inputs.ClusterConfigurationArgs>());
            set => _configurations = value;
        }

        [Input("ebsConfiguration")]
        public Input<Inputs.ClusterEbsConfigurationArgs>? EbsConfiguration { get; set; }

        [Input("instanceCount", required: true)]
        public Input<int> InstanceCount { get; set; } = null!;

        [Input("instanceType", required: true)]
        public Input<string> InstanceType { get; set; } = null!;

        [Input("market")]
        public Input<string>? Market { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        public ClusterInstanceGroupConfigArgs()
        {
        }
    }
}
