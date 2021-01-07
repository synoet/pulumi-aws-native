// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.AutoScaling.Outputs
{

    [OutputType]
    public sealed class AutoScalingGroupLaunchTemplateOverrides
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-mixedinstancespolicy-launchtemplateoverrides.html#cfn-autoscaling-autoscalinggroup-launchtemplateoverrides-instancetype
        /// </summary>
        public readonly string? InstanceType;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-mixedinstancespolicy-launchtemplateoverrides.html#cfn-autoscaling-autoscalinggroup-launchtemplateoverrides-launchtemplatespecification
        /// </summary>
        public readonly Outputs.AutoScalingGroupLaunchTemplateSpecification? LaunchTemplateSpecification;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-mixedinstancespolicy-launchtemplateoverrides.html#cfn-autoscaling-autoscalinggroup-launchtemplateoverrides-weightedcapacity
        /// </summary>
        public readonly string? WeightedCapacity;

        [OutputConstructor]
        private AutoScalingGroupLaunchTemplateOverrides(
            string? InstanceType,

            Outputs.AutoScalingGroupLaunchTemplateSpecification? LaunchTemplateSpecification,

            string? WeightedCapacity)
        {
            this.InstanceType = InstanceType;
            this.LaunchTemplateSpecification = LaunchTemplateSpecification;
            this.WeightedCapacity = WeightedCapacity;
        }
    }
}