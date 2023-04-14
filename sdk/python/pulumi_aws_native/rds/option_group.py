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

__all__ = ['OptionGroupArgs', 'OptionGroup']

@pulumi.input_type
class OptionGroupArgs:
    def __init__(__self__, *,
                 engine_name: pulumi.Input[str],
                 major_engine_version: pulumi.Input[str],
                 option_group_description: pulumi.Input[str],
                 option_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['OptionGroupOptionConfigurationArgs']]]] = None,
                 option_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['OptionGroupTagArgs']]]] = None):
        """
        The set of arguments for constructing a OptionGroup resource.
        :param pulumi.Input[str] engine_name: Indicates the name of the engine that this option group can be applied to.
        :param pulumi.Input[str] major_engine_version: Indicates the major engine version associated with this option group.
        :param pulumi.Input[str] option_group_description: Provides a description of the option group.
        :param pulumi.Input[Sequence[pulumi.Input['OptionGroupOptionConfigurationArgs']]] option_configurations: Indicates what options are available in the option group.
        :param pulumi.Input[str] option_group_name: Specifies the name of the option group.
        :param pulumi.Input[Sequence[pulumi.Input['OptionGroupTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "engine_name", engine_name)
        pulumi.set(__self__, "major_engine_version", major_engine_version)
        pulumi.set(__self__, "option_group_description", option_group_description)
        if option_configurations is not None:
            pulumi.set(__self__, "option_configurations", option_configurations)
        if option_group_name is not None:
            pulumi.set(__self__, "option_group_name", option_group_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="engineName")
    def engine_name(self) -> pulumi.Input[str]:
        """
        Indicates the name of the engine that this option group can be applied to.
        """
        return pulumi.get(self, "engine_name")

    @engine_name.setter
    def engine_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "engine_name", value)

    @property
    @pulumi.getter(name="majorEngineVersion")
    def major_engine_version(self) -> pulumi.Input[str]:
        """
        Indicates the major engine version associated with this option group.
        """
        return pulumi.get(self, "major_engine_version")

    @major_engine_version.setter
    def major_engine_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "major_engine_version", value)

    @property
    @pulumi.getter(name="optionGroupDescription")
    def option_group_description(self) -> pulumi.Input[str]:
        """
        Provides a description of the option group.
        """
        return pulumi.get(self, "option_group_description")

    @option_group_description.setter
    def option_group_description(self, value: pulumi.Input[str]):
        pulumi.set(self, "option_group_description", value)

    @property
    @pulumi.getter(name="optionConfigurations")
    def option_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OptionGroupOptionConfigurationArgs']]]]:
        """
        Indicates what options are available in the option group.
        """
        return pulumi.get(self, "option_configurations")

    @option_configurations.setter
    def option_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OptionGroupOptionConfigurationArgs']]]]):
        pulumi.set(self, "option_configurations", value)

    @property
    @pulumi.getter(name="optionGroupName")
    def option_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the option group.
        """
        return pulumi.get(self, "option_group_name")

    @option_group_name.setter
    def option_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "option_group_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OptionGroupTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OptionGroupTagArgs']]]]):
        pulumi.set(self, "tags", value)


class OptionGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 engine_name: Optional[pulumi.Input[str]] = None,
                 major_engine_version: Optional[pulumi.Input[str]] = None,
                 option_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OptionGroupOptionConfigurationArgs']]]]] = None,
                 option_group_description: Optional[pulumi.Input[str]] = None,
                 option_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OptionGroupTagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::RDS::OptionGroup resource creates an option group, to enable and configure features that are specific to a particular DB engine.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] engine_name: Indicates the name of the engine that this option group can be applied to.
        :param pulumi.Input[str] major_engine_version: Indicates the major engine version associated with this option group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OptionGroupOptionConfigurationArgs']]]] option_configurations: Indicates what options are available in the option group.
        :param pulumi.Input[str] option_group_description: Provides a description of the option group.
        :param pulumi.Input[str] option_group_name: Specifies the name of the option group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OptionGroupTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OptionGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::RDS::OptionGroup resource creates an option group, to enable and configure features that are specific to a particular DB engine.

        :param str resource_name: The name of the resource.
        :param OptionGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OptionGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 engine_name: Optional[pulumi.Input[str]] = None,
                 major_engine_version: Optional[pulumi.Input[str]] = None,
                 option_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OptionGroupOptionConfigurationArgs']]]]] = None,
                 option_group_description: Optional[pulumi.Input[str]] = None,
                 option_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OptionGroupTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OptionGroupArgs.__new__(OptionGroupArgs)

            if engine_name is None and not opts.urn:
                raise TypeError("Missing required property 'engine_name'")
            __props__.__dict__["engine_name"] = engine_name
            if major_engine_version is None and not opts.urn:
                raise TypeError("Missing required property 'major_engine_version'")
            __props__.__dict__["major_engine_version"] = major_engine_version
            __props__.__dict__["option_configurations"] = option_configurations
            if option_group_description is None and not opts.urn:
                raise TypeError("Missing required property 'option_group_description'")
            __props__.__dict__["option_group_description"] = option_group_description
            __props__.__dict__["option_group_name"] = option_group_name
            __props__.__dict__["tags"] = tags
        super(OptionGroup, __self__).__init__(
            'aws-native:rds:OptionGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OptionGroup':
        """
        Get an existing OptionGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OptionGroupArgs.__new__(OptionGroupArgs)

        __props__.__dict__["engine_name"] = None
        __props__.__dict__["major_engine_version"] = None
        __props__.__dict__["option_configurations"] = None
        __props__.__dict__["option_group_description"] = None
        __props__.__dict__["option_group_name"] = None
        __props__.__dict__["tags"] = None
        return OptionGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="engineName")
    def engine_name(self) -> pulumi.Output[str]:
        """
        Indicates the name of the engine that this option group can be applied to.
        """
        return pulumi.get(self, "engine_name")

    @property
    @pulumi.getter(name="majorEngineVersion")
    def major_engine_version(self) -> pulumi.Output[str]:
        """
        Indicates the major engine version associated with this option group.
        """
        return pulumi.get(self, "major_engine_version")

    @property
    @pulumi.getter(name="optionConfigurations")
    def option_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.OptionGroupOptionConfiguration']]]:
        """
        Indicates what options are available in the option group.
        """
        return pulumi.get(self, "option_configurations")

    @property
    @pulumi.getter(name="optionGroupDescription")
    def option_group_description(self) -> pulumi.Output[str]:
        """
        Provides a description of the option group.
        """
        return pulumi.get(self, "option_group_description")

    @property
    @pulumi.getter(name="optionGroupName")
    def option_group_name(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the name of the option group.
        """
        return pulumi.get(self, "option_group_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.OptionGroupTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

