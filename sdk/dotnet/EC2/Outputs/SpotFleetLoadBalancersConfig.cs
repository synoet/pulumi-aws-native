// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.EC2.Outputs
{

    [OutputType]
    public sealed class SpotFleetLoadBalancersConfig
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-loadbalancersconfig.html#cfn-ec2-spotfleet-loadbalancersconfig-classicloadbalancersconfig
        /// </summary>
        public readonly Outputs.SpotFleetClassicLoadBalancersConfig? ClassicLoadBalancersConfig;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-loadbalancersconfig.html#cfn-ec2-spotfleet-loadbalancersconfig-targetgroupsconfig
        /// </summary>
        public readonly Outputs.SpotFleetTargetGroupsConfig? TargetGroupsConfig;

        [OutputConstructor]
        private SpotFleetLoadBalancersConfig(
            Outputs.SpotFleetClassicLoadBalancersConfig? ClassicLoadBalancersConfig,

            Outputs.SpotFleetTargetGroupsConfig? TargetGroupsConfig)
        {
            this.ClassicLoadBalancersConfig = ClassicLoadBalancersConfig;
            this.TargetGroupsConfig = TargetGroupsConfig;
        }
    }
}