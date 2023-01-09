# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'NamespaceTagArgs',
    'NamespaceArgs',
    'WorkgroupConfigParameterArgs',
    'WorkgroupEndpointArgs',
    'WorkgroupNetworkInterfaceArgs',
    'WorkgroupTagArgs',
    'WorkgroupVpcEndpointArgs',
    'WorkgroupArgs',
]

@pulumi.input_type
class NamespaceTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class NamespaceArgs:
    def __init__(__self__, *,
                 admin_username: Optional[pulumi.Input[str]] = None,
                 creation_date: Optional[pulumi.Input[str]] = None,
                 db_name: Optional[pulumi.Input[str]] = None,
                 default_iam_role_arn: Optional[pulumi.Input[str]] = None,
                 iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 log_exports: Optional[pulumi.Input[Sequence[pulumi.Input['NamespaceLogExport']]]] = None,
                 namespace_arn: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['NamespaceStatus']] = None):
        if admin_username is not None:
            pulumi.set(__self__, "admin_username", admin_username)
        if creation_date is not None:
            pulumi.set(__self__, "creation_date", creation_date)
        if db_name is not None:
            pulumi.set(__self__, "db_name", db_name)
        if default_iam_role_arn is not None:
            pulumi.set(__self__, "default_iam_role_arn", default_iam_role_arn)
        if iam_roles is not None:
            pulumi.set(__self__, "iam_roles", iam_roles)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if log_exports is not None:
            pulumi.set(__self__, "log_exports", log_exports)
        if namespace_arn is not None:
            pulumi.set(__self__, "namespace_arn", namespace_arn)
        if namespace_id is not None:
            pulumi.set(__self__, "namespace_id", namespace_id)
        if namespace_name is not None:
            pulumi.set(__self__, "namespace_name", namespace_name)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "admin_username")

    @admin_username.setter
    def admin_username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "admin_username", value)

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "creation_date")

    @creation_date.setter
    def creation_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "creation_date", value)

    @property
    @pulumi.getter(name="dbName")
    def db_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "db_name")

    @db_name.setter
    def db_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_name", value)

    @property
    @pulumi.getter(name="defaultIamRoleArn")
    def default_iam_role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_iam_role_arn")

    @default_iam_role_arn.setter
    def default_iam_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_iam_role_arn", value)

    @property
    @pulumi.getter(name="iamRoles")
    def iam_roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "iam_roles")

    @iam_roles.setter
    def iam_roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "iam_roles", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="logExports")
    def log_exports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NamespaceLogExport']]]]:
        return pulumi.get(self, "log_exports")

    @log_exports.setter
    def log_exports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NamespaceLogExport']]]]):
        pulumi.set(self, "log_exports", value)

    @property
    @pulumi.getter(name="namespaceArn")
    def namespace_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "namespace_arn")

    @namespace_arn.setter
    def namespace_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_arn", value)

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "namespace_id")

    @namespace_id.setter
    def namespace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_id", value)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['NamespaceStatus']]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['NamespaceStatus']]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class WorkgroupConfigParameterArgs:
    def __init__(__self__, *,
                 parameter_key: Optional[pulumi.Input[str]] = None,
                 parameter_value: Optional[pulumi.Input[str]] = None):
        if parameter_key is not None:
            pulumi.set(__self__, "parameter_key", parameter_key)
        if parameter_value is not None:
            pulumi.set(__self__, "parameter_value", parameter_value)

    @property
    @pulumi.getter(name="parameterKey")
    def parameter_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "parameter_key")

    @parameter_key.setter
    def parameter_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameter_key", value)

    @property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "parameter_value")

    @parameter_value.setter
    def parameter_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameter_value", value)


@pulumi.input_type
class WorkgroupEndpointArgs:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 vpc_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input['WorkgroupVpcEndpointArgs']]]] = None):
        if address is not None:
            pulumi.set(__self__, "address", address)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if vpc_endpoints is not None:
            pulumi.set(__self__, "vpc_endpoints", vpc_endpoints)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="vpcEndpoints")
    def vpc_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkgroupVpcEndpointArgs']]]]:
        return pulumi.get(self, "vpc_endpoints")

    @vpc_endpoints.setter
    def vpc_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkgroupVpcEndpointArgs']]]]):
        pulumi.set(self, "vpc_endpoints", value)


