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
    public sealed class AutoScalingGroupLifecycleHookSpecification
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-defaultresult
        /// </summary>
        public readonly string? DefaultResult;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-heartbeattimeout
        /// </summary>
        public readonly int? HeartbeatTimeout;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-lifecyclehookname
        /// </summary>
        public readonly string LifecycleHookName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-lifecycletransition
        /// </summary>
        public readonly string LifecycleTransition;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-notificationmetadata
        /// </summary>
        public readonly string? NotificationMetadata;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-notificationtargetarn
        /// </summary>
        public readonly string? NotificationTargetARN;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-rolearn
        /// </summary>
        public readonly string? RoleARN;

        [OutputConstructor]
        private AutoScalingGroupLifecycleHookSpecification(
            string? DefaultResult,

            int? HeartbeatTimeout,

            string LifecycleHookName,

            string LifecycleTransition,

            string? NotificationMetadata,

            string? NotificationTargetARN,

            string? RoleARN)
        {
            this.DefaultResult = DefaultResult;
            this.HeartbeatTimeout = HeartbeatTimeout;
            this.LifecycleHookName = LifecycleHookName;
            this.LifecycleTransition = LifecycleTransition;
            this.NotificationMetadata = NotificationMetadata;
            this.NotificationTargetARN = NotificationTargetARN;
            this.RoleARN = RoleARN;
        }
    }
}