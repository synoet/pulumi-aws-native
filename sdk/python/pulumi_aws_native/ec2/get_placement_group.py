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
    'GetPlacementGroupResult',
    'AwaitableGetPlacementGroupResult',
    'get_placement_group',
    'get_placement_group_output',
]

@pulumi.output_type
class GetPlacementGroupResult:
    def __init__(__self__, group_name=None):
        if group_name and not isinstance(group_name, str):
            raise TypeError("Expected argument 'group_name' to be a str")
        pulumi.set(__self__, "group_name", group_name)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[str]:
        """
        The Group Name of Placement Group.
        """
        return pulumi.get(self, "group_name")


class AwaitableGetPlacementGroupResult(GetPlacementGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPlacementGroupResult(
            group_name=self.group_name)


def get_placement_group(group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPlacementGroupResult:
    """
    Resource Type definition for AWS::EC2::PlacementGroup


    :param str group_name: The Group Name of Placement Group.
    """
    __args__ = dict()
    __args__['groupName'] = group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getPlacementGroup', __args__, opts=opts, typ=GetPlacementGroupResult).value

    return AwaitableGetPlacementGroupResult(
        group_name=__ret__.group_name)


@_utilities.lift_output_func(get_placement_group)
def get_placement_group_output(group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPlacementGroupResult]:
    """
    Resource Type definition for AWS::EC2::PlacementGroup


    :param str group_name: The Group Name of Placement Group.
    """
    ...
