// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisAnalyticsV2.Inputs
{

    public sealed class ApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionArgs : global::Pulumi.ResourceArgs
    {
        [Input("logStreamARN", required: true)]
        public Input<string> LogStreamARN { get; set; } = null!;

        public ApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionArgs()
        {
        }
        public static new ApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionArgs Empty => new ApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionArgs();
    }
}
