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
    'GetFirewallRuleGroupAssociationResult',
    'AwaitableGetFirewallRuleGroupAssociationResult',
    'get_firewall_rule_group_association',
    'get_firewall_rule_group_association_output',
]

@pulumi.output_type
class GetFirewallRuleGroupAssociationResult:
    def __init__(__self__, arn=None, creation_time=None, creator_request_id=None, id=None, managed_owner_name=None, modification_time=None, mutation_protection=None, name=None, priority=None, status=None, status_message=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if creator_request_id and not isinstance(creator_request_id, str):
            raise TypeError("Expected argument 'creator_request_id' to be a str")
        pulumi.set(__self__, "creator_request_id", creator_request_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed_owner_name and not isinstance(managed_owner_name, str):
            raise TypeError("Expected argument 'managed_owner_name' to be a str")
        pulumi.set(__self__, "managed_owner_name", managed_owner_name)
        if modification_time and not isinstance(modification_time, str):
            raise TypeError("Expected argument 'modification_time' to be a str")
        pulumi.set(__self__, "modification_time", modification_time)
        if mutation_protection and not isinstance(mutation_protection, str):
            raise TypeError("Expected argument 'mutation_protection' to be a str")
        pulumi.set(__self__, "mutation_protection", mutation_protection)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if priority and not isinstance(priority, int):
            raise TypeError("Expected argument 'priority' to be a int")
        pulumi.set(__self__, "priority", priority)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if status_message and not isinstance(status_message, str):
            raise TypeError("Expected argument 'status_message' to be a str")
        pulumi.set(__self__, "status_message", status_message)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Arn
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        """
        Rfc3339TimeString
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="creatorRequestId")
    def creator_request_id(self) -> Optional[str]:
        """
        The id of the creator request.
        """
        return pulumi.get(self, "creator_request_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="managedOwnerName")
    def managed_owner_name(self) -> Optional[str]:
        """
        ServicePrincipal
        """
        return pulumi.get(self, "managed_owner_name")

    @property
    @pulumi.getter(name="modificationTime")
    def modification_time(self) -> Optional[str]:
        """
        Rfc3339TimeString
        """
        return pulumi.get(self, "modification_time")

    @property
    @pulumi.getter(name="mutationProtection")
    def mutation_protection(self) -> Optional['FirewallRuleGroupAssociationMutationProtection']:
        """
        MutationProtectionStatus
        """
        return pulumi.get(self, "mutation_protection")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        FirewallRuleGroupAssociationName
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> Optional[int]:
        """
        Priority
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def status(self) -> Optional['FirewallRuleGroupAssociationStatus']:
        """
        ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> Optional[str]:
        """
        FirewallDomainListAssociationStatus
        """
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.FirewallRuleGroupAssociationTag']]:
        """
        Tags
        """
        return pulumi.get(self, "tags")


class AwaitableGetFirewallRuleGroupAssociationResult(GetFirewallRuleGroupAssociationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFirewallRuleGroupAssociationResult(
            arn=self.arn,
            creation_time=self.creation_time,
            creator_request_id=self.creator_request_id,
            id=self.id,
            managed_owner_name=self.managed_owner_name,
            modification_time=self.modification_time,
            mutation_protection=self.mutation_protection,
            name=self.name,
            priority=self.priority,
            status=self.status,
            status_message=self.status_message,
            tags=self.tags)


def get_firewall_rule_group_association(id: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFirewallRuleGroupAssociationResult:
    """
    Resource schema for AWS::Route53Resolver::FirewallRuleGroupAssociation.


    :param str id: Id
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:route53resolver:getFirewallRuleGroupAssociation', __args__, opts=opts, typ=GetFirewallRuleGroupAssociationResult).value

    return AwaitableGetFirewallRuleGroupAssociationResult(
        arn=__ret__.arn,
        creation_time=__ret__.creation_time,
        creator_request_id=__ret__.creator_request_id,
        id=__ret__.id,
        managed_owner_name=__ret__.managed_owner_name,
        modification_time=__ret__.modification_time,
        mutation_protection=__ret__.mutation_protection,
        name=__ret__.name,
        priority=__ret__.priority,
        status=__ret__.status,
        status_message=__ret__.status_message,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_firewall_rule_group_association)
def get_firewall_rule_group_association_output(id: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFirewallRuleGroupAssociationResult]:
    """
    Resource schema for AWS::Route53Resolver::FirewallRuleGroupAssociation.


    :param str id: Id
    """
    ...
