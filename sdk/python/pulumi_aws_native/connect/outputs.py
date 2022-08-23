# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'ConstraintsProperties',
    'ContactFlowModuleTag',
    'ContactFlowTag',
    'HoursOfOperationConfig',
    'HoursOfOperationTag',
    'HoursOfOperationTimeSlice',
    'InstanceAttributes',
    'PhoneNumberTag',
    'QuickConnectConfig',
    'QuickConnectPhoneNumberQuickConnectConfig',
    'QuickConnectQueueQuickConnectConfig',
    'QuickConnectTag',
    'QuickConnectUserQuickConnectConfig',
    'TaskTemplateDefaultFieldValue',
    'TaskTemplateField',
    'TaskTemplateFieldIdentifier',
    'TaskTemplateInvisibleFieldInfo',
    'TaskTemplateReadOnlyFieldInfo',
    'TaskTemplateRequiredFieldInfo',
    'TaskTemplateTag',
    'UserIdentityInfo',
    'UserPhoneConfig',
    'UserTag',
]

@pulumi.output_type
class ConstraintsProperties(dict):
    """
    The constraints for the task template
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "invisibleFields":
            suggest = "invisible_fields"
        elif key == "readOnlyFields":
            suggest = "read_only_fields"
        elif key == "requiredFields":
            suggest = "required_fields"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConstraintsProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConstraintsProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConstraintsProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 invisible_fields: Optional[Sequence['outputs.TaskTemplateInvisibleFieldInfo']] = None,
                 read_only_fields: Optional[Sequence['outputs.TaskTemplateReadOnlyFieldInfo']] = None,
                 required_fields: Optional[Sequence['outputs.TaskTemplateRequiredFieldInfo']] = None):
        """
        The constraints for the task template
        """
        if invisible_fields is not None:
            pulumi.set(__self__, "invisible_fields", invisible_fields)
        if read_only_fields is not None:
            pulumi.set(__self__, "read_only_fields", read_only_fields)
        if required_fields is not None:
            pulumi.set(__self__, "required_fields", required_fields)

    @property
    @pulumi.getter(name="invisibleFields")
    def invisible_fields(self) -> Optional[Sequence['outputs.TaskTemplateInvisibleFieldInfo']]:
        return pulumi.get(self, "invisible_fields")

    @property
    @pulumi.getter(name="readOnlyFields")
    def read_only_fields(self) -> Optional[Sequence['outputs.TaskTemplateReadOnlyFieldInfo']]:
        return pulumi.get(self, "read_only_fields")

    @property
    @pulumi.getter(name="requiredFields")
    def required_fields(self) -> Optional[Sequence['outputs.TaskTemplateRequiredFieldInfo']]:
        return pulumi.get(self, "required_fields")


@pulumi.output_type
class ContactFlowModuleTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param str value: The value for the tag. You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class ContactFlowTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param str value: The value for the tag. . You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. . You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class HoursOfOperationConfig(dict):
    """
    Contains information about the hours of operation.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endTime":
            suggest = "end_time"
        elif key == "startTime":
            suggest = "start_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HoursOfOperationConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HoursOfOperationConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HoursOfOperationConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 day: 'HoursOfOperationConfigDay',
                 end_time: 'outputs.HoursOfOperationTimeSlice',
                 start_time: 'outputs.HoursOfOperationTimeSlice'):
        """
        Contains information about the hours of operation.
        :param 'HoursOfOperationConfigDay' day: The day that the hours of operation applies to.
        :param 'HoursOfOperationTimeSlice' end_time: The end time that your contact center closes.
        :param 'HoursOfOperationTimeSlice' start_time: The start time that your contact center opens.
        """
        pulumi.set(__self__, "day", day)
        pulumi.set(__self__, "end_time", end_time)
        pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter
    def day(self) -> 'HoursOfOperationConfigDay':
        """
        The day that the hours of operation applies to.
        """
        return pulumi.get(self, "day")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> 'outputs.HoursOfOperationTimeSlice':
        """
        The end time that your contact center closes.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> 'outputs.HoursOfOperationTimeSlice':
        """
        The start time that your contact center opens.
        """
        return pulumi.get(self, "start_time")


@pulumi.output_type
class HoursOfOperationTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param str value: The value for the tag. You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class HoursOfOperationTimeSlice(dict):
    """
    The start time or end time for an hours of operation.
    """
    def __init__(__self__, *,
                 hours: int,
                 minutes: int):
        """
        The start time or end time for an hours of operation.
        :param int hours: The hours.
        :param int minutes: The minutes.
        """
        pulumi.set(__self__, "hours", hours)
        pulumi.set(__self__, "minutes", minutes)

    @property
    @pulumi.getter
    def hours(self) -> int:
        """
        The hours.
        """
        return pulumi.get(self, "hours")

    @property
    @pulumi.getter
    def minutes(self) -> int:
        """
        The minutes.
        """
        return pulumi.get(self, "minutes")


@pulumi.output_type
class InstanceAttributes(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "inboundCalls":
            suggest = "inbound_calls"
        elif key == "outboundCalls":
            suggest = "outbound_calls"
        elif key == "autoResolveBestVoices":
            suggest = "auto_resolve_best_voices"
        elif key == "contactLens":
            suggest = "contact_lens"
        elif key == "contactflowLogs":
            suggest = "contactflow_logs"
        elif key == "earlyMedia":
            suggest = "early_media"
        elif key == "useCustomTTSVoices":
            suggest = "use_custom_tts_voices"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InstanceAttributes. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InstanceAttributes.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InstanceAttributes.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 inbound_calls: bool,
                 outbound_calls: bool,
                 auto_resolve_best_voices: Optional[bool] = None,
                 contact_lens: Optional[bool] = None,
                 contactflow_logs: Optional[bool] = None,
                 early_media: Optional[bool] = None,
                 use_custom_tts_voices: Optional[bool] = None):
        pulumi.set(__self__, "inbound_calls", inbound_calls)
        pulumi.set(__self__, "outbound_calls", outbound_calls)
        if auto_resolve_best_voices is not None:
            pulumi.set(__self__, "auto_resolve_best_voices", auto_resolve_best_voices)
        if contact_lens is not None:
            pulumi.set(__self__, "contact_lens", contact_lens)
        if contactflow_logs is not None:
            pulumi.set(__self__, "contactflow_logs", contactflow_logs)
        if early_media is not None:
            pulumi.set(__self__, "early_media", early_media)
        if use_custom_tts_voices is not None:
            pulumi.set(__self__, "use_custom_tts_voices", use_custom_tts_voices)

    @property
    @pulumi.getter(name="inboundCalls")
    def inbound_calls(self) -> bool:
        return pulumi.get(self, "inbound_calls")

    @property
    @pulumi.getter(name="outboundCalls")
    def outbound_calls(self) -> bool:
        return pulumi.get(self, "outbound_calls")

    @property
    @pulumi.getter(name="autoResolveBestVoices")
    def auto_resolve_best_voices(self) -> Optional[bool]:
        return pulumi.get(self, "auto_resolve_best_voices")

    @property
    @pulumi.getter(name="contactLens")
    def contact_lens(self) -> Optional[bool]:
        return pulumi.get(self, "contact_lens")

    @property
    @pulumi.getter(name="contactflowLogs")
    def contactflow_logs(self) -> Optional[bool]:
        return pulumi.get(self, "contactflow_logs")

    @property
    @pulumi.getter(name="earlyMedia")
    def early_media(self) -> Optional[bool]:
        return pulumi.get(self, "early_media")

    @property
    @pulumi.getter(name="useCustomTTSVoices")
    def use_custom_tts_voices(self) -> Optional[bool]:
        return pulumi.get(self, "use_custom_tts_voices")


@pulumi.output_type
class PhoneNumberTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param str value: The value for the tag. You can specify a value that is 1 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is 1 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class QuickConnectConfig(dict):
    """
    Configuration settings for the quick connect.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "quickConnectType":
            suggest = "quick_connect_type"
        elif key == "phoneConfig":
            suggest = "phone_config"
        elif key == "queueConfig":
            suggest = "queue_config"
        elif key == "userConfig":
            suggest = "user_config"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in QuickConnectConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        QuickConnectConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        QuickConnectConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 quick_connect_type: 'QuickConnectType',
                 phone_config: Optional['outputs.QuickConnectPhoneNumberQuickConnectConfig'] = None,
                 queue_config: Optional['outputs.QuickConnectQueueQuickConnectConfig'] = None,
                 user_config: Optional['outputs.QuickConnectUserQuickConnectConfig'] = None):
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
    def quick_connect_type(self) -> 'QuickConnectType':
        return pulumi.get(self, "quick_connect_type")

    @property
    @pulumi.getter(name="phoneConfig")
    def phone_config(self) -> Optional['outputs.QuickConnectPhoneNumberQuickConnectConfig']:
        return pulumi.get(self, "phone_config")

    @property
    @pulumi.getter(name="queueConfig")
    def queue_config(self) -> Optional['outputs.QuickConnectQueueQuickConnectConfig']:
        return pulumi.get(self, "queue_config")

    @property
    @pulumi.getter(name="userConfig")
    def user_config(self) -> Optional['outputs.QuickConnectUserQuickConnectConfig']:
        return pulumi.get(self, "user_config")


