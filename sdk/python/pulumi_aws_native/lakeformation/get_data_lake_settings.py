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
    'GetDataLakeSettingsResult',
    'AwaitableGetDataLakeSettingsResult',
    'get_data_lake_settings',
    'get_data_lake_settings_output',
]

@pulumi.output_type
class GetDataLakeSettingsResult:
    def __init__(__self__, admins=None, allow_external_data_filtering=None, authorized_session_tag_value_list=None, create_database_default_permissions=None, create_table_default_permissions=None, external_data_filtering_allow_list=None, id=None, parameters=None, trusted_resource_owners=None):
        if admins and not isinstance(admins, dict):
            raise TypeError("Expected argument 'admins' to be a dict")
        pulumi.set(__self__, "admins", admins)
        if allow_external_data_filtering and not isinstance(allow_external_data_filtering, bool):
            raise TypeError("Expected argument 'allow_external_data_filtering' to be a bool")
        pulumi.set(__self__, "allow_external_data_filtering", allow_external_data_filtering)
        if authorized_session_tag_value_list and not isinstance(authorized_session_tag_value_list, list):
            raise TypeError("Expected argument 'authorized_session_tag_value_list' to be a list")
        pulumi.set(__self__, "authorized_session_tag_value_list", authorized_session_tag_value_list)
        if create_database_default_permissions and not isinstance(create_database_default_permissions, dict):
            raise TypeError("Expected argument 'create_database_default_permissions' to be a dict")
        pulumi.set(__self__, "create_database_default_permissions", create_database_default_permissions)
        if create_table_default_permissions and not isinstance(create_table_default_permissions, dict):
            raise TypeError("Expected argument 'create_table_default_permissions' to be a dict")
        pulumi.set(__self__, "create_table_default_permissions", create_table_default_permissions)
        if external_data_filtering_allow_list and not isinstance(external_data_filtering_allow_list, dict):
            raise TypeError("Expected argument 'external_data_filtering_allow_list' to be a dict")
        pulumi.set(__self__, "external_data_filtering_allow_list", external_data_filtering_allow_list)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if trusted_resource_owners and not isinstance(trusted_resource_owners, list):
            raise TypeError("Expected argument 'trusted_resource_owners' to be a list")
        pulumi.set(__self__, "trusted_resource_owners", trusted_resource_owners)

    @property
    @pulumi.getter
    def admins(self) -> Optional['outputs.DataLakeSettingsAdmins']:
        return pulumi.get(self, "admins")

    @property
    @pulumi.getter(name="allowExternalDataFiltering")
    def allow_external_data_filtering(self) -> Optional[bool]:
        return pulumi.get(self, "allow_external_data_filtering")

    @property
    @pulumi.getter(name="authorizedSessionTagValueList")
    def authorized_session_tag_value_list(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "authorized_session_tag_value_list")

    @property
    @pulumi.getter(name="createDatabaseDefaultPermissions")
    def create_database_default_permissions(self) -> Optional['outputs.DataLakeSettingsCreateDatabaseDefaultPermissions']:
        return pulumi.get(self, "create_database_default_permissions")

    @property
    @pulumi.getter(name="createTableDefaultPermissions")
    def create_table_default_permissions(self) -> Optional['outputs.DataLakeSettingsCreateTableDefaultPermissions']:
        return pulumi.get(self, "create_table_default_permissions")

    @property
    @pulumi.getter(name="externalDataFilteringAllowList")
    def external_data_filtering_allow_list(self) -> Optional['outputs.DataLakeSettingsExternalDataFilteringAllowList']:
        return pulumi.get(self, "external_data_filtering_allow_list")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Any]:
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="trustedResourceOwners")
    def trusted_resource_owners(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "trusted_resource_owners")


class AwaitableGetDataLakeSettingsResult(GetDataLakeSettingsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataLakeSettingsResult(
            admins=self.admins,
            allow_external_data_filtering=self.allow_external_data_filtering,
            authorized_session_tag_value_list=self.authorized_session_tag_value_list,
            create_database_default_permissions=self.create_database_default_permissions,
            create_table_default_permissions=self.create_table_default_permissions,
            external_data_filtering_allow_list=self.external_data_filtering_allow_list,
            id=self.id,
            parameters=self.parameters,
            trusted_resource_owners=self.trusted_resource_owners)


def get_data_lake_settings(id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataLakeSettingsResult:
    """
    Resource Type definition for AWS::LakeFormation::DataLakeSettings
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:lakeformation:getDataLakeSettings', __args__, opts=opts, typ=GetDataLakeSettingsResult).value

    return AwaitableGetDataLakeSettingsResult(
        admins=__ret__.admins,
        allow_external_data_filtering=__ret__.allow_external_data_filtering,
        authorized_session_tag_value_list=__ret__.authorized_session_tag_value_list,
        create_database_default_permissions=__ret__.create_database_default_permissions,
        create_table_default_permissions=__ret__.create_table_default_permissions,
        external_data_filtering_allow_list=__ret__.external_data_filtering_allow_list,
        id=__ret__.id,
        parameters=__ret__.parameters,
        trusted_resource_owners=__ret__.trusted_resource_owners)


@_utilities.lift_output_func(get_data_lake_settings)
def get_data_lake_settings_output(id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDataLakeSettingsResult]:
    """
    Resource Type definition for AWS::LakeFormation::DataLakeSettings
    """
    ...
