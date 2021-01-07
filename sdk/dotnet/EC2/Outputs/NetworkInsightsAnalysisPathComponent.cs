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
    public sealed class NetworkInsightsAnalysisPathComponent
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-aclrule
        /// </summary>
        public readonly Outputs.NetworkInsightsAnalysisAnalysisAclRule? AclRule;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-component
        /// </summary>
        public readonly Outputs.NetworkInsightsAnalysisAnalysisComponent? Component;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-destinationvpc
        /// </summary>
        public readonly Outputs.NetworkInsightsAnalysisAnalysisComponent? DestinationVpc;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-inboundheader
        /// </summary>
        public readonly Outputs.NetworkInsightsAnalysisAnalysisPacketHeader? InboundHeader;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-outboundheader
        /// </summary>
        public readonly Outputs.NetworkInsightsAnalysisAnalysisPacketHeader? OutboundHeader;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-routetableroute
        /// </summary>
        public readonly Outputs.NetworkInsightsAnalysisAnalysisRouteTableRoute? RouteTableRoute;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-securitygrouprule
        /// </summary>
        public readonly Outputs.NetworkInsightsAnalysisAnalysisSecurityGroupRule? SecurityGroupRule;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-sequencenumber
        /// </summary>
        public readonly int? SequenceNumber;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-sourcevpc
        /// </summary>
        public readonly Outputs.NetworkInsightsAnalysisAnalysisComponent? SourceVpc;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-subnet
        /// </summary>
        public readonly Outputs.NetworkInsightsAnalysisAnalysisComponent? Subnet;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-vpc
        /// </summary>
        public readonly Outputs.NetworkInsightsAnalysisAnalysisComponent? Vpc;

        [OutputConstructor]
        private NetworkInsightsAnalysisPathComponent(
            Outputs.NetworkInsightsAnalysisAnalysisAclRule? AclRule,

            Outputs.NetworkInsightsAnalysisAnalysisComponent? Component,

            Outputs.NetworkInsightsAnalysisAnalysisComponent? DestinationVpc,

            Outputs.NetworkInsightsAnalysisAnalysisPacketHeader? InboundHeader,

            Outputs.NetworkInsightsAnalysisAnalysisPacketHeader? OutboundHeader,

            Outputs.NetworkInsightsAnalysisAnalysisRouteTableRoute? RouteTableRoute,

            Outputs.NetworkInsightsAnalysisAnalysisSecurityGroupRule? SecurityGroupRule,

            int? SequenceNumber,

            Outputs.NetworkInsightsAnalysisAnalysisComponent? SourceVpc,

            Outputs.NetworkInsightsAnalysisAnalysisComponent? Subnet,

            Outputs.NetworkInsightsAnalysisAnalysisComponent? Vpc)
        {
            this.AclRule = AclRule;
            this.Component = Component;
            this.DestinationVpc = DestinationVpc;
            this.InboundHeader = InboundHeader;
            this.OutboundHeader = OutboundHeader;
            this.RouteTableRoute = RouteTableRoute;
            this.SecurityGroupRule = SecurityGroupRule;
            this.SequenceNumber = SequenceNumber;
            this.SourceVpc = SourceVpc;
            this.Subnet = Subnet;
            this.Vpc = Vpc;
        }
    }
}