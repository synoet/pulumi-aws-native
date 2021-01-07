// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.EKS.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html
    /// </summary>
    public sealed class NodegroupScalingConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html#cfn-eks-nodegroup-scalingconfig-desiredsize
        /// </summary>
        [Input("DesiredSize")]
        public Input<double>? DesiredSize { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html#cfn-eks-nodegroup-scalingconfig-maxsize
        /// </summary>
        [Input("MaxSize")]
        public Input<double>? MaxSize { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html#cfn-eks-nodegroup-scalingconfig-minsize
        /// </summary>
        [Input("MinSize")]
        public Input<double>? MinSize { get; set; }

        public NodegroupScalingConfigArgs()
        {
        }
    }
}