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
from ._inputs import *

__all__ = ['ConnectionAliasArgs', 'ConnectionAlias']

@pulumi.input_type
class ConnectionAliasArgs:
    def __init__(__self__, *,
                 connection_string: pulumi.Input[str],
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionAliasTagArgs']]]] = None):
        """
        The set of arguments for constructing a ConnectionAlias resource.
        """
        pulumi.set(__self__, "connection_string", connection_string)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Input[str]:
        return pulumi.get(self, "connection_string")

    @connection_string.setter
    def connection_string(self, value: pulumi.Input[str]):
        pulumi.set(self, "connection_string", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionAliasTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionAliasTagArgs']]]]):
        pulumi.set(self, "tags", value)


class ConnectionAlias(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_string: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionAliasTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::WorkSpaces::ConnectionAlias

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectionAliasArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::WorkSpaces::ConnectionAlias

        :param str resource_name: The name of the resource.
        :param ConnectionAliasArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectionAliasArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_string: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionAliasTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectionAliasArgs.__new__(ConnectionAliasArgs)

            if connection_string is None and not opts.urn:
                raise TypeError("Missing required property 'connection_string'")
            __props__.__dict__["connection_string"] = connection_string
            __props__.__dict__["tags"] = tags
            __props__.__dict__["alias_id"] = None
            __props__.__dict__["associations"] = None
            __props__.__dict__["connection_alias_state"] = None
        super(ConnectionAlias, __self__).__init__(
            'aws-native:workspaces:ConnectionAlias',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConnectionAlias':
        """
        Get an existing ConnectionAlias resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectionAliasArgs.__new__(ConnectionAliasArgs)

        __props__.__dict__["alias_id"] = None
        __props__.__dict__["associations"] = None
        __props__.__dict__["connection_alias_state"] = None
        __props__.__dict__["connection_string"] = None
        __props__.__dict__["tags"] = None
        return ConnectionAlias(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aliasId")
    def alias_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "alias_id")

    @property
    @pulumi.getter
    def associations(self) -> pulumi.Output[Sequence['outputs.ConnectionAliasAssociation']]:
        return pulumi.get(self, "associations")

    @property
    @pulumi.getter(name="connectionAliasState")
    def connection_alias_state(self) -> pulumi.Output['ConnectionAliasState']:
        return pulumi.get(self, "connection_alias_state")

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Output[str]:
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ConnectionAliasTag']]]:
        return pulumi.get(self, "tags")

