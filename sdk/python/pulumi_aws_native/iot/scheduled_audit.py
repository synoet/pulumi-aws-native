# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs

__all__ = ['ScheduledAuditArgs', 'ScheduledAudit']

@pulumi.input_type
class ScheduledAuditArgs:
    def __init__(__self__, *,
                 frequency: pulumi.Input[str],
                 target_check_names: pulumi.Input[Sequence[pulumi.Input[str]]],
                 day_of_month: Optional[pulumi.Input[str]] = None,
                 day_of_week: Optional[pulumi.Input[str]] = None,
                 scheduled_audit_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a ScheduledAudit resource.
        :param pulumi.Input[str] frequency: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-frequency
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_check_names: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-targetchecknames
        :param pulumi.Input[str] day_of_month: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofmonth
        :param pulumi.Input[str] day_of_week: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofweek
        :param pulumi.Input[str] scheduled_audit_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-scheduledauditname
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-tags
        """
        pulumi.set(__self__, "frequency", frequency)
        pulumi.set(__self__, "target_check_names", target_check_names)
        if day_of_month is not None:
            pulumi.set(__self__, "day_of_month", day_of_month)
        if day_of_week is not None:
            pulumi.set(__self__, "day_of_week", day_of_week)
        if scheduled_audit_name is not None:
            pulumi.set(__self__, "scheduled_audit_name", scheduled_audit_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-frequency
        """
        return pulumi.get(self, "frequency")

    @frequency.setter
    def frequency(self, value: pulumi.Input[str]):
        pulumi.set(self, "frequency", value)

    @property
    @pulumi.getter(name="targetCheckNames")
    def target_check_names(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-targetchecknames
        """
        return pulumi.get(self, "target_check_names")

    @target_check_names.setter
    def target_check_names(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "target_check_names", value)

    @property
    @pulumi.getter(name="dayOfMonth")
    def day_of_month(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofmonth
        """
        return pulumi.get(self, "day_of_month")

    @day_of_month.setter
    def day_of_month(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "day_of_month", value)

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofweek
        """
        return pulumi.get(self, "day_of_week")

    @day_of_week.setter
    def day_of_week(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "day_of_week", value)

    @property
    @pulumi.getter(name="scheduledAuditName")
    def scheduled_audit_name(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-scheduledauditname
        """
        return pulumi.get(self, "scheduled_audit_name")

    @scheduled_audit_name.setter
    def scheduled_audit_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scheduled_audit_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class ScheduledAudit(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 day_of_month: Optional[pulumi.Input[str]] = None,
                 day_of_week: Optional[pulumi.Input[str]] = None,
                 frequency: Optional[pulumi.Input[str]] = None,
                 scheduled_audit_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 target_check_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] day_of_month: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofmonth
        :param pulumi.Input[str] day_of_week: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofweek
        :param pulumi.Input[str] frequency: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-frequency
        :param pulumi.Input[str] scheduled_audit_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-scheduledauditname
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-tags
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_check_names: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-targetchecknames
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScheduledAuditArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html

        :param str resource_name: The name of the resource.
        :param ScheduledAuditArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScheduledAuditArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 day_of_month: Optional[pulumi.Input[str]] = None,
                 day_of_week: Optional[pulumi.Input[str]] = None,
                 frequency: Optional[pulumi.Input[str]] = None,
                 scheduled_audit_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 target_check_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScheduledAuditArgs.__new__(ScheduledAuditArgs)

            __props__.__dict__["day_of_month"] = day_of_month
            __props__.__dict__["day_of_week"] = day_of_week
            if frequency is None and not opts.urn:
                raise TypeError("Missing required property 'frequency'")
            __props__.__dict__["frequency"] = frequency
            __props__.__dict__["scheduled_audit_name"] = scheduled_audit_name
            __props__.__dict__["tags"] = tags
            if target_check_names is None and not opts.urn:
                raise TypeError("Missing required property 'target_check_names'")
            __props__.__dict__["target_check_names"] = target_check_names
            __props__.__dict__["scheduled_audit_arn"] = None
        super(ScheduledAudit, __self__).__init__(
            'aws-native:iot:ScheduledAudit',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ScheduledAudit':
        """
        Get an existing ScheduledAudit resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScheduledAuditArgs.__new__(ScheduledAuditArgs)

        __props__.__dict__["day_of_month"] = None
        __props__.__dict__["day_of_week"] = None
        __props__.__dict__["frequency"] = None
        __props__.__dict__["scheduled_audit_arn"] = None
        __props__.__dict__["scheduled_audit_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_check_names"] = None
        return ScheduledAudit(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dayOfMonth")
    def day_of_month(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofmonth
        """
        return pulumi.get(self, "day_of_month")

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofweek
        """
        return pulumi.get(self, "day_of_week")

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Output[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-frequency
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter(name="scheduledAuditArn")
    def scheduled_audit_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "scheduled_audit_arn")

    @property
    @pulumi.getter(name="scheduledAuditName")
    def scheduled_audit_name(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-scheduledauditname
        """
        return pulumi.get(self, "scheduled_audit_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetCheckNames")
    def target_check_names(self) -> pulumi.Output[Sequence[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-targetchecknames
        """
        return pulumi.get(self, "target_check_names")

