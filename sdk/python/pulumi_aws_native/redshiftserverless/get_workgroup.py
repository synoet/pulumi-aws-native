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
    'GetWorkgroupResult',
    'AwaitableGetWorkgroupResult',
    'get_workgroup',
    'get_workgroup_output',
]

@pulumi.output_type
class GetWorkgroupResult:
    def __init__(__self__, workgroup=None):
        if workgroup and not isinstance(workgroup, dict):
            raise TypeError("Expected argument 'workgroup' to be a dict")
        pulumi.set(__self__, "workgroup", workgroup)

    @property
    @pulumi.getter
    def workgroup(self) -> Optional['outputs.Workgroup']:
        return pulumi.get(self, "workgroup")


class AwaitableGetWorkgroupResult(GetWorkgroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkgroupResult(
            workgroup=self.workgroup)


def get_workgroup(workgroup_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkgroupResult:
    """
    Definition of AWS::RedshiftServerless::Workgroup Resource Type
    """
    __args__ = dict()
    __args__['workgroupName'] = workgroup_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:redshiftserverless:getWorkgroup', __args__, opts=opts, typ=GetWorkgroupResult).value

    return AwaitableGetWorkgroupResult(
        workgroup=__ret__.workgroup)


@_utilities.lift_output_func(get_workgroup)
def get_workgroup_output(workgroup_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkgroupResult]:
    """
    Definition of AWS::RedshiftServerless::Workgroup Resource Type
    """
    ...
