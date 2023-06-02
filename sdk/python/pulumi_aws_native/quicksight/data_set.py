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

__all__ = ['DataSetArgs', 'DataSet']

@pulumi.input_type
class DataSetArgs:
    def __init__(__self__, *,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 column_groups: Optional[pulumi.Input[Sequence[pulumi.Input['DataSetColumnGroupArgs']]]] = None,
                 column_level_permission_rules: Optional[pulumi.Input[Sequence[pulumi.Input['DataSetColumnLevelPermissionRuleArgs']]]] = None,
                 data_set_id: Optional[pulumi.Input[str]] = None,
                 data_set_refresh_properties: Optional[pulumi.Input['DataSetRefreshPropertiesArgs']] = None,
                 data_set_usage_configuration: Optional[pulumi.Input['DataSetUsageConfigurationArgs']] = None,
                 dataset_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['DataSetDatasetParameterArgs']]]] = None,
                 field_folders: Optional[pulumi.Input['DataSetFieldFolderMapArgs']] = None,
                 import_mode: Optional[pulumi.Input['DataSetImportMode']] = None,
                 ingestion_wait_policy: Optional[pulumi.Input['DataSetIngestionWaitPolicyArgs']] = None,
                 logical_table_map: Optional[pulumi.Input['DataSetLogicalTableMapArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input['DataSetResourcePermissionArgs']]]] = None,
                 physical_table_map: Optional[pulumi.Input['DataSetPhysicalTableMapArgs']] = None,
                 row_level_permission_data_set: Optional[pulumi.Input['DataSetRowLevelPermissionDataSetArgs']] = None,
                 row_level_permission_tag_configuration: Optional[pulumi.Input['DataSetRowLevelPermissionTagConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DataSetTagArgs']]]] = None):
        """
        The set of arguments for constructing a DataSet resource.
        :param pulumi.Input[Sequence[pulumi.Input['DataSetColumnGroupArgs']]] column_groups: <p>Groupings of columns that work together in certain QuickSight features. Currently, only geospatial hierarchy is supported.</p>
        :param pulumi.Input[Sequence[pulumi.Input['DataSetDatasetParameterArgs']]] dataset_parameters: <p>The parameters declared in the dataset.</p>
        :param pulumi.Input[str] name: <p>The display name for the dataset.</p>
        :param pulumi.Input[Sequence[pulumi.Input['DataSetResourcePermissionArgs']]] permissions: <p>A list of resource permissions on the dataset.</p>
        :param pulumi.Input[Sequence[pulumi.Input['DataSetTagArgs']]] tags: <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.</p>
        """
        if aws_account_id is not None:
            pulumi.set(__self__, "aws_account_id", aws_account_id)
        if column_groups is not None:
            pulumi.set(__self__, "column_groups", column_groups)
        if column_level_permission_rules is not None:
            pulumi.set(__self__, "column_level_permission_rules", column_level_permission_rules)
        if data_set_id is not None:
            pulumi.set(__self__, "data_set_id", data_set_id)
        if data_set_refresh_properties is not None:
            pulumi.set(__self__, "data_set_refresh_properties", data_set_refresh_properties)
        if data_set_usage_configuration is not None:
            pulumi.set(__self__, "data_set_usage_configuration", data_set_usage_configuration)
        if dataset_parameters is not None:
            pulumi.set(__self__, "dataset_parameters", dataset_parameters)
        if field_folders is not None:
            pulumi.set(__self__, "field_folders", field_folders)
        if import_mode is not None:
            pulumi.set(__self__, "import_mode", import_mode)
        if ingestion_wait_policy is not None:
            pulumi.set(__self__, "ingestion_wait_policy", ingestion_wait_policy)
        if logical_table_map is not None:
            pulumi.set(__self__, "logical_table_map", logical_table_map)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if physical_table_map is not None:
            pulumi.set(__self__, "physical_table_map", physical_table_map)
        if row_level_permission_data_set is not None:
            pulumi.set(__self__, "row_level_permission_data_set", row_level_permission_data_set)
        if row_level_permission_tag_configuration is not None:
            pulumi.set(__self__, "row_level_permission_tag_configuration", row_level_permission_tag_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "aws_account_id")

    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_account_id", value)

    @property
    @pulumi.getter(name="columnGroups")
    def column_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataSetColumnGroupArgs']]]]:
        """
        <p>Groupings of columns that work together in certain QuickSight features. Currently, only geospatial hierarchy is supported.</p>
        """
        return pulumi.get(self, "column_groups")

    @column_groups.setter
    def column_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataSetColumnGroupArgs']]]]):
        pulumi.set(self, "column_groups", value)

    @property
    @pulumi.getter(name="columnLevelPermissionRules")
    def column_level_permission_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataSetColumnLevelPermissionRuleArgs']]]]:
        return pulumi.get(self, "column_level_permission_rules")

    @column_level_permission_rules.setter
    def column_level_permission_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataSetColumnLevelPermissionRuleArgs']]]]):
        pulumi.set(self, "column_level_permission_rules", value)

    @property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "data_set_id")

    @data_set_id.setter
    def data_set_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_set_id", value)

    @property
    @pulumi.getter(name="dataSetRefreshProperties")
    def data_set_refresh_properties(self) -> Optional[pulumi.Input['DataSetRefreshPropertiesArgs']]:
        return pulumi.get(self, "data_set_refresh_properties")

    @data_set_refresh_properties.setter
    def data_set_refresh_properties(self, value: Optional[pulumi.Input['DataSetRefreshPropertiesArgs']]):
        pulumi.set(self, "data_set_refresh_properties", value)

    @property
    @pulumi.getter(name="dataSetUsageConfiguration")
    def data_set_usage_configuration(self) -> Optional[pulumi.Input['DataSetUsageConfigurationArgs']]:
        return pulumi.get(self, "data_set_usage_configuration")

    @data_set_usage_configuration.setter
    def data_set_usage_configuration(self, value: Optional[pulumi.Input['DataSetUsageConfigurationArgs']]):
        pulumi.set(self, "data_set_usage_configuration", value)

    @property
    @pulumi.getter(name="datasetParameters")
    def dataset_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataSetDatasetParameterArgs']]]]:
        """
        <p>The parameters declared in the dataset.</p>
        """
        return pulumi.get(self, "dataset_parameters")

    @dataset_parameters.setter
    def dataset_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataSetDatasetParameterArgs']]]]):
        pulumi.set(self, "dataset_parameters", value)

    @property
    @pulumi.getter(name="fieldFolders")
    def field_folders(self) -> Optional[pulumi.Input['DataSetFieldFolderMapArgs']]:
        return pulumi.get(self, "field_folders")

    @field_folders.setter
    def field_folders(self, value: Optional[pulumi.Input['DataSetFieldFolderMapArgs']]):
        pulumi.set(self, "field_folders", value)

    @property
    @pulumi.getter(name="importMode")
    def import_mode(self) -> Optional[pulumi.Input['DataSetImportMode']]:
        return pulumi.get(self, "import_mode")

    @import_mode.setter
    def import_mode(self, value: Optional[pulumi.Input['DataSetImportMode']]):
        pulumi.set(self, "import_mode", value)

    @property
    @pulumi.getter(name="ingestionWaitPolicy")
    def ingestion_wait_policy(self) -> Optional[pulumi.Input['DataSetIngestionWaitPolicyArgs']]:
        return pulumi.get(self, "ingestion_wait_policy")

    @ingestion_wait_policy.setter
    def ingestion_wait_policy(self, value: Optional[pulumi.Input['DataSetIngestionWaitPolicyArgs']]):
        pulumi.set(self, "ingestion_wait_policy", value)

    @property
    @pulumi.getter(name="logicalTableMap")
    def logical_table_map(self) -> Optional[pulumi.Input['DataSetLogicalTableMapArgs']]:
        return pulumi.get(self, "logical_table_map")

    @logical_table_map.setter
    def logical_table_map(self, value: Optional[pulumi.Input['DataSetLogicalTableMapArgs']]):
        pulumi.set(self, "logical_table_map", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        <p>The display name for the dataset.</p>
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataSetResourcePermissionArgs']]]]:
        """
        <p>A list of resource permissions on the dataset.</p>
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataSetResourcePermissionArgs']]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter(name="physicalTableMap")
    def physical_table_map(self) -> Optional[pulumi.Input['DataSetPhysicalTableMapArgs']]:
        return pulumi.get(self, "physical_table_map")

    @physical_table_map.setter
    def physical_table_map(self, value: Optional[pulumi.Input['DataSetPhysicalTableMapArgs']]):
        pulumi.set(self, "physical_table_map", value)

    @property
    @pulumi.getter(name="rowLevelPermissionDataSet")
    def row_level_permission_data_set(self) -> Optional[pulumi.Input['DataSetRowLevelPermissionDataSetArgs']]:
        return pulumi.get(self, "row_level_permission_data_set")

    @row_level_permission_data_set.setter
    def row_level_permission_data_set(self, value: Optional[pulumi.Input['DataSetRowLevelPermissionDataSetArgs']]):
        pulumi.set(self, "row_level_permission_data_set", value)

    @property
    @pulumi.getter(name="rowLevelPermissionTagConfiguration")
    def row_level_permission_tag_configuration(self) -> Optional[pulumi.Input['DataSetRowLevelPermissionTagConfigurationArgs']]:
        return pulumi.get(self, "row_level_permission_tag_configuration")

    @row_level_permission_tag_configuration.setter
    def row_level_permission_tag_configuration(self, value: Optional[pulumi.Input['DataSetRowLevelPermissionTagConfigurationArgs']]):
        pulumi.set(self, "row_level_permission_tag_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataSetTagArgs']]]]:
        """
        <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.</p>
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataSetTagArgs']]]]):
        pulumi.set(self, "tags", value)


class DataSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 column_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSetColumnGroupArgs']]]]] = None,
                 column_level_permission_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSetColumnLevelPermissionRuleArgs']]]]] = None,
                 data_set_id: Optional[pulumi.Input[str]] = None,
                 data_set_refresh_properties: Optional[pulumi.Input[pulumi.InputType['DataSetRefreshPropertiesArgs']]] = None,
                 data_set_usage_configuration: Optional[pulumi.Input[pulumi.InputType['DataSetUsageConfigurationArgs']]] = None,
                 dataset_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSetDatasetParameterArgs']]]]] = None,
                 field_folders: Optional[pulumi.Input[pulumi.InputType['DataSetFieldFolderMapArgs']]] = None,
                 import_mode: Optional[pulumi.Input['DataSetImportMode']] = None,
                 ingestion_wait_policy: Optional[pulumi.Input[pulumi.InputType['DataSetIngestionWaitPolicyArgs']]] = None,
                 logical_table_map: Optional[pulumi.Input[pulumi.InputType['DataSetLogicalTableMapArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSetResourcePermissionArgs']]]]] = None,
                 physical_table_map: Optional[pulumi.Input[pulumi.InputType['DataSetPhysicalTableMapArgs']]] = None,
                 row_level_permission_data_set: Optional[pulumi.Input[pulumi.InputType['DataSetRowLevelPermissionDataSetArgs']]] = None,
                 row_level_permission_tag_configuration: Optional[pulumi.Input[pulumi.InputType['DataSetRowLevelPermissionTagConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSetTagArgs']]]]] = None,
                 __props__=None):
        """
        Definition of the AWS::QuickSight::DataSet Resource Type.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSetColumnGroupArgs']]]] column_groups: <p>Groupings of columns that work together in certain QuickSight features. Currently, only geospatial hierarchy is supported.</p>
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSetDatasetParameterArgs']]]] dataset_parameters: <p>The parameters declared in the dataset.</p>
        :param pulumi.Input[str] name: <p>The display name for the dataset.</p>
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSetResourcePermissionArgs']]]] permissions: <p>A list of resource permissions on the dataset.</p>
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSetTagArgs']]]] tags: <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.</p>
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DataSetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of the AWS::QuickSight::DataSet Resource Type.

        :param str resource_name: The name of the resource.
        :param DataSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 column_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSetColumnGroupArgs']]]]] = None,
                 column_level_permission_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSetColumnLevelPermissionRuleArgs']]]]] = None,
                 data_set_id: Optional[pulumi.Input[str]] = None,
                 data_set_refresh_properties: Optional[pulumi.Input[pulumi.InputType['DataSetRefreshPropertiesArgs']]] = None,
                 data_set_usage_configuration: Optional[pulumi.Input[pulumi.InputType['DataSetUsageConfigurationArgs']]] = None,
                 dataset_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSetDatasetParameterArgs']]]]] = None,
                 field_folders: Optional[pulumi.Input[pulumi.InputType['DataSetFieldFolderMapArgs']]] = None,
                 import_mode: Optional[pulumi.Input['DataSetImportMode']] = None,
                 ingestion_wait_policy: Optional[pulumi.Input[pulumi.InputType['DataSetIngestionWaitPolicyArgs']]] = None,
                 logical_table_map: Optional[pulumi.Input[pulumi.InputType['DataSetLogicalTableMapArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSetResourcePermissionArgs']]]]] = None,
                 physical_table_map: Optional[pulumi.Input[pulumi.InputType['DataSetPhysicalTableMapArgs']]] = None,
                 row_level_permission_data_set: Optional[pulumi.Input[pulumi.InputType['DataSetRowLevelPermissionDataSetArgs']]] = None,
                 row_level_permission_tag_configuration: Optional[pulumi.Input[pulumi.InputType['DataSetRowLevelPermissionTagConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataSetTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataSetArgs.__new__(DataSetArgs)

            __props__.__dict__["aws_account_id"] = aws_account_id
            __props__.__dict__["column_groups"] = column_groups
            __props__.__dict__["column_level_permission_rules"] = column_level_permission_rules
            __props__.__dict__["data_set_id"] = data_set_id
            __props__.__dict__["data_set_refresh_properties"] = data_set_refresh_properties
            __props__.__dict__["data_set_usage_configuration"] = data_set_usage_configuration
            __props__.__dict__["dataset_parameters"] = dataset_parameters
            __props__.__dict__["field_folders"] = field_folders
            __props__.__dict__["import_mode"] = import_mode
            __props__.__dict__["ingestion_wait_policy"] = ingestion_wait_policy
            __props__.__dict__["logical_table_map"] = logical_table_map
            __props__.__dict__["name"] = name
            __props__.__dict__["permissions"] = permissions
            __props__.__dict__["physical_table_map"] = physical_table_map
            __props__.__dict__["row_level_permission_data_set"] = row_level_permission_data_set
            __props__.__dict__["row_level_permission_tag_configuration"] = row_level_permission_tag_configuration
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["consumed_spice_capacity_in_bytes"] = None
            __props__.__dict__["created_time"] = None
            __props__.__dict__["last_updated_time"] = None
            __props__.__dict__["output_columns"] = None
        super(DataSet, __self__).__init__(
            'aws-native:quicksight:DataSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DataSet':
        """
        Get an existing DataSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DataSetArgs.__new__(DataSetArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["aws_account_id"] = None
        __props__.__dict__["column_groups"] = None
        __props__.__dict__["column_level_permission_rules"] = None
        __props__.__dict__["consumed_spice_capacity_in_bytes"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["data_set_id"] = None
        __props__.__dict__["data_set_refresh_properties"] = None
        __props__.__dict__["data_set_usage_configuration"] = None
        __props__.__dict__["dataset_parameters"] = None
        __props__.__dict__["field_folders"] = None
        __props__.__dict__["import_mode"] = None
        __props__.__dict__["ingestion_wait_policy"] = None
        __props__.__dict__["last_updated_time"] = None
        __props__.__dict__["logical_table_map"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["output_columns"] = None
        __props__.__dict__["permissions"] = None
        __props__.__dict__["physical_table_map"] = None
        __props__.__dict__["row_level_permission_data_set"] = None
        __props__.__dict__["row_level_permission_tag_configuration"] = None
        __props__.__dict__["tags"] = None
        return DataSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        <p>The Amazon Resource Name (ARN) of the resource.</p>
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "aws_account_id")

    @property
    @pulumi.getter(name="columnGroups")
    def column_groups(self) -> pulumi.Output[Optional[Sequence['outputs.DataSetColumnGroup']]]:
        """
        <p>Groupings of columns that work together in certain QuickSight features. Currently, only geospatial hierarchy is supported.</p>
        """
        return pulumi.get(self, "column_groups")

    @property
    @pulumi.getter(name="columnLevelPermissionRules")
    def column_level_permission_rules(self) -> pulumi.Output[Optional[Sequence['outputs.DataSetColumnLevelPermissionRule']]]:
        return pulumi.get(self, "column_level_permission_rules")

    @property
    @pulumi.getter(name="consumedSpiceCapacityInBytes")
    def consumed_spice_capacity_in_bytes(self) -> pulumi.Output[float]:
        """
        <p>The amount of SPICE capacity used by this dataset. This is 0 if the dataset isn't
                    imported into SPICE.</p>
        """
        return pulumi.get(self, "consumed_spice_capacity_in_bytes")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        """
        <p>The time that this dataset was created.</p>
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "data_set_id")

    @property
    @pulumi.getter(name="dataSetRefreshProperties")
    def data_set_refresh_properties(self) -> pulumi.Output[Optional['outputs.DataSetRefreshProperties']]:
        return pulumi.get(self, "data_set_refresh_properties")

    @property
    @pulumi.getter(name="dataSetUsageConfiguration")
    def data_set_usage_configuration(self) -> pulumi.Output[Optional['outputs.DataSetUsageConfiguration']]:
        return pulumi.get(self, "data_set_usage_configuration")

    @property
    @pulumi.getter(name="datasetParameters")
    def dataset_parameters(self) -> pulumi.Output[Optional[Sequence['outputs.DataSetDatasetParameter']]]:
        """
        <p>The parameters declared in the dataset.</p>
        """
        return pulumi.get(self, "dataset_parameters")

    @property
    @pulumi.getter(name="fieldFolders")
    def field_folders(self) -> pulumi.Output[Optional['outputs.DataSetFieldFolderMap']]:
        return pulumi.get(self, "field_folders")

    @property
    @pulumi.getter(name="importMode")
    def import_mode(self) -> pulumi.Output[Optional['DataSetImportMode']]:
        return pulumi.get(self, "import_mode")

    @property
    @pulumi.getter(name="ingestionWaitPolicy")
    def ingestion_wait_policy(self) -> pulumi.Output[Optional['outputs.DataSetIngestionWaitPolicy']]:
        return pulumi.get(self, "ingestion_wait_policy")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[str]:
        """
        <p>The last time that this dataset was updated.</p>
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter(name="logicalTableMap")
    def logical_table_map(self) -> pulumi.Output[Optional['outputs.DataSetLogicalTableMap']]:
        return pulumi.get(self, "logical_table_map")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        <p>The display name for the dataset.</p>
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outputColumns")
    def output_columns(self) -> pulumi.Output[Sequence['outputs.DataSetOutputColumn']]:
        """
        <p>The list of columns after all transforms. These columns are available in templates,
                    analyses, and dashboards.</p>
        """
        return pulumi.get(self, "output_columns")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[Sequence['outputs.DataSetResourcePermission']]]:
        """
        <p>A list of resource permissions on the dataset.</p>
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="physicalTableMap")
    def physical_table_map(self) -> pulumi.Output[Optional['outputs.DataSetPhysicalTableMap']]:
        return pulumi.get(self, "physical_table_map")

    @property
    @pulumi.getter(name="rowLevelPermissionDataSet")
    def row_level_permission_data_set(self) -> pulumi.Output[Optional['outputs.DataSetRowLevelPermissionDataSet']]:
        return pulumi.get(self, "row_level_permission_data_set")

    @property
    @pulumi.getter(name="rowLevelPermissionTagConfiguration")
    def row_level_permission_tag_configuration(self) -> pulumi.Output[Optional['outputs.DataSetRowLevelPermissionTagConfiguration']]:
        return pulumi.get(self, "row_level_permission_tag_configuration")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DataSetTag']]]:
        """
        <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.</p>
        """
        return pulumi.get(self, "tags")

