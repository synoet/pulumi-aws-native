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

__all__ = ['SchemaMappingArgs', 'SchemaMapping']

@pulumi.input_type
class SchemaMappingArgs:
    def __init__(__self__, *,
                 mapped_input_fields: pulumi.Input[Sequence[pulumi.Input['SchemaMappingSchemaInputAttributeArgs']]],
                 schema_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['SchemaMappingTagArgs']]]] = None):
        """
        The set of arguments for constructing a SchemaMapping resource.
        :param pulumi.Input[Sequence[pulumi.Input['SchemaMappingSchemaInputAttributeArgs']]] mapped_input_fields: The SchemaMapping attributes input
        :param pulumi.Input[str] schema_name: The name of the SchemaMapping
        :param pulumi.Input[str] description: The description of the SchemaMapping
        """
        pulumi.set(__self__, "mapped_input_fields", mapped_input_fields)
        pulumi.set(__self__, "schema_name", schema_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="mappedInputFields")
    def mapped_input_fields(self) -> pulumi.Input[Sequence[pulumi.Input['SchemaMappingSchemaInputAttributeArgs']]]:
        """
        The SchemaMapping attributes input
        """
        return pulumi.get(self, "mapped_input_fields")

    @mapped_input_fields.setter
    def mapped_input_fields(self, value: pulumi.Input[Sequence[pulumi.Input['SchemaMappingSchemaInputAttributeArgs']]]):
        pulumi.set(self, "mapped_input_fields", value)

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> pulumi.Input[str]:
        """
        The name of the SchemaMapping
        """
        return pulumi.get(self, "schema_name")

    @schema_name.setter
    def schema_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "schema_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the SchemaMapping
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SchemaMappingTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SchemaMappingTagArgs']]]]):
        pulumi.set(self, "tags", value)


class SchemaMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 mapped_input_fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SchemaMappingSchemaInputAttributeArgs']]]]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SchemaMappingTagArgs']]]]] = None,
                 __props__=None):
        """
        SchemaMapping defined in AWS Entity Resolution service

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the SchemaMapping
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SchemaMappingSchemaInputAttributeArgs']]]] mapped_input_fields: The SchemaMapping attributes input
        :param pulumi.Input[str] schema_name: The name of the SchemaMapping
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SchemaMappingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        SchemaMapping defined in AWS Entity Resolution service

        :param str resource_name: The name of the resource.
        :param SchemaMappingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SchemaMappingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 mapped_input_fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SchemaMappingSchemaInputAttributeArgs']]]]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SchemaMappingTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SchemaMappingArgs.__new__(SchemaMappingArgs)

            __props__.__dict__["description"] = description
            if mapped_input_fields is None and not opts.urn:
                raise TypeError("Missing required property 'mapped_input_fields'")
            __props__.__dict__["mapped_input_fields"] = mapped_input_fields
            if schema_name is None and not opts.urn:
                raise TypeError("Missing required property 'schema_name'")
            __props__.__dict__["schema_name"] = schema_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["created_at"] = None
            __props__.__dict__["schema_arn"] = None
            __props__.__dict__["updated_at"] = None
        super(SchemaMapping, __self__).__init__(
            'aws-native:entityresolution:SchemaMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SchemaMapping':
        """
        Get an existing SchemaMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SchemaMappingArgs.__new__(SchemaMappingArgs)

        __props__.__dict__["created_at"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["mapped_input_fields"] = None
        __props__.__dict__["schema_arn"] = None
        __props__.__dict__["schema_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["updated_at"] = None
        return SchemaMapping(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the SchemaMapping
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="mappedInputFields")
    def mapped_input_fields(self) -> pulumi.Output[Sequence['outputs.SchemaMappingSchemaInputAttribute']]:
        """
        The SchemaMapping attributes input
        """
        return pulumi.get(self, "mapped_input_fields")

    @property
    @pulumi.getter(name="schemaArn")
    def schema_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "schema_arn")

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> pulumi.Output[str]:
        """
        The name of the SchemaMapping
        """
        return pulumi.get(self, "schema_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.SchemaMappingTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "updated_at")

