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
    'ApplicationTagsArgs',
    'ConfigurationProfileTagsArgs',
    'ConfigurationProfileValidatorsArgs',
    'DeploymentStrategyTagsArgs',
    'DeploymentTagsArgs',
    'EnvironmentMonitorArgs',
    'EnvironmentTagArgs',
    'ExtensionActionArgs',
    'ExtensionAssociationTagArgs',
    'ExtensionParameterArgs',
    'ExtensionTagArgs',
]

@pulumi.input_type
class ApplicationTagsArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        Metadata to assign to the application. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
        :param pulumi.Input[str] key: The key-value string map. The valid character set is [a-zA-Z1-9 +-=._:/-]. The tag key can be up to 128 characters and must not start with aws:.
        :param pulumi.Input[str] value: The tag value can be up to 256 characters.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key-value string map. The valid character set is [a-zA-Z1-9 +-=._:/-]. The tag key can be up to 128 characters and must not start with aws:.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The tag value can be up to 256 characters.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ConfigurationProfileTagsArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Metadata to assign to the configuration profile. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
        :param pulumi.Input[str] key: The key-value string map. The tag key can be up to 128 characters and must not start with aws:.
        :param pulumi.Input[str] value: The tag value can be up to 256 characters.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The key-value string map. The tag key can be up to 128 characters and must not start with aws:.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The tag value can be up to 256 characters.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ConfigurationProfileValidatorsArgs:
    def __init__(__self__, *,
                 content: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        A list of methods for validating the configuration.
        :param pulumi.Input[str] content: Either the JSON Schema content or the Amazon Resource Name (ARN) of an Lambda function.
        :param pulumi.Input[str] type: AWS AppConfig supports validators of type JSON_SCHEMA and LAMBDA.
        """
        if content is not None:
            pulumi.set(__self__, "content", content)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[str]]:
        """
        Either the JSON Schema content or the Amazon Resource Name (ARN) of an Lambda function.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        AWS AppConfig supports validators of type JSON_SCHEMA and LAMBDA.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class DeploymentStrategyTagsArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class DeploymentTagsArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class EnvironmentMonitorArgs:
    def __init__(__self__, *,
                 alarm_arn: pulumi.Input[str],
                 alarm_role_arn: Optional[pulumi.Input[str]] = None):
        """
        Amazon CloudWatch alarm to monitor during the deployment process.
        :param pulumi.Input[str] alarm_arn: Amazon Resource Name (ARN) of the Amazon CloudWatch alarm.
        :param pulumi.Input[str] alarm_role_arn: ARN of an AWS Identity and Access Management (IAM) role for AWS AppConfig to monitor AlarmArn.
        """
        pulumi.set(__self__, "alarm_arn", alarm_arn)
        if alarm_role_arn is not None:
            pulumi.set(__self__, "alarm_role_arn", alarm_role_arn)

    @property
    @pulumi.getter(name="alarmArn")
    def alarm_arn(self) -> pulumi.Input[str]:
        """
        Amazon Resource Name (ARN) of the Amazon CloudWatch alarm.
        """
        return pulumi.get(self, "alarm_arn")

    @alarm_arn.setter
    def alarm_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "alarm_arn", value)

    @property
    @pulumi.getter(name="alarmRoleArn")
    def alarm_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of an AWS Identity and Access Management (IAM) role for AWS AppConfig to monitor AlarmArn.
        """
        return pulumi.get(self, "alarm_role_arn")

    @alarm_role_arn.setter
    def alarm_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alarm_role_arn", value)


@pulumi.input_type
class EnvironmentTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        Metadata to assign to the environment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
        :param pulumi.Input[str] key: The key-value string map. The valid character set is [a-zA-Z1-9+-=._:/]. The tag key can be up to 128 characters and must not start with aws:.
        :param pulumi.Input[str] value: The tag value can be up to 256 characters.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key-value string map. The valid character set is [a-zA-Z1-9+-=._:/]. The tag key can be up to 128 characters and must not start with aws:.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The tag value can be up to 256 characters.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ExtensionActionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 uri: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None):
        """
        An action for an extension to take at a specific action point.
        :param pulumi.Input[str] name: The name of the extension action.
        :param pulumi.Input[str] uri: The URI of the extension action.
        :param pulumi.Input[str] description: The description of the extension Action.
        :param pulumi.Input[str] role_arn: The ARN of the role for invoking the extension action.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "uri", uri)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the extension action.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Input[str]:
        """
        The URI of the extension action.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "uri", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the extension Action.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the role for invoking the extension action.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_arn", value)


@pulumi.input_type
class ExtensionAssociationTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
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
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ExtensionParameterArgs:
    def __init__(__self__, *,
                 required: pulumi.Input[bool],
                 description: Optional[pulumi.Input[str]] = None):
        """
        A parameter for the extension to send to a specific action.
        :param pulumi.Input[str] description: The description of the extension Parameter.
        """
        pulumi.set(__self__, "required", required)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def required(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "required")

    @required.setter
    def required(self, value: pulumi.Input[bool]):
        pulumi.set(self, "required", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the extension Parameter.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class ExtensionTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
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
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


