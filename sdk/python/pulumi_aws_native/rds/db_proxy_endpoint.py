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

__all__ = ['DbProxyEndpointArgs', 'DbProxyEndpoint']

@pulumi.input_type
class DbProxyEndpointArgs:
    def __init__(__self__, *,
                 db_proxy_name: pulumi.Input[str],
                 vpc_subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 db_proxy_endpoint_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DbProxyEndpointTagFormatArgs']]]] = None,
                 target_role: Optional[pulumi.Input['DbProxyEndpointTargetRole']] = None,
                 vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DbProxyEndpoint resource.
        :param pulumi.Input[str] db_proxy_name: The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] vpc_subnet_ids: VPC subnet IDs to associate with the new DB proxy endpoint.
        :param pulumi.Input[str] db_proxy_endpoint_name: The identifier for the DB proxy endpoint. This name must be unique for all DB proxy endpoints owned by your AWS account in the specified AWS Region.
        :param pulumi.Input[Sequence[pulumi.Input['DbProxyEndpointTagFormatArgs']]] tags: An optional set of key-value pairs to associate arbitrary data of your choosing with the DB proxy endpoint.
        :param pulumi.Input['DbProxyEndpointTargetRole'] target_role: A value that indicates whether the DB proxy endpoint can be used for read/write or read-only operations.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] vpc_security_group_ids: VPC security group IDs to associate with the new DB proxy endpoint.
        """
        pulumi.set(__self__, "db_proxy_name", db_proxy_name)
        pulumi.set(__self__, "vpc_subnet_ids", vpc_subnet_ids)
        if db_proxy_endpoint_name is not None:
            pulumi.set(__self__, "db_proxy_endpoint_name", db_proxy_endpoint_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if target_role is not None:
            pulumi.set(__self__, "target_role", target_role)
        if vpc_security_group_ids is not None:
            pulumi.set(__self__, "vpc_security_group_ids", vpc_security_group_ids)

    @property
    @pulumi.getter(name="dbProxyName")
    def db_proxy_name(self) -> pulumi.Input[str]:
        """
        The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.
        """
        return pulumi.get(self, "db_proxy_name")

    @db_proxy_name.setter
    def db_proxy_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "db_proxy_name", value)

    @property
    @pulumi.getter(name="vpcSubnetIds")
    def vpc_subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        VPC subnet IDs to associate with the new DB proxy endpoint.
        """
        return pulumi.get(self, "vpc_subnet_ids")

    @vpc_subnet_ids.setter
    def vpc_subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "vpc_subnet_ids", value)

    @property
    @pulumi.getter(name="dbProxyEndpointName")
    def db_proxy_endpoint_name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the DB proxy endpoint. This name must be unique for all DB proxy endpoints owned by your AWS account in the specified AWS Region.
        """
        return pulumi.get(self, "db_proxy_endpoint_name")

    @db_proxy_endpoint_name.setter
    def db_proxy_endpoint_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_proxy_endpoint_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DbProxyEndpointTagFormatArgs']]]]:
        """
        An optional set of key-value pairs to associate arbitrary data of your choosing with the DB proxy endpoint.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DbProxyEndpointTagFormatArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="targetRole")
    def target_role(self) -> Optional[pulumi.Input['DbProxyEndpointTargetRole']]:
        """
        A value that indicates whether the DB proxy endpoint can be used for read/write or read-only operations.
        """
        return pulumi.get(self, "target_role")

    @target_role.setter
    def target_role(self, value: Optional[pulumi.Input['DbProxyEndpointTargetRole']]):
        pulumi.set(self, "target_role", value)

    @property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        VPC security group IDs to associate with the new DB proxy endpoint.
        """
        return pulumi.get(self, "vpc_security_group_ids")

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "vpc_security_group_ids", value)


class DbProxyEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_proxy_endpoint_name: Optional[pulumi.Input[str]] = None,
                 db_proxy_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DbProxyEndpointTagFormatArgs']]]]] = None,
                 target_role: Optional[pulumi.Input['DbProxyEndpointTargetRole']] = None,
                 vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpc_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::RDS::DBProxyEndpoint.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] db_proxy_endpoint_name: The identifier for the DB proxy endpoint. This name must be unique for all DB proxy endpoints owned by your AWS account in the specified AWS Region.
        :param pulumi.Input[str] db_proxy_name: The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DbProxyEndpointTagFormatArgs']]]] tags: An optional set of key-value pairs to associate arbitrary data of your choosing with the DB proxy endpoint.
        :param pulumi.Input['DbProxyEndpointTargetRole'] target_role: A value that indicates whether the DB proxy endpoint can be used for read/write or read-only operations.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] vpc_security_group_ids: VPC security group IDs to associate with the new DB proxy endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] vpc_subnet_ids: VPC subnet IDs to associate with the new DB proxy endpoint.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DbProxyEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::RDS::DBProxyEndpoint.

        :param str resource_name: The name of the resource.
        :param DbProxyEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DbProxyEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_proxy_endpoint_name: Optional[pulumi.Input[str]] = None,
                 db_proxy_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DbProxyEndpointTagFormatArgs']]]]] = None,
                 target_role: Optional[pulumi.Input['DbProxyEndpointTargetRole']] = None,
                 vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpc_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DbProxyEndpointArgs.__new__(DbProxyEndpointArgs)

            __props__.__dict__["db_proxy_endpoint_name"] = db_proxy_endpoint_name
            if db_proxy_name is None and not opts.urn:
                raise TypeError("Missing required property 'db_proxy_name'")
            __props__.__dict__["db_proxy_name"] = db_proxy_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["target_role"] = target_role
            __props__.__dict__["vpc_security_group_ids"] = vpc_security_group_ids
            if vpc_subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_subnet_ids'")
            __props__.__dict__["vpc_subnet_ids"] = vpc_subnet_ids
            __props__.__dict__["db_proxy_endpoint_arn"] = None
            __props__.__dict__["endpoint"] = None
            __props__.__dict__["is_default"] = None
            __props__.__dict__["vpc_id"] = None
        super(DbProxyEndpoint, __self__).__init__(
            'aws-native:rds:DbProxyEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DbProxyEndpoint':
        """
        Get an existing DbProxyEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DbProxyEndpointArgs.__new__(DbProxyEndpointArgs)

        __props__.__dict__["db_proxy_endpoint_arn"] = None
        __props__.__dict__["db_proxy_endpoint_name"] = None
        __props__.__dict__["db_proxy_name"] = None
        __props__.__dict__["endpoint"] = None
        __props__.__dict__["is_default"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_role"] = None
        __props__.__dict__["vpc_id"] = None
        __props__.__dict__["vpc_security_group_ids"] = None
        __props__.__dict__["vpc_subnet_ids"] = None
        return DbProxyEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dbProxyEndpointArn")
    def db_proxy_endpoint_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) for the DB proxy endpoint.
        """
        return pulumi.get(self, "db_proxy_endpoint_arn")

    @property
    @pulumi.getter(name="dbProxyEndpointName")
    def db_proxy_endpoint_name(self) -> pulumi.Output[str]:
        """
        The identifier for the DB proxy endpoint. This name must be unique for all DB proxy endpoints owned by your AWS account in the specified AWS Region.
        """
        return pulumi.get(self, "db_proxy_endpoint_name")

    @property
    @pulumi.getter(name="dbProxyName")
    def db_proxy_name(self) -> pulumi.Output[str]:
        """
        The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.
        """
        return pulumi.get(self, "db_proxy_name")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        The endpoint that you can use to connect to the DB proxy. You include the endpoint value in the connection string for a database client application.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> pulumi.Output[bool]:
        """
        A value that indicates whether this endpoint is the default endpoint for the associated DB proxy. Default DB proxy endpoints always have read/write capability. Other endpoints that you associate with the DB proxy can be either read/write or read-only.
        """
        return pulumi.get(self, "is_default")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DbProxyEndpointTagFormat']]]:
        """
        An optional set of key-value pairs to associate arbitrary data of your choosing with the DB proxy endpoint.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetRole")
    def target_role(self) -> pulumi.Output[Optional['DbProxyEndpointTargetRole']]:
        """
        A value that indicates whether the DB proxy endpoint can be used for read/write or read-only operations.
        """
        return pulumi.get(self, "target_role")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        VPC ID to associate with the new DB proxy endpoint.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        VPC security group IDs to associate with the new DB proxy endpoint.
        """
        return pulumi.get(self, "vpc_security_group_ids")

    @property
    @pulumi.getter(name="vpcSubnetIds")
    def vpc_subnet_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        VPC subnet IDs to associate with the new DB proxy endpoint.
        """
        return pulumi.get(self, "vpc_subnet_ids")

