// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.ApplicationAutoScaling.Outputs
{

    [OutputType]
    public sealed class ScalableTargetScalableTargetAction
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-maxcapacity
        /// </summary>
        public readonly int? MaxCapacity;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-mincapacity
        /// </summary>
        public readonly int? MinCapacity;

        [OutputConstructor]
        private ScalableTargetScalableTargetAction(
            int? MaxCapacity,

            int? MinCapacity)
        {
            this.MaxCapacity = MaxCapacity;
            this.MinCapacity = MinCapacity;
        }
    }
}