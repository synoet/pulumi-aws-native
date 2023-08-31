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

__all__ = ['ConfigurationProfileArgs', 'ConfigurationProfile']

@pulumi.input_type
class ConfigurationProfileArgs:
    def __init__(__self__, *,
                 application_id: pulumi.Input[str],
                 location_uri: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 retrieval_role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationProfileTagsArgs']]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 validators: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationProfileValidatorsArgs']]]] = None):
        """
        The set of arguments for constructing a ConfigurationProfile resource.
        """
        pulumi.set(__self__, "application_id", application_id)
        pulumi.set(__self__, "location_uri", location_uri)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if retrieval_role_arn is not None:
            pulumi.set(__self__, "retrieval_role_arn", retrieval_role_arn)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if validators is not None:
            pulumi.set(__self__, "validators", validators)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> pulumi.Input[str]:
        return pulumi.get(self, "location_uri")

    @location_uri.setter
    def location_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "location_uri", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="retrievalRoleArn")
    def retrieval_role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "retrieval_role_arn")

    @retrieval_role_arn.setter
    def retrieval_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "retrieval_role_arn", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationProfileTagsArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationProfileTagsArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def validators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationProfileValidatorsArgs']]]]:
        return pulumi.get(self, "validators")

    @validators.setter
    def validators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationProfileValidatorsArgs']]]]):
        pulumi.set(self, "validators", value)


warnings.warn("""ConfigurationProfile is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ConfigurationProfile(pulumi.CustomResource):
    warnings.warn("""ConfigurationProfile is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location_uri: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 retrieval_role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigurationProfileTagsArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 validators: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigurationProfileValidatorsArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::AppConfig::ConfigurationProfile

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigurationProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::AppConfig::ConfigurationProfile

        :param str resource_name: The name of the resource.
        :param ConfigurationProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigurationProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location_uri: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 retrieval_role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigurationProfileTagsArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 validators: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigurationProfileValidatorsArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""ConfigurationProfile is deprecated: ConfigurationProfile is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigurationProfileArgs.__new__(ConfigurationProfileArgs)

            if application_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_id'")
            __props__.__dict__["application_id"] = application_id
            __props__.__dict__["description"] = description
            if location_uri is None and not opts.urn:
                raise TypeError("Missing required property 'location_uri'")
            __props__.__dict__["location_uri"] = location_uri
            __props__.__dict__["name"] = name
            __props__.__dict__["retrieval_role_arn"] = retrieval_role_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["type"] = type
            __props__.__dict__["validators"] = validators
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["application_id", "location_uri", "type"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ConfigurationProfile, __self__).__init__(
            'aws-native:appconfig:ConfigurationProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConfigurationProfile':
        """
        Get an existing ConfigurationProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConfigurationProfileArgs.__new__(ConfigurationProfileArgs)

        __props__.__dict__["application_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["location_uri"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["retrieval_role_arn"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["validators"] = None
        return ConfigurationProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location_uri")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="retrievalRoleArn")
    def retrieval_role_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "retrieval_role_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ConfigurationProfileTags']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def validators(self) -> pulumi.Output[Optional[Sequence['outputs.ConfigurationProfileValidators']]]:
        return pulumi.get(self, "validators")

