// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.SNS.Outputs
{

    [OutputType]
    public sealed class TopicSubscription
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-subscription.html#cfn-sns-topic-subscription-endpoint
        /// </summary>
        public readonly string Endpoint;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-subscription.html#cfn-sns-topic-subscription-protocol
        /// </summary>
        public readonly string Protocol;

        [OutputConstructor]
        private TopicSubscription(
            string Endpoint,

            string Protocol)
        {
            this.Endpoint = Endpoint;
            this.Protocol = Protocol;
        }
    }
}