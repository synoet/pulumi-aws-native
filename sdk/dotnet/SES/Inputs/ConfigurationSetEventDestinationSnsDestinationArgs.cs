// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SES.Inputs
{

    /// <summary>
    /// An object that contains SNS topic ARN associated event destination.
    /// </summary>
    public sealed class ConfigurationSetEventDestinationSnsDestinationArgs : global::Pulumi.ResourceArgs
    {
        [Input("topicArn", required: true)]
        public Input<string> TopicArn { get; set; } = null!;

        public ConfigurationSetEventDestinationSnsDestinationArgs()
        {
        }
        public static new ConfigurationSetEventDestinationSnsDestinationArgs Empty => new ConfigurationSetEventDestinationSnsDestinationArgs();
    }
}
