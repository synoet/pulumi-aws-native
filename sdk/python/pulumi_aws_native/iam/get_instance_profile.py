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
    'GetInstanceProfileResult',
    'AwaitableGetInstanceProfileResult',
    'get_instance_profile',
    'get_instance_profile_output',
]

@pulumi.output_type
class GetInstanceProfileResult:
    def __init__(__self__, arn=None, roles=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if roles and not isinstance(roles, list):
            raise TypeError("Expected argument 'roles' to be a list")
        pulumi.set(__self__, "roles", roles)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the instance profile.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[str]]:
        """
        The name of the role to associate with the instance profile. Only one role can be assigned to an EC2 instance at a time, and all applications on the instance share the same role and permissions.
        """
        return pulumi.get(self, "roles")


class AwaitableGetInstanceProfileResult(GetInstanceProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceProfileResult(
            arn=self.arn,
            roles=self.roles)


def get_instance_profile(instance_profile_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceProfileResult:
    """
    Resource Type definition for AWS::IAM::InstanceProfile


    :param str instance_profile_name: The name of the instance profile to create.
    """
    __args__ = dict()
    __args__['instanceProfileName'] = instance_profile_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iam:getInstanceProfile', __args__, opts=opts, typ=GetInstanceProfileResult).value

    return AwaitableGetInstanceProfileResult(
        arn=__ret__.arn,
        roles=__ret__.roles)


@_utilities.lift_output_func(get_instance_profile)
def get_instance_profile_output(instance_profile_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceProfileResult]:
    """
    Resource Type definition for AWS::IAM::InstanceProfile


    :param str instance_profile_name: The name of the instance profile to create.
    """
    ...
