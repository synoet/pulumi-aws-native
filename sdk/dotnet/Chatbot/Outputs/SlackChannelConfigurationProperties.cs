// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Chatbot.Outputs
{

    [OutputType]
    public sealed class SlackChannelConfigurationProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-configurationname
        /// </summary>
        public readonly string ConfigurationName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-iamrolearn
        /// </summary>
        public readonly string IamRoleArn;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-logginglevel
        /// </summary>
        public readonly string? LoggingLevel;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-slackchannelid
        /// </summary>
        public readonly string SlackChannelId;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-slackworkspaceid
        /// </summary>
        public readonly string SlackWorkspaceId;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-snstopicarns
        /// </summary>
        public readonly ImmutableArray<string> SnsTopicArns;

        [OutputConstructor]
        private SlackChannelConfigurationProperties(
            string ConfigurationName,

            string IamRoleArn,

            string? LoggingLevel,

            string SlackChannelId,

            string SlackWorkspaceId,

            ImmutableArray<string> SnsTopicArns)
        {
            this.ConfigurationName = ConfigurationName;
            this.IamRoleArn = IamRoleArn;
            this.LoggingLevel = LoggingLevel;
            this.SlackChannelId = SlackChannelId;
            this.SlackWorkspaceId = SlackWorkspaceId;
            this.SnsTopicArns = SnsTopicArns;
        }
    }
}