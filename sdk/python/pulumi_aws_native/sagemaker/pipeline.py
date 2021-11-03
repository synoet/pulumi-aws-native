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

__all__ = ['PipelineArgs', 'Pipeline']

@pulumi.input_type
class PipelineArgs:
    def __init__(__self__, *,
                 pipeline_definition: Any,
                 role_arn: pulumi.Input[str],
                 pipeline_description: Optional[pulumi.Input[str]] = None,
                 pipeline_display_name: Optional[pulumi.Input[str]] = None,
                 pipeline_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineTagArgs']]]] = None):
        """
        The set of arguments for constructing a Pipeline resource.
        :param pulumi.Input[str] role_arn: Role Arn
        :param pulumi.Input[str] pipeline_description: The description of the Pipeline.
        :param pulumi.Input[str] pipeline_display_name: The display name of the Pipeline.
        :param pulumi.Input[str] pipeline_name: The name of the Pipeline.
        """
        pulumi.set(__self__, "pipeline_definition", pipeline_definition)
        pulumi.set(__self__, "role_arn", role_arn)
        if pipeline_description is not None:
            pulumi.set(__self__, "pipeline_description", pipeline_description)
        if pipeline_display_name is not None:
            pulumi.set(__self__, "pipeline_display_name", pipeline_display_name)
        if pipeline_name is not None:
            pulumi.set(__self__, "pipeline_name", pipeline_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="pipelineDefinition")
    def pipeline_definition(self) -> Any:
        return pulumi.get(self, "pipeline_definition")

    @pipeline_definition.setter
    def pipeline_definition(self, value: Any):
        pulumi.set(self, "pipeline_definition", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        Role Arn
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="pipelineDescription")
    def pipeline_description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Pipeline.
        """
        return pulumi.get(self, "pipeline_description")

    @pipeline_description.setter
    def pipeline_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pipeline_description", value)

    @property
    @pulumi.getter(name="pipelineDisplayName")
    def pipeline_display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the Pipeline.
        """
        return pulumi.get(self, "pipeline_display_name")

    @pipeline_display_name.setter
    def pipeline_display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pipeline_display_name", value)

    @property
    @pulumi.getter(name="pipelineName")
    def pipeline_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Pipeline.
        """
        return pulumi.get(self, "pipeline_name")

    @pipeline_name.setter
    def pipeline_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pipeline_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PipelineTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Pipeline(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pipeline_definition: Optional[Any] = None,
                 pipeline_description: Optional[pulumi.Input[str]] = None,
                 pipeline_display_name: Optional[pulumi.Input[str]] = None,
                 pipeline_name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SageMaker::Pipeline

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] pipeline_description: The description of the Pipeline.
        :param pulumi.Input[str] pipeline_display_name: The display name of the Pipeline.
        :param pulumi.Input[str] pipeline_name: The name of the Pipeline.
        :param pulumi.Input[str] role_arn: Role Arn
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PipelineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SageMaker::Pipeline

        :param str resource_name: The name of the resource.
        :param PipelineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PipelineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pipeline_definition: Optional[Any] = None,
                 pipeline_description: Optional[pulumi.Input[str]] = None,
                 pipeline_display_name: Optional[pulumi.Input[str]] = None,
                 pipeline_name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineTagArgs']]]]] = None,
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
            __props__ = PipelineArgs.__new__(PipelineArgs)

            if pipeline_definition is None and not opts.urn:
                raise TypeError("Missing required property 'pipeline_definition'")
            __props__.__dict__["pipeline_definition"] = pipeline_definition
            __props__.__dict__["pipeline_description"] = pipeline_description
            __props__.__dict__["pipeline_display_name"] = pipeline_display_name
            __props__.__dict__["pipeline_name"] = pipeline_name
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["tags"] = tags
        super(Pipeline, __self__).__init__(
            'aws-native:sagemaker:Pipeline',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Pipeline':
        """
        Get an existing Pipeline resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PipelineArgs.__new__(PipelineArgs)

        __props__.__dict__["pipeline_definition"] = None
        __props__.__dict__["pipeline_description"] = None
        __props__.__dict__["pipeline_display_name"] = None
        __props__.__dict__["pipeline_name"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["tags"] = None
        return Pipeline(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="pipelineDefinition")
    def pipeline_definition(self) -> pulumi.Output[Any]:
        return pulumi.get(self, "pipeline_definition")

    @property
    @pulumi.getter(name="pipelineDescription")
    def pipeline_description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the Pipeline.
        """
        return pulumi.get(self, "pipeline_description")

    @property
    @pulumi.getter(name="pipelineDisplayName")
    def pipeline_display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name of the Pipeline.
        """
        return pulumi.get(self, "pipeline_display_name")

    @property
    @pulumi.getter(name="pipelineName")
    def pipeline_name(self) -> pulumi.Output[str]:
        """
        The name of the Pipeline.
        """
        return pulumi.get(self, "pipeline_name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        Role Arn
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.PipelineTag']]]:
        return pulumi.get(self, "tags")

