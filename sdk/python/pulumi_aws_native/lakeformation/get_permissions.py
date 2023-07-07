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
    'GetPermissionsResult',
    'AwaitableGetPermissionsResult',
    'get_permissions',
    'get_permissions_output',
]

@pulumi.output_type
class GetPermissionsResult:
    def __init__(__self__, id=None, permissions=None, permissions_with_grant_option=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if permissions and not isinstance(permissions, list):
            raise TypeError("Expected argument 'permissions' to be a list")
        pulumi.set(__self__, "permissions", permissions)
        if permissions_with_grant_option and not isinstance(permissions_with_grant_option, list):
            raise TypeError("Expected argument 'permissions_with_grant_option' to be a list")
        pulumi.set(__self__, "permissions_with_grant_option", permissions_with_grant_option)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def permissions(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="permissionsWithGrantOption")
    def permissions_with_grant_option(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "permissions_with_grant_option")


class AwaitableGetPermissionsResult(GetPermissionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPermissionsResult(
            id=self.id,
            permissions=self.permissions,
            permissions_with_grant_option=self.permissions_with_grant_option)


def get_permissions(id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPermissionsResult:
    """
    Resource Type definition for AWS::LakeFormation::Permissions
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:lakeformation:getPermissions', __args__, opts=opts, typ=GetPermissionsResult).value

    return AwaitableGetPermissionsResult(
        id=__ret__.id,
        permissions=__ret__.permissions,
        permissions_with_grant_option=__ret__.permissions_with_grant_option)


@_utilities.lift_output_func(get_permissions)
def get_permissions_output(id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPermissionsResult]:
    """
    Resource Type definition for AWS::LakeFormation::Permissions
    """
    ...
