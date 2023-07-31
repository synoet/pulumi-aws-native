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

__all__ = ['ReplicationInstanceArgs', 'ReplicationInstance']

@pulumi.input_type
class ReplicationInstanceArgs:
    def __init__(__self__, *,
                 replication_instance_class: pulumi.Input[str],
                 allocated_storage: Optional[pulumi.Input[int]] = None,
                 allow_major_version_upgrade: Optional[pulumi.Input[bool]] = None,
                 auto_minor_version_upgrade: Optional[pulumi.Input[bool]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 multi_az: Optional[pulumi.Input[bool]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 publicly_accessible: Optional[pulumi.Input[bool]] = None,
                 replication_instance_identifier: Optional[pulumi.Input[str]] = None,
                 replication_subnet_group_identifier: Optional[pulumi.Input[str]] = None,
                 resource_identifier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ReplicationInstanceTagArgs']]]] = None,
                 vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ReplicationInstance resource.
        """
        pulumi.set(__self__, "replication_instance_class", replication_instance_class)
        if allocated_storage is not None:
            pulumi.set(__self__, "allocated_storage", allocated_storage)
        if allow_major_version_upgrade is not None:
            pulumi.set(__self__, "allow_major_version_upgrade", allow_major_version_upgrade)
        if auto_minor_version_upgrade is not None:
            pulumi.set(__self__, "auto_minor_version_upgrade", auto_minor_version_upgrade)
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if engine_version is not None:
            pulumi.set(__self__, "engine_version", engine_version)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if multi_az is not None:
            pulumi.set(__self__, "multi_az", multi_az)
        if preferred_maintenance_window is not None:
            pulumi.set(__self__, "preferred_maintenance_window", preferred_maintenance_window)
        if publicly_accessible is not None:
            pulumi.set(__self__, "publicly_accessible", publicly_accessible)
        if replication_instance_identifier is not None:
            pulumi.set(__self__, "replication_instance_identifier", replication_instance_identifier)
        if replication_subnet_group_identifier is not None:
            pulumi.set(__self__, "replication_subnet_group_identifier", replication_subnet_group_identifier)
        if resource_identifier is not None:
            pulumi.set(__self__, "resource_identifier", resource_identifier)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vpc_security_group_ids is not None:
            pulumi.set(__self__, "vpc_security_group_ids", vpc_security_group_ids)

    @property
    @pulumi.getter(name="replicationInstanceClass")
    def replication_instance_class(self) -> pulumi.Input[str]:
        return pulumi.get(self, "replication_instance_class")

    @replication_instance_class.setter
    def replication_instance_class(self, value: pulumi.Input[str]):
        pulumi.set(self, "replication_instance_class", value)

    @property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "allocated_storage")

    @allocated_storage.setter
    def allocated_storage(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "allocated_storage", value)

    @property
    @pulumi.getter(name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allow_major_version_upgrade")

    @allow_major_version_upgrade.setter
    def allow_major_version_upgrade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_major_version_upgrade", value)

    @property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "auto_minor_version_upgrade")

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_minor_version_upgrade", value)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "engine_version")

    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "engine_version", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "multi_az")

    @multi_az.setter
    def multi_az(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "multi_az", value)

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "preferred_maintenance_window")

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preferred_maintenance_window", value)

    @property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "publicly_accessible")

    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "publicly_accessible", value)

    @property
    @pulumi.getter(name="replicationInstanceIdentifier")
    def replication_instance_identifier(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "replication_instance_identifier")

    @replication_instance_identifier.setter
    def replication_instance_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "replication_instance_identifier", value)

    @property
    @pulumi.getter(name="replicationSubnetGroupIdentifier")
    def replication_subnet_group_identifier(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "replication_subnet_group_identifier")

    @replication_subnet_group_identifier.setter
    def replication_subnet_group_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "replication_subnet_group_identifier", value)

    @property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "resource_identifier")

    @resource_identifier.setter
    def resource_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_identifier", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ReplicationInstanceTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ReplicationInstanceTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "vpc_security_group_ids")

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "vpc_security_group_ids", value)


warnings.warn("""ReplicationInstance is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ReplicationInstance(pulumi.CustomResource):
    warnings.warn("""ReplicationInstance is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocated_storage: Optional[pulumi.Input[int]] = None,
                 allow_major_version_upgrade: Optional[pulumi.Input[bool]] = None,
                 auto_minor_version_upgrade: Optional[pulumi.Input[bool]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 multi_az: Optional[pulumi.Input[bool]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 publicly_accessible: Optional[pulumi.Input[bool]] = None,
                 replication_instance_class: Optional[pulumi.Input[str]] = None,
                 replication_instance_identifier: Optional[pulumi.Input[str]] = None,
                 replication_subnet_group_identifier: Optional[pulumi.Input[str]] = None,
                 resource_identifier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReplicationInstanceTagArgs']]]]] = None,
                 vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::DMS::ReplicationInstance

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReplicationInstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::DMS::ReplicationInstance

        :param str resource_name: The name of the resource.
        :param ReplicationInstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReplicationInstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocated_storage: Optional[pulumi.Input[int]] = None,
                 allow_major_version_upgrade: Optional[pulumi.Input[bool]] = None,
                 auto_minor_version_upgrade: Optional[pulumi.Input[bool]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 multi_az: Optional[pulumi.Input[bool]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 publicly_accessible: Optional[pulumi.Input[bool]] = None,
                 replication_instance_class: Optional[pulumi.Input[str]] = None,
                 replication_instance_identifier: Optional[pulumi.Input[str]] = None,
                 replication_subnet_group_identifier: Optional[pulumi.Input[str]] = None,
                 resource_identifier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReplicationInstanceTagArgs']]]]] = None,
                 vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        pulumi.log.warn("""ReplicationInstance is deprecated: ReplicationInstance is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ReplicationInstanceArgs.__new__(ReplicationInstanceArgs)

            __props__.__dict__["allocated_storage"] = allocated_storage
            __props__.__dict__["allow_major_version_upgrade"] = allow_major_version_upgrade
            __props__.__dict__["auto_minor_version_upgrade"] = auto_minor_version_upgrade
            __props__.__dict__["availability_zone"] = availability_zone
            __props__.__dict__["engine_version"] = engine_version
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["multi_az"] = multi_az
            __props__.__dict__["preferred_maintenance_window"] = preferred_maintenance_window
            __props__.__dict__["publicly_accessible"] = publicly_accessible
            if replication_instance_class is None and not opts.urn:
                raise TypeError("Missing required property 'replication_instance_class'")
            __props__.__dict__["replication_instance_class"] = replication_instance_class
            __props__.__dict__["replication_instance_identifier"] = replication_instance_identifier
            __props__.__dict__["replication_subnet_group_identifier"] = replication_subnet_group_identifier
            __props__.__dict__["resource_identifier"] = resource_identifier
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vpc_security_group_ids"] = vpc_security_group_ids
            __props__.__dict__["replication_instance_private_ip_addresses"] = None
            __props__.__dict__["replication_instance_public_ip_addresses"] = None
        super(ReplicationInstance, __self__).__init__(
            'aws-native:dms:ReplicationInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ReplicationInstance':
        """
        Get an existing ReplicationInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ReplicationInstanceArgs.__new__(ReplicationInstanceArgs)

        __props__.__dict__["allocated_storage"] = None
        __props__.__dict__["allow_major_version_upgrade"] = None
        __props__.__dict__["auto_minor_version_upgrade"] = None
        __props__.__dict__["availability_zone"] = None
        __props__.__dict__["engine_version"] = None
        __props__.__dict__["kms_key_id"] = None
        __props__.__dict__["multi_az"] = None
        __props__.__dict__["preferred_maintenance_window"] = None
        __props__.__dict__["publicly_accessible"] = None
        __props__.__dict__["replication_instance_class"] = None
        __props__.__dict__["replication_instance_identifier"] = None
        __props__.__dict__["replication_instance_private_ip_addresses"] = None
        __props__.__dict__["replication_instance_public_ip_addresses"] = None
        __props__.__dict__["replication_subnet_group_identifier"] = None
        __props__.__dict__["resource_identifier"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpc_security_group_ids"] = None
        return ReplicationInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "allocated_storage")

    @property
    @pulumi.getter(name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "allow_major_version_upgrade")

    @property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "auto_minor_version_upgrade")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "multi_az")

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "preferred_maintenance_window")

    @property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "publicly_accessible")

    @property
    @pulumi.getter(name="replicationInstanceClass")
    def replication_instance_class(self) -> pulumi.Output[str]:
        return pulumi.get(self, "replication_instance_class")

    @property
    @pulumi.getter(name="replicationInstanceIdentifier")
    def replication_instance_identifier(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "replication_instance_identifier")

    @property
    @pulumi.getter(name="replicationInstancePrivateIpAddresses")
    def replication_instance_private_ip_addresses(self) -> pulumi.Output[str]:
        return pulumi.get(self, "replication_instance_private_ip_addresses")

    @property
    @pulumi.getter(name="replicationInstancePublicIpAddresses")
    def replication_instance_public_ip_addresses(self) -> pulumi.Output[str]:
        return pulumi.get(self, "replication_instance_public_ip_addresses")

    @property
    @pulumi.getter(name="replicationSubnetGroupIdentifier")
    def replication_subnet_group_identifier(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "replication_subnet_group_identifier")

    @property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "resource_identifier")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ReplicationInstanceTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "vpc_security_group_ids")

