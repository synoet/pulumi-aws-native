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

__all__ = ['DBSubnetGroupArgs', 'DBSubnetGroup']

@pulumi.input_type
class DBSubnetGroupArgs:
    def __init__(__self__, *,
                 d_b_subnet_group_description: pulumi.Input[str],
                 subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 d_b_subnet_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DBSubnetGroupTagArgs']]]] = None):
        """
        The set of arguments for constructing a DBSubnetGroup resource.
        """
        pulumi.set(__self__, "d_b_subnet_group_description", d_b_subnet_group_description)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if d_b_subnet_group_name is not None:
            pulumi.set(__self__, "d_b_subnet_group_name", d_b_subnet_group_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dBSubnetGroupDescription")
    def d_b_subnet_group_description(self) -> pulumi.Input[str]:
        return pulumi.get(self, "d_b_subnet_group_description")

    @d_b_subnet_group_description.setter
    def d_b_subnet_group_description(self, value: pulumi.Input[str]):
        pulumi.set(self, "d_b_subnet_group_description", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="dBSubnetGroupName")
    def d_b_subnet_group_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "d_b_subnet_group_name")

    @d_b_subnet_group_name.setter
    def d_b_subnet_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "d_b_subnet_group_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DBSubnetGroupTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DBSubnetGroupTagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""DBSubnetGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class DBSubnetGroup(pulumi.CustomResource):
    warnings.warn("""DBSubnetGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 d_b_subnet_group_description: Optional[pulumi.Input[str]] = None,
                 d_b_subnet_group_name: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DBSubnetGroupTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Neptune::DBSubnetGroup

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DBSubnetGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Neptune::DBSubnetGroup

        :param str resource_name: The name of the resource.
        :param DBSubnetGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DBSubnetGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 d_b_subnet_group_description: Optional[pulumi.Input[str]] = None,
                 d_b_subnet_group_name: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DBSubnetGroupTagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""DBSubnetGroup is deprecated: DBSubnetGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DBSubnetGroupArgs.__new__(DBSubnetGroupArgs)

            if d_b_subnet_group_description is None and not opts.urn:
                raise TypeError("Missing required property 'd_b_subnet_group_description'")
            __props__.__dict__["d_b_subnet_group_description"] = d_b_subnet_group_description
            __props__.__dict__["d_b_subnet_group_name"] = d_b_subnet_group_name
            if subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_ids'")
            __props__.__dict__["subnet_ids"] = subnet_ids
            __props__.__dict__["tags"] = tags
        super(DBSubnetGroup, __self__).__init__(
            'aws-native:neptune:DBSubnetGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DBSubnetGroup':
        """
        Get an existing DBSubnetGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DBSubnetGroupArgs.__new__(DBSubnetGroupArgs)

        __props__.__dict__["d_b_subnet_group_description"] = None
        __props__.__dict__["d_b_subnet_group_name"] = None
        __props__.__dict__["subnet_ids"] = None
        __props__.__dict__["tags"] = None
        return DBSubnetGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dBSubnetGroupDescription")
    def d_b_subnet_group_description(self) -> pulumi.Output[str]:
        return pulumi.get(self, "d_b_subnet_group_description")

    @property
    @pulumi.getter(name="dBSubnetGroupName")
    def d_b_subnet_group_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "d_b_subnet_group_name")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DBSubnetGroupTag']]]:
        return pulumi.get(self, "tags")

