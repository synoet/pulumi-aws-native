// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MSK.Inputs
{

    public sealed class ClusterLoggingInfoArgs : global::Pulumi.ResourceArgs
    {
        [Input("brokerLogs", required: true)]
        public Input<Inputs.ClusterBrokerLogsArgs> BrokerLogs { get; set; } = null!;

        public ClusterLoggingInfoArgs()
        {
        }
        public static new ClusterLoggingInfoArgs Empty => new ClusterLoggingInfoArgs();
    }
}
