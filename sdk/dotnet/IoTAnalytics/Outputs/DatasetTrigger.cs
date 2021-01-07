// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.IoTAnalytics.Outputs
{

    [OutputType]
    public sealed class DatasetTrigger
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger.html#cfn-iotanalytics-dataset-trigger-schedule
        /// </summary>
        public readonly Outputs.DatasetSchedule? Schedule;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger.html#cfn-iotanalytics-dataset-trigger-triggeringdataset
        /// </summary>
        public readonly Outputs.DatasetTriggeringDataset? TriggeringDataset;

        [OutputConstructor]
        private DatasetTrigger(
            Outputs.DatasetSchedule? Schedule,

            Outputs.DatasetTriggeringDataset? TriggeringDataset)
        {
            this.Schedule = Schedule;
            this.TriggeringDataset = TriggeringDataset;
        }
    }
}