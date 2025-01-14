// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Outputs
{

    /// <summary>
    /// Describes the options for instance hostnames.
    /// </summary>
    [OutputType]
    public sealed class LaunchTemplatePrivateDnsNameOptions
    {
        /// <summary>
        /// Indicates whether to respond to DNS queries for instance hostnames with DNS A records.
        /// </summary>
        public readonly bool? EnableResourceNameDnsARecord;
        /// <summary>
        /// Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.
        /// </summary>
        public readonly bool? EnableResourceNameDnsAaaaRecord;
        /// <summary>
        /// The type of hostname for EC2 instances.
        /// </summary>
        public readonly string? HostnameType;

        [OutputConstructor]
        private LaunchTemplatePrivateDnsNameOptions(
            bool? enableResourceNameDnsARecord,

            bool? enableResourceNameDnsAaaaRecord,

            string? hostnameType)
        {
            EnableResourceNameDnsARecord = enableResourceNameDnsARecord;
            EnableResourceNameDnsAaaaRecord = enableResourceNameDnsAaaaRecord;
            HostnameType = hostnameType;
        }
    }
}
