// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT.Outputs
{

    [OutputType]
    public sealed class TopicRuleCloudwatchAlarmAction
    {
        public readonly string AlarmName;
        public readonly string RoleArn;
        public readonly string StateReason;
        public readonly string StateValue;

        [OutputConstructor]
        private TopicRuleCloudwatchAlarmAction(
            string alarmName,

            string roleArn,

            string stateReason,

            string stateValue)
        {
            AlarmName = alarmName;
            RoleArn = roleArn;
            StateReason = stateReason;
            StateValue = stateValue;
        }
    }
}
