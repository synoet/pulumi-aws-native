// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.GreengrassV2.Outputs
{

    [OutputType]
    public sealed class ComponentVersionLambdaEventSource
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaeventsource.html#cfn-greengrassv2-componentversion-lambdaeventsource-topic
        /// </summary>
        public readonly string? Topic;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaeventsource.html#cfn-greengrassv2-componentversion-lambdaeventsource-type
        /// </summary>
        public readonly string? Type;

        [OutputConstructor]
        private ComponentVersionLambdaEventSource(
            string? Topic,

            string? Type)
        {
            this.Topic = Topic;
            this.Type = Type;
        }
    }
}