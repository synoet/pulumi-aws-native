// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.SageMaker.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinputs.html
    /// </summary>
    public sealed class MonitoringScheduleMonitoringInputsArgs : Pulumi.ResourceArgs
    {
        [Input("MonitoringInputs")]
        private InputList<Inputs.MonitoringScheduleMonitoringInputArgs>? _MonitoringInputs;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinputs.html#cfn-sagemaker-monitoringschedule-monitoringinputs-monitoringinputs
        /// </summary>
        public InputList<Inputs.MonitoringScheduleMonitoringInputArgs> MonitoringInputs
        {
            get => _MonitoringInputs ?? (_MonitoringInputs = new InputList<Inputs.MonitoringScheduleMonitoringInputArgs>());
            set => _MonitoringInputs = value;
        }

        public MonitoringScheduleMonitoringInputsArgs()
        {
        }
    }
}