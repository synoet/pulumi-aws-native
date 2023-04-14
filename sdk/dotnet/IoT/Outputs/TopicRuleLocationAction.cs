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
    public sealed class TopicRuleLocationAction
    {
        public readonly string DeviceId;
        public readonly string Latitude;
        public readonly string Longitude;
        public readonly string RoleArn;
        public readonly Outputs.TopicRuleTimestamp? Timestamp;
        public readonly string TrackerName;

        [OutputConstructor]
        private TopicRuleLocationAction(
            string deviceId,

            string latitude,

            string longitude,

            string roleArn,

            Outputs.TopicRuleTimestamp? timestamp,

            string trackerName)
        {
            DeviceId = deviceId;
            Latitude = latitude;
            Longitude = longitude;
            RoleArn = roleArn;
            Timestamp = timestamp;
            TrackerName = trackerName;
        }
    }
}
