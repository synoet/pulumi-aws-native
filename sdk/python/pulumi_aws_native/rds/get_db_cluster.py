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
    def __init__(__self__, associated_roles=None, backtrack_window=None, backup_retention_period=None, copy_tags_to_snapshot=None, d_b_cluster_parameter_group_name=None, deletion_protection=None, enable_cloudwatch_logs_exports=None, enable_http_endpoint=None, enable_iam_database_authentication=None, endpoint_address=None, endpoint_port=None, engine=None, engine_version=None, global_cluster_identifier=None, id=None, master_user_password=None, port=None, preferred_backup_window=None, preferred_maintenance_window=None, read_endpoint_address=None, replication_source_identifier=None, scaling_configuration=None, tags=None, vpc_security_group_ids=None):
        if associated_roles and not isinstance(associated_roles, list):
            raise TypeError("Expected argument 'associated_roles' to be a list")
        pulumi.set(__self__, "associated_roles", associated_roles)
        if backtrack_window and not isinstance(backtrack_window, int):
            raise TypeError("Expected argument 'backtrack_window' to be a int")
        pulumi.set(__self__, "backtrack_window", backtrack_window)
        if backup_retention_period and not isinstance(backup_retention_period, int):
            raise TypeError("Expected argument 'backup_retention_period' to be a int")
        pulumi.set(__self__, "backup_retention_period", backup_retention_period)
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
        if enable_http_endpoint and not isinstance(enable_http_endpoint, bool):
            raise TypeError("Expected argument 'enable_http_endpoint' to be a bool")
        pulumi.set(__self__, "enable_http_endpoint", enable_http_endpoint)
        if enable_iam_database_authentication and not isinstance(enable_iam_database_authentication, bool):
            raise TypeError("Expected argument 'enable_iam_database_authentication' to be a bool")
        pulumi.set(__self__, "enable_iam_database_authentication", enable_iam_database_authentication)
        if endpoint_address and not isinstance(endpoint_address, str):
            raise TypeError("Expected argument 'endpoint_address' to be a str")
        pulumi.set(__self__, "endpoint_address", endpoint_address)
        if endpoint_port and not isinstance(endpoint_port, str):
            raise TypeError("Expected argument 'endpoint_port' to be a str")
        pulumi.set(__self__, "endpoint_port", endpoint_port)
        if engine and not isinstance(engine, str):
            raise TypeError("Expected argument 'engine' to be a str")
        pulumi.set(__self__, "engine", engine)
        if engine_version and not isinstance(engine_version, str):
            raise TypeError("Expected argument 'engine_version' to be a str")
        pulumi.set(__self__, "engine_version", engine_version)
        if global_cluster_identifier and not isinstance(global_cluster_identifier, str):
            raise TypeError("Expected argument 'global_cluster_identifier' to be a str")
        pulumi.set(__self__, "global_cluster_identifier", global_cluster_identifier)
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
        if read_endpoint_address and not isinstance(read_endpoint_address, str):
            raise TypeError("Expected argument 'read_endpoint_address' to be a str")
        pulumi.set(__self__, "read_endpoint_address", read_endpoint_address)
        if replication_source_identifier and not isinstance(replication_source_identifier, str):
            raise TypeError("Expected argument 'replication_source_identifier' to be a str")
        pulumi.set(__self__, "replication_source_identifier", replication_source_identifier)
        if scaling_configuration and not isinstance(scaling_configuration, dict):
            raise TypeError("Expected argument 'scaling_configuration' to be a dict")
        pulumi.set(__self__, "scaling_configuration", scaling_configuration)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if vpc_security_group_ids and not isinstance(vpc_security_group_ids, list):
            raise TypeError("Expected argument 'vpc_security_group_ids' to be a list")
        pulumi.set(__self__, "vpc_security_group_ids", vpc_security_group_ids)

    @property
    @pulumi.getter(name="associatedRoles")
    def associated_roles(self) -> Optional[Sequence['outputs.DBClusterRole']]:
        return pulumi.get(self, "associated_roles")

    @property
    @pulumi.getter(name="backtrackWindow")
    def backtrack_window(self) -> Optional[int]:
        return pulumi.get(self, "backtrack_window")

    @property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> Optional[int]:
        return pulumi.get(self, "backup_retention_period")

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
    @pulumi.getter(name="enableHttpEndpoint")
    def enable_http_endpoint(self) -> Optional[bool]:
        return pulumi.get(self, "enable_http_endpoint")

    @property
    @pulumi.getter(name="enableIAMDatabaseAuthentication")
    def enable_iam_database_authentication(self) -> Optional[bool]:
        return pulumi.get(self, "enable_iam_database_authentication")

    @property
    @pulumi.getter(name="endpointAddress")
    def endpoint_address(self) -> Optional[str]:
        return pulumi.get(self, "endpoint_address")

    @property
    @pulumi.getter(name="endpointPort")
    def endpoint_port(self) -> Optional[str]:
        return pulumi.get(self, "endpoint_port")

    @property
    @pulumi.getter
    def engine(self) -> Optional[str]:
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[str]:
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> Optional[str]:
        return pulumi.get(self, "global_cluster_identifier")

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
    @pulumi.getter(name="readEndpointAddress")
    def read_endpoint_address(self) -> Optional[str]:
        return pulumi.get(self, "read_endpoint_address")

    @property
    @pulumi.getter(name="replicationSourceIdentifier")
    def replication_source_identifier(self) -> Optional[str]:
        return pulumi.get(self, "replication_source_identifier")

    @property
    @pulumi.getter(name="scalingConfiguration")
    def scaling_configuration(self) -> Optional['outputs.DBClusterScalingConfiguration']:
        return pulumi.get(self, "scaling_configuration")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DBClusterTag']]:
        return pulumi.get(self, "tags")

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
            associated_roles=self.associated_roles,
            backtrack_window=self.backtrack_window,
            backup_retention_period=self.backup_retention_period,
            copy_tags_to_snapshot=self.copy_tags_to_snapshot,
            d_b_cluster_parameter_group_name=self.d_b_cluster_parameter_group_name,
            deletion_protection=self.deletion_protection,
            enable_cloudwatch_logs_exports=self.enable_cloudwatch_logs_exports,
            enable_http_endpoint=self.enable_http_endpoint,
            enable_iam_database_authentication=self.enable_iam_database_authentication,
            endpoint_address=self.endpoint_address,
            endpoint_port=self.endpoint_port,
            engine=self.engine,
            engine_version=self.engine_version,
            global_cluster_identifier=self.global_cluster_identifier,
            id=self.id,
            master_user_password=self.master_user_password,
            port=self.port,
            preferred_backup_window=self.preferred_backup_window,
            preferred_maintenance_window=self.preferred_maintenance_window,
            read_endpoint_address=self.read_endpoint_address,
            replication_source_identifier=self.replication_source_identifier,
            scaling_configuration=self.scaling_configuration,
            tags=self.tags,
            vpc_security_group_ids=self.vpc_security_group_ids)


