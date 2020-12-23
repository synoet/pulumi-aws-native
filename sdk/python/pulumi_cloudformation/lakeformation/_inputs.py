# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'DataLakeSettingsAdminsArgs',
    'DataLakeSettingsPropertiesArgs',
    'PermissionsColumnWildcardArgs',
    'PermissionsDataLakePrincipalArgs',
    'PermissionsDataLocationResourceArgs',
    'PermissionsDatabaseResourceArgs',
    'PermissionsPropertiesArgs',
    'PermissionsResourceArgs',
    'PermissionsTableResourceArgs',
    'PermissionsTableWildcardArgs',
    'PermissionsTableWithColumnsResourceArgs',
    'ResourcePropertiesArgs',
]

@pulumi.input_type
class DataLakeSettingsAdminsArgs:
    def __init__(__self__):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-admins.html
        """
        pass


@pulumi.input_type
class DataLakeSettingsPropertiesArgs:
    def __init__(__self__, *,
                 admins: Optional[pulumi.Input['DataLakeSettingsAdminsArgs']] = None,
                 trusted_resource_owners: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html
        :param pulumi.Input['DataLakeSettingsAdminsArgs'] admins: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-admins
        :param pulumi.Input[Sequence[pulumi.Input[str]]] trusted_resource_owners: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-trustedresourceowners
        """
        if admins is not None:
            pulumi.set(__self__, "admins", admins)
        if trusted_resource_owners is not None:
            pulumi.set(__self__, "trusted_resource_owners", trusted_resource_owners)

    @property
    @pulumi.getter(name="Admins")
    def admins(self) -> Optional[pulumi.Input['DataLakeSettingsAdminsArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-admins
        """
        return pulumi.get(self, "admins")

    @admins.setter
    def admins(self, value: Optional[pulumi.Input['DataLakeSettingsAdminsArgs']]):
        pulumi.set(self, "admins", value)

    @property
    @pulumi.getter(name="TrustedResourceOwners")
    def trusted_resource_owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-trustedresourceowners
        """
        return pulumi.get(self, "trusted_resource_owners")

    @trusted_resource_owners.setter
    def trusted_resource_owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "trusted_resource_owners", value)


@pulumi.input_type
class PermissionsColumnWildcardArgs:
    def __init__(__self__, *,
                 excluded_column_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html
        :param pulumi.Input[Sequence[pulumi.Input[str]]] excluded_column_names: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html#cfn-lakeformation-permissions-columnwildcard-excludedcolumnnames
        """
        if excluded_column_names is not None:
            pulumi.set(__self__, "excluded_column_names", excluded_column_names)

    @property
    @pulumi.getter(name="ExcludedColumnNames")
    def excluded_column_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html#cfn-lakeformation-permissions-columnwildcard-excludedcolumnnames
        """
        return pulumi.get(self, "excluded_column_names")

    @excluded_column_names.setter
    def excluded_column_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "excluded_column_names", value)


@pulumi.input_type
class PermissionsDataLakePrincipalArgs:
    def __init__(__self__, *,
                 data_lake_principal_identifier: Optional[pulumi.Input[str]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html
        :param pulumi.Input[str] data_lake_principal_identifier: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html#cfn-lakeformation-permissions-datalakeprincipal-datalakeprincipalidentifier
        """
        if data_lake_principal_identifier is not None:
            pulumi.set(__self__, "data_lake_principal_identifier", data_lake_principal_identifier)

    @property
    @pulumi.getter(name="DataLakePrincipalIdentifier")
    def data_lake_principal_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html#cfn-lakeformation-permissions-datalakeprincipal-datalakeprincipalidentifier
        """
        return pulumi.get(self, "data_lake_principal_identifier")

    @data_lake_principal_identifier.setter
    def data_lake_principal_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_lake_principal_identifier", value)


@pulumi.input_type
class PermissionsDataLocationResourceArgs:
    def __init__(__self__, *,
                 catalog_id: Optional[pulumi.Input[str]] = None,
                 s3_resource: Optional[pulumi.Input[str]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html
        :param pulumi.Input[str] catalog_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-catalogid
        :param pulumi.Input[str] s3_resource: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-s3resource
        """
        if catalog_id is not None:
            pulumi.set(__self__, "catalog_id", catalog_id)
        if s3_resource is not None:
            pulumi.set(__self__, "s3_resource", s3_resource)

    @property
    @pulumi.getter(name="CatalogId")
    def catalog_id(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-catalogid
        """
        return pulumi.get(self, "catalog_id")

    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog_id", value)

    @property
    @pulumi.getter(name="S3Resource")
    def s3_resource(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-s3resource
        """
        return pulumi.get(self, "s3_resource")

    @s3_resource.setter
    def s3_resource(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "s3_resource", value)


@pulumi.input_type
class PermissionsDatabaseResourceArgs:
    def __init__(__self__, *,
                 catalog_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html
        :param pulumi.Input[str] catalog_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-catalogid
        :param pulumi.Input[str] name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-name
        """
        if catalog_id is not None:
            pulumi.set(__self__, "catalog_id", catalog_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="CatalogId")
    def catalog_id(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-catalogid
        """
        return pulumi.get(self, "catalog_id")

    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog_id", value)

    @property
    @pulumi.getter(name="Name")
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class PermissionsPropertiesArgs:
    def __init__(__self__, *,
                 data_lake_principal: pulumi.Input['PermissionsDataLakePrincipalArgs'],
                 resource: pulumi.Input['PermissionsResourceArgs'],
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 permissions_with_grant_option: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html
        :param pulumi.Input['PermissionsDataLakePrincipalArgs'] data_lake_principal: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-datalakeprincipal
        :param pulumi.Input['PermissionsResourceArgs'] resource: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-resource
        :param pulumi.Input[Sequence[pulumi.Input[str]]] permissions: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissions
        :param pulumi.Input[Sequence[pulumi.Input[str]]] permissions_with_grant_option: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissionswithgrantoption
        """
        pulumi.set(__self__, "data_lake_principal", data_lake_principal)
        pulumi.set(__self__, "resource", resource)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if permissions_with_grant_option is not None:
            pulumi.set(__self__, "permissions_with_grant_option", permissions_with_grant_option)

    @property
    @pulumi.getter(name="DataLakePrincipal")
    def data_lake_principal(self) -> pulumi.Input['PermissionsDataLakePrincipalArgs']:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-datalakeprincipal
        """
        return pulumi.get(self, "data_lake_principal")

    @data_lake_principal.setter
    def data_lake_principal(self, value: pulumi.Input['PermissionsDataLakePrincipalArgs']):
        pulumi.set(self, "data_lake_principal", value)

    @property
    @pulumi.getter(name="Resource")
    def resource(self) -> pulumi.Input['PermissionsResourceArgs']:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-resource
        """
        return pulumi.get(self, "resource")

    @resource.setter
    def resource(self, value: pulumi.Input['PermissionsResourceArgs']):
        pulumi.set(self, "resource", value)

    @property
    @pulumi.getter(name="Permissions")
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissions
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter(name="PermissionsWithGrantOption")
    def permissions_with_grant_option(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissionswithgrantoption
        """
        return pulumi.get(self, "permissions_with_grant_option")

    @permissions_with_grant_option.setter
    def permissions_with_grant_option(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "permissions_with_grant_option", value)


@pulumi.input_type
class PermissionsResourceArgs:
    def __init__(__self__, *,
                 data_location_resource: Optional[pulumi.Input['PermissionsDataLocationResourceArgs']] = None,
                 database_resource: Optional[pulumi.Input['PermissionsDatabaseResourceArgs']] = None,
                 table_resource: Optional[pulumi.Input['PermissionsTableResourceArgs']] = None,
                 table_with_columns_resource: Optional[pulumi.Input['PermissionsTableWithColumnsResourceArgs']] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html
        :param pulumi.Input['PermissionsDataLocationResourceArgs'] data_location_resource: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-datalocationresource
        :param pulumi.Input['PermissionsDatabaseResourceArgs'] database_resource: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-databaseresource
        :param pulumi.Input['PermissionsTableResourceArgs'] table_resource: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tableresource
        :param pulumi.Input['PermissionsTableWithColumnsResourceArgs'] table_with_columns_resource: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tablewithcolumnsresource
        """
        if data_location_resource is not None:
            pulumi.set(__self__, "data_location_resource", data_location_resource)
        if database_resource is not None:
            pulumi.set(__self__, "database_resource", database_resource)
        if table_resource is not None:
            pulumi.set(__self__, "table_resource", table_resource)
        if table_with_columns_resource is not None:
            pulumi.set(__self__, "table_with_columns_resource", table_with_columns_resource)

    @property
    @pulumi.getter(name="DataLocationResource")
    def data_location_resource(self) -> Optional[pulumi.Input['PermissionsDataLocationResourceArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-datalocationresource
        """
        return pulumi.get(self, "data_location_resource")

    @data_location_resource.setter
    def data_location_resource(self, value: Optional[pulumi.Input['PermissionsDataLocationResourceArgs']]):
        pulumi.set(self, "data_location_resource", value)

    @property
    @pulumi.getter(name="DatabaseResource")
    def database_resource(self) -> Optional[pulumi.Input['PermissionsDatabaseResourceArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-databaseresource
        """
        return pulumi.get(self, "database_resource")

    @database_resource.setter
    def database_resource(self, value: Optional[pulumi.Input['PermissionsDatabaseResourceArgs']]):
        pulumi.set(self, "database_resource", value)

    @property
    @pulumi.getter(name="TableResource")
    def table_resource(self) -> Optional[pulumi.Input['PermissionsTableResourceArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tableresource
        """
        return pulumi.get(self, "table_resource")

    @table_resource.setter
    def table_resource(self, value: Optional[pulumi.Input['PermissionsTableResourceArgs']]):
        pulumi.set(self, "table_resource", value)

    @property
    @pulumi.getter(name="TableWithColumnsResource")
    def table_with_columns_resource(self) -> Optional[pulumi.Input['PermissionsTableWithColumnsResourceArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tablewithcolumnsresource
        """
        return pulumi.get(self, "table_with_columns_resource")

    @table_with_columns_resource.setter
    def table_with_columns_resource(self, value: Optional[pulumi.Input['PermissionsTableWithColumnsResourceArgs']]):
        pulumi.set(self, "table_with_columns_resource", value)


@pulumi.input_type
class PermissionsTableResourceArgs:
    def __init__(__self__, *,
                 catalog_id: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 table_wildcard: Optional[pulumi.Input['PermissionsTableWildcardArgs']] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html
        :param pulumi.Input[str] catalog_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-catalogid
        :param pulumi.Input[str] database_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-databasename
        :param pulumi.Input[str] name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-name
        :param pulumi.Input['PermissionsTableWildcardArgs'] table_wildcard: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-tablewildcard
        """
        if catalog_id is not None:
            pulumi.set(__self__, "catalog_id", catalog_id)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if table_wildcard is not None:
            pulumi.set(__self__, "table_wildcard", table_wildcard)

    @property
    @pulumi.getter(name="CatalogId")
    def catalog_id(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-catalogid
        """
        return pulumi.get(self, "catalog_id")

    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog_id", value)

    @property
    @pulumi.getter(name="DatabaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-databasename
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="Name")
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="TableWildcard")
    def table_wildcard(self) -> Optional[pulumi.Input['PermissionsTableWildcardArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-tablewildcard
        """
        return pulumi.get(self, "table_wildcard")

    @table_wildcard.setter
    def table_wildcard(self, value: Optional[pulumi.Input['PermissionsTableWildcardArgs']]):
        pulumi.set(self, "table_wildcard", value)


@pulumi.input_type
class PermissionsTableWildcardArgs:
    def __init__(__self__):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewildcard.html
        """
        pass


@pulumi.input_type
class PermissionsTableWithColumnsResourceArgs:
    def __init__(__self__, *,
                 catalog_id: Optional[pulumi.Input[str]] = None,
                 column_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 column_wildcard: Optional[pulumi.Input['PermissionsColumnWildcardArgs']] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html
        :param pulumi.Input[str] catalog_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-catalogid
        :param pulumi.Input[Sequence[pulumi.Input[str]]] column_names: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnnames
        :param pulumi.Input['PermissionsColumnWildcardArgs'] column_wildcard: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnwildcard
        :param pulumi.Input[str] database_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-databasename
        :param pulumi.Input[str] name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-name
        """
        if catalog_id is not None:
            pulumi.set(__self__, "catalog_id", catalog_id)
        if column_names is not None:
            pulumi.set(__self__, "column_names", column_names)
        if column_wildcard is not None:
            pulumi.set(__self__, "column_wildcard", column_wildcard)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="CatalogId")
    def catalog_id(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-catalogid
        """
        return pulumi.get(self, "catalog_id")

    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog_id", value)

    @property
    @pulumi.getter(name="ColumnNames")
    def column_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnnames
        """
        return pulumi.get(self, "column_names")

    @column_names.setter
    def column_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "column_names", value)

    @property
    @pulumi.getter(name="ColumnWildcard")
    def column_wildcard(self) -> Optional[pulumi.Input['PermissionsColumnWildcardArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnwildcard
        """
        return pulumi.get(self, "column_wildcard")

    @column_wildcard.setter
    def column_wildcard(self, value: Optional[pulumi.Input['PermissionsColumnWildcardArgs']]):
        pulumi.set(self, "column_wildcard", value)

    @property
    @pulumi.getter(name="DatabaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-databasename
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="Name")
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class ResourcePropertiesArgs:
    def __init__(__self__, *,
                 resource_arn: pulumi.Input[str],
                 use_service_linked_role: pulumi.Input[bool],
                 role_arn: Optional[pulumi.Input[str]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html
        :param pulumi.Input[str] resource_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-resourcearn
        :param pulumi.Input[bool] use_service_linked_role: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-useservicelinkedrole
        :param pulumi.Input[str] role_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-rolearn
        """
        pulumi.set(__self__, "resource_arn", resource_arn)
        pulumi.set(__self__, "use_service_linked_role", use_service_linked_role)
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)

    @property
    @pulumi.getter(name="ResourceArn")
    def resource_arn(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-resourcearn
        """
        return pulumi.get(self, "resource_arn")

    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_arn", value)

    @property
    @pulumi.getter(name="UseServiceLinkedRole")
    def use_service_linked_role(self) -> pulumi.Input[bool]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-useservicelinkedrole
        """
        return pulumi.get(self, "use_service_linked_role")

    @use_service_linked_role.setter
    def use_service_linked_role(self, value: pulumi.Input[bool]):
        pulumi.set(self, "use_service_linked_role", value)

    @property
    @pulumi.getter(name="RoleArn")
    def role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-rolearn
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_arn", value)


