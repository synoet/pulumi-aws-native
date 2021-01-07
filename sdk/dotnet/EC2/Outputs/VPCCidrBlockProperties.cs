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
    public sealed class VPCCidrBlockProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-amazonprovidedipv6cidrblock
        /// </summary>
        public readonly bool? AmazonProvidedIpv6CidrBlock;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-cidrblock
        /// </summary>
        public readonly string? CidrBlock;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-vpcid
        /// </summary>
        public readonly string VpcId;

        [OutputConstructor]
        private VPCCidrBlockProperties(
            bool? AmazonProvidedIpv6CidrBlock,

            string? CidrBlock,

            string VpcId)
        {
            this.AmazonProvidedIpv6CidrBlock = AmazonProvidedIpv6CidrBlock;
            this.CidrBlock = CidrBlock;
            this.VpcId = VpcId;
        }
    }
}