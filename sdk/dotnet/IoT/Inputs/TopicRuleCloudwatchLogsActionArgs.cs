// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT.Inputs
{

    public sealed class TopicRuleCloudwatchLogsActionArgs : global::Pulumi.ResourceArgs
    {
        [Input("batchMode")]
        public Input<bool>? BatchMode { get; set; }

        [Input("logGroupName", required: true)]
        public Input<string> LogGroupName { get; set; } = null!;

        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

        public TopicRuleCloudwatchLogsActionArgs()
        {
        }
        public static new TopicRuleCloudwatchLogsActionArgs Empty => new TopicRuleCloudwatchLogsActionArgs();
    }
}
