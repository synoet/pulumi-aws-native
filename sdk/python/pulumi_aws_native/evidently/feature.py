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

__all__ = ['FeatureArgs', 'Feature']

@pulumi.input_type
class FeatureArgs:
    def __init__(__self__, *,
                 project: pulumi.Input[str],
                 variations: pulumi.Input[Sequence[pulumi.Input['FeatureVariationObjectArgs']]],
                 default_variation: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 entity_overrides: Optional[pulumi.Input[Sequence[pulumi.Input['FeatureEntityOverrideArgs']]]] = None,
                 evaluation_strategy: Optional[pulumi.Input['FeatureEvaluationStrategy']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['FeatureTagArgs']]]] = None):
        """
        The set of arguments for constructing a Feature resource.
        :param pulumi.Input[Sequence[pulumi.Input['FeatureTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "project", project)
        pulumi.set(__self__, "variations", variations)
        if default_variation is not None:
            pulumi.set(__self__, "default_variation", default_variation)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if entity_overrides is not None:
            pulumi.set(__self__, "entity_overrides", entity_overrides)
        if evaluation_strategy is not None:
            pulumi.set(__self__, "evaluation_strategy", evaluation_strategy)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def variations(self) -> pulumi.Input[Sequence[pulumi.Input['FeatureVariationObjectArgs']]]:
        return pulumi.get(self, "variations")

    @variations.setter
    def variations(self, value: pulumi.Input[Sequence[pulumi.Input['FeatureVariationObjectArgs']]]):
        pulumi.set(self, "variations", value)

    @property
    @pulumi.getter(name="defaultVariation")
    def default_variation(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_variation")

    @default_variation.setter
    def default_variation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_variation", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="entityOverrides")
    def entity_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FeatureEntityOverrideArgs']]]]:
        return pulumi.get(self, "entity_overrides")

    @entity_overrides.setter
    def entity_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FeatureEntityOverrideArgs']]]]):
        pulumi.set(self, "entity_overrides", value)

    @property
    @pulumi.getter(name="evaluationStrategy")
    def evaluation_strategy(self) -> Optional[pulumi.Input['FeatureEvaluationStrategy']]:
        return pulumi.get(self, "evaluation_strategy")

    @evaluation_strategy.setter
    def evaluation_strategy(self, value: Optional[pulumi.Input['FeatureEvaluationStrategy']]):
        pulumi.set(self, "evaluation_strategy", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FeatureTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FeatureTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Feature(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_variation: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 entity_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FeatureEntityOverrideArgs']]]]] = None,
                 evaluation_strategy: Optional[pulumi.Input['FeatureEvaluationStrategy']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FeatureTagArgs']]]]] = None,
                 variations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FeatureVariationObjectArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Evidently::Feature.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FeatureTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FeatureArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Evidently::Feature.

        :param str resource_name: The name of the resource.
        :param FeatureArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FeatureArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_variation: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 entity_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FeatureEntityOverrideArgs']]]]] = None,
                 evaluation_strategy: Optional[pulumi.Input['FeatureEvaluationStrategy']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FeatureTagArgs']]]]] = None,
                 variations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FeatureVariationObjectArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FeatureArgs.__new__(FeatureArgs)

            __props__.__dict__["default_variation"] = default_variation
            __props__.__dict__["description"] = description
            __props__.__dict__["entity_overrides"] = entity_overrides
            __props__.__dict__["evaluation_strategy"] = evaluation_strategy
            __props__.__dict__["name"] = name
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            __props__.__dict__["tags"] = tags
            if variations is None and not opts.urn:
                raise TypeError("Missing required property 'variations'")
            __props__.__dict__["variations"] = variations
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Feature, __self__).__init__(
            'aws-native:evidently:Feature',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Feature':
        """
        Get an existing Feature resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FeatureArgs.__new__(FeatureArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["default_variation"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["entity_overrides"] = None
        __props__.__dict__["evaluation_strategy"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["variations"] = None
        return Feature(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="defaultVariation")
    def default_variation(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "default_variation")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="entityOverrides")
    def entity_overrides(self) -> pulumi.Output[Optional[Sequence['outputs.FeatureEntityOverride']]]:
        return pulumi.get(self, "entity_overrides")

    @property
    @pulumi.getter(name="evaluationStrategy")
    def evaluation_strategy(self) -> pulumi.Output[Optional['FeatureEvaluationStrategy']]:
        return pulumi.get(self, "evaluation_strategy")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.FeatureTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def variations(self) -> pulumi.Output[Sequence['outputs.FeatureVariationObject']]:
        return pulumi.get(self, "variations")

