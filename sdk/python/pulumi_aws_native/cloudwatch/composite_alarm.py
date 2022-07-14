# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CompositeAlarmArgs', 'CompositeAlarm']

@pulumi.input_type
class CompositeAlarmArgs:
    def __init__(__self__, *,
                 alarm_name: pulumi.Input[str],
                 alarm_rule: pulumi.Input[str],
                 actions_enabled: Optional[pulumi.Input[bool]] = None,
                 alarm_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 alarm_description: Optional[pulumi.Input[str]] = None,
                 insufficient_data_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 o_k_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a CompositeAlarm resource.
        :param pulumi.Input[str] alarm_name: The name of the Composite Alarm
        :param pulumi.Input[str] alarm_rule: Expression which aggregates the state of other Alarms (Metric or Composite Alarms)
        :param pulumi.Input[bool] actions_enabled: Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] alarm_actions: The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN).
        :param pulumi.Input[str] alarm_description: The description of the alarm
        :param pulumi.Input[Sequence[pulumi.Input[str]]] insufficient_data_actions: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] o_k_actions: The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        """
        pulumi.set(__self__, "alarm_name", alarm_name)
        pulumi.set(__self__, "alarm_rule", alarm_rule)
        if actions_enabled is not None:
            pulumi.set(__self__, "actions_enabled", actions_enabled)
        if alarm_actions is not None:
            pulumi.set(__self__, "alarm_actions", alarm_actions)
        if alarm_description is not None:
            pulumi.set(__self__, "alarm_description", alarm_description)
        if insufficient_data_actions is not None:
            pulumi.set(__self__, "insufficient_data_actions", insufficient_data_actions)
        if o_k_actions is not None:
            pulumi.set(__self__, "o_k_actions", o_k_actions)

    @property
    @pulumi.getter(name="alarmName")
    def alarm_name(self) -> pulumi.Input[str]:
        """
        The name of the Composite Alarm
        """
        return pulumi.get(self, "alarm_name")

    @alarm_name.setter
    def alarm_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "alarm_name", value)

    @property
    @pulumi.getter(name="alarmRule")
    def alarm_rule(self) -> pulumi.Input[str]:
        """
        Expression which aggregates the state of other Alarms (Metric or Composite Alarms)
        """
        return pulumi.get(self, "alarm_rule")

    @alarm_rule.setter
    def alarm_rule(self, value: pulumi.Input[str]):
        pulumi.set(self, "alarm_rule", value)

    @property
    @pulumi.getter(name="actionsEnabled")
    def actions_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
        """
        return pulumi.get(self, "actions_enabled")

    @actions_enabled.setter
    def actions_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "actions_enabled", value)

    @property
    @pulumi.getter(name="alarmActions")
    def alarm_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN).
        """
        return pulumi.get(self, "alarm_actions")

    @alarm_actions.setter
    def alarm_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "alarm_actions", value)

    @property
    @pulumi.getter(name="alarmDescription")
    def alarm_description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the alarm
        """
        return pulumi.get(self, "alarm_description")

    @alarm_description.setter
    def alarm_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alarm_description", value)

    @property
    @pulumi.getter(name="insufficientDataActions")
    def insufficient_data_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        """
        return pulumi.get(self, "insufficient_data_actions")

    @insufficient_data_actions.setter
    def insufficient_data_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "insufficient_data_actions", value)

    @property
    @pulumi.getter(name="oKActions")
    def o_k_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        """
        return pulumi.get(self, "o_k_actions")

    @o_k_actions.setter
    def o_k_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "o_k_actions", value)


class CompositeAlarm(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions_enabled: Optional[pulumi.Input[bool]] = None,
                 alarm_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 alarm_description: Optional[pulumi.Input[str]] = None,
                 alarm_name: Optional[pulumi.Input[str]] = None,
                 alarm_rule: Optional[pulumi.Input[str]] = None,
                 insufficient_data_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 o_k_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The AWS::CloudWatch::CompositeAlarm type specifies an alarm which aggregates the states of other Alarms (Metric or Composite Alarms) as defined by the AlarmRule expression

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] actions_enabled: Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] alarm_actions: The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN).
        :param pulumi.Input[str] alarm_description: The description of the alarm
        :param pulumi.Input[str] alarm_name: The name of the Composite Alarm
        :param pulumi.Input[str] alarm_rule: Expression which aggregates the state of other Alarms (Metric or Composite Alarms)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] insufficient_data_actions: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] o_k_actions: The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CompositeAlarmArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::CloudWatch::CompositeAlarm type specifies an alarm which aggregates the states of other Alarms (Metric or Composite Alarms) as defined by the AlarmRule expression

        :param str resource_name: The name of the resource.
        :param CompositeAlarmArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CompositeAlarmArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions_enabled: Optional[pulumi.Input[bool]] = None,
                 alarm_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 alarm_description: Optional[pulumi.Input[str]] = None,
                 alarm_name: Optional[pulumi.Input[str]] = None,
                 alarm_rule: Optional[pulumi.Input[str]] = None,
                 insufficient_data_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 o_k_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CompositeAlarmArgs.__new__(CompositeAlarmArgs)

            __props__.__dict__["actions_enabled"] = actions_enabled
            __props__.__dict__["alarm_actions"] = alarm_actions
            __props__.__dict__["alarm_description"] = alarm_description
            if alarm_name is None and not opts.urn:
                raise TypeError("Missing required property 'alarm_name'")
            __props__.__dict__["alarm_name"] = alarm_name
            if alarm_rule is None and not opts.urn:
                raise TypeError("Missing required property 'alarm_rule'")
            __props__.__dict__["alarm_rule"] = alarm_rule
            __props__.__dict__["insufficient_data_actions"] = insufficient_data_actions
            __props__.__dict__["o_k_actions"] = o_k_actions
            __props__.__dict__["arn"] = None
        super(CompositeAlarm, __self__).__init__(
            'aws-native:cloudwatch:CompositeAlarm',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CompositeAlarm':
        """
        Get an existing CompositeAlarm resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CompositeAlarmArgs.__new__(CompositeAlarmArgs)

        __props__.__dict__["actions_enabled"] = None
        __props__.__dict__["alarm_actions"] = None
        __props__.__dict__["alarm_description"] = None
        __props__.__dict__["alarm_name"] = None
        __props__.__dict__["alarm_rule"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["insufficient_data_actions"] = None
        __props__.__dict__["o_k_actions"] = None
        return CompositeAlarm(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="actionsEnabled")
    def actions_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
        """
        return pulumi.get(self, "actions_enabled")

    @property
    @pulumi.getter(name="alarmActions")
    def alarm_actions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN).
        """
        return pulumi.get(self, "alarm_actions")

    @property
    @pulumi.getter(name="alarmDescription")
    def alarm_description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the alarm
        """
        return pulumi.get(self, "alarm_description")

    @property
    @pulumi.getter(name="alarmName")
    def alarm_name(self) -> pulumi.Output[str]:
        """
        The name of the Composite Alarm
        """
        return pulumi.get(self, "alarm_name")

    @property
    @pulumi.getter(name="alarmRule")
    def alarm_rule(self) -> pulumi.Output[str]:
        """
        Expression which aggregates the state of other Alarms (Metric or Composite Alarms)
        """
        return pulumi.get(self, "alarm_rule")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the alarm
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="insufficientDataActions")
    def insufficient_data_actions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        """
        return pulumi.get(self, "insufficient_data_actions")

    @property
    @pulumi.getter(name="oKActions")
    def o_k_actions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        """
        return pulumi.get(self, "o_k_actions")

