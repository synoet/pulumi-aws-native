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

__all__ = [
    'GetDBClusterResult',
    'AwaitableGetDBClusterResult',
    'get_db_cluster',
    'get_db_cluster_output',
]

@pulumi.output_type
class GetDBClusterResult:
    def __init__(__self__, backup_retention_period=None, cluster_resource_id=None, copy_tags_to_snapshot=None, d_b_cluster_parameter_group_name=None, deletion_protection=None, enable_cloudwatch_logs_exports=None, endpoint=None, id=None, master_user_password=None, port=None, preferred_backup_window=None, preferred_maintenance_window=None, read_endpoint=None, restore_to_time=None, restore_type=None, tags=None, use_latest_restorable_time=None, vpc_security_group_ids=None):
        if backup_retention_period and not isinstance(backup_retention_period, int):
            raise TypeError("Expected argument 'backup_retention_period' to be a int")
        pulumi.set(__self__, "backup_retention_period", backup_retention_period)
        if cluster_resource_id and not isinstance(cluster_resource_id, str):
            raise TypeError("Expected argument 'cluster_resource_id' to be a str")
        pulumi.set(__self__, "cluster_resource_id", cluster_resource_id)
        if copy_tags_to_snapshot and not isinstance(copy_tags_to_snapshot, bool):
            raise TypeError("Expected argument 'copy_tags_to_snapshot' to be a bool")
        pulumi.set(__self__, "copy_tags_to_snapshot", copy_tags_to_snapshot)
        if d_b_cluster_parameter_group_name and not isinstance(d_b_cluster_parameter_group_name, str):
            raise TypeError("Expected argument 'd_b_cluster_parameter_group_name' to be a str")
        pulumi.set(__self__, "d_b_cluster_parameter_group_name", d_b_cluster_parameter_group_name)
        if deletion_protection and not isinstance(deletion_protection, bool):
            raise TypeError("Expected argument 'deletion_protection' to be a bool")
        pulumi.set(__self__, "deletion_protection", deletion_protection)
        if enable_cloudwatch_logs_exports and not isinstance(enable_cloudwatch_logs_exports, list):
            raise TypeError("Expected argument 'enable_cloudwatch_logs_exports' to be a list")
        pulumi.set(__self__, "enable_cloudwatch_logs_exports", enable_cloudwatch_logs_exports)
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if master_user_password and not isinstance(master_user_password, str):
            raise TypeError("Expected argument 'master_user_password' to be a str")
        pulumi.set(__self__, "master_user_password", master_user_password)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if preferred_backup_window and not isinstance(preferred_backup_window, str):
            raise TypeError("Expected argument 'preferred_backup_window' to be a str")
        pulumi.set(__self__, "preferred_backup_window", preferred_backup_window)
        if preferred_maintenance_window and not isinstance(preferred_maintenance_window, str):
            raise TypeError("Expected argument 'preferred_maintenance_window' to be a str")
        pulumi.set(__self__, "preferred_maintenance_window", preferred_maintenance_window)
        if read_endpoint and not isinstance(read_endpoint, str):
            raise TypeError("Expected argument 'read_endpoint' to be a str")
        pulumi.set(__self__, "read_endpoint", read_endpoint)
        if restore_to_time and not isinstance(restore_to_time, str):
            raise TypeError("Expected argument 'restore_to_time' to be a str")
        pulumi.set(__self__, "restore_to_time", restore_to_time)
        if restore_type and not isinstance(restore_type, str):
            raise TypeError("Expected argument 'restore_type' to be a str")
        pulumi.set(__self__, "restore_type", restore_type)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if use_latest_restorable_time and not isinstance(use_latest_restorable_time, bool):
            raise TypeError("Expected argument 'use_latest_restorable_time' to be a bool")
        pulumi.set(__self__, "use_latest_restorable_time", use_latest_restorable_time)
        if vpc_security_group_ids and not isinstance(vpc_security_group_ids, list):
            raise TypeError("Expected argument 'vpc_security_group_ids' to be a list")
        pulumi.set(__self__, "vpc_security_group_ids", vpc_security_group_ids)

    @property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> Optional[int]:
        return pulumi.get(self, "backup_retention_period")

    @property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> Optional[str]:
        return pulumi.get(self, "cluster_resource_id")

    @property
    @pulumi.getter(name="copyTagsToSnapshot")
    def copy_tags_to_snapshot(self) -> Optional[bool]:
        return pulumi.get(self, "copy_tags_to_snapshot")

    @property
    @pulumi.getter(name="dBClusterParameterGroupName")
    def d_b_cluster_parameter_group_name(self) -> Optional[str]:
        return pulumi.get(self, "d_b_cluster_parameter_group_name")

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[bool]:
        return pulumi.get(self, "deletion_protection")

    @property
    @pulumi.getter(name="enableCloudwatchLogsExports")
    def enable_cloudwatch_logs_exports(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "enable_cloudwatch_logs_exports")

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[str]:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="masterUserPassword")
    def master_user_password(self) -> Optional[str]:
        return pulumi.get(self, "master_user_password")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> Optional[str]:
        return pulumi.get(self, "preferred_backup_window")

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[str]:
        return pulumi.get(self, "preferred_maintenance_window")

    @property
    @pulumi.getter(name="readEndpoint")
    def read_endpoint(self) -> Optional[str]:
        return pulumi.get(self, "read_endpoint")

    @property
    @pulumi.getter(name="restoreToTime")
    def restore_to_time(self) -> Optional[str]:
        return pulumi.get(self, "restore_to_time")

    @property
    @pulumi.getter(name="restoreType")
    def restore_type(self) -> Optional[str]:
        return pulumi.get(self, "restore_type")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DBClusterTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="useLatestRestorableTime")
    def use_latest_restorable_time(self) -> Optional[bool]:
        return pulumi.get(self, "use_latest_restorable_time")

    @property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "vpc_security_group_ids")


