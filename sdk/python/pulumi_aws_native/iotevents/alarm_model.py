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
from ._inputs import *

__all__ = ['AlarmModelArgs', 'AlarmModel']

@pulumi.input_type
class AlarmModelArgs:
    def __init__(__self__, *,
                 alarm_rule: pulumi.Input['AlarmModelAlarmRuleArgs'],
                 role_arn: pulumi.Input[str],
                 alarm_capabilities: Optional[pulumi.Input['AlarmModelAlarmCapabilitiesArgs']] = None,
                 alarm_event_actions: Optional[pulumi.Input['AlarmModelAlarmEventActionsArgs']] = None,
                 alarm_model_description: Optional[pulumi.Input[str]] = None,
                 alarm_model_name: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 severity: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['AlarmModelTagArgs']]]] = None):
        """
        The set of arguments for constructing a AlarmModel resource.
        :param pulumi.Input[str] role_arn: The ARN of the role that grants permission to AWS IoT Events to perform its operations.
        :param pulumi.Input[str] alarm_model_description: A brief description of the alarm model.
        :param pulumi.Input[str] alarm_model_name: The name of the alarm model.
        :param pulumi.Input[str] key: The value used to identify a alarm instance. When a device or system sends input, a new alarm instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding alarm instance based on this identifying information.
               
               This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct alarm instance, the device must send a message payload that contains the same attribute-value.
        :param pulumi.Input[int] severity: A non-negative integer that reflects the severity level of the alarm.
        :param pulumi.Input[Sequence[pulumi.Input['AlarmModelTagArgs']]] tags: An array of key-value pairs to apply to this resource.
               
               For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        """
        pulumi.set(__self__, "alarm_rule", alarm_rule)
        pulumi.set(__self__, "role_arn", role_arn)
        if alarm_capabilities is not None:
            pulumi.set(__self__, "alarm_capabilities", alarm_capabilities)
        if alarm_event_actions is not None:
            pulumi.set(__self__, "alarm_event_actions", alarm_event_actions)
        if alarm_model_description is not None:
            pulumi.set(__self__, "alarm_model_description", alarm_model_description)
        if alarm_model_name is not None:
            pulumi.set(__self__, "alarm_model_name", alarm_model_name)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if severity is not None:
            pulumi.set(__self__, "severity", severity)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="alarmRule")
    def alarm_rule(self) -> pulumi.Input['AlarmModelAlarmRuleArgs']:
        return pulumi.get(self, "alarm_rule")

    @alarm_rule.setter
    def alarm_rule(self, value: pulumi.Input['AlarmModelAlarmRuleArgs']):
        pulumi.set(self, "alarm_rule", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the role that grants permission to AWS IoT Events to perform its operations.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="alarmCapabilities")
    def alarm_capabilities(self) -> Optional[pulumi.Input['AlarmModelAlarmCapabilitiesArgs']]:
        return pulumi.get(self, "alarm_capabilities")

    @alarm_capabilities.setter
    def alarm_capabilities(self, value: Optional[pulumi.Input['AlarmModelAlarmCapabilitiesArgs']]):
        pulumi.set(self, "alarm_capabilities", value)

    @property
    @pulumi.getter(name="alarmEventActions")
    def alarm_event_actions(self) -> Optional[pulumi.Input['AlarmModelAlarmEventActionsArgs']]:
        return pulumi.get(self, "alarm_event_actions")

    @alarm_event_actions.setter
    def alarm_event_actions(self, value: Optional[pulumi.Input['AlarmModelAlarmEventActionsArgs']]):
        pulumi.set(self, "alarm_event_actions", value)

    @property
    @pulumi.getter(name="alarmModelDescription")
    def alarm_model_description(self) -> Optional[pulumi.Input[str]]:
        """
        A brief description of the alarm model.
        """
        return pulumi.get(self, "alarm_model_description")

    @alarm_model_description.setter
    def alarm_model_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alarm_model_description", value)

    @property
    @pulumi.getter(name="alarmModelName")
    def alarm_model_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the alarm model.
        """
        return pulumi.get(self, "alarm_model_name")

    @alarm_model_name.setter
    def alarm_model_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alarm_model_name", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The value used to identify a alarm instance. When a device or system sends input, a new alarm instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding alarm instance based on this identifying information.

        This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct alarm instance, the device must send a message payload that contains the same attribute-value.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[int]]:
        """
        A non-negative integer that reflects the severity level of the alarm.
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "severity", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AlarmModelTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.

        For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AlarmModelTagArgs']]]]):
        pulumi.set(self, "tags", value)