@pulumi.input_type
class WorkgroupNetworkInterfaceArgs:
    def __init__(__self__, *,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 private_ip_address: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None):
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if network_interface_id is not None:
            pulumi.set(__self__, "network_interface_id", network_interface_id)
        if private_ip_address is not None:
            pulumi.set(__self__, "private_ip_address", private_ip_address)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "network_interface_id")

    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_interface_id", value)

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "private_ip_address")

    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_ip_address", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)


@pulumi.input_type
class WorkgroupTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class WorkgroupVpcEndpointArgs:
    def __init__(__self__, *,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input['WorkgroupNetworkInterfaceArgs']]]] = None,
                 vpc_endpoint_id: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        if network_interfaces is not None:
            pulumi.set(__self__, "network_interfaces", network_interfaces)
        if vpc_endpoint_id is not None:
            pulumi.set(__self__, "vpc_endpoint_id", vpc_endpoint_id)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkgroupNetworkInterfaceArgs']]]]:
        return pulumi.get(self, "network_interfaces")

    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkgroupNetworkInterfaceArgs']]]]):
        pulumi.set(self, "network_interfaces", value)

    @property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "vpc_endpoint_id")

    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_endpoint_id", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


@pulumi.input_type
class WorkgroupArgs:
    def __init__(__self__, *,
                 base_capacity: Optional[pulumi.Input[int]] = None,
                 config_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['WorkgroupConfigParameterArgs']]]] = None,
                 creation_date: Optional[pulumi.Input[str]] = None,
                 endpoint: Optional[pulumi.Input['WorkgroupEndpointArgs']] = None,
                 enhanced_vpc_routing: Optional[pulumi.Input[bool]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 publicly_accessible: Optional[pulumi.Input[bool]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input['WorkgroupStatus']] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 workgroup_arn: Optional[pulumi.Input[str]] = None,
                 workgroup_id: Optional[pulumi.Input[str]] = None,
                 workgroup_name: Optional[pulumi.Input[str]] = None):
        if base_capacity is not None:
            pulumi.set(__self__, "base_capacity", base_capacity)
        if config_parameters is not None:
            pulumi.set(__self__, "config_parameters", config_parameters)
        if creation_date is not None:
            pulumi.set(__self__, "creation_date", creation_date)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if enhanced_vpc_routing is not None:
            pulumi.set(__self__, "enhanced_vpc_routing", enhanced_vpc_routing)
        if namespace_name is not None:
            pulumi.set(__self__, "namespace_name", namespace_name)
        if publicly_accessible is not None:
            pulumi.set(__self__, "publicly_accessible", publicly_accessible)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)
        if workgroup_arn is not None:
            pulumi.set(__self__, "workgroup_arn", workgroup_arn)
        if workgroup_id is not None:
            pulumi.set(__self__, "workgroup_id", workgroup_id)
        if workgroup_name is not None:
            pulumi.set(__self__, "workgroup_name", workgroup_name)

    @property
    @pulumi.getter(name="baseCapacity")
    def base_capacity(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "base_capacity")

    @base_capacity.setter
    def base_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "base_capacity", value)

    @property
    @pulumi.getter(name="configParameters")
    def config_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkgroupConfigParameterArgs']]]]:
        return pulumi.get(self, "config_parameters")

    @config_parameters.setter
    def config_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkgroupConfigParameterArgs']]]]):
        pulumi.set(self, "config_parameters", value)

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "creation_date")

    @creation_date.setter
    def creation_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "creation_date", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input['WorkgroupEndpointArgs']]:
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input['WorkgroupEndpointArgs']]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter(name="enhancedVpcRouting")
    def enhanced_vpc_routing(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enhanced_vpc_routing")

    @enhanced_vpc_routing.setter
    def enhanced_vpc_routing(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enhanced_vpc_routing", value)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "publicly_accessible")

    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "publicly_accessible", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['WorkgroupStatus']]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['WorkgroupStatus']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="workgroupArn")
    def workgroup_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "workgroup_arn")

    @workgroup_arn.setter
    def workgroup_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workgroup_arn", value)

    @property
    @pulumi.getter(name="workgroupId")
    def workgroup_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "workgroup_id")

    @workgroup_id.setter
    def workgroup_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workgroup_id", value)

    @property
    @pulumi.getter(name="workgroupName")
    def workgroup_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "workgroup_name")

    @workgroup_name.setter
    def workgroup_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workgroup_name", value)