class AwaitableGetDBClusterResult(GetDBClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDBClusterResult(
            backup_retention_period=self.backup_retention_period,
            cluster_resource_id=self.cluster_resource_id,
            copy_tags_to_snapshot=self.copy_tags_to_snapshot,
            d_b_cluster_parameter_group_name=self.d_b_cluster_parameter_group_name,
            deletion_protection=self.deletion_protection,
            enable_cloudwatch_logs_exports=self.enable_cloudwatch_logs_exports,
            endpoint=self.endpoint,
            id=self.id,
            master_user_password=self.master_user_password,
            port=self.port,
            preferred_backup_window=self.preferred_backup_window,
            preferred_maintenance_window=self.preferred_maintenance_window,
            read_endpoint=self.read_endpoint,
            restore_to_time=self.restore_to_time,
            restore_type=self.restore_type,
            tags=self.tags,
            use_latest_restorable_time=self.use_latest_restorable_time,
            vpc_security_group_ids=self.vpc_security_group_ids)


def get_db_cluster(id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDBClusterResult:
    """
    Resource Type definition for AWS::DocDB::DBCluster
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:docdb:getDBCluster', __args__, opts=opts, typ=GetDBClusterResult).value

    return AwaitableGetDBClusterResult(
        backup_retention_period=__ret__.backup_retention_period,
        cluster_resource_id=__ret__.cluster_resource_id,
        copy_tags_to_snapshot=__ret__.copy_tags_to_snapshot,
        d_b_cluster_parameter_group_name=__ret__.d_b_cluster_parameter_group_name,
        deletion_protection=__ret__.deletion_protection,
        enable_cloudwatch_logs_exports=__ret__.enable_cloudwatch_logs_exports,
        endpoint=__ret__.endpoint,
        id=__ret__.id,
        master_user_password=__ret__.master_user_password,
        port=__ret__.port,
        preferred_backup_window=__ret__.preferred_backup_window,
        preferred_maintenance_window=__ret__.preferred_maintenance_window,
        read_endpoint=__ret__.read_endpoint,
        restore_to_time=__ret__.restore_to_time,
        restore_type=__ret__.restore_type,
        tags=__ret__.tags,
        use_latest_restorable_time=__ret__.use_latest_restorable_time,
        vpc_security_group_ids=__ret__.vpc_security_group_ids)


@_utilities.lift_output_func(get_db_cluster)
def get_db_cluster_output(id: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDBClusterResult]:
    """
    Resource Type definition for AWS::DocDB::DBCluster
    """
    ...
