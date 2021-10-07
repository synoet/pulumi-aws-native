# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ExperimentTemplateArgs', 'ExperimentTemplate']

@pulumi.input_type
class ExperimentTemplateArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 role_arn: pulumi.Input[str],
                 stop_conditions: pulumi.Input[Sequence[pulumi.Input['ExperimentTemplateStopConditionArgs']]],
                 tags: Any,
                 targets: pulumi.Input['ExperimentTemplateTargetMapArgs'],
                 actions: Optional[pulumi.Input['ExperimentTemplateActionMapArgs']] = None):
        """
        The set of arguments for constructing a ExperimentTemplate resource.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "role_arn", role_arn)
        pulumi.set(__self__, "stop_conditions", stop_conditions)
        pulumi.set(__self__, "tags", tags)
        pulumi.set(__self__, "targets", targets)
        if actions is not None:
            pulumi.set(__self__, "actions", actions)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="stopConditions")
    def stop_conditions(self) -> pulumi.Input[Sequence[pulumi.Input['ExperimentTemplateStopConditionArgs']]]:
        return pulumi.get(self, "stop_conditions")

    @stop_conditions.setter
    def stop_conditions(self, value: pulumi.Input[Sequence[pulumi.Input['ExperimentTemplateStopConditionArgs']]]):
        pulumi.set(self, "stop_conditions", value)

    @property
    @pulumi.getter
    def tags(self) -> Any:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Any):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def targets(self) -> pulumi.Input['ExperimentTemplateTargetMapArgs']:
        return pulumi.get(self, "targets")

    @targets.setter
    def targets(self, value: pulumi.Input['ExperimentTemplateTargetMapArgs']):
        pulumi.set(self, "targets", value)

    @property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input['ExperimentTemplateActionMapArgs']]:
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: Optional[pulumi.Input['ExperimentTemplateActionMapArgs']]):
        pulumi.set(self, "actions", value)


class ExperimentTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[pulumi.InputType['ExperimentTemplateActionMapArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 stop_conditions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExperimentTemplateStopConditionArgs']]]]] = None,
                 tags: Optional[Any] = None,
                 targets: Optional[pulumi.Input[pulumi.InputType['ExperimentTemplateTargetMapArgs']]] = None,
                 __props__=None):
        """
        Resource schema for AWS::FIS::ExperimentTemplate

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExperimentTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::FIS::ExperimentTemplate

        :param str resource_name: The name of the resource.
        :param ExperimentTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExperimentTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[pulumi.InputType['ExperimentTemplateActionMapArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 stop_conditions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExperimentTemplateStopConditionArgs']]]]] = None,
                 tags: Optional[Any] = None,
                 targets: Optional[pulumi.Input[pulumi.InputType['ExperimentTemplateTargetMapArgs']]] = None,
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
            __props__ = ExperimentTemplateArgs.__new__(ExperimentTemplateArgs)

            __props__.__dict__["actions"] = actions
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            if stop_conditions is None and not opts.urn:
                raise TypeError("Missing required property 'stop_conditions'")
            __props__.__dict__["stop_conditions"] = stop_conditions
            if tags is None and not opts.urn:
                raise TypeError("Missing required property 'tags'")
            __props__.__dict__["tags"] = tags
            if targets is None and not opts.urn:
                raise TypeError("Missing required property 'targets'")
            __props__.__dict__["targets"] = targets
        super(ExperimentTemplate, __self__).__init__(
            'aws-native:fis:ExperimentTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ExperimentTemplate':
        """
        Get an existing ExperimentTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExperimentTemplateArgs.__new__(ExperimentTemplateArgs)

        __props__.__dict__["actions"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["stop_conditions"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["targets"] = None
        return ExperimentTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Optional['outputs.ExperimentTemplateActionMap']]:
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="stopConditions")
    def stop_conditions(self) -> pulumi.Output[Sequence['outputs.ExperimentTemplateStopCondition']]:
        return pulumi.get(self, "stop_conditions")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Any]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def targets(self) -> pulumi.Output['outputs.ExperimentTemplateTargetMap']:
        return pulumi.get(self, "targets")

