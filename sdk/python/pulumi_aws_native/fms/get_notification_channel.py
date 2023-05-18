# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetNotificationChannelResult',
    'AwaitableGetNotificationChannelResult',
    'get_notification_channel',
    'get_notification_channel_output',
]

@pulumi.output_type
class GetNotificationChannelResult:
    def __init__(__self__, sns_role_name=None, sns_topic_arn=None):
        if sns_role_name and not isinstance(sns_role_name, str):
            raise TypeError("Expected argument 'sns_role_name' to be a str")
        pulumi.set(__self__, "sns_role_name", sns_role_name)
        if sns_topic_arn and not isinstance(sns_topic_arn, str):
            raise TypeError("Expected argument 'sns_topic_arn' to be a str")
        pulumi.set(__self__, "sns_topic_arn", sns_topic_arn)

    @property
    @pulumi.getter(name="snsRoleName")
    def sns_role_name(self) -> Optional[str]:
        return pulumi.get(self, "sns_role_name")

    @property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[str]:
        return pulumi.get(self, "sns_topic_arn")


class AwaitableGetNotificationChannelResult(GetNotificationChannelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNotificationChannelResult(
            sns_role_name=self.sns_role_name,
            sns_topic_arn=self.sns_topic_arn)


def get_notification_channel(sns_topic_arn: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNotificationChannelResult:
    """
    Designates the IAM role and Amazon Simple Notification Service (SNS) topic that AWS Firewall Manager uses to record SNS logs.
    """
    __args__ = dict()
    __args__['snsTopicArn'] = sns_topic_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:fms:getNotificationChannel', __args__, opts=opts, typ=GetNotificationChannelResult).value

    return AwaitableGetNotificationChannelResult(
        sns_role_name=__ret__.sns_role_name,
        sns_topic_arn=__ret__.sns_topic_arn)


@_utilities.lift_output_func(get_notification_channel)
def get_notification_channel_output(sns_topic_arn: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNotificationChannelResult]:
    """
    Designates the IAM role and Amazon Simple Notification Service (SNS) topic that AWS Firewall Manager uses to record SNS logs.
    """
    ...
