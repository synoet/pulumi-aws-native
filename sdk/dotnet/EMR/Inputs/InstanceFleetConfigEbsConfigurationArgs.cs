// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.EMR.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ebsconfiguration.html
    /// </summary>
    public sealed class InstanceFleetConfigEbsConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("EbsBlockDeviceConfigs")]
        private InputList<Inputs.InstanceFleetConfigEbsBlockDeviceConfigArgs>? _EbsBlockDeviceConfigs;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ebsconfiguration.html#cfn-elasticmapreduce-instancefleetconfig-ebsconfiguration-ebsblockdeviceconfigs
        /// </summary>
        public InputList<Inputs.InstanceFleetConfigEbsBlockDeviceConfigArgs> EbsBlockDeviceConfigs
        {
            get => _EbsBlockDeviceConfigs ?? (_EbsBlockDeviceConfigs = new InputList<Inputs.InstanceFleetConfigEbsBlockDeviceConfigArgs>());
            set => _EbsBlockDeviceConfigs = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ebsconfiguration.html#cfn-elasticmapreduce-instancefleetconfig-ebsconfiguration-ebsoptimized
        /// </summary>
        [Input("EbsOptimized")]
        public Input<bool>? EbsOptimized { get; set; }

        public InstanceFleetConfigEbsConfigurationArgs()
        {
        }
    }
}