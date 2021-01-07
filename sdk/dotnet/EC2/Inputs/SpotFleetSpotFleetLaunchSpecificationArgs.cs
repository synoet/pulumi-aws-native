// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.EC2.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html
    /// </summary>
    public sealed class SpotFleetSpotFleetLaunchSpecificationArgs : Pulumi.ResourceArgs
    {
        [Input("BlockDeviceMappings")]
        private InputList<Inputs.SpotFleetBlockDeviceMappingArgs>? _BlockDeviceMappings;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-blockdevicemappings
        /// </summary>
        public InputList<Inputs.SpotFleetBlockDeviceMappingArgs> BlockDeviceMappings
        {
            get => _BlockDeviceMappings ?? (_BlockDeviceMappings = new InputList<Inputs.SpotFleetBlockDeviceMappingArgs>());
            set => _BlockDeviceMappings = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-ebsoptimized
        /// </summary>
        [Input("EbsOptimized")]
        public Input<bool>? EbsOptimized { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-iaminstanceprofile
        /// </summary>
        [Input("IamInstanceProfile")]
        public Input<Inputs.SpotFleetIamInstanceProfileSpecificationArgs>? IamInstanceProfile { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-imageid
        /// </summary>
        [Input("ImageId", required: true)]
        public Input<string> ImageId { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-instancetype
        /// </summary>
        [Input("InstanceType", required: true)]
        public Input<string> InstanceType { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-kernelid
        /// </summary>
        [Input("KernelId")]
        public Input<string>? KernelId { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-keyname
        /// </summary>
        [Input("KeyName")]
        public Input<string>? KeyName { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-monitoring
        /// </summary>
        [Input("Monitoring")]
        public Input<Inputs.SpotFleetSpotFleetMonitoringArgs>? Monitoring { get; set; }

        [Input("NetworkInterfaces")]
        private InputList<Inputs.SpotFleetInstanceNetworkInterfaceSpecificationArgs>? _NetworkInterfaces;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-networkinterfaces
        /// </summary>
        public InputList<Inputs.SpotFleetInstanceNetworkInterfaceSpecificationArgs> NetworkInterfaces
        {
            get => _NetworkInterfaces ?? (_NetworkInterfaces = new InputList<Inputs.SpotFleetInstanceNetworkInterfaceSpecificationArgs>());
            set => _NetworkInterfaces = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-placement
        /// </summary>
        [Input("Placement")]
        public Input<Inputs.SpotFleetSpotPlacementArgs>? Placement { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-ramdiskid
        /// </summary>
        [Input("RamdiskId")]
        public Input<string>? RamdiskId { get; set; }

        [Input("SecurityGroups")]
        private InputList<Inputs.SpotFleetGroupIdentifierArgs>? _SecurityGroups;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-securitygroups
        /// </summary>
        public InputList<Inputs.SpotFleetGroupIdentifierArgs> SecurityGroups
        {
            get => _SecurityGroups ?? (_SecurityGroups = new InputList<Inputs.SpotFleetGroupIdentifierArgs>());
            set => _SecurityGroups = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-spotprice
        /// </summary>
        [Input("SpotPrice")]
        public Input<string>? SpotPrice { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-subnetid
        /// </summary>
        [Input("SubnetId")]
        public Input<string>? SubnetId { get; set; }

        [Input("TagSpecifications")]
        private InputList<Inputs.SpotFleetSpotFleetTagSpecificationArgs>? _TagSpecifications;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-tagspecifications
        /// </summary>
        public InputList<Inputs.SpotFleetSpotFleetTagSpecificationArgs> TagSpecifications
        {
            get => _TagSpecifications ?? (_TagSpecifications = new InputList<Inputs.SpotFleetSpotFleetTagSpecificationArgs>());
            set => _TagSpecifications = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-userdata
        /// </summary>
        [Input("UserData")]
        public Input<string>? UserData { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-weightedcapacity
        /// </summary>
        [Input("WeightedCapacity")]
        public Input<double>? WeightedCapacity { get; set; }

        public SpotFleetSpotFleetLaunchSpecificationArgs()
        {
        }
    }
}