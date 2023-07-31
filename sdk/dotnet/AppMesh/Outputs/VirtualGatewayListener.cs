// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppMesh.Outputs
{

    [OutputType]
    public sealed class VirtualGatewayListener
    {
        public readonly Outputs.VirtualGatewayConnectionPool? ConnectionPool;
        public readonly Outputs.VirtualGatewayHealthCheckPolicy? HealthCheck;
        public readonly Outputs.VirtualGatewayPortMapping PortMapping;
        public readonly Outputs.VirtualGatewayListenerTls? Tls;

        [OutputConstructor]
        private VirtualGatewayListener(
            Outputs.VirtualGatewayConnectionPool? connectionPool,

            Outputs.VirtualGatewayHealthCheckPolicy? healthCheck,

            Outputs.VirtualGatewayPortMapping portMapping,

            Outputs.VirtualGatewayListenerTls? tls)
        {
            ConnectionPool = connectionPool;
            HealthCheck = healthCheck;
            PortMapping = portMapping;
            Tls = tls;
        }
    }
}
