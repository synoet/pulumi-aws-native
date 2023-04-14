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
    'GetDeploymentStrategyResult',
    'AwaitableGetDeploymentStrategyResult',
    'get_deployment_strategy',
    'get_deployment_strategy_output',
]

@pulumi.output_type
class GetDeploymentStrategyResult:
    def __init__(__self__, deployment_duration_in_minutes=None, description=None, final_bake_time_in_minutes=None, growth_factor=None, growth_type=None, id=None, tags=None):
        if deployment_duration_in_minutes and not isinstance(deployment_duration_in_minutes, float):
            raise TypeError("Expected argument 'deployment_duration_in_minutes' to be a float")
        pulumi.set(__self__, "deployment_duration_in_minutes", deployment_duration_in_minutes)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if final_bake_time_in_minutes and not isinstance(final_bake_time_in_minutes, float):
            raise TypeError("Expected argument 'final_bake_time_in_minutes' to be a float")
        pulumi.set(__self__, "final_bake_time_in_minutes", final_bake_time_in_minutes)
        if growth_factor and not isinstance(growth_factor, float):
            raise TypeError("Expected argument 'growth_factor' to be a float")
        pulumi.set(__self__, "growth_factor", growth_factor)
        if growth_type and not isinstance(growth_type, str):
            raise TypeError("Expected argument 'growth_type' to be a str")
        pulumi.set(__self__, "growth_type", growth_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="deploymentDurationInMinutes")
    def deployment_duration_in_minutes(self) -> Optional[float]:
        return pulumi.get(self, "deployment_duration_in_minutes")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="finalBakeTimeInMinutes")
    def final_bake_time_in_minutes(self) -> Optional[float]:
        return pulumi.get(self, "final_bake_time_in_minutes")

    @property
    @pulumi.getter(name="growthFactor")
    def growth_factor(self) -> Optional[float]:
        return pulumi.get(self, "growth_factor")

    @property
    @pulumi.getter(name="growthType")
    def growth_type(self) -> Optional[str]:
        return pulumi.get(self, "growth_type")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DeploymentStrategyTags']]:
        return pulumi.get(self, "tags")


class AwaitableGetDeploymentStrategyResult(GetDeploymentStrategyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeploymentStrategyResult(
            deployment_duration_in_minutes=self.deployment_duration_in_minutes,
            description=self.description,
            final_bake_time_in_minutes=self.final_bake_time_in_minutes,
            growth_factor=self.growth_factor,
            growth_type=self.growth_type,
            id=self.id,
            tags=self.tags)


def get_deployment_strategy(id: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeploymentStrategyResult:
    """
    Resource Type definition for AWS::AppConfig::DeploymentStrategy
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:appconfig:getDeploymentStrategy', __args__, opts=opts, typ=GetDeploymentStrategyResult).value

    return AwaitableGetDeploymentStrategyResult(
        deployment_duration_in_minutes=__ret__.deployment_duration_in_minutes,
        description=__ret__.description,
        final_bake_time_in_minutes=__ret__.final_bake_time_in_minutes,
        growth_factor=__ret__.growth_factor,
        growth_type=__ret__.growth_type,
        id=__ret__.id,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_deployment_strategy)
def get_deployment_strategy_output(id: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeploymentStrategyResult]:
    """
    Resource Type definition for AWS::AppConfig::DeploymentStrategy
    """
    ...
