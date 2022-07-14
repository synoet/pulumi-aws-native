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
    'GetBuildResult',
    'AwaitableGetBuildResult',
    'get_build',
    'get_build_output',
]

@pulumi.output_type
class GetBuildResult:
    def __init__(__self__, id=None, name=None, version=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        return pulumi.get(self, "version")


class AwaitableGetBuildResult(GetBuildResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBuildResult(
            id=self.id,
            name=self.name,
            version=self.version)


def get_build(id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBuildResult:
    """
    Resource Type definition for AWS::GameLift::Build
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:gamelift:getBuild', __args__, opts=opts, typ=GetBuildResult).value

    return AwaitableGetBuildResult(
        id=__ret__.id,
        name=__ret__.name,
        version=__ret__.version)


@_utilities.lift_output_func(get_build)
def get_build_output(id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBuildResult]:
    """
    Resource Type definition for AWS::GameLift::Build
    """
    ...
