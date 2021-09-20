// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaConnect.Inputs
{

    /// <summary>
    /// The settings for the source of the flow.
    /// </summary>
    public sealed class FlowSourceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The type of encryption that is used on the content ingested from this source.
        /// </summary>
        [Input("decryption")]
        public Input<Inputs.FlowEncryptionArgs>? Decryption { get; set; }

        /// <summary>
        /// A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator's flow.
        /// </summary>
        [Input("entitlementArn")]
        public Input<string>? EntitlementArn { get; set; }

        /// <summary>
        /// The IP address that the flow will be listening on for incoming content.
        /// </summary>
        [Input("ingestIp")]
        public Input<string>? IngestIp { get; set; }

        /// <summary>
        /// The port that the flow will be listening on for incoming content.
        /// </summary>
        [Input("ingestPort")]
        public Input<int>? IngestPort { get; set; }

        /// <summary>
        /// The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
        /// </summary>
        [Input("maxBitrate")]
        public Input<int>? MaxBitrate { get; set; }

        /// <summary>
        /// The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
        /// </summary>
        [Input("maxLatency")]
        public Input<int>? MaxLatency { get; set; }

        /// <summary>
        /// The name of the source.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The protocol that is used by the source or output.
        /// </summary>
        [Input("protocol")]
        public Input<Pulumi.AwsNative.MediaConnect.FlowSourceProtocol>? Protocol { get; set; }

        /// <summary>
        /// The ARN of the source.
        /// </summary>
        [Input("sourceArn")]
        public Input<string>? SourceArn { get; set; }

        /// <summary>
        /// The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
        /// </summary>
        [Input("streamId")]
        public Input<string>? StreamId { get; set; }

        /// <summary>
        /// The name of the VPC Interface this Source is configured with.
        /// </summary>
        [Input("vpcInterfaceName")]
        public Input<string>? VpcInterfaceName { get; set; }

        /// <summary>
        /// The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
        /// </summary>
        [Input("whitelistCidr")]
        public Input<string>? WhitelistCidr { get; set; }

        public FlowSourceArgs()
        {
        }
    }
}
