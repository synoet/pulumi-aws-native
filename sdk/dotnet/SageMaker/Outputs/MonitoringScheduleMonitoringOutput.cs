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
    public sealed class MonitoringScheduleMonitoringOutput
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutput.html#cfn-sagemaker-monitoringschedule-monitoringoutput-s3output
        /// </summary>
        public readonly Outputs.MonitoringScheduleS3Output S3Output;

        [OutputConstructor]
        private MonitoringScheduleMonitoringOutput(Outputs.MonitoringScheduleS3Output S3Output)
        {
            this.S3Output = S3Output;
        }
    }
}