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
    'GetAllowListResult',
    'AwaitableGetAllowListResult',
    'get_allow_list',
    'get_allow_list_output',
]

@pulumi.output_type
class GetAllowListResult:
    def __init__(__self__, arn=None, criteria=None, description=None, id=None, name=None, status=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if criteria and not isinstance(criteria, dict):
            raise TypeError("Expected argument 'criteria' to be a dict")
        pulumi.set(__self__, "criteria", criteria)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        AllowList ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def criteria(self) -> Optional['outputs.AllowListCriteria']:
        """
        AllowList criteria.
        """
        return pulumi.get(self, "criteria")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of AllowList.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        AllowList ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of AllowList.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> Optional['AllowListStatus']:
        """
        AllowList status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.AllowListTag']]:
        """
        A collection of tags associated with a resource
        """
        return pulumi.get(self, "tags")


class AwaitableGetAllowListResult(GetAllowListResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAllowListResult(
            arn=self.arn,
            criteria=self.criteria,
            description=self.description,
            id=self.id,
            name=self.name,
            status=self.status,
            tags=self.tags)


def get_allow_list(id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAllowListResult:
    """
    Macie AllowList resource schema


    :param str id: AllowList ID.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:macie:getAllowList', __args__, opts=opts, typ=GetAllowListResult).value

    return AwaitableGetAllowListResult(
        arn=__ret__.arn,
        criteria=__ret__.criteria,
        description=__ret__.description,
        id=__ret__.id,
        name=__ret__.name,
        status=__ret__.status,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_allow_list)
def get_allow_list_output(id: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAllowListResult]:
    """
    Macie AllowList resource schema


    :param str id: AllowList ID.
    """
    ...
