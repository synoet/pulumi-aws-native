// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RDS.Outputs
{

    [OutputType]
    public sealed class DBSecurityGroupIngress
    {
        public readonly string? Cidrip;
        public readonly string? Ec2SecurityGroupId;
        public readonly string? Ec2SecurityGroupName;
        public readonly string? Ec2SecurityGroupOwnerId;

        [OutputConstructor]
        private DBSecurityGroupIngress(
            string? cidrip,

            string? ec2SecurityGroupId,

            string? ec2SecurityGroupName,

            string? ec2SecurityGroupOwnerId)
        {
            Cidrip = cidrip;
            Ec2SecurityGroupId = ec2SecurityGroupId;
            Ec2SecurityGroupName = ec2SecurityGroupName;
            Ec2SecurityGroupOwnerId = ec2SecurityGroupOwnerId;
        }
    }
}