def get_db_cluster(id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDBClusterResult:
    """
    Resource Type definition for AWS::RDS::DBCluster
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:rds:getDBCluster', __args__, opts=opts, typ=GetDBClusterResult).value

    return AwaitableGetDBClusterResult(
        associated_roles=__ret__.associated_roles,
        backtrack_window=__ret__.backtrack_window,
        backup_retention_period=__ret__.backup_retention_period,
        copy_tags_to_snapshot=__ret__.copy_tags_to_snapshot,
        d_b_cluster_parameter_group_name=__ret__.d_b_cluster_parameter_group_name,
        deletion_protection=__ret__.deletion_protection,
        enable_cloudwatch_logs_exports=__ret__.enable_cloudwatch_logs_exports,
        enable_http_endpoint=__ret__.enable_http_endpoint,
        enable_iam_database_authentication=__ret__.enable_iam_database_authentication,
        endpoint_address=__ret__.endpoint_address,
        endpoint_port=__ret__.endpoint_port,
        engine=__ret__.engine,
        engine_version=__ret__.engine_version,
        global_cluster_identifier=__ret__.global_cluster_identifier,
        id=__ret__.id,
        master_user_password=__ret__.master_user_password,
        port=__ret__.port,
        preferred_backup_window=__ret__.preferred_backup_window,
        preferred_maintenance_window=__ret__.preferred_maintenance_window,
        read_endpoint_address=__ret__.read_endpoint_address,
        replication_source_identifier=__ret__.replication_source_identifier,
        scaling_configuration=__ret__.scaling_configuration,
        tags=__ret__.tags,
        vpc_security_group_ids=__ret__.vpc_security_group_ids)


@_utilities.lift_output_func(get_db_cluster)
def get_db_cluster_output(id: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDBClusterResult]:
    """
    Resource Type definition for AWS::RDS::DBCluster
    """
    ...
