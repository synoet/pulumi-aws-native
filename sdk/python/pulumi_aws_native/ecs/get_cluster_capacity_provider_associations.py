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
    'GetClusterCapacityProviderAssociationsResult',
    'AwaitableGetClusterCapacityProviderAssociationsResult',
    'get_cluster_capacity_provider_associations',
    'get_cluster_capacity_provider_associations_output',
]

@pulumi.output_type
class GetClusterCapacityProviderAssociationsResult:
    def __init__(__self__, capacity_providers=None, default_capacity_provider_strategy=None):
        if capacity_providers and not isinstance(capacity_providers, list):
            raise TypeError("Expected argument 'capacity_providers' to be a list")
        pulumi.set(__self__, "capacity_providers", capacity_providers)
        if default_capacity_provider_strategy and not isinstance(default_capacity_provider_strategy, list):
            raise TypeError("Expected argument 'default_capacity_provider_strategy' to be a list")
        pulumi.set(__self__, "default_capacity_provider_strategy", default_capacity_provider_strategy)

    @property
    @pulumi.getter(name="capacityProviders")
    def capacity_providers(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "capacity_providers")

    @property
    @pulumi.getter(name="defaultCapacityProviderStrategy")
    def default_capacity_provider_strategy(self) -> Optional[Sequence['outputs.ClusterCapacityProviderAssociationsCapacityProviderStrategy']]:
        return pulumi.get(self, "default_capacity_provider_strategy")


class AwaitableGetClusterCapacityProviderAssociationsResult(GetClusterCapacityProviderAssociationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterCapacityProviderAssociationsResult(
            capacity_providers=self.capacity_providers,
            default_capacity_provider_strategy=self.default_capacity_provider_strategy)


def get_cluster_capacity_provider_associations(cluster: Optional[str] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterCapacityProviderAssociationsResult:
    """
    Associate a set of ECS Capacity Providers with a specified ECS Cluster
    """
    __args__ = dict()
    __args__['cluster'] = cluster
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ecs:getClusterCapacityProviderAssociations', __args__, opts=opts, typ=GetClusterCapacityProviderAssociationsResult).value

    return AwaitableGetClusterCapacityProviderAssociationsResult(
        capacity_providers=__ret__.capacity_providers,
        default_capacity_provider_strategy=__ret__.default_capacity_provider_strategy)


@_utilities.lift_output_func(get_cluster_capacity_provider_associations)
def get_cluster_capacity_provider_associations_output(cluster: Optional[pulumi.Input[str]] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterCapacityProviderAssociationsResult]:
    """
    Associate a set of ECS Capacity Providers with a specified ECS Cluster
    """
    ...
