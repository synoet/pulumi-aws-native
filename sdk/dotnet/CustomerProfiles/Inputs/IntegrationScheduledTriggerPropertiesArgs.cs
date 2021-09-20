// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CustomerProfiles.Inputs
{

    public sealed class IntegrationScheduledTriggerPropertiesArgs : Pulumi.ResourceArgs
    {
        [Input("dataPullMode")]
        public Input<Pulumi.AwsNative.CustomerProfiles.IntegrationScheduledTriggerPropertiesDataPullMode>? DataPullMode { get; set; }

        [Input("firstExecutionFrom")]
        public Input<double>? FirstExecutionFrom { get; set; }

        [Input("scheduleEndTime")]
        public Input<double>? ScheduleEndTime { get; set; }

        [Input("scheduleExpression", required: true)]
        public Input<string> ScheduleExpression { get; set; } = null!;

        [Input("scheduleOffset")]
        public Input<int>? ScheduleOffset { get; set; }

        [Input("scheduleStartTime")]
        public Input<double>? ScheduleStartTime { get; set; }

        [Input("timezone")]
        public Input<string>? Timezone { get; set; }

        public IntegrationScheduledTriggerPropertiesArgs()
        {
        }
    }
}
