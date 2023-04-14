// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AutoScaling.Inputs
{

    public sealed class AutoScalingGroupMixedInstancesPolicyArgs : global::Pulumi.ResourceArgs
    {
        [Input("instancesDistribution")]
        public Input<Inputs.AutoScalingGroupInstancesDistributionArgs>? InstancesDistribution { get; set; }

        [Input("launchTemplate", required: true)]
        public Input<Inputs.AutoScalingGroupLaunchTemplateArgs> LaunchTemplate { get; set; } = null!;

        public AutoScalingGroupMixedInstancesPolicyArgs()
        {
        }
        public static new AutoScalingGroupMixedInstancesPolicyArgs Empty => new AutoScalingGroupMixedInstancesPolicyArgs();
    }
}
