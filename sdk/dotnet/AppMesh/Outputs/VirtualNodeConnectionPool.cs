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
    public sealed class VirtualNodeConnectionPool
    {
        public readonly Outputs.VirtualNodeGrpcConnectionPool? Grpc;
        public readonly Outputs.VirtualNodeHttpConnectionPool? Http;
        public readonly Outputs.VirtualNodeHttp2ConnectionPool? Http2;
        public readonly Outputs.VirtualNodeTcpConnectionPool? Tcp;

        [OutputConstructor]
        private VirtualNodeConnectionPool(
            Outputs.VirtualNodeGrpcConnectionPool? grpc,

            Outputs.VirtualNodeHttpConnectionPool? http,

            Outputs.VirtualNodeHttp2ConnectionPool? http2,

            Outputs.VirtualNodeTcpConnectionPool? tcp)
        {
            Grpc = grpc;
            Http = http;
            Http2 = http2;
            Tcp = tcp;
        }
    }
}
