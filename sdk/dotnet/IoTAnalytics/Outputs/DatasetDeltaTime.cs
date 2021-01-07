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
    public sealed class DatasetDeltaTime
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatime.html#cfn-iotanalytics-dataset-deltatime-offsetseconds
        /// </summary>
        public readonly int OffsetSeconds;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatime.html#cfn-iotanalytics-dataset-deltatime-timeexpression
        /// </summary>
        public readonly string TimeExpression;

        [OutputConstructor]
        private DatasetDeltaTime(
            int OffsetSeconds,

            string TimeExpression)
        {
            this.OffsetSeconds = OffsetSeconds;
            this.TimeExpression = TimeExpression;
        }
    }
}