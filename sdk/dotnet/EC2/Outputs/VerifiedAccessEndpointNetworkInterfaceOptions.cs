// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2.Outputs
{

    /// <summary>
    /// The options for network-interface type endpoint.
    /// </summary>
    [OutputType]
    public sealed class VerifiedAccessEndpointNetworkInterfaceOptions
    {
        /// <summary>
        /// The ID of the network interface.
        /// </summary>
        public readonly string? NetworkInterfaceId;
        /// <summary>
        /// The IP port number.
        /// </summary>
        public readonly int? Port;
        /// <summary>
        /// The IP protocol.
        /// </summary>
        public readonly string? Protocol;

        [OutputConstructor]
        private VerifiedAccessEndpointNetworkInterfaceOptions(
            string? networkInterfaceId,

            int? port,

            string? protocol)
        {
            NetworkInterfaceId = networkInterfaceId;
            Port = port;
            Protocol = protocol;
        }
    }
}
