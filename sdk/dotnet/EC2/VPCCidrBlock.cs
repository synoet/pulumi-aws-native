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
    /// Resource Type definition for AWS::EC2::VPCCidrBlock
    /// </summary>
    [Obsolete(@"VPCCidrBlock is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:ec2:VPCCidrBlock")]
    public partial class VPCCidrBlock : Pulumi.CustomResource
    {
        [Output("amazonProvidedIpv6CidrBlock")]
        public Output<bool?> AmazonProvidedIpv6CidrBlock { get; private set; } = null!;

        [Output("cidrBlock")]
        public Output<string?> CidrBlock { get; private set; } = null!;

        [Output("ipv6CidrBlock")]
        public Output<string?> Ipv6CidrBlock { get; private set; } = null!;

        [Output("ipv6Pool")]
        public Output<string?> Ipv6Pool { get; private set; } = null!;

        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;


        /// <summary>
        /// Create a VPCCidrBlock resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VPCCidrBlock(string name, VPCCidrBlockArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:VPCCidrBlock", name, args ?? new VPCCidrBlockArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VPCCidrBlock(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:VPCCidrBlock", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing VPCCidrBlock resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VPCCidrBlock Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new VPCCidrBlock(name, id, options);
        }
    }

    public sealed class VPCCidrBlockArgs : Pulumi.ResourceArgs
    {
        [Input("amazonProvidedIpv6CidrBlock")]
        public Input<bool>? AmazonProvidedIpv6CidrBlock { get; set; }

        [Input("cidrBlock")]
        public Input<string>? CidrBlock { get; set; }

        [Input("ipv6CidrBlock")]
        public Input<string>? Ipv6CidrBlock { get; set; }

        [Input("ipv6Pool")]
        public Input<string>? Ipv6Pool { get; set; }

        [Input("vpcId", required: true)]
        public Input<string> VpcId { get; set; } = null!;

        public VPCCidrBlockArgs()
        {
        }
    }
}
