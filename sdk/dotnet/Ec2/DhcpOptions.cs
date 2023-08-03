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
    /// Resource Type definition for AWS::EC2::DHCPOptions
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:DhcpOptions")]
    public partial class DhcpOptions : global::Pulumi.CustomResource
    {
        [Output("dhcpOptionsId")]
        public Output<string> DhcpOptionsId { get; private set; } = null!;

        /// <summary>
        /// This value is used to complete unqualified DNS hostnames.
        /// </summary>
        [Output("domainName")]
        public Output<string?> DomainName { get; private set; } = null!;

        /// <summary>
        /// The IPv4 addresses of up to four domain name servers, or AmazonProvidedDNS.
        /// </summary>
        [Output("domainNameServers")]
        public Output<ImmutableArray<string>> DomainNameServers { get; private set; } = null!;

        /// <summary>
        /// The IPv4 addresses of up to four NetBIOS name servers.
        /// </summary>
        [Output("netbiosNameServers")]
        public Output<ImmutableArray<string>> NetbiosNameServers { get; private set; } = null!;

        /// <summary>
        /// The NetBIOS node type (1, 2, 4, or 8).
        /// </summary>
        [Output("netbiosNodeType")]
        public Output<int?> NetbiosNodeType { get; private set; } = null!;

        /// <summary>
        /// The IPv4 addresses of up to four Network Time Protocol (NTP) servers.
        /// </summary>
        [Output("ntpServers")]
        public Output<ImmutableArray<string>> NtpServers { get; private set; } = null!;

        /// <summary>
        /// Any tags assigned to the DHCP options set.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.DhcpOptionsTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a DhcpOptions resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DhcpOptions(string name, DhcpOptionsArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:ec2:DhcpOptions", name, args ?? new DhcpOptionsArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DhcpOptions(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:DhcpOptions", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing DhcpOptions resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DhcpOptions Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DhcpOptions(name, id, options);
        }
    }

    public sealed class DhcpOptionsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// This value is used to complete unqualified DNS hostnames.
        /// </summary>
        [Input("domainName")]
        public Input<string>? DomainName { get; set; }

        [Input("domainNameServers")]
        private InputList<string>? _domainNameServers;

        /// <summary>
        /// The IPv4 addresses of up to four domain name servers, or AmazonProvidedDNS.
        /// </summary>
        public InputList<string> DomainNameServers
        {
            get => _domainNameServers ?? (_domainNameServers = new InputList<string>());
            set => _domainNameServers = value;
        }

        [Input("netbiosNameServers")]
        private InputList<string>? _netbiosNameServers;

        /// <summary>
        /// The IPv4 addresses of up to four NetBIOS name servers.
        /// </summary>
        public InputList<string> NetbiosNameServers
        {
            get => _netbiosNameServers ?? (_netbiosNameServers = new InputList<string>());
            set => _netbiosNameServers = value;
        }

        /// <summary>
        /// The NetBIOS node type (1, 2, 4, or 8).
        /// </summary>
        [Input("netbiosNodeType")]
        public Input<int>? NetbiosNodeType { get; set; }

        [Input("ntpServers")]
        private InputList<string>? _ntpServers;

        /// <summary>
        /// The IPv4 addresses of up to four Network Time Protocol (NTP) servers.
        /// </summary>
        public InputList<string> NtpServers
        {
            get => _ntpServers ?? (_ntpServers = new InputList<string>());
            set => _ntpServers = value;
        }

        [Input("tags")]
        private InputList<Inputs.DhcpOptionsTagArgs>? _tags;

        /// <summary>
        /// Any tags assigned to the DHCP options set.
        /// </summary>
        public InputList<Inputs.DhcpOptionsTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.DhcpOptionsTagArgs>());
            set => _tags = value;
        }

        public DhcpOptionsArgs()
        {
        }
        public static new DhcpOptionsArgs Empty => new DhcpOptionsArgs();
    }
}
