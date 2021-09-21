// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    /// <summary>
    /// Resource Type definition for AWS::EC2::VPCGatewayAttachment
    /// </summary>
    [Obsolete(@"VPCGatewayAttachment is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:ec2:VPCGatewayAttachment")]
    public partial class VPCGatewayAttachment : Pulumi.CustomResource
    {
        [Output("internetGatewayId")]
        public Output<string?> InternetGatewayId { get; private set; } = null!;

        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;

        [Output("vpnGatewayId")]
        public Output<string?> VpnGatewayId { get; private set; } = null!;


        /// <summary>
        /// Create a VPCGatewayAttachment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VPCGatewayAttachment(string name, VPCGatewayAttachmentArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:VPCGatewayAttachment", name, args ?? new VPCGatewayAttachmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VPCGatewayAttachment(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:VPCGatewayAttachment", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing VPCGatewayAttachment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VPCGatewayAttachment Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new VPCGatewayAttachment(name, id, options);
        }
    }

    public sealed class VPCGatewayAttachmentArgs : Pulumi.ResourceArgs
    {
        [Input("internetGatewayId")]
        public Input<string>? InternetGatewayId { get; set; }

        [Input("vpcId", required: true)]
        public Input<string> VpcId { get; set; } = null!;

        [Input("vpnGatewayId")]
        public Input<string>? VpnGatewayId { get; set; }

        public VPCGatewayAttachmentArgs()
        {
        }
    }
}
