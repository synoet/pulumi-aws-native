// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GroundStation.Outputs
{

    /// <summary>
    /// Information about AwsGroundStationAgentEndpoint.
    /// </summary>
    [OutputType]
    public sealed class DataflowEndpointGroupAwsGroundStationAgentEndpoint
    {
        public readonly Pulumi.AwsNative.GroundStation.DataflowEndpointGroupAgentStatus? AgentStatus;
        public readonly Pulumi.AwsNative.GroundStation.DataflowEndpointGroupAuditResults? AuditResults;
        public readonly Outputs.DataflowEndpointGroupConnectionDetails? EgressAddress;
        public readonly Outputs.DataflowEndpointGroupRangedConnectionDetails? IngressAddress;
        public readonly string? Name;

        [OutputConstructor]
        private DataflowEndpointGroupAwsGroundStationAgentEndpoint(
            Pulumi.AwsNative.GroundStation.DataflowEndpointGroupAgentStatus? agentStatus,

            Pulumi.AwsNative.GroundStation.DataflowEndpointGroupAuditResults? auditResults,

            Outputs.DataflowEndpointGroupConnectionDetails? egressAddress,

            Outputs.DataflowEndpointGroupRangedConnectionDetails? ingressAddress,

            string? name)
        {
            AgentStatus = agentStatus;
            AuditResults = auditResults;
            EgressAddress = egressAddress;
            IngressAddress = ingressAddress;
            Name = name;
        }
    }
}
