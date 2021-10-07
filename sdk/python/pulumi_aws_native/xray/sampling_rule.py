# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['SamplingRuleInitArgs', 'SamplingRule']

@pulumi.input_type
class SamplingRuleInitArgs:
    def __init__(__self__, *,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 sampling_rule: Optional[pulumi.Input['SamplingRuleArgs']] = None,
                 sampling_rule_record: Optional[pulumi.Input['SamplingRuleRecordArgs']] = None,
                 sampling_rule_update: Optional[pulumi.Input['SamplingRuleUpdateArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[Any]]] = None):
        """
        The set of arguments for constructing a SamplingRule resource.
        """
        if rule_name is not None:
            pulumi.set(__self__, "rule_name", rule_name)
        if sampling_rule is not None:
            pulumi.set(__self__, "sampling_rule", sampling_rule)
        if sampling_rule_record is not None:
            pulumi.set(__self__, "sampling_rule_record", sampling_rule_record)
        if sampling_rule_update is not None:
            pulumi.set(__self__, "sampling_rule_update", sampling_rule_update)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "rule_name")

    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_name", value)

    @property
    @pulumi.getter(name="samplingRule")
    def sampling_rule(self) -> Optional[pulumi.Input['SamplingRuleArgs']]:
        return pulumi.get(self, "sampling_rule")

    @sampling_rule.setter
    def sampling_rule(self, value: Optional[pulumi.Input['SamplingRuleArgs']]):
        pulumi.set(self, "sampling_rule", value)

    @property
    @pulumi.getter(name="samplingRuleRecord")
    def sampling_rule_record(self) -> Optional[pulumi.Input['SamplingRuleRecordArgs']]:
        return pulumi.get(self, "sampling_rule_record")

    @sampling_rule_record.setter
    def sampling_rule_record(self, value: Optional[pulumi.Input['SamplingRuleRecordArgs']]):
        pulumi.set(self, "sampling_rule_record", value)

    @property
    @pulumi.getter(name="samplingRuleUpdate")
    def sampling_rule_update(self) -> Optional[pulumi.Input['SamplingRuleUpdateArgs']]:
        return pulumi.get(self, "sampling_rule_update")

    @sampling_rule_update.setter
    def sampling_rule_update(self, value: Optional[pulumi.Input['SamplingRuleUpdateArgs']]):
        pulumi.set(self, "sampling_rule_update", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[Any]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[Any]]]):
        pulumi.set(self, "tags", value)


class SamplingRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 sampling_rule: Optional[pulumi.Input[pulumi.InputType['SamplingRuleArgs']]] = None,
                 sampling_rule_record: Optional[pulumi.Input[pulumi.InputType['SamplingRuleRecordArgs']]] = None,
                 sampling_rule_update: Optional[pulumi.Input[pulumi.InputType['SamplingRuleUpdateArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[Any]]] = None,
                 __props__=None):
        """
        This schema provides construct and validation rules for AWS-XRay SamplingRule resource parameters.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SamplingRuleInitArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This schema provides construct and validation rules for AWS-XRay SamplingRule resource parameters.

        :param str resource_name: The name of the resource.
        :param SamplingRuleInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SamplingRuleInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 sampling_rule: Optional[pulumi.Input[pulumi.InputType['SamplingRuleArgs']]] = None,
                 sampling_rule_record: Optional[pulumi.Input[pulumi.InputType['SamplingRuleRecordArgs']]] = None,
                 sampling_rule_update: Optional[pulumi.Input[pulumi.InputType['SamplingRuleUpdateArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[Any]]] = None,
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
            __props__ = SamplingRuleInitArgs.__new__(SamplingRuleInitArgs)

            __props__.__dict__["rule_name"] = rule_name
            __props__.__dict__["sampling_rule"] = sampling_rule
            __props__.__dict__["sampling_rule_record"] = sampling_rule_record
            __props__.__dict__["sampling_rule_update"] = sampling_rule_update
            __props__.__dict__["tags"] = tags
            __props__.__dict__["rule_arn"] = None
        super(SamplingRule, __self__).__init__(
            'aws-native:xray:SamplingRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SamplingRule':
        """
        Get an existing SamplingRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SamplingRuleInitArgs.__new__(SamplingRuleInitArgs)

        __props__.__dict__["rule_arn"] = None
        __props__.__dict__["rule_name"] = None
        __props__.__dict__["sampling_rule"] = None
        __props__.__dict__["sampling_rule_record"] = None
        __props__.__dict__["sampling_rule_update"] = None
        __props__.__dict__["tags"] = None
        return SamplingRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ruleARN")
    def rule_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "rule_arn")

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "rule_name")

    @property
    @pulumi.getter(name="samplingRule")
    def sampling_rule(self) -> pulumi.Output[Optional['outputs.SamplingRule']]:
        return pulumi.get(self, "sampling_rule")

    @property
    @pulumi.getter(name="samplingRuleRecord")
    def sampling_rule_record(self) -> pulumi.Output[Optional['outputs.SamplingRuleRecord']]:
        return pulumi.get(self, "sampling_rule_record")

    @property
    @pulumi.getter(name="samplingRuleUpdate")
    def sampling_rule_update(self) -> pulumi.Output[Optional['outputs.SamplingRuleUpdate']]:
        return pulumi.get(self, "sampling_rule_update")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        return pulumi.get(self, "tags")

