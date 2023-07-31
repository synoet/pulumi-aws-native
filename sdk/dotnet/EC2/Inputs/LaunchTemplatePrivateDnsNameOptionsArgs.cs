// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2.Inputs
{

    /// <summary>
    /// Describes the options for instance hostnames.
    /// </summary>
    public sealed class LaunchTemplatePrivateDnsNameOptionsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates whether to respond to DNS queries for instance hostnames with DNS A records.
        /// </summary>
        [Input("enableResourceNameDnsARecord")]
        public Input<bool>? EnableResourceNameDnsARecord { get; set; }

        /// <summary>
        /// Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.
        /// </summary>
        [Input("enableResourceNameDnsAaaaRecord")]
        public Input<bool>? EnableResourceNameDnsAaaaRecord { get; set; }

        /// <summary>
        /// The type of hostname for EC2 instances.
        /// </summary>
        [Input("hostnameType")]
        public Input<string>? HostnameType { get; set; }

        public LaunchTemplatePrivateDnsNameOptionsArgs()
        {
        }
        public static new LaunchTemplatePrivateDnsNameOptionsArgs Empty => new LaunchTemplatePrivateDnsNameOptionsArgs();
    }
}
