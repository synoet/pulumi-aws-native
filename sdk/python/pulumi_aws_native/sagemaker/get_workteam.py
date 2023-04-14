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

__all__ = [
    'GetWorkteamResult',
    'AwaitableGetWorkteamResult',
    'get_workteam',
    'get_workteam_output',
]

@pulumi.output_type
class GetWorkteamResult:
    def __init__(__self__, description=None, id=None, member_definitions=None, notification_configuration=None, tags=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if member_definitions and not isinstance(member_definitions, list):
            raise TypeError("Expected argument 'member_definitions' to be a list")
        pulumi.set(__self__, "member_definitions", member_definitions)
        if notification_configuration and not isinstance(notification_configuration, dict):
            raise TypeError("Expected argument 'notification_configuration' to be a dict")
        pulumi.set(__self__, "notification_configuration", notification_configuration)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="memberDefinitions")
    def member_definitions(self) -> Optional[Sequence['outputs.WorkteamMemberDefinition']]:
        return pulumi.get(self, "member_definitions")

    @property
    @pulumi.getter(name="notificationConfiguration")
    def notification_configuration(self) -> Optional['outputs.WorkteamNotificationConfiguration']:
        return pulumi.get(self, "notification_configuration")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.WorkteamTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetWorkteamResult(GetWorkteamResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkteamResult(
            description=self.description,
            id=self.id,
            member_definitions=self.member_definitions,
            notification_configuration=self.notification_configuration,
            tags=self.tags)


def get_workteam(id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkteamResult:
    """
    Resource Type definition for AWS::SageMaker::Workteam
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:sagemaker:getWorkteam', __args__, opts=opts, typ=GetWorkteamResult).value

    return AwaitableGetWorkteamResult(
        description=__ret__.description,
        id=__ret__.id,
        member_definitions=__ret__.member_definitions,
        notification_configuration=__ret__.notification_configuration,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_workteam)
def get_workteam_output(id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkteamResult]:
    """
    Resource Type definition for AWS::SageMaker::Workteam
    """
    ...
