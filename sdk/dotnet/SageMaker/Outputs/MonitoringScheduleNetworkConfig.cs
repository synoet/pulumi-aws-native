// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.SageMaker.Outputs
{

    [OutputType]
    public sealed class MonitoringScheduleNetworkConfig
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html#cfn-sagemaker-monitoringschedule-networkconfig-enableintercontainertrafficencryption
        /// </summary>
        public readonly bool? EnableInterContainerTrafficEncryption;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html#cfn-sagemaker-monitoringschedule-networkconfig-enablenetworkisolation
        /// </summary>
        public readonly bool? EnableNetworkIsolation;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html#cfn-sagemaker-monitoringschedule-networkconfig-vpcconfig
        /// </summary>
        public readonly Outputs.MonitoringScheduleVpcConfig? VpcConfig;

        [OutputConstructor]
        private MonitoringScheduleNetworkConfig(
            bool? EnableInterContainerTrafficEncryption,

            bool? EnableNetworkIsolation,

            Outputs.MonitoringScheduleVpcConfig? VpcConfig)
        {
            this.EnableInterContainerTrafficEncryption = EnableInterContainerTrafficEncryption;
            this.EnableNetworkIsolation = EnableNetworkIsolation;
            this.VpcConfig = VpcConfig;
        }
    }
}