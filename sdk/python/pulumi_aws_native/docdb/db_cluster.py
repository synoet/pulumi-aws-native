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

__all__ = ['DbClusterArgs', 'DbCluster']

@pulumi.input_type
class DbClusterArgs:
    def __init__(__self__, *,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 backup_retention_period: Optional[pulumi.Input[int]] = None,
                 copy_tags_to_snapshot: Optional[pulumi.Input[bool]] = None,
                 db_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 db_cluster_parameter_group_name: Optional[pulumi.Input[str]] = None,
                 db_subnet_group_name: Optional[pulumi.Input[str]] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 enable_cloudwatch_logs_exports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 master_user_password: Optional[pulumi.Input[str]] = None,
                 master_username: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 preferred_backup_window: Optional[pulumi.Input[str]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 restore_to_time: Optional[pulumi.Input[str]] = None,
                 restore_type: Optional[pulumi.Input[str]] = None,
                 snapshot_identifier: Optional[pulumi.Input[str]] = None,
                 source_db_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 storage_encrypted: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DbClusterTagArgs']]]] = None,
                 use_latest_restorable_time: Optional[pulumi.Input[bool]] = None,
                 vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DbCluster resource.
        """
        if availability_zones is not None:
            pulumi.set(__self__, "availability_zones", availability_zones)
        if backup_retention_period is not None:
            pulumi.set(__self__, "backup_retention_period", backup_retention_period)
        if copy_tags_to_snapshot is not None:
            pulumi.set(__self__, "copy_tags_to_snapshot", copy_tags_to_snapshot)
        if db_cluster_identifier is not None:
            pulumi.set(__self__, "db_cluster_identifier", db_cluster_identifier)
        if db_cluster_parameter_group_name is not None:
            pulumi.set(__self__, "db_cluster_parameter_group_name", db_cluster_parameter_group_name)
        if db_subnet_group_name is not None:
            pulumi.set(__self__, "db_subnet_group_name", db_subnet_group_name)
        if deletion_protection is not None:
            pulumi.set(__self__, "deletion_protection", deletion_protection)
        if enable_cloudwatch_logs_exports is not None:
            pulumi.set(__self__, "enable_cloudwatch_logs_exports", enable_cloudwatch_logs_exports)
        if engine_version is not None:
            pulumi.set(__self__, "engine_version", engine_version)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if master_user_password is not None:
            pulumi.set(__self__, "master_user_password", master_user_password)
        if master_username is not None:
            pulumi.set(__self__, "master_username", master_username)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if preferred_backup_window is not None:
            pulumi.set(__self__, "preferred_backup_window", preferred_backup_window)
        if preferred_maintenance_window is not None:
            pulumi.set(__self__, "preferred_maintenance_window", preferred_maintenance_window)
        if restore_to_time is not None:
            pulumi.set(__self__, "restore_to_time", restore_to_time)
        if restore_type is not None:
            pulumi.set(__self__, "restore_type", restore_type)
        if snapshot_identifier is not None:
            pulumi.set(__self__, "snapshot_identifier", snapshot_identifier)
        if source_db_cluster_identifier is not None:
            pulumi.set(__self__, "source_db_cluster_identifier", source_db_cluster_identifier)
        if storage_encrypted is not None:
            pulumi.set(__self__, "storage_encrypted", storage_encrypted)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if use_latest_restorable_time is not None:
            pulumi.set(__self__, "use_latest_restorable_time", use_latest_restorable_time)
        if vpc_security_group_ids is not None:
            pulumi.set(__self__, "vpc_security_group_ids", vpc_security_group_ids)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "availability_zones")

    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "availability_zones", value)

    @property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "backup_retention_period")

    @backup_retention_period.setter
    def backup_retention_period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "backup_retention_period", value)

    @property
    @pulumi.getter(name="copyTagsToSnapshot")
    def copy_tags_to_snapshot(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "copy_tags_to_snapshot")

    @copy_tags_to_snapshot.setter
    def copy_tags_to_snapshot(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "copy_tags_to_snapshot", value)

    @property
    @pulumi.getter(name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "db_cluster_identifier")

    @db_cluster_identifier.setter
    def db_cluster_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_cluster_identifier", value)

    @property
    @pulumi.getter(name="dbClusterParameterGroupName")
    def db_cluster_parameter_group_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "db_cluster_parameter_group_name")

    @db_cluster_parameter_group_name.setter
    def db_cluster_parameter_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_cluster_parameter_group_name", value)

    @property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "db_subnet_group_name")

    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_subnet_group_name", value)

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "deletion_protection")

    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "deletion_protection", value)

    @property
    @pulumi.getter(name="enableCloudwatchLogsExports")
    def enable_cloudwatch_logs_exports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "enable_cloudwatch_logs_exports")

    @enable_cloudwatch_logs_exports.setter
    def enable_cloudwatch_logs_exports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "enable_cloudwatch_logs_exports", value)

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
    @pulumi.getter(name="masterUserPassword")
    def master_user_password(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "master_user_password")

    @master_user_password.setter
    def master_user_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "master_user_password", value)

    @property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "master_username")

    @master_username.setter
    def master_username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "master_username", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "preferred_backup_window")

    @preferred_backup_window.setter
    def preferred_backup_window(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preferred_backup_window", value)

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "preferred_maintenance_window")

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preferred_maintenance_window", value)

    @property
    @pulumi.getter(name="restoreToTime")
    def restore_to_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "restore_to_time")

    @restore_to_time.setter
    def restore_to_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "restore_to_time", value)

    @property
    @pulumi.getter(name="restoreType")
    def restore_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "restore_type")

    @restore_type.setter
    def restore_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "restore_type", value)

    @property
    @pulumi.getter(name="snapshotIdentifier")
    def snapshot_identifier(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "snapshot_identifier")

    @snapshot_identifier.setter
    def snapshot_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "snapshot_identifier", value)

    @property
    @pulumi.getter(name="sourceDbClusterIdentifier")
    def source_db_cluster_identifier(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_db_cluster_identifier")

    @source_db_cluster_identifier.setter
    def source_db_cluster_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_db_cluster_identifier", value)

    @property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "storage_encrypted")

    @storage_encrypted.setter
    def storage_encrypted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "storage_encrypted", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DbClusterTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DbClusterTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="useLatestRestorableTime")
    def use_latest_restorable_time(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "use_latest_restorable_time")

    @use_latest_restorable_time.setter
    def use_latest_restorable_time(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_latest_restorable_time", value)

    @property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "vpc_security_group_ids")

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "vpc_security_group_ids", value)


warnings.warn("""DbCluster is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class DbCluster(pulumi.CustomResource):
    warnings.warn("""DbCluster is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 backup_retention_period: Optional[pulumi.Input[int]] = None,
                 copy_tags_to_snapshot: Optional[pulumi.Input[bool]] = None,
                 db_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 db_cluster_parameter_group_name: Optional[pulumi.Input[str]] = None,
                 db_subnet_group_name: Optional[pulumi.Input[str]] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 enable_cloudwatch_logs_exports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 master_user_password: Optional[pulumi.Input[str]] = None,
                 master_username: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 preferred_backup_window: Optional[pulumi.Input[str]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 restore_to_time: Optional[pulumi.Input[str]] = None,
                 restore_type: Optional[pulumi.Input[str]] = None,
                 snapshot_identifier: Optional[pulumi.Input[str]] = None,
                 source_db_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 storage_encrypted: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DbClusterTagArgs']]]]] = None,
                 use_latest_restorable_time: Optional[pulumi.Input[bool]] = None,
                 vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::DocDB::DBCluster

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DbClusterArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::DocDB::DBCluster

        :param str resource_name: The name of the resource.
        :param DbClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DbClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 backup_retention_period: Optional[pulumi.Input[int]] = None,
                 copy_tags_to_snapshot: Optional[pulumi.Input[bool]] = None,
                 db_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 db_cluster_parameter_group_name: Optional[pulumi.Input[str]] = None,
                 db_subnet_group_name: Optional[pulumi.Input[str]] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 enable_cloudwatch_logs_exports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 master_user_password: Optional[pulumi.Input[str]] = None,
                 master_username: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 preferred_backup_window: Optional[pulumi.Input[str]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 restore_to_time: Optional[pulumi.Input[str]] = None,
                 restore_type: Optional[pulumi.Input[str]] = None,
                 snapshot_identifier: Optional[pulumi.Input[str]] = None,
                 source_db_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 storage_encrypted: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DbClusterTagArgs']]]]] = None,
                 use_latest_restorable_time: Optional[pulumi.Input[bool]] = None,
                 vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        pulumi.log.warn("""DbCluster is deprecated: DbCluster is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DbClusterArgs.__new__(DbClusterArgs)

            __props__.__dict__["availability_zones"] = availability_zones
            __props__.__dict__["backup_retention_period"] = backup_retention_period
            __props__.__dict__["copy_tags_to_snapshot"] = copy_tags_to_snapshot
            __props__.__dict__["db_cluster_identifier"] = db_cluster_identifier
            __props__.__dict__["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
            __props__.__dict__["db_subnet_group_name"] = db_subnet_group_name
            __props__.__dict__["deletion_protection"] = deletion_protection
            __props__.__dict__["enable_cloudwatch_logs_exports"] = enable_cloudwatch_logs_exports
            __props__.__dict__["engine_version"] = engine_version
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["master_user_password"] = master_user_password
            __props__.__dict__["master_username"] = master_username
            __props__.__dict__["port"] = port
            __props__.__dict__["preferred_backup_window"] = preferred_backup_window
            __props__.__dict__["preferred_maintenance_window"] = preferred_maintenance_window
            __props__.__dict__["restore_to_time"] = restore_to_time
            __props__.__dict__["restore_type"] = restore_type
            __props__.__dict__["snapshot_identifier"] = snapshot_identifier
            __props__.__dict__["source_db_cluster_identifier"] = source_db_cluster_identifier
            __props__.__dict__["storage_encrypted"] = storage_encrypted
            __props__.__dict__["tags"] = tags
            __props__.__dict__["use_latest_restorable_time"] = use_latest_restorable_time
            __props__.__dict__["vpc_security_group_ids"] = vpc_security_group_ids
            __props__.__dict__["cluster_resource_id"] = None
            __props__.__dict__["endpoint"] = None
            __props__.__dict__["read_endpoint"] = None
        super(DbCluster, __self__).__init__(
            'aws-native:docdb:DbCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DbCluster':
        """
        Get an existing DbCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DbClusterArgs.__new__(DbClusterArgs)

        __props__.__dict__["availability_zones"] = None
        __props__.__dict__["backup_retention_period"] = None
        __props__.__dict__["cluster_resource_id"] = None
        __props__.__dict__["copy_tags_to_snapshot"] = None
        __props__.__dict__["db_cluster_identifier"] = None
        __props__.__dict__["db_cluster_parameter_group_name"] = None
        __props__.__dict__["db_subnet_group_name"] = None
        __props__.__dict__["deletion_protection"] = None
        __props__.__dict__["enable_cloudwatch_logs_exports"] = None
        __props__.__dict__["endpoint"] = None
        __props__.__dict__["engine_version"] = None
        __props__.__dict__["kms_key_id"] = None
        __props__.__dict__["master_user_password"] = None
        __props__.__dict__["master_username"] = None
        __props__.__dict__["port"] = None
        __props__.__dict__["preferred_backup_window"] = None
        __props__.__dict__["preferred_maintenance_window"] = None
        __props__.__dict__["read_endpoint"] = None
        __props__.__dict__["restore_to_time"] = None
        __props__.__dict__["restore_type"] = None
        __props__.__dict__["snapshot_identifier"] = None
        __props__.__dict__["source_db_cluster_identifier"] = None
        __props__.__dict__["storage_encrypted"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["use_latest_restorable_time"] = None
        __props__.__dict__["vpc_security_group_ids"] = None
        return DbCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "backup_retention_period")

    @property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "cluster_resource_id")

    @property
    @pulumi.getter(name="copyTagsToSnapshot")
    def copy_tags_to_snapshot(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "copy_tags_to_snapshot")

    @property
    @pulumi.getter(name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "db_cluster_identifier")

    @property
    @pulumi.getter(name="dbClusterParameterGroupName")
    def db_cluster_parameter_group_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "db_cluster_parameter_group_name")

    @property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "db_subnet_group_name")

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "deletion_protection")

    @property
    @pulumi.getter(name="enableCloudwatchLogsExports")
    def enable_cloudwatch_logs_exports(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "enable_cloudwatch_logs_exports")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="masterUserPassword")
    def master_user_password(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "master_user_password")

    @property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "master_username")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "preferred_backup_window")

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "preferred_maintenance_window")

    @property
    @pulumi.getter(name="readEndpoint")
    def read_endpoint(self) -> pulumi.Output[str]:
        return pulumi.get(self, "read_endpoint")

    @property
    @pulumi.getter(name="restoreToTime")
    def restore_to_time(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "restore_to_time")

    @property
    @pulumi.getter(name="restoreType")
    def restore_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "restore_type")

    @property
    @pulumi.getter(name="snapshotIdentifier")
    def snapshot_identifier(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "snapshot_identifier")

    @property
    @pulumi.getter(name="sourceDbClusterIdentifier")
    def source_db_cluster_identifier(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "source_db_cluster_identifier")

    @property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "storage_encrypted")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DbClusterTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="useLatestRestorableTime")
    def use_latest_restorable_time(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "use_latest_restorable_time")

    @property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "vpc_security_group_ids")

