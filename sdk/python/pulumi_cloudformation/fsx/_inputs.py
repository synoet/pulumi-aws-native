# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from .. import _inputs as _root_inputs

__all__ = [
    'FileSystemLustreConfigurationArgs',
    'FileSystemPropertiesArgs',
    'FileSystemSelfManagedActiveDirectoryConfigurationArgs',
    'FileSystemWindowsConfigurationArgs',
]

@pulumi.input_type
class FileSystemLustreConfigurationArgs:
    def __init__(__self__, *,
                 auto_import_policy: Optional[pulumi.Input[str]] = None,
                 automatic_backup_retention_days: Optional[pulumi.Input[int]] = None,
                 copy_tags_to_backups: Optional[pulumi.Input[bool]] = None,
                 daily_automatic_backup_start_time: Optional[pulumi.Input[str]] = None,
                 deployment_type: Optional[pulumi.Input[str]] = None,
                 drive_cache_type: Optional[pulumi.Input[str]] = None,
                 export_path: Optional[pulumi.Input[str]] = None,
                 import_path: Optional[pulumi.Input[str]] = None,
                 imported_file_chunk_size: Optional[pulumi.Input[int]] = None,
                 per_unit_storage_throughput: Optional[pulumi.Input[int]] = None,
                 weekly_maintenance_start_time: Optional[pulumi.Input[str]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html
        :param pulumi.Input[str] auto_import_policy: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-autoimportpolicy
        :param pulumi.Input[int] automatic_backup_retention_days: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-automaticbackupretentiondays
        :param pulumi.Input[bool] copy_tags_to_backups: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-copytagstobackups
        :param pulumi.Input[str] daily_automatic_backup_start_time: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-dailyautomaticbackupstarttime
        :param pulumi.Input[str] deployment_type: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-deploymenttype
        :param pulumi.Input[str] drive_cache_type: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-drivecachetype
        :param pulumi.Input[str] export_path: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-exportpath
        :param pulumi.Input[str] import_path: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-importpath
        :param pulumi.Input[int] imported_file_chunk_size: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-importedfilechunksize
        :param pulumi.Input[int] per_unit_storage_throughput: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-perunitstoragethroughput
        :param pulumi.Input[str] weekly_maintenance_start_time: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-weeklymaintenancestarttime
        """
        if auto_import_policy is not None:
            pulumi.set(__self__, "auto_import_policy", auto_import_policy)
        if automatic_backup_retention_days is not None:
            pulumi.set(__self__, "automatic_backup_retention_days", automatic_backup_retention_days)
        if copy_tags_to_backups is not None:
            pulumi.set(__self__, "copy_tags_to_backups", copy_tags_to_backups)
        if daily_automatic_backup_start_time is not None:
            pulumi.set(__self__, "daily_automatic_backup_start_time", daily_automatic_backup_start_time)
        if deployment_type is not None:
            pulumi.set(__self__, "deployment_type", deployment_type)
        if drive_cache_type is not None:
            pulumi.set(__self__, "drive_cache_type", drive_cache_type)
        if export_path is not None:
            pulumi.set(__self__, "export_path", export_path)
        if import_path is not None:
            pulumi.set(__self__, "import_path", import_path)
        if imported_file_chunk_size is not None:
            pulumi.set(__self__, "imported_file_chunk_size", imported_file_chunk_size)
        if per_unit_storage_throughput is not None:
            pulumi.set(__self__, "per_unit_storage_throughput", per_unit_storage_throughput)
        if weekly_maintenance_start_time is not None:
            pulumi.set(__self__, "weekly_maintenance_start_time", weekly_maintenance_start_time)

    @property
    @pulumi.getter(name="AutoImportPolicy")
    def auto_import_policy(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-autoimportpolicy
        """
        return pulumi.get(self, "auto_import_policy")

    @auto_import_policy.setter
    def auto_import_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auto_import_policy", value)

    @property
    @pulumi.getter(name="AutomaticBackupRetentionDays")
    def automatic_backup_retention_days(self) -> Optional[pulumi.Input[int]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-automaticbackupretentiondays
        """
        return pulumi.get(self, "automatic_backup_retention_days")

    @automatic_backup_retention_days.setter
    def automatic_backup_retention_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "automatic_backup_retention_days", value)

    @property
    @pulumi.getter(name="CopyTagsToBackups")
    def copy_tags_to_backups(self) -> Optional[pulumi.Input[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-copytagstobackups
        """
        return pulumi.get(self, "copy_tags_to_backups")

    @copy_tags_to_backups.setter
    def copy_tags_to_backups(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "copy_tags_to_backups", value)

    @property
    @pulumi.getter(name="DailyAutomaticBackupStartTime")
    def daily_automatic_backup_start_time(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-dailyautomaticbackupstarttime
        """
        return pulumi.get(self, "daily_automatic_backup_start_time")

    @daily_automatic_backup_start_time.setter
    def daily_automatic_backup_start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "daily_automatic_backup_start_time", value)

    @property
    @pulumi.getter(name="DeploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-deploymenttype
        """
        return pulumi.get(self, "deployment_type")

    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_type", value)

    @property
    @pulumi.getter(name="DriveCacheType")
    def drive_cache_type(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-drivecachetype
        """
        return pulumi.get(self, "drive_cache_type")

    @drive_cache_type.setter
    def drive_cache_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "drive_cache_type", value)

    @property
    @pulumi.getter(name="ExportPath")
    def export_path(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-exportpath
        """
        return pulumi.get(self, "export_path")

    @export_path.setter
    def export_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "export_path", value)

    @property
    @pulumi.getter(name="ImportPath")
    def import_path(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-importpath
        """
        return pulumi.get(self, "import_path")

    @import_path.setter
    def import_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "import_path", value)

    @property
    @pulumi.getter(name="ImportedFileChunkSize")
    def imported_file_chunk_size(self) -> Optional[pulumi.Input[int]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-importedfilechunksize
        """
        return pulumi.get(self, "imported_file_chunk_size")

    @imported_file_chunk_size.setter
    def imported_file_chunk_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "imported_file_chunk_size", value)

    @property
    @pulumi.getter(name="PerUnitStorageThroughput")
    def per_unit_storage_throughput(self) -> Optional[pulumi.Input[int]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-perunitstoragethroughput
        """
        return pulumi.get(self, "per_unit_storage_throughput")

    @per_unit_storage_throughput.setter
    def per_unit_storage_throughput(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "per_unit_storage_throughput", value)

    @property
    @pulumi.getter(name="WeeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-weeklymaintenancestarttime
        """
        return pulumi.get(self, "weekly_maintenance_start_time")

    @weekly_maintenance_start_time.setter
    def weekly_maintenance_start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "weekly_maintenance_start_time", value)


@pulumi.input_type
class FileSystemPropertiesArgs:
    def __init__(__self__, *,
                 file_system_type: pulumi.Input[str],
                 subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 backup_id: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 lustre_configuration: Optional[pulumi.Input['FileSystemLustreConfigurationArgs']] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 storage_capacity: Optional[pulumi.Input[int]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 windows_configuration: Optional[pulumi.Input['FileSystemWindowsConfigurationArgs']] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html
        :param pulumi.Input[str] file_system_type: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-filesystemtype
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-subnetids
        :param pulumi.Input[str] backup_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-backupid
        :param pulumi.Input[str] kms_key_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-kmskeyid
        :param pulumi.Input['FileSystemLustreConfigurationArgs'] lustre_configuration: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-lustreconfiguration
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-securitygroupids
        :param pulumi.Input[int] storage_capacity: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-storagecapacity
        :param pulumi.Input[str] storage_type: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-storagetype
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-tags
        :param pulumi.Input['FileSystemWindowsConfigurationArgs'] windows_configuration: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-windowsconfiguration
        """
        pulumi.set(__self__, "file_system_type", file_system_type)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if backup_id is not None:
            pulumi.set(__self__, "backup_id", backup_id)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if lustre_configuration is not None:
            pulumi.set(__self__, "lustre_configuration", lustre_configuration)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if storage_capacity is not None:
            pulumi.set(__self__, "storage_capacity", storage_capacity)
        if storage_type is not None:
            pulumi.set(__self__, "storage_type", storage_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if windows_configuration is not None:
            pulumi.set(__self__, "windows_configuration", windows_configuration)

    @property
    @pulumi.getter(name="FileSystemType")
    def file_system_type(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-filesystemtype
        """
        return pulumi.get(self, "file_system_type")

    @file_system_type.setter
    def file_system_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "file_system_type", value)

    @property
    @pulumi.getter(name="SubnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-subnetids
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="BackupId")
    def backup_id(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-backupid
        """
        return pulumi.get(self, "backup_id")

    @backup_id.setter
    def backup_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backup_id", value)

    @property
    @pulumi.getter(name="KmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-kmskeyid
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="LustreConfiguration")
    def lustre_configuration(self) -> Optional[pulumi.Input['FileSystemLustreConfigurationArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-lustreconfiguration
        """
        return pulumi.get(self, "lustre_configuration")

    @lustre_configuration.setter
    def lustre_configuration(self, value: Optional[pulumi.Input['FileSystemLustreConfigurationArgs']]):
        pulumi.set(self, "lustre_configuration", value)

    @property
    @pulumi.getter(name="SecurityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-securitygroupids
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="StorageCapacity")
    def storage_capacity(self) -> Optional[pulumi.Input[int]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-storagecapacity
        """
        return pulumi.get(self, "storage_capacity")

    @storage_capacity.setter
    def storage_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "storage_capacity", value)

    @property
    @pulumi.getter(name="StorageType")
    def storage_type(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-storagetype
        """
        return pulumi.get(self, "storage_type")

    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_type", value)

    @property
    @pulumi.getter(name="Tags")
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="WindowsConfiguration")
    def windows_configuration(self) -> Optional[pulumi.Input['FileSystemWindowsConfigurationArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-windowsconfiguration
        """
        return pulumi.get(self, "windows_configuration")

    @windows_configuration.setter
    def windows_configuration(self, value: Optional[pulumi.Input['FileSystemWindowsConfigurationArgs']]):
        pulumi.set(self, "windows_configuration", value)


@pulumi.input_type
class FileSystemSelfManagedActiveDirectoryConfigurationArgs:
    def __init__(__self__, *,
                 dns_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 file_system_administrators_group: Optional[pulumi.Input[str]] = None,
                 organizational_unit_distinguished_name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_ips: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-dnsips
        :param pulumi.Input[str] domain_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-domainname
        :param pulumi.Input[str] file_system_administrators_group: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-filesystemadministratorsgroup
        :param pulumi.Input[str] organizational_unit_distinguished_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-organizationalunitdistinguishedname
        :param pulumi.Input[str] password: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-password
        :param pulumi.Input[str] user_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-username
        """
        if dns_ips is not None:
            pulumi.set(__self__, "dns_ips", dns_ips)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if file_system_administrators_group is not None:
            pulumi.set(__self__, "file_system_administrators_group", file_system_administrators_group)
        if organizational_unit_distinguished_name is not None:
            pulumi.set(__self__, "organizational_unit_distinguished_name", organizational_unit_distinguished_name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if user_name is not None:
            pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="DnsIps")
    def dns_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-dnsips
        """
        return pulumi.get(self, "dns_ips")

    @dns_ips.setter
    def dns_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dns_ips", value)

    @property
    @pulumi.getter(name="DomainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-domainname
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="FileSystemAdministratorsGroup")
    def file_system_administrators_group(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-filesystemadministratorsgroup
        """
        return pulumi.get(self, "file_system_administrators_group")

    @file_system_administrators_group.setter
    def file_system_administrators_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_system_administrators_group", value)

    @property
    @pulumi.getter(name="OrganizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-organizationalunitdistinguishedname
        """
        return pulumi.get(self, "organizational_unit_distinguished_name")

    @organizational_unit_distinguished_name.setter
    def organizational_unit_distinguished_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organizational_unit_distinguished_name", value)

    @property
    @pulumi.getter(name="Password")
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-password
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="UserName")
    def user_name(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-username
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_name", value)


@pulumi.input_type
class FileSystemWindowsConfigurationArgs:
    def __init__(__self__, *,
                 active_directory_id: Optional[pulumi.Input[str]] = None,
                 automatic_backup_retention_days: Optional[pulumi.Input[int]] = None,
                 copy_tags_to_backups: Optional[pulumi.Input[bool]] = None,
                 daily_automatic_backup_start_time: Optional[pulumi.Input[str]] = None,
                 deployment_type: Optional[pulumi.Input[str]] = None,
                 preferred_subnet_id: Optional[pulumi.Input[str]] = None,
                 self_managed_active_directory_configuration: Optional[pulumi.Input['FileSystemSelfManagedActiveDirectoryConfigurationArgs']] = None,
                 throughput_capacity: Optional[pulumi.Input[int]] = None,
                 weekly_maintenance_start_time: Optional[pulumi.Input[str]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html
        :param pulumi.Input[str] active_directory_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-activedirectoryid
        :param pulumi.Input[int] automatic_backup_retention_days: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-automaticbackupretentiondays
        :param pulumi.Input[bool] copy_tags_to_backups: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-copytagstobackups
        :param pulumi.Input[str] daily_automatic_backup_start_time: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-dailyautomaticbackupstarttime
        :param pulumi.Input[str] deployment_type: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-deploymenttype
        :param pulumi.Input[str] preferred_subnet_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-preferredsubnetid
        :param pulumi.Input['FileSystemSelfManagedActiveDirectoryConfigurationArgs'] self_managed_active_directory_configuration: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration
        :param pulumi.Input[int] throughput_capacity: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-throughputcapacity
        :param pulumi.Input[str] weekly_maintenance_start_time: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-weeklymaintenancestarttime
        """
        if active_directory_id is not None:
            pulumi.set(__self__, "active_directory_id", active_directory_id)
        if automatic_backup_retention_days is not None:
            pulumi.set(__self__, "automatic_backup_retention_days", automatic_backup_retention_days)
        if copy_tags_to_backups is not None:
            pulumi.set(__self__, "copy_tags_to_backups", copy_tags_to_backups)
        if daily_automatic_backup_start_time is not None:
            pulumi.set(__self__, "daily_automatic_backup_start_time", daily_automatic_backup_start_time)
        if deployment_type is not None:
            pulumi.set(__self__, "deployment_type", deployment_type)
        if preferred_subnet_id is not None:
            pulumi.set(__self__, "preferred_subnet_id", preferred_subnet_id)
        if self_managed_active_directory_configuration is not None:
            pulumi.set(__self__, "self_managed_active_directory_configuration", self_managed_active_directory_configuration)
        if throughput_capacity is not None:
            pulumi.set(__self__, "throughput_capacity", throughput_capacity)
        if weekly_maintenance_start_time is not None:
            pulumi.set(__self__, "weekly_maintenance_start_time", weekly_maintenance_start_time)

    @property
    @pulumi.getter(name="ActiveDirectoryId")
    def active_directory_id(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-activedirectoryid
        """
        return pulumi.get(self, "active_directory_id")

    @active_directory_id.setter
    def active_directory_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "active_directory_id", value)

    @property
    @pulumi.getter(name="AutomaticBackupRetentionDays")
    def automatic_backup_retention_days(self) -> Optional[pulumi.Input[int]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-automaticbackupretentiondays
        """
        return pulumi.get(self, "automatic_backup_retention_days")

    @automatic_backup_retention_days.setter
    def automatic_backup_retention_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "automatic_backup_retention_days", value)

    @property
    @pulumi.getter(name="CopyTagsToBackups")
    def copy_tags_to_backups(self) -> Optional[pulumi.Input[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-copytagstobackups
        """
        return pulumi.get(self, "copy_tags_to_backups")

    @copy_tags_to_backups.setter
    def copy_tags_to_backups(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "copy_tags_to_backups", value)

    @property
    @pulumi.getter(name="DailyAutomaticBackupStartTime")
    def daily_automatic_backup_start_time(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-dailyautomaticbackupstarttime
        """
        return pulumi.get(self, "daily_automatic_backup_start_time")

    @daily_automatic_backup_start_time.setter
    def daily_automatic_backup_start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "daily_automatic_backup_start_time", value)

    @property
    @pulumi.getter(name="DeploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-deploymenttype
        """
        return pulumi.get(self, "deployment_type")

    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_type", value)

    @property
    @pulumi.getter(name="PreferredSubnetId")
    def preferred_subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-preferredsubnetid
        """
        return pulumi.get(self, "preferred_subnet_id")

    @preferred_subnet_id.setter
    def preferred_subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preferred_subnet_id", value)

    @property
    @pulumi.getter(name="SelfManagedActiveDirectoryConfiguration")
    def self_managed_active_directory_configuration(self) -> Optional[pulumi.Input['FileSystemSelfManagedActiveDirectoryConfigurationArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration
        """
        return pulumi.get(self, "self_managed_active_directory_configuration")

    @self_managed_active_directory_configuration.setter
    def self_managed_active_directory_configuration(self, value: Optional[pulumi.Input['FileSystemSelfManagedActiveDirectoryConfigurationArgs']]):
        pulumi.set(self, "self_managed_active_directory_configuration", value)

    @property
    @pulumi.getter(name="ThroughputCapacity")
    def throughput_capacity(self) -> Optional[pulumi.Input[int]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-throughputcapacity
        """
        return pulumi.get(self, "throughput_capacity")

    @throughput_capacity.setter
    def throughput_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "throughput_capacity", value)

    @property
    @pulumi.getter(name="WeeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-weeklymaintenancestarttime
        """
        return pulumi.get(self, "weekly_maintenance_start_time")

    @weekly_maintenance_start_time.setter
    def weekly_maintenance_start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "weekly_maintenance_start_time", value)

