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

__all__ = ['ExtensionArgs', 'Extension']

@pulumi.input_type
class ExtensionArgs:
    def __init__(__self__, *,
                 actions: Any,
                 description: Optional[pulumi.Input[str]] = None,
                 latest_version_number: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ExtensionTagArgs']]]] = None):
        """
        The set of arguments for constructing a Extension resource.
        :param pulumi.Input[str] description: Description of the extension.
        :param pulumi.Input[str] name: Name of the extension.
        :param pulumi.Input[Sequence[pulumi.Input['ExtensionTagArgs']]] tags: An array of key-value tags to apply to this resource.
        """
        pulumi.set(__self__, "actions", actions)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if latest_version_number is not None:
            pulumi.set(__self__, "latest_version_number", latest_version_number)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def actions(self) -> Any:
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: Any):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the extension.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="latestVersionNumber")
    def latest_version_number(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "latest_version_number")

    @latest_version_number.setter
    def latest_version_number(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "latest_version_number", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the extension.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Any]:
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[Any]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ExtensionTagArgs']]]]:
        """
        An array of key-value tags to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ExtensionTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Extension(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[Any] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 latest_version_number: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExtensionTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::AppConfig::Extension

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the extension.
        :param pulumi.Input[str] name: Name of the extension.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExtensionTagArgs']]]] tags: An array of key-value tags to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExtensionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::AppConfig::Extension

        :param str resource_name: The name of the resource.
        :param ExtensionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExtensionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[Any] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 latest_version_number: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExtensionTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExtensionArgs.__new__(ExtensionArgs)

            if actions is None and not opts.urn:
                raise TypeError("Missing required property 'actions'")
            __props__.__dict__["actions"] = actions
            __props__.__dict__["description"] = description
            __props__.__dict__["latest_version_number"] = latest_version_number
            __props__.__dict__["name"] = name
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["version_number"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name", "tags[*]"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Extension, __self__).__init__(
            'aws-native:appconfig:Extension',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Extension':
        """
        Get an existing Extension resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExtensionArgs.__new__(ExtensionArgs)

        __props__.__dict__["actions"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["latest_version_number"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["version_number"] = None
        return Extension(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Any]:
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the extension.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="latestVersionNumber")
    def latest_version_number(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "latest_version_number")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the extension.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ExtensionTag']]]:
        """
        An array of key-value tags to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="versionNumber")
    def version_number(self) -> pulumi.Output[int]:
        return pulumi.get(self, "version_number")

