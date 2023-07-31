// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AutoScaling.Inputs
{

    public sealed class AutoScalingGroupLifecycleHookSpecificationArgs : global::Pulumi.ResourceArgs
    {
        [Input("defaultResult")]
        public Input<string>? DefaultResult { get; set; }

        [Input("heartbeatTimeout")]
        public Input<int>? HeartbeatTimeout { get; set; }

        [Input("lifecycleHookName", required: true)]
        public Input<string> LifecycleHookName { get; set; } = null!;

        [Input("lifecycleTransition", required: true)]
        public Input<string> LifecycleTransition { get; set; } = null!;

        [Input("notificationMetadata")]
        public Input<string>? NotificationMetadata { get; set; }

        [Input("notificationTargetArn")]
        public Input<string>? NotificationTargetArn { get; set; }

        [Input("roleArn")]
        public Input<string>? RoleArn { get; set; }

        public AutoScalingGroupLifecycleHookSpecificationArgs()
        {
        }
        public static new AutoScalingGroupLifecycleHookSpecificationArgs Empty => new AutoScalingGroupLifecycleHookSpecificationArgs();
    }
}
