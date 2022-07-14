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
    'GetThemeResult',
    'AwaitableGetThemeResult',
    'get_theme',
    'get_theme_output',
]

@pulumi.output_type
class GetThemeResult:
    def __init__(__self__, app_id=None, created_at=None, environment_name=None, id=None, modified_at=None, name=None, overrides=None, values=None):
        if app_id and not isinstance(app_id, str):
            raise TypeError("Expected argument 'app_id' to be a str")
        pulumi.set(__self__, "app_id", app_id)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if environment_name and not isinstance(environment_name, str):
            raise TypeError("Expected argument 'environment_name' to be a str")
        pulumi.set(__self__, "environment_name", environment_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if modified_at and not isinstance(modified_at, str):
            raise TypeError("Expected argument 'modified_at' to be a str")
        pulumi.set(__self__, "modified_at", modified_at)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if overrides and not isinstance(overrides, list):
            raise TypeError("Expected argument 'overrides' to be a list")
        pulumi.set(__self__, "overrides", overrides)
        if values and not isinstance(values, list):
            raise TypeError("Expected argument 'values' to be a list")
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[str]:
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[str]:
        return pulumi.get(self, "environment_name")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> Optional[str]:
        return pulumi.get(self, "modified_at")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def overrides(self) -> Optional[Sequence['outputs.ThemeValues']]:
        return pulumi.get(self, "overrides")

    @property
    @pulumi.getter
    def values(self) -> Optional[Sequence['outputs.ThemeValues']]:
        return pulumi.get(self, "values")


class AwaitableGetThemeResult(GetThemeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetThemeResult(
            app_id=self.app_id,
            created_at=self.created_at,
            environment_name=self.environment_name,
            id=self.id,
            modified_at=self.modified_at,
            name=self.name,
            overrides=self.overrides,
            values=self.values)


def get_theme(app_id: Optional[str] = None,
              environment_name: Optional[str] = None,
              id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetThemeResult:
    """
    Definition of AWS::AmplifyUIBuilder::Theme Resource Type
    """
    __args__ = dict()
    __args__['appId'] = app_id
    __args__['environmentName'] = environment_name
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:amplifyuibuilder:getTheme', __args__, opts=opts, typ=GetThemeResult).value

    return AwaitableGetThemeResult(
        app_id=__ret__.app_id,
        created_at=__ret__.created_at,
        environment_name=__ret__.environment_name,
        id=__ret__.id,
        modified_at=__ret__.modified_at,
        name=__ret__.name,
        overrides=__ret__.overrides,
        values=__ret__.values)


@_utilities.lift_output_func(get_theme)
def get_theme_output(app_id: Optional[pulumi.Input[str]] = None,
                     environment_name: Optional[pulumi.Input[str]] = None,
                     id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetThemeResult]:
    """
    Definition of AWS::AmplifyUIBuilder::Theme Resource Type
    """
    ...
