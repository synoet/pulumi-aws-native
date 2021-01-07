// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.EC2.Outputs
{

    [OutputType]
    public sealed class InstanceInstanceIpv6Address
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-instanceipv6address.html#cfn-ec2-instance-instanceipv6address-ipv6address
        /// </summary>
        public readonly string Ipv6Address;

        [OutputConstructor]
        private InstanceInstanceIpv6Address(string Ipv6Address)
        {
            this.Ipv6Address = Ipv6Address;
        }
    }
}