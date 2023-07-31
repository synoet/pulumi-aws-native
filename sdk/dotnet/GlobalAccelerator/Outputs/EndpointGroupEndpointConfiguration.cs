// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GlobalAccelerator.Outputs
{

    /// <summary>
    /// The configuration for a given endpoint
    /// </summary>
    [OutputType]
    public sealed class EndpointGroupEndpointConfiguration
    {
        /// <summary>
        /// true if client ip should be preserved
        /// </summary>
        public readonly bool? ClientIpPreservationEnabled;
        /// <summary>
        /// Id of the endpoint. For Network/Application Load Balancer this value is the ARN.  For EIP, this value is the allocation ID.  For EC2 instances, this is the EC2 instance ID
        /// </summary>
        public readonly string EndpointId;
        /// <summary>
        /// The weight for the endpoint.
        /// </summary>
        public readonly int? Weight;

        [OutputConstructor]
        private EndpointGroupEndpointConfiguration(
            bool? clientIpPreservationEnabled,

            string endpointId,

            int? weight)
        {
            ClientIpPreservationEnabled = clientIpPreservationEnabled;
            EndpointId = endpointId;
            Weight = weight;
        }
    }
}
