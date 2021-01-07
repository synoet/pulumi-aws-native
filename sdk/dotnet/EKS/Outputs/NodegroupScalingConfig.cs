// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.EKS.Outputs
{

    [OutputType]
    public sealed class NodegroupScalingConfig
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html#cfn-eks-nodegroup-scalingconfig-desiredsize
        /// </summary>
        public readonly double? DesiredSize;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html#cfn-eks-nodegroup-scalingconfig-maxsize
        /// </summary>
        public readonly double? MaxSize;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html#cfn-eks-nodegroup-scalingconfig-minsize
        /// </summary>
        public readonly double? MinSize;

        [OutputConstructor]
        private NodegroupScalingConfig(
            double? DesiredSize,

            double? MaxSize,

            double? MinSize)
        {
            this.DesiredSize = DesiredSize;
            this.MaxSize = MaxSize;
            this.MinSize = MinSize;
        }
    }
}