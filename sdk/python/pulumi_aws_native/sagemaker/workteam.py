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

__all__ = ['WorkteamArgs', 'Workteam']

@pulumi.input_type
class WorkteamArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 member_definitions: Optional[pulumi.Input[Sequence[pulumi.Input['WorkteamMemberDefinitionArgs']]]] = None,
                 notification_configuration: Optional[pulumi.Input['WorkteamNotificationConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['WorkteamTagArgs']]]] = None,
                 workforce_name: Optional[pulumi.Input[str]] = None,
                 workteam_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Workteam resource.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if member_definitions is not None:
            pulumi.set(__self__, "member_definitions", member_definitions)
        if notification_configuration is not None:
            pulumi.set(__self__, "notification_configuration", notification_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if workforce_name is not None:
            pulumi.set(__self__, "workforce_name", workforce_name)
        if workteam_name is not None:
            pulumi.set(__self__, "workteam_name", workteam_name)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="memberDefinitions")
    def member_definitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkteamMemberDefinitionArgs']]]]:
        return pulumi.get(self, "member_definitions")

    @member_definitions.setter
    def member_definitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkteamMemberDefinitionArgs']]]]):
        pulumi.set(self, "member_definitions", value)

    @property
    @pulumi.getter(name="notificationConfiguration")
    def notification_configuration(self) -> Optional[pulumi.Input['WorkteamNotificationConfigurationArgs']]:
        return pulumi.get(self, "notification_configuration")

    @notification_configuration.setter
    def notification_configuration(self, value: Optional[pulumi.Input['WorkteamNotificationConfigurationArgs']]):
        pulumi.set(self, "notification_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkteamTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkteamTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="workforceName")
    def workforce_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "workforce_name")

    @workforce_name.setter
    def workforce_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workforce_name", value)

    @property
    @pulumi.getter(name="workteamName")
    def workteam_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "workteam_name")

    @workteam_name.setter
    def workteam_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workteam_name", value)


warnings.warn("""Workteam is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Workteam(pulumi.CustomResource):
    warnings.warn("""Workteam is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 member_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkteamMemberDefinitionArgs']]]]] = None,
                 notification_configuration: Optional[pulumi.Input[pulumi.InputType['WorkteamNotificationConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkteamTagArgs']]]]] = None,
                 workforce_name: Optional[pulumi.Input[str]] = None,
                 workteam_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SageMaker::Workteam

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[WorkteamArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SageMaker::Workteam

        :param str resource_name: The name of the resource.
        :param WorkteamArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkteamArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 member_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkteamMemberDefinitionArgs']]]]] = None,
                 notification_configuration: Optional[pulumi.Input[pulumi.InputType['WorkteamNotificationConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkteamTagArgs']]]]] = None,
                 workforce_name: Optional[pulumi.Input[str]] = None,
                 workteam_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Workteam is deprecated: Workteam is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkteamArgs.__new__(WorkteamArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["member_definitions"] = member_definitions
            __props__.__dict__["notification_configuration"] = notification_configuration
            __props__.__dict__["tags"] = tags
            __props__.__dict__["workforce_name"] = workforce_name
            __props__.__dict__["workteam_name"] = workteam_name
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["workforce_name", "workteam_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Workteam, __self__).__init__(
            'aws-native:sagemaker:Workteam',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Workteam':
        """
        Get an existing Workteam resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkteamArgs.__new__(WorkteamArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["member_definitions"] = None
        __props__.__dict__["notification_configuration"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["workforce_name"] = None
        __props__.__dict__["workteam_name"] = None
        return Workteam(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="memberDefinitions")
    def member_definitions(self) -> pulumi.Output[Optional[Sequence['outputs.WorkteamMemberDefinition']]]:
        return pulumi.get(self, "member_definitions")

    @property
    @pulumi.getter(name="notificationConfiguration")
    def notification_configuration(self) -> pulumi.Output[Optional['outputs.WorkteamNotificationConfiguration']]:
        return pulumi.get(self, "notification_configuration")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.WorkteamTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="workforceName")
    def workforce_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "workforce_name")

    @property
    @pulumi.getter(name="workteamName")
    def workteam_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "workteam_name")

