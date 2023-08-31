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
from ._inputs import *

__all__ = ['GroupMembershipArgs', 'GroupMembership']

@pulumi.input_type
class GroupMembershipArgs:
    def __init__(__self__, *,
                 group_id: pulumi.Input[str],
                 identity_store_id: pulumi.Input[str],
                 member_id: pulumi.Input['GroupMembershipMemberIdArgs']):
        """
        The set of arguments for constructing a GroupMembership resource.
        :param pulumi.Input[str] group_id: The unique identifier for a group in the identity store.
        :param pulumi.Input[str] identity_store_id: The globally unique identifier for the identity store.
        :param pulumi.Input['GroupMembershipMemberIdArgs'] member_id: An object containing the identifier of a group member.
        """
        pulumi.set(__self__, "group_id", group_id)
        pulumi.set(__self__, "identity_store_id", identity_store_id)
        pulumi.set(__self__, "member_id", member_id)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[str]:
        """
        The unique identifier for a group in the identity store.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> pulumi.Input[str]:
        """
        The globally unique identifier for the identity store.
        """
        return pulumi.get(self, "identity_store_id")

    @identity_store_id.setter
    def identity_store_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "identity_store_id", value)

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> pulumi.Input['GroupMembershipMemberIdArgs']:
        """
        An object containing the identifier of a group member.
        """
        return pulumi.get(self, "member_id")

    @member_id.setter
    def member_id(self, value: pulumi.Input['GroupMembershipMemberIdArgs']):
        pulumi.set(self, "member_id", value)


class GroupMembership(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 identity_store_id: Optional[pulumi.Input[str]] = None,
                 member_id: Optional[pulumi.Input[pulumi.InputType['GroupMembershipMemberIdArgs']]] = None,
                 __props__=None):
        """
        Resource Type Definition for AWS:IdentityStore::GroupMembership

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: The unique identifier for a group in the identity store.
        :param pulumi.Input[str] identity_store_id: The globally unique identifier for the identity store.
        :param pulumi.Input[pulumi.InputType['GroupMembershipMemberIdArgs']] member_id: An object containing the identifier of a group member.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroupMembershipArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type Definition for AWS:IdentityStore::GroupMembership

        :param str resource_name: The name of the resource.
        :param GroupMembershipArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupMembershipArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 identity_store_id: Optional[pulumi.Input[str]] = None,
                 member_id: Optional[pulumi.Input[pulumi.InputType['GroupMembershipMemberIdArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GroupMembershipArgs.__new__(GroupMembershipArgs)

            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            if identity_store_id is None and not opts.urn:
                raise TypeError("Missing required property 'identity_store_id'")
            __props__.__dict__["identity_store_id"] = identity_store_id
            if member_id is None and not opts.urn:
                raise TypeError("Missing required property 'member_id'")
            __props__.__dict__["member_id"] = member_id
            __props__.__dict__["membership_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["identity_store_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(GroupMembership, __self__).__init__(
            'aws-native:identitystore:GroupMembership',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GroupMembership':
        """
        Get an existing GroupMembership resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GroupMembershipArgs.__new__(GroupMembershipArgs)

        __props__.__dict__["group_id"] = None
        __props__.__dict__["identity_store_id"] = None
        __props__.__dict__["member_id"] = None
        __props__.__dict__["membership_id"] = None
        return GroupMembership(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        The unique identifier for a group in the identity store.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> pulumi.Output[str]:
        """
        The globally unique identifier for the identity store.
        """
        return pulumi.get(self, "identity_store_id")

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> pulumi.Output['outputs.GroupMembershipMemberId']:
        """
        An object containing the identifier of a group member.
        """
        return pulumi.get(self, "member_id")

    @property
    @pulumi.getter(name="membershipId")
    def membership_id(self) -> pulumi.Output[str]:
        """
        The identifier for a GroupMembership in the identity store.
        """
        return pulumi.get(self, "membership_id")

