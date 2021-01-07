// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.MediaConvert.Outputs
{

    [OutputType]
    public sealed class JobTemplateHopDestination
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html#cfn-mediaconvert-jobtemplate-hopdestination-priority
        /// </summary>
        public readonly int? Priority;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html#cfn-mediaconvert-jobtemplate-hopdestination-queue
        /// </summary>
        public readonly string? Queue;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html#cfn-mediaconvert-jobtemplate-hopdestination-waitminutes
        /// </summary>
        public readonly int? WaitMinutes;

        [OutputConstructor]
        private JobTemplateHopDestination(
            int? Priority,

            string? Queue,

            int? WaitMinutes)
        {
            this.Priority = Priority;
            this.Queue = Queue;
            this.WaitMinutes = WaitMinutes;
        }
    }
}