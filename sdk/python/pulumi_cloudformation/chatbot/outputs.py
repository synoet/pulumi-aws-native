# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'SlackChannelConfigurationAttributes',
    'SlackChannelConfigurationProperties',
]

@pulumi.output_type
class SlackChannelConfigurationAttributes(dict):
    def __init__(__self__, *,
                 arn: str):
        pulumi.set(__self__, "arn", arn)

    @property
    @pulumi.getter(name="Arn")
    def arn(self) -> str:
        return pulumi.get(self, "arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SlackChannelConfigurationProperties(dict):
    """
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html
    """
    def __init__(__self__, *,
                 configuration_name: str,
                 iam_role_arn: str,
                 slack_channel_id: str,
                 slack_workspace_id: str,
                 logging_level: Optional[str] = None,
                 sns_topic_arns: Optional[Sequence[str]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html
        :param str configuration_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-configurationname
        :param str iam_role_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-iamrolearn
        :param str slack_channel_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-slackchannelid
        :param str slack_workspace_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-slackworkspaceid
        :param str logging_level: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-logginglevel
        :param Sequence[str] sns_topic_arns: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-snstopicarns
        """
        pulumi.set(__self__, "configuration_name", configuration_name)
        pulumi.set(__self__, "iam_role_arn", iam_role_arn)
        pulumi.set(__self__, "slack_channel_id", slack_channel_id)
        pulumi.set(__self__, "slack_workspace_id", slack_workspace_id)
        if logging_level is not None:
            pulumi.set(__self__, "logging_level", logging_level)
        if sns_topic_arns is not None:
            pulumi.set(__self__, "sns_topic_arns", sns_topic_arns)

    @property
    @pulumi.getter(name="ConfigurationName")
    def configuration_name(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-configurationname
        """
        return pulumi.get(self, "configuration_name")

    @property
    @pulumi.getter(name="IamRoleArn")
    def iam_role_arn(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-iamrolearn
        """
        return pulumi.get(self, "iam_role_arn")

    @property
    @pulumi.getter(name="SlackChannelId")
    def slack_channel_id(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-slackchannelid
        """
        return pulumi.get(self, "slack_channel_id")

    @property
    @pulumi.getter(name="SlackWorkspaceId")
    def slack_workspace_id(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-slackworkspaceid
        """
        return pulumi.get(self, "slack_workspace_id")

    @property
    @pulumi.getter(name="LoggingLevel")
    def logging_level(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-logginglevel
        """
        return pulumi.get(self, "logging_level")

    @property
    @pulumi.getter(name="SnsTopicArns")
    def sns_topic_arns(self) -> Optional[Sequence[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-snstopicarns
        """
        return pulumi.get(self, "sns_topic_arns")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


