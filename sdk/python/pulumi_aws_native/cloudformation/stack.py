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
from ._inputs import *

__all__ = ['StackArgs', 'Stack']

@pulumi.input_type
class StackArgs:
    def __init__(__self__, *,
                 template_url: pulumi.Input[str],
                 notification_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 parameters: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['StackTagArgs']]]] = None,
                 timeout_in_minutes: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Stack resource.
        """
        pulumi.set(__self__, "template_url", template_url)
        if notification_arns is not None:
            pulumi.set(__self__, "notification_arns", notification_arns)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if timeout_in_minutes is not None:
            pulumi.set(__self__, "timeout_in_minutes", timeout_in_minutes)

    @property
    @pulumi.getter(name="templateURL")
    def template_url(self) -> pulumi.Input[str]:
        return pulumi.get(self, "template_url")

    @template_url.setter
    def template_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "template_url", value)

    @property
    @pulumi.getter(name="notificationARNs")
    def notification_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "notification_arns")

    @notification_arns.setter
    def notification_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "notification_arns", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Any]:
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[Any]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StackTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StackTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="timeoutInMinutes")
    def timeout_in_minutes(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "timeout_in_minutes")

    @timeout_in_minutes.setter
    def timeout_in_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout_in_minutes", value)


warnings.warn("""Stack is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Stack(pulumi.CustomResource):
    warnings.warn("""Stack is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 notification_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 parameters: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackTagArgs']]]]] = None,
                 template_url: Optional[pulumi.Input[str]] = None,
                 timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::CloudFormation::Stack

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StackArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::CloudFormation::Stack

        :param str resource_name: The name of the resource.
        :param StackArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StackArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 notification_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 parameters: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackTagArgs']]]]] = None,
                 template_url: Optional[pulumi.Input[str]] = None,
                 timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        pulumi.log.warn("""Stack is deprecated: Stack is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StackArgs.__new__(StackArgs)

            __props__.__dict__["notification_arns"] = notification_arns
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["tags"] = tags
            if template_url is None and not opts.urn:
                raise TypeError("Missing required property 'template_url'")
            __props__.__dict__["template_url"] = template_url
            __props__.__dict__["timeout_in_minutes"] = timeout_in_minutes
        super(Stack, __self__).__init__(
            'aws-native:cloudformation:Stack',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Stack':
        """
        Get an existing Stack resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StackArgs.__new__(StackArgs)

        __props__.__dict__["notification_arns"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["template_url"] = None
        __props__.__dict__["timeout_in_minutes"] = None
        return Stack(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="notificationARNs")
    def notification_arns(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "notification_arns")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.StackTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateURL")
    def template_url(self) -> pulumi.Output[str]:
        return pulumi.get(self, "template_url")

    @property
    @pulumi.getter(name="timeoutInMinutes")
    def timeout_in_minutes(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "timeout_in_minutes")

