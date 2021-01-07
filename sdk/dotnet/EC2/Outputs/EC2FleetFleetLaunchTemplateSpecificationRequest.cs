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
    public sealed class EC2FleetFleetLaunchTemplateSpecificationRequest
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-launchtemplateid
        /// </summary>
        public readonly string? LaunchTemplateId;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-launchtemplatename
        /// </summary>
        public readonly string? LaunchTemplateName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-version
        /// </summary>
        public readonly string? Version;

        [OutputConstructor]
        private EC2FleetFleetLaunchTemplateSpecificationRequest(
            string? LaunchTemplateId,

            string? LaunchTemplateName,

            string? Version)
        {
            this.LaunchTemplateId = LaunchTemplateId;
            this.LaunchTemplateName = LaunchTemplateName;
            this.Version = Version;
        }
    }
}