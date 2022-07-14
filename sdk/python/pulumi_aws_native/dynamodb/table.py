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

__all__ = ['TableArgs', 'Table']

@pulumi.input_type
class TableArgs:
    def __init__(__self__, *,
                 key_schema: pulumi.Input[Sequence[pulumi.Input['TableKeySchemaArgs']]],
                 attribute_definitions: Optional[pulumi.Input[Sequence[pulumi.Input['TableAttributeDefinitionArgs']]]] = None,
                 billing_mode: Optional[pulumi.Input[str]] = None,
                 contributor_insights_specification: Optional[pulumi.Input['TableContributorInsightsSpecificationArgs']] = None,
                 global_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input['TableGlobalSecondaryIndexArgs']]]] = None,
                 kinesis_stream_specification: Optional[pulumi.Input['TableKinesisStreamSpecificationArgs']] = None,
                 local_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input['TableLocalSecondaryIndexArgs']]]] = None,
                 point_in_time_recovery_specification: Optional[pulumi.Input['TablePointInTimeRecoverySpecificationArgs']] = None,
                 provisioned_throughput: Optional[pulumi.Input['TableProvisionedThroughputArgs']] = None,
                 s_se_specification: Optional[pulumi.Input['TableSSESpecificationArgs']] = None,
                 stream_specification: Optional[pulumi.Input['TableStreamSpecificationArgs']] = None,
                 table_class: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['TableTagArgs']]]] = None,
                 time_to_live_specification: Optional[pulumi.Input['TableTimeToLiveSpecificationArgs']] = None):
        """
        The set of arguments for constructing a Table resource.
        """
        pulumi.set(__self__, "key_schema", key_schema)
        if attribute_definitions is not None:
            pulumi.set(__self__, "attribute_definitions", attribute_definitions)
        if billing_mode is not None:
            pulumi.set(__self__, "billing_mode", billing_mode)
        if contributor_insights_specification is not None:
            pulumi.set(__self__, "contributor_insights_specification", contributor_insights_specification)
        if global_secondary_indexes is not None:
            pulumi.set(__self__, "global_secondary_indexes", global_secondary_indexes)
        if kinesis_stream_specification is not None:
            pulumi.set(__self__, "kinesis_stream_specification", kinesis_stream_specification)
        if local_secondary_indexes is not None:
            pulumi.set(__self__, "local_secondary_indexes", local_secondary_indexes)
        if point_in_time_recovery_specification is not None:
            pulumi.set(__self__, "point_in_time_recovery_specification", point_in_time_recovery_specification)
        if provisioned_throughput is not None:
            pulumi.set(__self__, "provisioned_throughput", provisioned_throughput)
        if s_se_specification is not None:
            pulumi.set(__self__, "s_se_specification", s_se_specification)
        if stream_specification is not None:
            pulumi.set(__self__, "stream_specification", stream_specification)
        if table_class is not None:
            pulumi.set(__self__, "table_class", table_class)
        if table_name is not None:
            pulumi.set(__self__, "table_name", table_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if time_to_live_specification is not None:
            pulumi.set(__self__, "time_to_live_specification", time_to_live_specification)

    @property
    @pulumi.getter(name="keySchema")
    def key_schema(self) -> pulumi.Input[Sequence[pulumi.Input['TableKeySchemaArgs']]]:
        return pulumi.get(self, "key_schema")

    @key_schema.setter
    def key_schema(self, value: pulumi.Input[Sequence[pulumi.Input['TableKeySchemaArgs']]]):
        pulumi.set(self, "key_schema", value)

    @property
    @pulumi.getter(name="attributeDefinitions")
    def attribute_definitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableAttributeDefinitionArgs']]]]:
        return pulumi.get(self, "attribute_definitions")

    @attribute_definitions.setter
    def attribute_definitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableAttributeDefinitionArgs']]]]):
        pulumi.set(self, "attribute_definitions", value)

    @property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "billing_mode")

    @billing_mode.setter
    def billing_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "billing_mode", value)

    @property
    @pulumi.getter(name="contributorInsightsSpecification")
    def contributor_insights_specification(self) -> Optional[pulumi.Input['TableContributorInsightsSpecificationArgs']]:
        return pulumi.get(self, "contributor_insights_specification")

    @contributor_insights_specification.setter
    def contributor_insights_specification(self, value: Optional[pulumi.Input['TableContributorInsightsSpecificationArgs']]):
        pulumi.set(self, "contributor_insights_specification", value)

    @property
    @pulumi.getter(name="globalSecondaryIndexes")
    def global_secondary_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableGlobalSecondaryIndexArgs']]]]:
        return pulumi.get(self, "global_secondary_indexes")

    @global_secondary_indexes.setter
    def global_secondary_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableGlobalSecondaryIndexArgs']]]]):
        pulumi.set(self, "global_secondary_indexes", value)

    @property
    @pulumi.getter(name="kinesisStreamSpecification")
    def kinesis_stream_specification(self) -> Optional[pulumi.Input['TableKinesisStreamSpecificationArgs']]:
        return pulumi.get(self, "kinesis_stream_specification")

    @kinesis_stream_specification.setter
    def kinesis_stream_specification(self, value: Optional[pulumi.Input['TableKinesisStreamSpecificationArgs']]):
        pulumi.set(self, "kinesis_stream_specification", value)

    @property
    @pulumi.getter(name="localSecondaryIndexes")
    def local_secondary_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableLocalSecondaryIndexArgs']]]]:
        return pulumi.get(self, "local_secondary_indexes")

    @local_secondary_indexes.setter
    def local_secondary_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableLocalSecondaryIndexArgs']]]]):
        pulumi.set(self, "local_secondary_indexes", value)

    @property
    @pulumi.getter(name="pointInTimeRecoverySpecification")
    def point_in_time_recovery_specification(self) -> Optional[pulumi.Input['TablePointInTimeRecoverySpecificationArgs']]:
        return pulumi.get(self, "point_in_time_recovery_specification")

    @point_in_time_recovery_specification.setter
    def point_in_time_recovery_specification(self, value: Optional[pulumi.Input['TablePointInTimeRecoverySpecificationArgs']]):
        pulumi.set(self, "point_in_time_recovery_specification", value)

    @property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> Optional[pulumi.Input['TableProvisionedThroughputArgs']]:
        return pulumi.get(self, "provisioned_throughput")

    @provisioned_throughput.setter
    def provisioned_throughput(self, value: Optional[pulumi.Input['TableProvisionedThroughputArgs']]):
        pulumi.set(self, "provisioned_throughput", value)

    @property
    @pulumi.getter(name="sSESpecification")
    def s_se_specification(self) -> Optional[pulumi.Input['TableSSESpecificationArgs']]:
        return pulumi.get(self, "s_se_specification")

    @s_se_specification.setter
    def s_se_specification(self, value: Optional[pulumi.Input['TableSSESpecificationArgs']]):
        pulumi.set(self, "s_se_specification", value)

    @property
    @pulumi.getter(name="streamSpecification")
    def stream_specification(self) -> Optional[pulumi.Input['TableStreamSpecificationArgs']]:
        return pulumi.get(self, "stream_specification")

    @stream_specification.setter
    def stream_specification(self, value: Optional[pulumi.Input['TableStreamSpecificationArgs']]):
        pulumi.set(self, "stream_specification", value)

    @property
    @pulumi.getter(name="tableClass")
    def table_class(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "table_class")

    @table_class.setter
    def table_class(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table_class", value)

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "table_name")

    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="timeToLiveSpecification")
    def time_to_live_specification(self) -> Optional[pulumi.Input['TableTimeToLiveSpecificationArgs']]:
        return pulumi.get(self, "time_to_live_specification")

    @time_to_live_specification.setter
    def time_to_live_specification(self, value: Optional[pulumi.Input['TableTimeToLiveSpecificationArgs']]):
        pulumi.set(self, "time_to_live_specification", value)


