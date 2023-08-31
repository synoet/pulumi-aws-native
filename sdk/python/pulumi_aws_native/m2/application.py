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

__all__ = ['ApplicationArgs', 'Application']

@pulumi.input_type
class ApplicationArgs:
    def __init__(__self__, *,
                 definition: pulumi.Input[Union['ApplicationDefinition0PropertiesArgs', 'ApplicationDefinition1PropertiesArgs']],
                 engine_type: pulumi.Input['ApplicationEngineType'],
                 description: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input['ApplicationTagMapArgs']] = None):
        """
        The set of arguments for constructing a Application resource.
        :param pulumi.Input[str] kms_key_id: The ID or the Amazon Resource Name (ARN) of the customer managed KMS Key used for encrypting application-related resources.
        """
        pulumi.set(__self__, "definition", definition)
        pulumi.set(__self__, "engine_type", engine_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Input[Union['ApplicationDefinition0PropertiesArgs', 'ApplicationDefinition1PropertiesArgs']]:
        return pulumi.get(self, "definition")

    @definition.setter
    def definition(self, value: pulumi.Input[Union['ApplicationDefinition0PropertiesArgs', 'ApplicationDefinition1PropertiesArgs']]):
        pulumi.set(self, "definition", value)

    @property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> pulumi.Input['ApplicationEngineType']:
        return pulumi.get(self, "engine_type")

    @engine_type.setter
    def engine_type(self, value: pulumi.Input['ApplicationEngineType']):
        pulumi.set(self, "engine_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID or the Amazon Resource Name (ARN) of the customer managed KMS Key used for encrypting application-related resources.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input['ApplicationTagMapArgs']]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input['ApplicationTagMapArgs']]):
        pulumi.set(self, "tags", value)


class Application(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 definition: Optional[pulumi.Input[Union[pulumi.InputType['ApplicationDefinition0PropertiesArgs'], pulumi.InputType['ApplicationDefinition1PropertiesArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 engine_type: Optional[pulumi.Input['ApplicationEngineType']] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['ApplicationTagMapArgs']]] = None,
                 __props__=None):
        """
        Represents an application that runs on an AWS Mainframe Modernization Environment

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] kms_key_id: The ID or the Amazon Resource Name (ARN) of the customer managed KMS Key used for encrypting application-related resources.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents an application that runs on an AWS Mainframe Modernization Environment

        :param str resource_name: The name of the resource.
        :param ApplicationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 definition: Optional[pulumi.Input[Union[pulumi.InputType['ApplicationDefinition0PropertiesArgs'], pulumi.InputType['ApplicationDefinition1PropertiesArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 engine_type: Optional[pulumi.Input['ApplicationEngineType']] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['ApplicationTagMapArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationArgs.__new__(ApplicationArgs)

            if definition is None and not opts.urn:
                raise TypeError("Missing required property 'definition'")
            __props__.__dict__["definition"] = definition
            __props__.__dict__["description"] = description
            if engine_type is None and not opts.urn:
                raise TypeError("Missing required property 'engine_type'")
            __props__.__dict__["engine_type"] = engine_type
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["name"] = name
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["application_arn"] = None
            __props__.__dict__["application_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["engine_type", "kms_key_id", "name", "role_arn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Application, __self__).__init__(
            'aws-native:m2:Application',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Application':
        """
        Get an existing Application resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApplicationArgs.__new__(ApplicationArgs)

        __props__.__dict__["application_arn"] = None
        __props__.__dict__["application_id"] = None
        __props__.__dict__["definition"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["engine_type"] = None
        __props__.__dict__["kms_key_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["tags"] = None
        return Application(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_arn")

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Output[Any]:
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> pulumi.Output['ApplicationEngineType']:
        return pulumi.get(self, "engine_type")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID or the Amazon Resource Name (ARN) of the customer managed KMS Key used for encrypting application-related resources.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional['outputs.ApplicationTagMap']]:
        return pulumi.get(self, "tags")