class AlarmModel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alarm_capabilities: Optional[pulumi.Input[pulumi.InputType['AlarmModelAlarmCapabilitiesArgs']]] = None,
                 alarm_event_actions: Optional[pulumi.Input[pulumi.InputType['AlarmModelAlarmEventActionsArgs']]] = None,
                 alarm_model_description: Optional[pulumi.Input[str]] = None,
                 alarm_model_name: Optional[pulumi.Input[str]] = None,
                 alarm_rule: Optional[pulumi.Input[pulumi.InputType['AlarmModelAlarmRuleArgs']]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 severity: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AlarmModelTagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::IoTEvents::AlarmModel resource creates a alarm model. AWS IoT Events alarms help you monitor your data for changes. The data can be metrics that you measure for your equipment and processes. You can create alarms that send notifications when a threshold is breached. Alarms help you detect issues, streamline maintenance, and optimize performance of your equipment and processes.

        Alarms are instances of alarm models. The alarm model specifies what to detect, when to send notifications, who gets notified, and more. You can also specify one or more supported actions that occur when the alarm state changes. AWS IoT Events routes input attributes derived from your data to the appropriate alarms. If the data that you're monitoring is outside the specified range, the alarm is invoked. You can also acknowledge the alarms or set them to the snooze mode.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alarm_model_description: A brief description of the alarm model.
        :param pulumi.Input[str] alarm_model_name: The name of the alarm model.
        :param pulumi.Input[str] key: The value used to identify a alarm instance. When a device or system sends input, a new alarm instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding alarm instance based on this identifying information.
               
               This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct alarm instance, the device must send a message payload that contains the same attribute-value.
        :param pulumi.Input[str] role_arn: The ARN of the role that grants permission to AWS IoT Events to perform its operations.
        :param pulumi.Input[int] severity: A non-negative integer that reflects the severity level of the alarm.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AlarmModelTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
               
               For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AlarmModelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::IoTEvents::AlarmModel resource creates a alarm model. AWS IoT Events alarms help you monitor your data for changes. The data can be metrics that you measure for your equipment and processes. You can create alarms that send notifications when a threshold is breached. Alarms help you detect issues, streamline maintenance, and optimize performance of your equipment and processes.

        Alarms are instances of alarm models. The alarm model specifies what to detect, when to send notifications, who gets notified, and more. You can also specify one or more supported actions that occur when the alarm state changes. AWS IoT Events routes input attributes derived from your data to the appropriate alarms. If the data that you're monitoring is outside the specified range, the alarm is invoked. You can also acknowledge the alarms or set them to the snooze mode.

        :param str resource_name: The name of the resource.
        :param AlarmModelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AlarmModelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alarm_capabilities: Optional[pulumi.Input[pulumi.InputType['AlarmModelAlarmCapabilitiesArgs']]] = None,
                 alarm_event_actions: Optional[pulumi.Input[pulumi.InputType['AlarmModelAlarmEventActionsArgs']]] = None,
                 alarm_model_description: Optional[pulumi.Input[str]] = None,
                 alarm_model_name: Optional[pulumi.Input[str]] = None,
                 alarm_rule: Optional[pulumi.Input[pulumi.InputType['AlarmModelAlarmRuleArgs']]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 severity: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AlarmModelTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AlarmModelArgs.__new__(AlarmModelArgs)

            __props__.__dict__["alarm_capabilities"] = alarm_capabilities
            __props__.__dict__["alarm_event_actions"] = alarm_event_actions
            __props__.__dict__["alarm_model_description"] = alarm_model_description
            __props__.__dict__["alarm_model_name"] = alarm_model_name
            if alarm_rule is None and not opts.urn:
                raise TypeError("Missing required property 'alarm_rule'")
            __props__.__dict__["alarm_rule"] = alarm_rule
            __props__.__dict__["key"] = key
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["severity"] = severity
            __props__.__dict__["tags"] = tags
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["alarm_model_name", "key"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(AlarmModel, __self__).__init__(
            'aws-native:iotevents:AlarmModel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AlarmModel':
        """
        Get an existing AlarmModel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AlarmModelArgs.__new__(AlarmModelArgs)

        __props__.__dict__["alarm_capabilities"] = None
        __props__.__dict__["alarm_event_actions"] = None
        __props__.__dict__["alarm_model_description"] = None
        __props__.__dict__["alarm_model_name"] = None
        __props__.__dict__["alarm_rule"] = None
        __props__.__dict__["key"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["severity"] = None
        __props__.__dict__["tags"] = None
        return AlarmModel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="alarmCapabilities")
    def alarm_capabilities(self) -> pulumi.Output[Optional['outputs.AlarmModelAlarmCapabilities']]:
        return pulumi.get(self, "alarm_capabilities")

    @property
    @pulumi.getter(name="alarmEventActions")
    def alarm_event_actions(self) -> pulumi.Output[Optional['outputs.AlarmModelAlarmEventActions']]:
        return pulumi.get(self, "alarm_event_actions")

    @property
    @pulumi.getter(name="alarmModelDescription")
    def alarm_model_description(self) -> pulumi.Output[Optional[str]]:
        """
        A brief description of the alarm model.
        """
        return pulumi.get(self, "alarm_model_description")

    @property
    @pulumi.getter(name="alarmModelName")
    def alarm_model_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the alarm model.
        """
        return pulumi.get(self, "alarm_model_name")

    @property
    @pulumi.getter(name="alarmRule")
    def alarm_rule(self) -> pulumi.Output['outputs.AlarmModelAlarmRule']:
        return pulumi.get(self, "alarm_rule")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[Optional[str]]:
        """
        The value used to identify a alarm instance. When a device or system sends input, a new alarm instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding alarm instance based on this identifying information.

        This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct alarm instance, the device must send a message payload that contains the same attribute-value.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the role that grants permission to AWS IoT Events to perform its operations.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def severity(self) -> pulumi.Output[Optional[int]]:
        """
        A non-negative integer that reflects the severity level of the alarm.
        """
        return pulumi.get(self, "severity")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.AlarmModelTag']]]:
        """
        An array of key-value pairs to apply to this resource.

        For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        """
        return pulumi.get(self, "tags")