warnings.warn("""Table is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Table(pulumi.CustomResource):
    warnings.warn("""Table is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attribute_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableAttributeDefinitionArgs']]]]] = None,
                 billing_mode: Optional[pulumi.Input[str]] = None,
                 contributor_insights_specification: Optional[pulumi.Input[pulumi.InputType['TableContributorInsightsSpecificationArgs']]] = None,
                 global_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableGlobalSecondaryIndexArgs']]]]] = None,
                 key_schema: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableKeySchemaArgs']]]]] = None,
                 kinesis_stream_specification: Optional[pulumi.Input[pulumi.InputType['TableKinesisStreamSpecificationArgs']]] = None,
                 local_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableLocalSecondaryIndexArgs']]]]] = None,
                 point_in_time_recovery_specification: Optional[pulumi.Input[pulumi.InputType['TablePointInTimeRecoverySpecificationArgs']]] = None,
                 provisioned_throughput: Optional[pulumi.Input[pulumi.InputType['TableProvisionedThroughputArgs']]] = None,
                 s_se_specification: Optional[pulumi.Input[pulumi.InputType['TableSSESpecificationArgs']]] = None,
                 stream_specification: Optional[pulumi.Input[pulumi.InputType['TableStreamSpecificationArgs']]] = None,
                 table_class: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableTagArgs']]]]] = None,
                 time_to_live_specification: Optional[pulumi.Input[pulumi.InputType['TableTimeToLiveSpecificationArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::DynamoDB::Table

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::DynamoDB::Table

        :param str resource_name: The name of the resource.
        :param TableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attribute_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableAttributeDefinitionArgs']]]]] = None,
                 billing_mode: Optional[pulumi.Input[str]] = None,
                 contributor_insights_specification: Optional[pulumi.Input[pulumi.InputType['TableContributorInsightsSpecificationArgs']]] = None,
                 global_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableGlobalSecondaryIndexArgs']]]]] = None,
                 key_schema: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableKeySchemaArgs']]]]] = None,
                 kinesis_stream_specification: Optional[pulumi.Input[pulumi.InputType['TableKinesisStreamSpecificationArgs']]] = None,
                 local_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableLocalSecondaryIndexArgs']]]]] = None,
                 point_in_time_recovery_specification: Optional[pulumi.Input[pulumi.InputType['TablePointInTimeRecoverySpecificationArgs']]] = None,
                 provisioned_throughput: Optional[pulumi.Input[pulumi.InputType['TableProvisionedThroughputArgs']]] = None,
                 s_se_specification: Optional[pulumi.Input[pulumi.InputType['TableSSESpecificationArgs']]] = None,
                 stream_specification: Optional[pulumi.Input[pulumi.InputType['TableStreamSpecificationArgs']]] = None,
                 table_class: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableTagArgs']]]]] = None,
                 time_to_live_specification: Optional[pulumi.Input[pulumi.InputType['TableTimeToLiveSpecificationArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""Table is deprecated: Table is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TableArgs.__new__(TableArgs)

            __props__.__dict__["attribute_definitions"] = attribute_definitions
            __props__.__dict__["billing_mode"] = billing_mode
            __props__.__dict__["contributor_insights_specification"] = contributor_insights_specification
            __props__.__dict__["global_secondary_indexes"] = global_secondary_indexes
            if key_schema is None and not opts.urn:
                raise TypeError("Missing required property 'key_schema'")
            __props__.__dict__["key_schema"] = key_schema
            __props__.__dict__["kinesis_stream_specification"] = kinesis_stream_specification
            __props__.__dict__["local_secondary_indexes"] = local_secondary_indexes
            __props__.__dict__["point_in_time_recovery_specification"] = point_in_time_recovery_specification
            __props__.__dict__["provisioned_throughput"] = provisioned_throughput
            __props__.__dict__["s_se_specification"] = s_se_specification
            __props__.__dict__["stream_specification"] = stream_specification
            __props__.__dict__["table_class"] = table_class
            __props__.__dict__["table_name"] = table_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["time_to_live_specification"] = time_to_live_specification
            __props__.__dict__["arn"] = None
            __props__.__dict__["stream_arn"] = None
        super(Table, __self__).__init__(
            'aws-native:dynamodb:Table',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Table':
        """
        Get an existing Table resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TableArgs.__new__(TableArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["attribute_definitions"] = None
        __props__.__dict__["billing_mode"] = None
        __props__.__dict__["contributor_insights_specification"] = None
        __props__.__dict__["global_secondary_indexes"] = None
        __props__.__dict__["key_schema"] = None
        __props__.__dict__["kinesis_stream_specification"] = None
        __props__.__dict__["local_secondary_indexes"] = None
        __props__.__dict__["point_in_time_recovery_specification"] = None
        __props__.__dict__["provisioned_throughput"] = None
        __props__.__dict__["s_se_specification"] = None
        __props__.__dict__["stream_arn"] = None
        __props__.__dict__["stream_specification"] = None
        __props__.__dict__["table_class"] = None
        __props__.__dict__["table_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["time_to_live_specification"] = None
        return Table(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="attributeDefinitions")
    def attribute_definitions(self) -> pulumi.Output[Optional[Sequence['outputs.TableAttributeDefinition']]]:
        return pulumi.get(self, "attribute_definitions")

    @property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "billing_mode")

    @property
    @pulumi.getter(name="contributorInsightsSpecification")
    def contributor_insights_specification(self) -> pulumi.Output[Optional['outputs.TableContributorInsightsSpecification']]:
        return pulumi.get(self, "contributor_insights_specification")

    @property
    @pulumi.getter(name="globalSecondaryIndexes")
    def global_secondary_indexes(self) -> pulumi.Output[Optional[Sequence['outputs.TableGlobalSecondaryIndex']]]:
        return pulumi.get(self, "global_secondary_indexes")

    @property
    @pulumi.getter(name="keySchema")
    def key_schema(self) -> pulumi.Output[Sequence['outputs.TableKeySchema']]:
        return pulumi.get(self, "key_schema")

    @property
    @pulumi.getter(name="kinesisStreamSpecification")
    def kinesis_stream_specification(self) -> pulumi.Output[Optional['outputs.TableKinesisStreamSpecification']]:
        return pulumi.get(self, "kinesis_stream_specification")

    @property
    @pulumi.getter(name="localSecondaryIndexes")
    def local_secondary_indexes(self) -> pulumi.Output[Optional[Sequence['outputs.TableLocalSecondaryIndex']]]:
        return pulumi.get(self, "local_secondary_indexes")

    @property
    @pulumi.getter(name="pointInTimeRecoverySpecification")
    def point_in_time_recovery_specification(self) -> pulumi.Output[Optional['outputs.TablePointInTimeRecoverySpecification']]:
        return pulumi.get(self, "point_in_time_recovery_specification")

    @property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> pulumi.Output[Optional['outputs.TableProvisionedThroughput']]:
        return pulumi.get(self, "provisioned_throughput")

    @property
    @pulumi.getter(name="sSESpecification")
    def s_se_specification(self) -> pulumi.Output[Optional['outputs.TableSSESpecification']]:
        return pulumi.get(self, "s_se_specification")

    @property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "stream_arn")

    @property
    @pulumi.getter(name="streamSpecification")
    def stream_specification(self) -> pulumi.Output[Optional['outputs.TableStreamSpecification']]:
        return pulumi.get(self, "stream_specification")

    @property
    @pulumi.getter(name="tableClass")
    def table_class(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "table_class")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "table_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.TableTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeToLiveSpecification")
    def time_to_live_specification(self) -> pulumi.Output[Optional['outputs.TableTimeToLiveSpecification']]:
        return pulumi.get(self, "time_to_live_specification")

