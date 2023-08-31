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

__all__ = ['DataIntegrationArgs', 'DataIntegration']

@pulumi.input_type
class DataIntegrationArgs:
    def __init__(__self__, *,
                 kms_key: pulumi.Input[str],
                 schedule_config: pulumi.Input['DataIntegrationScheduleConfigArgs'],
                 source_uri: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 file_configuration: Optional[pulumi.Input['DataIntegrationFileConfigurationArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 object_configuration: Optional[pulumi.Input['DataIntegrationObjectConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DataIntegrationTagArgs']]]] = None):
        """
        The set of arguments for constructing a DataIntegration resource.
        :param pulumi.Input[str] kms_key: The KMS key of the data integration.
        :param pulumi.Input['DataIntegrationScheduleConfigArgs'] schedule_config: The name of the data and how often it should be pulled from the source.
        :param pulumi.Input[str] source_uri: The URI of the data source.
        :param pulumi.Input[str] description: The data integration description.
        :param pulumi.Input['DataIntegrationFileConfigurationArgs'] file_configuration: The configuration for what files should be pulled from the source.
        :param pulumi.Input[str] name: The name of the data integration.
        :param pulumi.Input['DataIntegrationObjectConfigurationArgs'] object_configuration: The configuration for what data should be pulled from the source.
        :param pulumi.Input[Sequence[pulumi.Input['DataIntegrationTagArgs']]] tags: The tags (keys and values) associated with the data integration.
        """
        pulumi.set(__self__, "kms_key", kms_key)
        pulumi.set(__self__, "schedule_config", schedule_config)
        pulumi.set(__self__, "source_uri", source_uri)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if file_configuration is not None:
            pulumi.set(__self__, "file_configuration", file_configuration)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if object_configuration is not None:
            pulumi.set(__self__, "object_configuration", object_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Input[str]:
        """
        The KMS key of the data integration.
        """
        return pulumi.get(self, "kms_key")

    @kms_key.setter
    def kms_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "kms_key", value)

    @property
    @pulumi.getter(name="scheduleConfig")
    def schedule_config(self) -> pulumi.Input['DataIntegrationScheduleConfigArgs']:
        """
        The name of the data and how often it should be pulled from the source.
        """
        return pulumi.get(self, "schedule_config")

    @schedule_config.setter
    def schedule_config(self, value: pulumi.Input['DataIntegrationScheduleConfigArgs']):
        pulumi.set(self, "schedule_config", value)

    @property
    @pulumi.getter(name="sourceUri")
    def source_uri(self) -> pulumi.Input[str]:
        """
        The URI of the data source.
        """
        return pulumi.get(self, "source_uri")

    @source_uri.setter
    def source_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_uri", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The data integration description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="fileConfiguration")
    def file_configuration(self) -> Optional[pulumi.Input['DataIntegrationFileConfigurationArgs']]:
        """
        The configuration for what files should be pulled from the source.
        """
        return pulumi.get(self, "file_configuration")

    @file_configuration.setter
    def file_configuration(self, value: Optional[pulumi.Input['DataIntegrationFileConfigurationArgs']]):
        pulumi.set(self, "file_configuration", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the data integration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="objectConfiguration")
    def object_configuration(self) -> Optional[pulumi.Input['DataIntegrationObjectConfigurationArgs']]:
        """
        The configuration for what data should be pulled from the source.
        """
        return pulumi.get(self, "object_configuration")

    @object_configuration.setter
    def object_configuration(self, value: Optional[pulumi.Input['DataIntegrationObjectConfigurationArgs']]):
        pulumi.set(self, "object_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataIntegrationTagArgs']]]]:
        """
        The tags (keys and values) associated with the data integration.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataIntegrationTagArgs']]]]):
        pulumi.set(self, "tags", value)


class DataIntegration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 file_configuration: Optional[pulumi.Input[pulumi.InputType['DataIntegrationFileConfigurationArgs']]] = None,
                 kms_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 object_configuration: Optional[pulumi.Input[pulumi.InputType['DataIntegrationObjectConfigurationArgs']]] = None,
                 schedule_config: Optional[pulumi.Input[pulumi.InputType['DataIntegrationScheduleConfigArgs']]] = None,
                 source_uri: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataIntegrationTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::AppIntegrations::DataIntegration

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The data integration description.
        :param pulumi.Input[pulumi.InputType['DataIntegrationFileConfigurationArgs']] file_configuration: The configuration for what files should be pulled from the source.
        :param pulumi.Input[str] kms_key: The KMS key of the data integration.
        :param pulumi.Input[str] name: The name of the data integration.
        :param pulumi.Input[pulumi.InputType['DataIntegrationObjectConfigurationArgs']] object_configuration: The configuration for what data should be pulled from the source.
        :param pulumi.Input[pulumi.InputType['DataIntegrationScheduleConfigArgs']] schedule_config: The name of the data and how often it should be pulled from the source.
        :param pulumi.Input[str] source_uri: The URI of the data source.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataIntegrationTagArgs']]]] tags: The tags (keys and values) associated with the data integration.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataIntegrationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::AppIntegrations::DataIntegration

        :param str resource_name: The name of the resource.
        :param DataIntegrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataIntegrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 file_configuration: Optional[pulumi.Input[pulumi.InputType['DataIntegrationFileConfigurationArgs']]] = None,
                 kms_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 object_configuration: Optional[pulumi.Input[pulumi.InputType['DataIntegrationObjectConfigurationArgs']]] = None,
                 schedule_config: Optional[pulumi.Input[pulumi.InputType['DataIntegrationScheduleConfigArgs']]] = None,
                 source_uri: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataIntegrationTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataIntegrationArgs.__new__(DataIntegrationArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["file_configuration"] = file_configuration
            if kms_key is None and not opts.urn:
                raise TypeError("Missing required property 'kms_key'")
            __props__.__dict__["kms_key"] = kms_key
            __props__.__dict__["name"] = name
            __props__.__dict__["object_configuration"] = object_configuration
            if schedule_config is None and not opts.urn:
                raise TypeError("Missing required property 'schedule_config'")
            __props__.__dict__["schedule_config"] = schedule_config
            if source_uri is None and not opts.urn:
                raise TypeError("Missing required property 'source_uri'")
            __props__.__dict__["source_uri"] = source_uri
            __props__.__dict__["tags"] = tags
            __props__.__dict__["data_integration_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["kms_key", "schedule_config", "source_uri"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DataIntegration, __self__).__init__(
            'aws-native:appintegrations:DataIntegration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DataIntegration':
        """
        Get an existing DataIntegration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DataIntegrationArgs.__new__(DataIntegrationArgs)

        __props__.__dict__["data_integration_arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["file_configuration"] = None
        __props__.__dict__["kms_key"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["object_configuration"] = None
        __props__.__dict__["schedule_config"] = None
        __props__.__dict__["source_uri"] = None
        __props__.__dict__["tags"] = None
        return DataIntegration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataIntegrationArn")
    def data_integration_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the data integration.
        """
        return pulumi.get(self, "data_integration_arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The data integration description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="fileConfiguration")
    def file_configuration(self) -> pulumi.Output[Optional['outputs.DataIntegrationFileConfiguration']]:
        """
        The configuration for what files should be pulled from the source.
        """
        return pulumi.get(self, "file_configuration")

    @property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Output[str]:
        """
        The KMS key of the data integration.
        """
        return pulumi.get(self, "kms_key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the data integration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="objectConfiguration")
    def object_configuration(self) -> pulumi.Output[Optional['outputs.DataIntegrationObjectConfiguration']]:
        """
        The configuration for what data should be pulled from the source.
        """
        return pulumi.get(self, "object_configuration")

    @property
    @pulumi.getter(name="scheduleConfig")
    def schedule_config(self) -> pulumi.Output['outputs.DataIntegrationScheduleConfig']:
        """
        The name of the data and how often it should be pulled from the source.
        """
        return pulumi.get(self, "schedule_config")

    @property
    @pulumi.getter(name="sourceUri")
    def source_uri(self) -> pulumi.Output[str]:
        """
        The URI of the data source.
        """
        return pulumi.get(self, "source_uri")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DataIntegrationTag']]]:
        """
        The tags (keys and values) associated with the data integration.
        """
        return pulumi.get(self, "tags")

