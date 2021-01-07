// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.KinesisAnalytics.Outputs
{

    [OutputType]
    public sealed class ApplicationInputLambdaProcessor
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html#cfn-kinesisanalytics-application-inputlambdaprocessor-resourcearn
        /// </summary>
        public readonly string ResourceARN;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html#cfn-kinesisanalytics-application-inputlambdaprocessor-rolearn
        /// </summary>
        public readonly string RoleARN;

        [OutputConstructor]
        private ApplicationInputLambdaProcessor(
            string ResourceARN,

            string RoleARN)
        {
            this.ResourceARN = ResourceARN;
            this.RoleARN = RoleARN;
        }
    }
}