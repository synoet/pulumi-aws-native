// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    /// <summary>
    /// Resource Type definition for AWS::EC2::VPNConnectionRoute
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:VpnConnectionRoute")]
    public partial class VpnConnectionRoute : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The CIDR block associated with the local subnet of the customer network.
        /// </summary>
        [Output("destinationCidrBlock")]
        public Output<string> DestinationCidrBlock { get; private set; } = null!;

        /// <summary>
        /// The ID of the VPN connection.
        /// </summary>
        [Output("vpnConnectionId")]
        public Output<string> VpnConnectionId { get; private set; } = null!;


        /// <summary>
        /// Create a VpnConnectionRoute resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VpnConnectionRoute(string name, VpnConnectionRouteArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:VpnConnectionRoute", name, args ?? new VpnConnectionRouteArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VpnConnectionRoute(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:VpnConnectionRoute", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing VpnConnectionRoute resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VpnConnectionRoute Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new VpnConnectionRoute(name, id, options);
        }
    }

    public sealed class VpnConnectionRouteArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The CIDR block associated with the local subnet of the customer network.
        /// </summary>
        [Input("destinationCidrBlock", required: true)]
        public Input<string> DestinationCidrBlock { get; set; } = null!;

        /// <summary>
        /// The ID of the VPN connection.
        /// </summary>
        [Input("vpnConnectionId", required: true)]
        public Input<string> VpnConnectionId { get; set; } = null!;

        public VpnConnectionRouteArgs()
        {
        }
        public static new VpnConnectionRouteArgs Empty => new VpnConnectionRouteArgs();
    }
}
