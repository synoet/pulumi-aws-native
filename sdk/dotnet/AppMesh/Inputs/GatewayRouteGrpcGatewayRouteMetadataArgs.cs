// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppMesh.Inputs
{

    public sealed class GatewayRouteGrpcGatewayRouteMetadataArgs : global::Pulumi.ResourceArgs
    {
        [Input("invert")]
        public Input<bool>? Invert { get; set; }

        [Input("match")]
        public Input<Inputs.GatewayRouteMetadataMatchArgs>? Match { get; set; }

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GatewayRouteGrpcGatewayRouteMetadataArgs()
        {
        }
        public static new GatewayRouteGrpcGatewayRouteMetadataArgs Empty => new GatewayRouteGrpcGatewayRouteMetadataArgs();
    }
}