@pulumi.output_type
class QuickConnectPhoneNumberQuickConnectConfig(dict):
    """
    The phone configuration. This is required only if QuickConnectType is PHONE_NUMBER.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "phoneNumber":
            suggest = "phone_number"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in QuickConnectPhoneNumberQuickConnectConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        QuickConnectPhoneNumberQuickConnectConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        QuickConnectPhoneNumberQuickConnectConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 phone_number: str):
        """
        The phone configuration. This is required only if QuickConnectType is PHONE_NUMBER.
        """
        pulumi.set(__self__, "phone_number", phone_number)

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> str:
        return pulumi.get(self, "phone_number")


@pulumi.output_type
class QuickConnectQueueQuickConnectConfig(dict):
    """
    The queue configuration. This is required only if QuickConnectType is QUEUE.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "contactFlowArn":
            suggest = "contact_flow_arn"
        elif key == "queueArn":
            suggest = "queue_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in QuickConnectQueueQuickConnectConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        QuickConnectQueueQuickConnectConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        QuickConnectQueueQuickConnectConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 contact_flow_arn: str,
                 queue_arn: str):
        """
        The queue configuration. This is required only if QuickConnectType is QUEUE.
        """
        pulumi.set(__self__, "contact_flow_arn", contact_flow_arn)
        pulumi.set(__self__, "queue_arn", queue_arn)

    @property
    @pulumi.getter(name="contactFlowArn")
    def contact_flow_arn(self) -> str:
        return pulumi.get(self, "contact_flow_arn")

    @property
    @pulumi.getter(name="queueArn")
    def queue_arn(self) -> str:
        return pulumi.get(self, "queue_arn")


