# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from .. import outputs as _root_outputs

__all__ = [
    'DBClusterAttributes',
    'DBClusterParameterGroupAttributes',
    'DBClusterParameterGroupProperties',
    'DBClusterProperties',
    'DBInstanceAttributes',
    'DBInstanceProperties',
    'DBSubnetGroupAttributes',
    'DBSubnetGroupProperties',
]

@pulumi.output_type
class DBClusterAttributes(dict):
    def __init__(__self__, *,
                 cluster_resource_id: str,
                 endpoint: str,
                 port: str,
                 read_endpoint: str):
        pulumi.set(__self__, "cluster_resource_id", cluster_resource_id)
        pulumi.set(__self__, "endpoint", endpoint)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "read_endpoint", read_endpoint)

    @property
    @pulumi.getter(name="ClusterResourceId")
    def cluster_resource_id(self) -> str:
        return pulumi.get(self, "cluster_resource_id")

    @property
    @pulumi.getter(name="Endpoint")
    def endpoint(self) -> str:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="Port")
    def port(self) -> str:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="ReadEndpoint")
    def read_endpoint(self) -> str:
        return pulumi.get(self, "read_endpoint")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DBClusterParameterGroupAttributes(dict):
    def __init__(__self__):
        pass

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DBClusterParameterGroupProperties(dict):
    """
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html
    """
    def __init__(__self__, *,
                 description: str,
                 family: str,
                 parameters: str,
                 name: Optional[str] = None,
                 tags: Optional[Sequence['_root_outputs.Tag']] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html
        :param str description: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-description
        :param str family: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-family
        :param Union[Any, str] parameters: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-parameters
        :param str name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-name
        :param Sequence['_root_inputs.TagArgs'] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-tags
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "family", family)
        pulumi.set(__self__, "parameters", parameters)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="Description")
    def description(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="Family")
    def family(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-family
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter(name="Parameters")
    def parameters(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-parameters
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="Name")
    def name(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="Tags")
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-tags
        """
        return pulumi.get(self, "tags")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DBClusterProperties(dict):
    """
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html
    """
    def __init__(__self__, *,
                 master_user_password: str,
                 master_username: str,
                 availability_zones: Optional[Sequence[str]] = None,
                 backup_retention_period: Optional[int] = None,
                 db_cluster_identifier: Optional[str] = None,
                 db_cluster_parameter_group_name: Optional[str] = None,
                 db_subnet_group_name: Optional[str] = None,
                 deletion_protection: Optional[bool] = None,
                 enable_cloudwatch_logs_exports: Optional[Sequence[str]] = None,
                 engine_version: Optional[str] = None,
                 kms_key_id: Optional[str] = None,
                 port: Optional[int] = None,
                 preferred_backup_window: Optional[str] = None,
                 preferred_maintenance_window: Optional[str] = None,
                 snapshot_identifier: Optional[str] = None,
                 storage_encrypted: Optional[bool] = None,
                 tags: Optional[Sequence['_root_outputs.Tag']] = None,
                 vpc_security_group_ids: Optional[Sequence[str]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html
        :param str master_user_password: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-masteruserpassword
        :param str master_username: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-masterusername
        :param Sequence[str] availability_zones: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-availabilityzones
        :param int backup_retention_period: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-backupretentionperiod
        :param str db_cluster_identifier: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbclusteridentifier
        :param str db_cluster_parameter_group_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbclusterparametergroupname
        :param str db_subnet_group_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbsubnetgroupname
        :param bool deletion_protection: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-deletionprotection
        :param Sequence[str] enable_cloudwatch_logs_exports: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-enablecloudwatchlogsexports
        :param str engine_version: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-engineversion
        :param str kms_key_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-kmskeyid
        :param int port: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-port
        :param str preferred_backup_window: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-preferredbackupwindow
        :param str preferred_maintenance_window: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-preferredmaintenancewindow
        :param str snapshot_identifier: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-snapshotidentifier
        :param bool storage_encrypted: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-storageencrypted
        :param Sequence['_root_inputs.TagArgs'] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-tags
        :param Sequence[str] vpc_security_group_ids: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-vpcsecuritygroupids
        """
        pulumi.set(__self__, "master_user_password", master_user_password)
        pulumi.set(__self__, "master_username", master_username)
        if availability_zones is not None:
            pulumi.set(__self__, "availability_zones", availability_zones)
        if backup_retention_period is not None:
            pulumi.set(__self__, "backup_retention_period", backup_retention_period)
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
        if port is not None:
            pulumi.set(__self__, "port", port)
        if preferred_backup_window is not None:
            pulumi.set(__self__, "preferred_backup_window", preferred_backup_window)
        if preferred_maintenance_window is not None:
            pulumi.set(__self__, "preferred_maintenance_window", preferred_maintenance_window)
        if snapshot_identifier is not None:
            pulumi.set(__self__, "snapshot_identifier", snapshot_identifier)
        if storage_encrypted is not None:
            pulumi.set(__self__, "storage_encrypted", storage_encrypted)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vpc_security_group_ids is not None:
            pulumi.set(__self__, "vpc_security_group_ids", vpc_security_group_ids)

    @property
    @pulumi.getter(name="MasterUserPassword")
    def master_user_password(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-masteruserpassword
        """
        return pulumi.get(self, "master_user_password")

    @property
    @pulumi.getter(name="MasterUsername")
    def master_username(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-masterusername
        """
        return pulumi.get(self, "master_username")

    @property
    @pulumi.getter(name="AvailabilityZones")
    def availability_zones(self) -> Optional[Sequence[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-availabilityzones
        """
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter(name="BackupRetentionPeriod")
    def backup_retention_period(self) -> Optional[int]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-backupretentionperiod
        """
        return pulumi.get(self, "backup_retention_period")

    @property
    @pulumi.getter(name="DBClusterIdentifier")
    def db_cluster_identifier(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbclusteridentifier
        """
        return pulumi.get(self, "db_cluster_identifier")

    @property
    @pulumi.getter(name="DBClusterParameterGroupName")
    def db_cluster_parameter_group_name(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbclusterparametergroupname
        """
        return pulumi.get(self, "db_cluster_parameter_group_name")

    @property
    @pulumi.getter(name="DBSubnetGroupName")
    def db_subnet_group_name(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbsubnetgroupname
        """
        return pulumi.get(self, "db_subnet_group_name")

    @property
    @pulumi.getter(name="DeletionProtection")
    def deletion_protection(self) -> Optional[bool]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-deletionprotection
        """
        return pulumi.get(self, "deletion_protection")

    @property
    @pulumi.getter(name="EnableCloudwatchLogsExports")
    def enable_cloudwatch_logs_exports(self) -> Optional[Sequence[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-enablecloudwatchlogsexports
        """
        return pulumi.get(self, "enable_cloudwatch_logs_exports")

    @property
    @pulumi.getter(name="EngineVersion")
    def engine_version(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-engineversion
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="KmsKeyId")
    def kms_key_id(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-kmskeyid
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="Port")
    def port(self) -> Optional[int]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-port
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="PreferredBackupWindow")
    def preferred_backup_window(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-preferredbackupwindow
        """
        return pulumi.get(self, "preferred_backup_window")

    @property
    @pulumi.getter(name="PreferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-preferredmaintenancewindow
        """
        return pulumi.get(self, "preferred_maintenance_window")

    @property
    @pulumi.getter(name="SnapshotIdentifier")
    def snapshot_identifier(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-snapshotidentifier
        """
        return pulumi.get(self, "snapshot_identifier")

    @property
    @pulumi.getter(name="StorageEncrypted")
    def storage_encrypted(self) -> Optional[bool]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-storageencrypted
        """
        return pulumi.get(self, "storage_encrypted")

    @property
    @pulumi.getter(name="Tags")
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="VpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[Sequence[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-vpcsecuritygroupids
        """
        return pulumi.get(self, "vpc_security_group_ids")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DBInstanceAttributes(dict):
    def __init__(__self__, *,
                 endpoint: str,
                 port: str):
        pulumi.set(__self__, "endpoint", endpoint)
        pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter(name="Endpoint")
    def endpoint(self) -> str:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="Port")
    def port(self) -> str:
        return pulumi.get(self, "port")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DBInstanceProperties(dict):
    """
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html
    """
    def __init__(__self__, *,
                 db_cluster_identifier: str,
                 db_instance_class: str,
                 auto_minor_version_upgrade: Optional[bool] = None,
                 availability_zone: Optional[str] = None,
                 db_instance_identifier: Optional[str] = None,
                 preferred_maintenance_window: Optional[str] = None,
                 tags: Optional[Sequence['_root_outputs.Tag']] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html
        :param str db_cluster_identifier: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbclusteridentifier
        :param str db_instance_class: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbinstanceclass
        :param bool auto_minor_version_upgrade: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-autominorversionupgrade
        :param str availability_zone: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-availabilityzone
        :param str db_instance_identifier: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbinstanceidentifier
        :param str preferred_maintenance_window: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-preferredmaintenancewindow
        :param Sequence['_root_inputs.TagArgs'] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-tags
        """
        pulumi.set(__self__, "db_cluster_identifier", db_cluster_identifier)
        pulumi.set(__self__, "db_instance_class", db_instance_class)
        if auto_minor_version_upgrade is not None:
            pulumi.set(__self__, "auto_minor_version_upgrade", auto_minor_version_upgrade)
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if db_instance_identifier is not None:
            pulumi.set(__self__, "db_instance_identifier", db_instance_identifier)
        if preferred_maintenance_window is not None:
            pulumi.set(__self__, "preferred_maintenance_window", preferred_maintenance_window)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="DBClusterIdentifier")
    def db_cluster_identifier(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbclusteridentifier
        """
        return pulumi.get(self, "db_cluster_identifier")

    @property
    @pulumi.getter(name="DBInstanceClass")
    def db_instance_class(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbinstanceclass
        """
        return pulumi.get(self, "db_instance_class")

    @property
    @pulumi.getter(name="AutoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[bool]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-autominorversionupgrade
        """
        return pulumi.get(self, "auto_minor_version_upgrade")

    @property
    @pulumi.getter(name="AvailabilityZone")
    def availability_zone(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-availabilityzone
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="DBInstanceIdentifier")
    def db_instance_identifier(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbinstanceidentifier
        """
        return pulumi.get(self, "db_instance_identifier")

    @property
    @pulumi.getter(name="PreferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-preferredmaintenancewindow
        """
        return pulumi.get(self, "preferred_maintenance_window")

    @property
    @pulumi.getter(name="Tags")
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-tags
        """
        return pulumi.get(self, "tags")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DBSubnetGroupAttributes(dict):
    def __init__(__self__):
        pass

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DBSubnetGroupProperties(dict):
    """
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html
    """
    def __init__(__self__, *,
                 db_subnet_group_description: str,
                 subnet_ids: Sequence[str],
                 db_subnet_group_name: Optional[str] = None,
                 tags: Optional[Sequence['_root_outputs.Tag']] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html
        :param str db_subnet_group_description: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-dbsubnetgroupdescription
        :param Sequence[str] subnet_ids: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-subnetids
        :param str db_subnet_group_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-dbsubnetgroupname
        :param Sequence['_root_inputs.TagArgs'] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-tags
        """
        pulumi.set(__self__, "db_subnet_group_description", db_subnet_group_description)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if db_subnet_group_name is not None:
            pulumi.set(__self__, "db_subnet_group_name", db_subnet_group_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="DBSubnetGroupDescription")
    def db_subnet_group_description(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-dbsubnetgroupdescription
        """
        return pulumi.get(self, "db_subnet_group_description")

    @property
    @pulumi.getter(name="SubnetIds")
    def subnet_ids(self) -> Sequence[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-subnetids
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="DBSubnetGroupName")
    def db_subnet_group_name(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-dbsubnetgroupname
        """
        return pulumi.get(self, "db_subnet_group_name")

    @property
    @pulumi.getter(name="Tags")
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-tags
        """
        return pulumi.get(self, "tags")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

