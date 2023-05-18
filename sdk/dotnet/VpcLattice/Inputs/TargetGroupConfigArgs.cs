// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.VpcLattice.Inputs
{

    public sealed class TargetGroupConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("healthCheck")]
        public Input<Inputs.TargetGroupHealthCheckConfigArgs>? HealthCheck { get; set; }

        [Input("ipAddressType")]
        public Input<Pulumi.AwsNative.VpcLattice.TargetGroupConfigIpAddressType>? IpAddressType { get; set; }

        [Input("port", required: true)]
        public Input<int> Port { get; set; } = null!;

        [Input("protocol", required: true)]
        public Input<Pulumi.AwsNative.VpcLattice.TargetGroupConfigProtocol> Protocol { get; set; } = null!;

        [Input("protocolVersion")]
        public Input<Pulumi.AwsNative.VpcLattice.TargetGroupConfigProtocolVersion>? ProtocolVersion { get; set; }

        [Input("vpcIdentifier", required: true)]
        public Input<string> VpcIdentifier { get; set; } = null!;

        public TargetGroupConfigArgs()
        {
        }
        public static new TargetGroupConfigArgs Empty => new TargetGroupConfigArgs();
    }
}