@pulumi.output_type
class QuickConnectTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param str value: The value for the tag. You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class QuickConnectUserQuickConnectConfig(dict):
    """
    The user configuration. This is required only if QuickConnectType is USER.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "contactFlowArn":
            suggest = "contact_flow_arn"
        elif key == "userArn":
            suggest = "user_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in QuickConnectUserQuickConnectConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        QuickConnectUserQuickConnectConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        QuickConnectUserQuickConnectConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 contact_flow_arn: str,
                 user_arn: str):
        """
        The user configuration. This is required only if QuickConnectType is USER.
        """
        pulumi.set(__self__, "contact_flow_arn", contact_flow_arn)
        pulumi.set(__self__, "user_arn", user_arn)

    @property
    @pulumi.getter(name="contactFlowArn")
    def contact_flow_arn(self) -> str:
        return pulumi.get(self, "contact_flow_arn")

    @property
    @pulumi.getter(name="userArn")
    def user_arn(self) -> str:
        return pulumi.get(self, "user_arn")


@pulumi.output_type
class TaskTemplateDefaultFieldValue(dict):
    """
    the default value for the task template's field
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "defaultValue":
            suggest = "default_value"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TaskTemplateDefaultFieldValue. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TaskTemplateDefaultFieldValue.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TaskTemplateDefaultFieldValue.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 default_value: str,
                 id: 'outputs.TaskTemplateFieldIdentifier'):
        """
        the default value for the task template's field
        """
        pulumi.set(__self__, "default_value", default_value)
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> str:
        return pulumi.get(self, "default_value")

    @property
    @pulumi.getter
    def id(self) -> 'outputs.TaskTemplateFieldIdentifier':
        return pulumi.get(self, "id")


@pulumi.output_type
class TaskTemplateField(dict):
    """
    A task template field object.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "singleSelectOptions":
            suggest = "single_select_options"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TaskTemplateField. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TaskTemplateField.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TaskTemplateField.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id: 'outputs.TaskTemplateFieldIdentifier',
                 type: 'TaskTemplateFieldType',
                 description: Optional[str] = None,
                 single_select_options: Optional[Sequence[str]] = None):
        """
        A task template field object.
        :param str description: The description of the task template's field
        :param Sequence[str] single_select_options: list of field options to be used with single select
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "type", type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if single_select_options is not None:
            pulumi.set(__self__, "single_select_options", single_select_options)

    @property
    @pulumi.getter
    def id(self) -> 'outputs.TaskTemplateFieldIdentifier':
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def type(self) -> 'TaskTemplateFieldType':
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the task template's field
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="singleSelectOptions")
    def single_select_options(self) -> Optional[Sequence[str]]:
        """
        list of field options to be used with single select
        """
        return pulumi.get(self, "single_select_options")


