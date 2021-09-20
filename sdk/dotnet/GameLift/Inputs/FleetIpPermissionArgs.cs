// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GameLift.Inputs
{

    /// <summary>
    /// A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift hosting resource. New game sessions that are started on the fleet are assigned an IP address/port number combination, which must fall into the fleet's allowed ranges. For fleets created with a custom game server, the ranges reflect the server's game session assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two port ranges, one for TCP messaging and one for UDP, for use by the Realtime servers.
    /// </summary>
    public sealed class FleetIpPermissionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A starting value for a range of allowed port numbers.
        /// </summary>
        [Input("fromPort", required: true)]
        public Input<int> FromPort { get; set; } = null!;

        /// <summary>
        /// A range of allowed IP addresses. This value must be expressed in CIDR notation. Example: "000.000.000.000/[subnet mask]" or optionally the shortened version "0.0.0.0/[subnet mask]".
        /// </summary>
        [Input("ipRange", required: true)]
        public Input<string> IpRange { get; set; } = null!;

        /// <summary>
        /// The network communication protocol used by the fleet.
        /// </summary>
        [Input("protocol", required: true)]
        public Input<Pulumi.AwsNative.GameLift.FleetIpPermissionProtocol> Protocol { get; set; } = null!;

        /// <summary>
        /// An ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than FromPort.
        /// </summary>
        [Input("toPort", required: true)]
        public Input<int> ToPort { get; set; } = null!;

        public FleetIpPermissionArgs()
        {
        }
    }
}
