// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DataSync.Inputs
{

    /// <summary>
    /// HDFS Name Node IP and port information.
    /// </summary>
    public sealed class LocationHdfsNameNodeArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The DNS name or IP address of the Name Node in the customer's on premises HDFS cluster.
        /// </summary>
        [Input("hostname", required: true)]
        public Input<string> Hostname { get; set; } = null!;

        /// <summary>
        /// The port on which the Name Node is listening on for client requests.
        /// </summary>
        [Input("port", required: true)]
        public Input<int> Port { get; set; } = null!;

        public LocationHdfsNameNodeArgs()
        {
        }
        public static new LocationHdfsNameNodeArgs Empty => new LocationHdfsNameNodeArgs();
    }
}
