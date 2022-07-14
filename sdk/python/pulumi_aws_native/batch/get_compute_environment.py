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
    'GetComputeEnvironmentResult',
    'AwaitableGetComputeEnvironmentResult',
    'get_compute_environment',
    'get_compute_environment_output',
]

@pulumi.output_type
class GetComputeEnvironmentResult:
    def __init__(__self__, compute_environment_arn=None, compute_resources=None, service_role=None, state=None, unmanagedv_cpus=None, update_policy=None):
        if compute_environment_arn and not isinstance(compute_environment_arn, str):
            raise TypeError("Expected argument 'compute_environment_arn' to be a str")
        pulumi.set(__self__, "compute_environment_arn", compute_environment_arn)
        if compute_resources and not isinstance(compute_resources, dict):
            raise TypeError("Expected argument 'compute_resources' to be a dict")
        pulumi.set(__self__, "compute_resources", compute_resources)
        if service_role and not isinstance(service_role, str):
            raise TypeError("Expected argument 'service_role' to be a str")
        pulumi.set(__self__, "service_role", service_role)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if unmanagedv_cpus and not isinstance(unmanagedv_cpus, int):
            raise TypeError("Expected argument 'unmanagedv_cpus' to be a int")
        pulumi.set(__self__, "unmanagedv_cpus", unmanagedv_cpus)
        if update_policy and not isinstance(update_policy, dict):
            raise TypeError("Expected argument 'update_policy' to be a dict")
        pulumi.set(__self__, "update_policy", update_policy)

    @property
    @pulumi.getter(name="computeEnvironmentArn")
    def compute_environment_arn(self) -> Optional[str]:
        return pulumi.get(self, "compute_environment_arn")

    @property
    @pulumi.getter(name="computeResources")
    def compute_resources(self) -> Optional['outputs.ComputeEnvironmentComputeResources']:
        return pulumi.get(self, "compute_resources")

    @property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> Optional[str]:
        return pulumi.get(self, "service_role")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="unmanagedvCpus")
    def unmanagedv_cpus(self) -> Optional[int]:
        return pulumi.get(self, "unmanagedv_cpus")

    @property
    @pulumi.getter(name="updatePolicy")
    def update_policy(self) -> Optional['outputs.ComputeEnvironmentUpdatePolicy']:
        return pulumi.get(self, "update_policy")


class AwaitableGetComputeEnvironmentResult(GetComputeEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetComputeEnvironmentResult(
            compute_environment_arn=self.compute_environment_arn,
            compute_resources=self.compute_resources,
            service_role=self.service_role,
            state=self.state,
            unmanagedv_cpus=self.unmanagedv_cpus,
            update_policy=self.update_policy)


def get_compute_environment(compute_environment_arn: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetComputeEnvironmentResult:
    """
    Resource Type definition for AWS::Batch::ComputeEnvironment
    """
    __args__ = dict()
    __args__['computeEnvironmentArn'] = compute_environment_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:batch:getComputeEnvironment', __args__, opts=opts, typ=GetComputeEnvironmentResult).value

    return AwaitableGetComputeEnvironmentResult(
        compute_environment_arn=__ret__.compute_environment_arn,
        compute_resources=__ret__.compute_resources,
        service_role=__ret__.service_role,
        state=__ret__.state,
        unmanagedv_cpus=__ret__.unmanagedv_cpus,
        update_policy=__ret__.update_policy)


@_utilities.lift_output_func(get_compute_environment)
def get_compute_environment_output(compute_environment_arn: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetComputeEnvironmentResult]:
    """
    Resource Type definition for AWS::Batch::ComputeEnvironment
    """
    ...
