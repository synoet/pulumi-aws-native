# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._inputs import *

__all__ = ['WorkGroupArgs', 'WorkGroup']

@pulumi.input_type
class WorkGroupArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 recursive_delete_option: Optional[pulumi.Input[bool]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 work_group_configuration: Optional[pulumi.Input['WorkGroupWorkGroupConfigurationArgs']] = None,
                 work_group_configuration_updates: Optional[pulumi.Input['WorkGroupWorkGroupConfigurationUpdatesArgs']] = None):
        """
        The set of arguments for constructing a WorkGroup resource.
        :param pulumi.Input[str] name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-name
        :param pulumi.Input[str] description: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-description
        :param pulumi.Input[bool] recursive_delete_option: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-recursivedeleteoption
        :param pulumi.Input[str] state: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-state
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-tags
        :param pulumi.Input['WorkGroupWorkGroupConfigurationArgs'] work_group_configuration: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfiguration
        :param pulumi.Input['WorkGroupWorkGroupConfigurationUpdatesArgs'] work_group_configuration_updates: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfigurationupdates
        """
        pulumi.set(__self__, "name", name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if recursive_delete_option is not None:
            pulumi.set(__self__, "recursive_delete_option", recursive_delete_option)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if work_group_configuration is not None:
            pulumi.set(__self__, "work_group_configuration", work_group_configuration)
        if work_group_configuration_updates is not None:
            pulumi.set(__self__, "work_group_configuration_updates", work_group_configuration_updates)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="recursiveDeleteOption")
    def recursive_delete_option(self) -> Optional[pulumi.Input[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-recursivedeleteoption
        """
        return pulumi.get(self, "recursive_delete_option")

    @recursive_delete_option.setter
    def recursive_delete_option(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "recursive_delete_option", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-state
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="workGroupConfiguration")
    def work_group_configuration(self) -> Optional[pulumi.Input['WorkGroupWorkGroupConfigurationArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfiguration
        """
        return pulumi.get(self, "work_group_configuration")

    @work_group_configuration.setter
    def work_group_configuration(self, value: Optional[pulumi.Input['WorkGroupWorkGroupConfigurationArgs']]):
        pulumi.set(self, "work_group_configuration", value)

    @property
    @pulumi.getter(name="workGroupConfigurationUpdates")
    def work_group_configuration_updates(self) -> Optional[pulumi.Input['WorkGroupWorkGroupConfigurationUpdatesArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfigurationupdates
        """
        return pulumi.get(self, "work_group_configuration_updates")

    @work_group_configuration_updates.setter
    def work_group_configuration_updates(self, value: Optional[pulumi.Input['WorkGroupWorkGroupConfigurationUpdatesArgs']]):
        pulumi.set(self, "work_group_configuration_updates", value)


class WorkGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recursive_delete_option: Optional[pulumi.Input[bool]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 work_group_configuration: Optional[pulumi.Input[pulumi.InputType['WorkGroupWorkGroupConfigurationArgs']]] = None,
                 work_group_configuration_updates: Optional[pulumi.Input[pulumi.InputType['WorkGroupWorkGroupConfigurationUpdatesArgs']]] = None,
                 __props__=None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-description
        :param pulumi.Input[str] name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-name
        :param pulumi.Input[bool] recursive_delete_option: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-recursivedeleteoption
        :param pulumi.Input[str] state: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-state
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-tags
        :param pulumi.Input[pulumi.InputType['WorkGroupWorkGroupConfigurationArgs']] work_group_configuration: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfiguration
        :param pulumi.Input[pulumi.InputType['WorkGroupWorkGroupConfigurationUpdatesArgs']] work_group_configuration_updates: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfigurationupdates
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html

        :param str resource_name: The name of the resource.
        :param WorkGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recursive_delete_option: Optional[pulumi.Input[bool]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 work_group_configuration: Optional[pulumi.Input[pulumi.InputType['WorkGroupWorkGroupConfigurationArgs']]] = None,
                 work_group_configuration_updates: Optional[pulumi.Input[pulumi.InputType['WorkGroupWorkGroupConfigurationUpdatesArgs']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkGroupArgs.__new__(WorkGroupArgs)

            __props__.__dict__["description"] = description
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["recursive_delete_option"] = recursive_delete_option
            __props__.__dict__["state"] = state
            __props__.__dict__["tags"] = tags
            __props__.__dict__["work_group_configuration"] = work_group_configuration
            __props__.__dict__["work_group_configuration_updates"] = work_group_configuration_updates
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["work_group_configuration_engine_version_effective_engine_version"] = None
            __props__.__dict__["work_group_configuration_updates_engine_version_effective_engine_version"] = None
        super(WorkGroup, __self__).__init__(
            'aws-native:athena:WorkGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkGroup':
        """
        Get an existing WorkGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkGroupArgs.__new__(WorkGroupArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["recursive_delete_option"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["work_group_configuration"] = None
        __props__.__dict__["work_group_configuration_engine_version_effective_engine_version"] = None
        __props__.__dict__["work_group_configuration_updates"] = None
        __props__.__dict__["work_group_configuration_updates_engine_version_effective_engine_version"] = None
        return WorkGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recursiveDeleteOption")
    def recursive_delete_option(self) -> pulumi.Output[Optional[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-recursivedeleteoption
        """
        return pulumi.get(self, "recursive_delete_option")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-state
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="workGroupConfiguration")
    def work_group_configuration(self) -> pulumi.Output[Optional['outputs.WorkGroupWorkGroupConfiguration']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfiguration
        """
        return pulumi.get(self, "work_group_configuration")

    @property
    @pulumi.getter(name="workGroupConfigurationEngineVersionEffectiveEngineVersion")
    def work_group_configuration_engine_version_effective_engine_version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "work_group_configuration_engine_version_effective_engine_version")

    @property
    @pulumi.getter(name="workGroupConfigurationUpdates")
    def work_group_configuration_updates(self) -> pulumi.Output[Optional['outputs.WorkGroupWorkGroupConfigurationUpdates']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfigurationupdates
        """
        return pulumi.get(self, "work_group_configuration_updates")

    @property
    @pulumi.getter(name="workGroupConfigurationUpdatesEngineVersionEffectiveEngineVersion")
    def work_group_configuration_updates_engine_version_effective_engine_version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "work_group_configuration_updates_engine_version_effective_engine_version")

