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
    /// Resource Type definition for AWS::EC2::NetworkAclEntry
    /// </summary>
    [Obsolete(@"NetworkAclEntry is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:ec2:NetworkAclEntry")]
    public partial class NetworkAclEntry : Pulumi.CustomResource
    {
        [Output("cidrBlock")]
        public Output<string?> CidrBlock { get; private set; } = null!;

        [Output("egress")]
        public Output<bool?> Egress { get; private set; } = null!;

        [Output("icmp")]
        public Output<Outputs.NetworkAclEntryIcmp?> Icmp { get; private set; } = null!;

        [Output("ipv6CidrBlock")]
        public Output<string?> Ipv6CidrBlock { get; private set; } = null!;

        [Output("networkAclId")]
        public Output<string> NetworkAclId { get; private set; } = null!;

        [Output("portRange")]
        public Output<Outputs.NetworkAclEntryPortRange?> PortRange { get; private set; } = null!;

        [Output("protocol")]
        public Output<int> Protocol { get; private set; } = null!;

        [Output("ruleAction")]
        public Output<string> RuleAction { get; private set; } = null!;

        [Output("ruleNumber")]
        public Output<int> RuleNumber { get; private set; } = null!;


        /// <summary>
        /// Create a NetworkAclEntry resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NetworkAclEntry(string name, NetworkAclEntryArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:NetworkAclEntry", name, args ?? new NetworkAclEntryArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NetworkAclEntry(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:NetworkAclEntry", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing NetworkAclEntry resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NetworkAclEntry Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new NetworkAclEntry(name, id, options);
        }
    }

    public sealed class NetworkAclEntryArgs : Pulumi.ResourceArgs
    {
        [Input("cidrBlock")]
        public Input<string>? CidrBlock { get; set; }

        [Input("egress")]
        public Input<bool>? Egress { get; set; }

        [Input("icmp")]
        public Input<Inputs.NetworkAclEntryIcmpArgs>? Icmp { get; set; }

        [Input("ipv6CidrBlock")]
        public Input<string>? Ipv6CidrBlock { get; set; }

        [Input("networkAclId", required: true)]
        public Input<string> NetworkAclId { get; set; } = null!;

        [Input("portRange")]
        public Input<Inputs.NetworkAclEntryPortRangeArgs>? PortRange { get; set; }

        [Input("protocol", required: true)]
        public Input<int> Protocol { get; set; } = null!;

        [Input("ruleAction", required: true)]
        public Input<string> RuleAction { get; set; } = null!;

        [Input("ruleNumber", required: true)]
        public Input<int> RuleNumber { get; set; } = null!;

        public NetworkAclEntryArgs()
        {
        }
    }
}
