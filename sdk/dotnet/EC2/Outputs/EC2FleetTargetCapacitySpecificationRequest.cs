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
    public sealed class EC2FleetTargetCapacitySpecificationRequest
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html#cfn-ec2-ec2fleet-targetcapacityspecificationrequest-defaulttargetcapacitytype
        /// </summary>
        public readonly string? DefaultTargetCapacityType;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html#cfn-ec2-ec2fleet-targetcapacityspecificationrequest-ondemandtargetcapacity
        /// </summary>
        public readonly int? OnDemandTargetCapacity;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html#cfn-ec2-ec2fleet-targetcapacityspecificationrequest-spottargetcapacity
        /// </summary>
        public readonly int? SpotTargetCapacity;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html#cfn-ec2-ec2fleet-targetcapacityspecificationrequest-totaltargetcapacity
        /// </summary>
        public readonly int TotalTargetCapacity;

        [OutputConstructor]
        private EC2FleetTargetCapacitySpecificationRequest(
            string? DefaultTargetCapacityType,

            int? OnDemandTargetCapacity,

            int? SpotTargetCapacity,

            int TotalTargetCapacity)
        {
            this.DefaultTargetCapacityType = DefaultTargetCapacityType;
            this.OnDemandTargetCapacity = OnDemandTargetCapacity;
            this.SpotTargetCapacity = SpotTargetCapacity;
            this.TotalTargetCapacity = TotalTargetCapacity;
        }
    }
}