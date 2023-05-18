// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2.Inputs
{

    public sealed class LaunchTemplateNetworkInterfaceArgs : global::Pulumi.ResourceArgs
    {
        [Input("associateCarrierIpAddress")]
        public Input<bool>? AssociateCarrierIpAddress { get; set; }

        [Input("associatePublicIpAddress")]
        public Input<bool>? AssociatePublicIpAddress { get; set; }

        [Input("deleteOnTermination")]
        public Input<bool>? DeleteOnTermination { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("deviceIndex")]
        public Input<int>? DeviceIndex { get; set; }

        [Input("groups")]
        private InputList<string>? _groups;
        public InputList<string> Groups
        {
            get => _groups ?? (_groups = new InputList<string>());
            set => _groups = value;
        }

        [Input("interfaceType")]
        public Input<string>? InterfaceType { get; set; }

        [Input("ipv4PrefixCount")]
        public Input<int>? Ipv4PrefixCount { get; set; }

        [Input("ipv4Prefixes")]
        private InputList<Inputs.LaunchTemplateIpv4PrefixSpecificationArgs>? _ipv4Prefixes;
        public InputList<Inputs.LaunchTemplateIpv4PrefixSpecificationArgs> Ipv4Prefixes
        {
            get => _ipv4Prefixes ?? (_ipv4Prefixes = new InputList<Inputs.LaunchTemplateIpv4PrefixSpecificationArgs>());
            set => _ipv4Prefixes = value;
        }

        [Input("ipv6AddressCount")]
        public Input<int>? Ipv6AddressCount { get; set; }

        [Input("ipv6Addresses")]
        private InputList<Inputs.LaunchTemplateIpv6AddArgs>? _ipv6Addresses;
        public InputList<Inputs.LaunchTemplateIpv6AddArgs> Ipv6Addresses
        {
            get => _ipv6Addresses ?? (_ipv6Addresses = new InputList<Inputs.LaunchTemplateIpv6AddArgs>());
            set => _ipv6Addresses = value;
        }

        [Input("ipv6PrefixCount")]
        public Input<int>? Ipv6PrefixCount { get; set; }

        [Input("ipv6Prefixes")]
        private InputList<Inputs.LaunchTemplateIpv6PrefixSpecificationArgs>? _ipv6Prefixes;
        public InputList<Inputs.LaunchTemplateIpv6PrefixSpecificationArgs> Ipv6Prefixes
        {
            get => _ipv6Prefixes ?? (_ipv6Prefixes = new InputList<Inputs.LaunchTemplateIpv6PrefixSpecificationArgs>());
            set => _ipv6Prefixes = value;
        }

        [Input("networkCardIndex")]
        public Input<int>? NetworkCardIndex { get; set; }

        [Input("networkInterfaceId")]
        public Input<string>? NetworkInterfaceId { get; set; }

        [Input("privateIpAddress")]
        public Input<string>? PrivateIpAddress { get; set; }

        [Input("privateIpAddresses")]
        private InputList<Inputs.LaunchTemplatePrivateIpAddArgs>? _privateIpAddresses;
        public InputList<Inputs.LaunchTemplatePrivateIpAddArgs> PrivateIpAddresses
        {
            get => _privateIpAddresses ?? (_privateIpAddresses = new InputList<Inputs.LaunchTemplatePrivateIpAddArgs>());
            set => _privateIpAddresses = value;
        }

        [Input("secondaryPrivateIpAddressCount")]
        public Input<int>? SecondaryPrivateIpAddressCount { get; set; }

        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        public LaunchTemplateNetworkInterfaceArgs()
        {
        }
        public static new LaunchTemplateNetworkInterfaceArgs Empty => new LaunchTemplateNetworkInterfaceArgs();
    }
}
