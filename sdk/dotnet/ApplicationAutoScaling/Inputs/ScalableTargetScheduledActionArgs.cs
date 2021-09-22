// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApplicationAutoScaling.Inputs
{

    public sealed class ScalableTargetScheduledActionArgs : Pulumi.ResourceArgs
    {
        [Input("endTime")]
        public Input<string>? EndTime { get; set; }

        [Input("scalableTargetAction")]
        public Input<Inputs.ScalableTargetScalableTargetActionArgs>? ScalableTargetAction { get; set; }

        [Input("schedule", required: true)]
        public Input<string> Schedule { get; set; } = null!;

        [Input("scheduledActionName", required: true)]
        public Input<string> ScheduledActionName { get; set; } = null!;

        [Input("startTime")]
        public Input<string>? StartTime { get; set; }

        [Input("timezone")]
        public Input<string>? Timezone { get; set; }

        public ScalableTargetScheduledActionArgs()
        {
        }
    }
}
