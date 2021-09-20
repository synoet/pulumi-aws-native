# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'GlobalReplicationGroupGlobalReplicationGroupMemberArgs',
    'GlobalReplicationGroupRegionalConfigurationArgs',
    'GlobalReplicationGroupReshardingConfigurationArgs',
]

@pulumi.input_type
class GlobalReplicationGroupGlobalReplicationGroupMemberArgs:
    def __init__(__self__, *,
                 replication_group_id: Optional[pulumi.Input[str]] = None,
                 replication_group_region: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input['GlobalReplicationGroupGlobalReplicationGroupMemberRole']] = None):
        """
        :param pulumi.Input[str] replication_group_id: Regionally unique identifier for the member i.e. ReplicationGroupId.
        :param pulumi.Input[str] replication_group_region: The AWS region of the Global Datastore member.
        :param pulumi.Input['GlobalReplicationGroupGlobalReplicationGroupMemberRole'] role: Indicates the role of the member, primary or secondary.
        """
        if replication_group_id is not None:
            pulumi.set(__self__, "replication_group_id", replication_group_id)
        if replication_group_region is not None:
            pulumi.set(__self__, "replication_group_region", replication_group_region)
        if role is not None:
            pulumi.set(__self__, "role", role)

    @property
    @pulumi.getter(name="replicationGroupId")
    def replication_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Regionally unique identifier for the member i.e. ReplicationGroupId.
        """
        return pulumi.get(self, "replication_group_id")

    @replication_group_id.setter
    def replication_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "replication_group_id", value)

    @property
    @pulumi.getter(name="replicationGroupRegion")
    def replication_group_region(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS region of the Global Datastore member.
        """
        return pulumi.get(self, "replication_group_region")

    @replication_group_region.setter
    def replication_group_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "replication_group_region", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input['GlobalReplicationGroupGlobalReplicationGroupMemberRole']]:
        """
        Indicates the role of the member, primary or secondary.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input['GlobalReplicationGroupGlobalReplicationGroupMemberRole']]):
        pulumi.set(self, "role", value)


@pulumi.input_type
class GlobalReplicationGroupRegionalConfigurationArgs:
    def __init__(__self__, *,
                 replication_group_id: Optional[pulumi.Input[str]] = None,
                 replication_group_region: Optional[pulumi.Input[str]] = None,
                 resharding_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['GlobalReplicationGroupReshardingConfigurationArgs']]]] = None):
        """
        :param pulumi.Input[str] replication_group_id: The replication group id of the Global Datastore member.
        :param pulumi.Input[str] replication_group_region: The AWS region of the Global Datastore member.
        :param pulumi.Input[Sequence[pulumi.Input['GlobalReplicationGroupReshardingConfigurationArgs']]] resharding_configurations: A list of PreferredAvailabilityZones objects that specifies the configuration of a node group in the resharded cluster. 
        """
        if replication_group_id is not None:
            pulumi.set(__self__, "replication_group_id", replication_group_id)
        if replication_group_region is not None:
            pulumi.set(__self__, "replication_group_region", replication_group_region)
        if resharding_configurations is not None:
            pulumi.set(__self__, "resharding_configurations", resharding_configurations)

    @property
    @pulumi.getter(name="replicationGroupId")
    def replication_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The replication group id of the Global Datastore member.
        """
        return pulumi.get(self, "replication_group_id")

    @replication_group_id.setter
    def replication_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "replication_group_id", value)

    @property
    @pulumi.getter(name="replicationGroupRegion")
    def replication_group_region(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS region of the Global Datastore member.
        """
        return pulumi.get(self, "replication_group_region")

    @replication_group_region.setter
    def replication_group_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "replication_group_region", value)

    @property
    @pulumi.getter(name="reshardingConfigurations")
    def resharding_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GlobalReplicationGroupReshardingConfigurationArgs']]]]:
        """
        A list of PreferredAvailabilityZones objects that specifies the configuration of a node group in the resharded cluster. 
        """
        return pulumi.get(self, "resharding_configurations")

    @resharding_configurations.setter
    def resharding_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GlobalReplicationGroupReshardingConfigurationArgs']]]]):
        pulumi.set(self, "resharding_configurations", value)


@pulumi.input_type
class GlobalReplicationGroupReshardingConfigurationArgs:
    def __init__(__self__, *,
                 node_group_id: Optional[pulumi.Input[str]] = None,
                 preferred_availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] node_group_id: Unique identifier for the Node Group. This is either auto-generated by ElastiCache (4-digit id) or a user supplied id.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] preferred_availability_zones: A list of preferred availability zones for the nodes of new node groups.
        """
        if node_group_id is not None:
            pulumi.set(__self__, "node_group_id", node_group_id)
        if preferred_availability_zones is not None:
            pulumi.set(__self__, "preferred_availability_zones", preferred_availability_zones)

    @property
    @pulumi.getter(name="nodeGroupId")
    def node_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier for the Node Group. This is either auto-generated by ElastiCache (4-digit id) or a user supplied id.
        """
        return pulumi.get(self, "node_group_id")

    @node_group_id.setter
    def node_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_group_id", value)

    @property
    @pulumi.getter(name="preferredAvailabilityZones")
    def preferred_availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of preferred availability zones for the nodes of new node groups.
        """
        return pulumi.get(self, "preferred_availability_zones")

    @preferred_availability_zones.setter
    def preferred_availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "preferred_availability_zones", value)