@pulumi.output_type
class TaskTemplateFieldIdentifier(dict):
    """
    the identifier (name) for the task template field
    """
    def __init__(__self__, *,
                 name: str):
        """
        the identifier (name) for the task template field
        :param str name: The name of the task template field
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the task template field
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class TaskTemplateInvisibleFieldInfo(dict):
    """
    Invisible field info
    """
    def __init__(__self__, *,
                 id: 'outputs.TaskTemplateFieldIdentifier'):
        """
        Invisible field info
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> 'outputs.TaskTemplateFieldIdentifier':
        return pulumi.get(self, "id")


@pulumi.output_type
class TaskTemplateReadOnlyFieldInfo(dict):
    """
    ReadOnly field info
    """
    def __init__(__self__, *,
                 id: 'outputs.TaskTemplateFieldIdentifier'):
        """
        ReadOnly field info
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> 'outputs.TaskTemplateFieldIdentifier':
        return pulumi.get(self, "id")


@pulumi.output_type
class TaskTemplateRequiredFieldInfo(dict):
    """
    Required field info
    """
    def __init__(__self__, *,
                 id: 'outputs.TaskTemplateFieldIdentifier'):
        """
        Required field info
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> 'outputs.TaskTemplateFieldIdentifier':
        return pulumi.get(self, "id")


@pulumi.output_type
class TaskTemplateTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param str value: The value for the tag. . You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. . You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class UserIdentityInfo(dict):
    """
    Contains information about the identity of a user.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "firstName":
            suggest = "first_name"
        elif key == "lastName":
            suggest = "last_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserIdentityInfo. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserIdentityInfo.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserIdentityInfo.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 email: Optional[str] = None,
                 first_name: Optional[str] = None,
                 last_name: Optional[str] = None):
        """
        Contains information about the identity of a user.
        """
        if email is not None:
            pulumi.set(__self__, "email", email)
        if first_name is not None:
            pulumi.set(__self__, "first_name", first_name)
        if last_name is not None:
            pulumi.set(__self__, "last_name", last_name)

    @property
    @pulumi.getter
    def email(self) -> Optional[str]:
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[str]:
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[str]:
        return pulumi.get(self, "last_name")


@pulumi.output_type
class UserPhoneConfig(dict):
    """
    Contains information about the phone configuration settings for a user.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "phoneType":
            suggest = "phone_type"
        elif key == "afterContactWorkTimeLimit":
            suggest = "after_contact_work_time_limit"
        elif key == "autoAccept":
            suggest = "auto_accept"
        elif key == "deskPhoneNumber":
            suggest = "desk_phone_number"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserPhoneConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserPhoneConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserPhoneConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 phone_type: 'UserPhoneType',
                 after_contact_work_time_limit: Optional[int] = None,
                 auto_accept: Optional[bool] = None,
                 desk_phone_number: Optional[str] = None):
        """
        Contains information about the phone configuration settings for a user.
        """
        pulumi.set(__self__, "phone_type", phone_type)
        if after_contact_work_time_limit is not None:
            pulumi.set(__self__, "after_contact_work_time_limit", after_contact_work_time_limit)
        if auto_accept is not None:
            pulumi.set(__self__, "auto_accept", auto_accept)
        if desk_phone_number is not None:
            pulumi.set(__self__, "desk_phone_number", desk_phone_number)

    @property
    @pulumi.getter(name="phoneType")
    def phone_type(self) -> 'UserPhoneType':
        return pulumi.get(self, "phone_type")

    @property
    @pulumi.getter(name="afterContactWorkTimeLimit")
    def after_contact_work_time_limit(self) -> Optional[int]:
        return pulumi.get(self, "after_contact_work_time_limit")

    @property
    @pulumi.getter(name="autoAccept")
    def auto_accept(self) -> Optional[bool]:
        return pulumi.get(self, "auto_accept")

    @property
    @pulumi.getter(name="deskPhoneNumber")
    def desk_phone_number(self) -> Optional[str]:
        return pulumi.get(self, "desk_phone_number")


@pulumi.output_type
class UserTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param str value: The value for the tag. You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")


