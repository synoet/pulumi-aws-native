# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'QuickConnectPhoneNumberQuickConnectConfigArgs',
    'QuickConnectQueueQuickConnectConfigArgs',
    'QuickConnectQuickConnectConfigArgs',
    'QuickConnectTagArgs',
    'QuickConnectUserQuickConnectConfigArgs',
]

@pulumi.input_type
class QuickConnectPhoneNumberQuickConnectConfigArgs:
    def __init__(__self__, *,
                 phone_number: pulumi.Input[str]):
        """
        The phone configuration. This is required only if QuickConnectType is PHONE_NUMBER.
        """
        pulumi.set(__self__, "phone_number", phone_number)

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[str]:
        return pulumi.get(self, "phone_number")

    @phone_number.setter
    def phone_number(self, value: pulumi.Input[str]):
        pulumi.set(self, "phone_number", value)


@pulumi.input_type
class QuickConnectQueueQuickConnectConfigArgs:
    def __init__(__self__, *,
                 contact_flow_arn: pulumi.Input[str],
                 queue_arn: pulumi.Input[str]):
        """
        The queue configuration. This is required only if QuickConnectType is QUEUE.
        """
        pulumi.set(__self__, "contact_flow_arn", contact_flow_arn)
        pulumi.set(__self__, "queue_arn", queue_arn)

    @property
    @pulumi.getter(name="contactFlowArn")
    def contact_flow_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "contact_flow_arn")

    @contact_flow_arn.setter
    def contact_flow_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "contact_flow_arn", value)

    @property
    @pulumi.getter(name="queueArn")
    def queue_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "queue_arn")

    @queue_arn.setter
    def queue_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "queue_arn", value)


@pulumi.input_type
class QuickConnectQuickConnectConfigArgs:
    def __init__(__self__, *,
                 quick_connect_type: pulumi.Input['QuickConnectQuickConnectType'],
                 phone_config: Optional[pulumi.Input['QuickConnectPhoneNumberQuickConnectConfigArgs']] = None,
                 queue_config: Optional[pulumi.Input['QuickConnectQueueQuickConnectConfigArgs']] = None,
                 user_config: Optional[pulumi.Input['QuickConnectUserQuickConnectConfigArgs']] = None):
        """
        Configuration settings for the quick connect.
        """
        pulumi.set(__self__, "quick_connect_type", quick_connect_type)
        if phone_config is not None:
            pulumi.set(__self__, "phone_config", phone_config)
        if queue_config is not None:
            pulumi.set(__self__, "queue_config", queue_config)
        if user_config is not None:
            pulumi.set(__self__, "user_config", user_config)

    @property
    @pulumi.getter(name="quickConnectType")
    def quick_connect_type(self) -> pulumi.Input['QuickConnectQuickConnectType']:
        return pulumi.get(self, "quick_connect_type")

    @quick_connect_type.setter
    def quick_connect_type(self, value: pulumi.Input['QuickConnectQuickConnectType']):
        pulumi.set(self, "quick_connect_type", value)

    @property
    @pulumi.getter(name="phoneConfig")
    def phone_config(self) -> Optional[pulumi.Input['QuickConnectPhoneNumberQuickConnectConfigArgs']]:
        return pulumi.get(self, "phone_config")

    @phone_config.setter
    def phone_config(self, value: Optional[pulumi.Input['QuickConnectPhoneNumberQuickConnectConfigArgs']]):
        pulumi.set(self, "phone_config", value)

    @property
    @pulumi.getter(name="queueConfig")
    def queue_config(self) -> Optional[pulumi.Input['QuickConnectQueueQuickConnectConfigArgs']]:
        return pulumi.get(self, "queue_config")

    @queue_config.setter
    def queue_config(self, value: Optional[pulumi.Input['QuickConnectQueueQuickConnectConfigArgs']]):
        pulumi.set(self, "queue_config", value)

    @property
    @pulumi.getter(name="userConfig")
    def user_config(self) -> Optional[pulumi.Input['QuickConnectUserQuickConnectConfigArgs']]:
        return pulumi.get(self, "user_config")

    @user_config.setter
    def user_config(self, value: Optional[pulumi.Input['QuickConnectUserQuickConnectConfigArgs']]):
        pulumi.set(self, "user_config", value)


@pulumi.input_type
class QuickConnectTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class QuickConnectUserQuickConnectConfigArgs:
    def __init__(__self__, *,
                 contact_flow_arn: pulumi.Input[str],
                 user_arn: pulumi.Input[str]):
        """
        The user configuration. This is required only if QuickConnectType is USER.
        """
        pulumi.set(__self__, "contact_flow_arn", contact_flow_arn)
        pulumi.set(__self__, "user_arn", user_arn)

    @property
    @pulumi.getter(name="contactFlowArn")
    def contact_flow_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "contact_flow_arn")

    @contact_flow_arn.setter
    def contact_flow_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "contact_flow_arn", value)

    @property
    @pulumi.getter(name="userArn")
    def user_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "user_arn")

    @user_arn.setter
    def user_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_arn", value)


