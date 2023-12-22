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

__all__ = ['PipelineArgs', 'Pipeline']

@pulumi.input_type
class PipelineArgs:
    def __init__(__self__, *,
                 role_arn: pulumi.Input[str],
                 stages: pulumi.Input[Sequence[pulumi.Input['PipelineStageDeclarationArgs']]],
                 artifact_store: Optional[pulumi.Input['PipelineArtifactStoreArgs']] = None,
                 artifact_stores: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineArtifactStoreMapArgs']]]] = None,
                 disable_inbound_stage_transitions: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineStageTransitionArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pipeline_type: Optional[pulumi.Input[str]] = None,
                 restart_execution_on_update: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineTagArgs']]]] = None,
                 triggers: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineTriggerDeclarationArgs']]]] = None,
                 variables: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineVariableDeclarationArgs']]]] = None):
        """
        The set of arguments for constructing a Pipeline resource.
        """
        pulumi.set(__self__, "role_arn", role_arn)
        pulumi.set(__self__, "stages", stages)
        if artifact_store is not None:
            pulumi.set(__self__, "artifact_store", artifact_store)
        if artifact_stores is not None:
            pulumi.set(__self__, "artifact_stores", artifact_stores)
        if disable_inbound_stage_transitions is not None:
            pulumi.set(__self__, "disable_inbound_stage_transitions", disable_inbound_stage_transitions)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if pipeline_type is not None:
            pulumi.set(__self__, "pipeline_type", pipeline_type)
        if restart_execution_on_update is not None:
            pulumi.set(__self__, "restart_execution_on_update", restart_execution_on_update)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if triggers is not None:
            pulumi.set(__self__, "triggers", triggers)
        if variables is not None:
            pulumi.set(__self__, "variables", variables)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter
    def stages(self) -> pulumi.Input[Sequence[pulumi.Input['PipelineStageDeclarationArgs']]]:
        return pulumi.get(self, "stages")

    @stages.setter
    def stages(self, value: pulumi.Input[Sequence[pulumi.Input['PipelineStageDeclarationArgs']]]):
        pulumi.set(self, "stages", value)

    @property
    @pulumi.getter(name="artifactStore")
    def artifact_store(self) -> Optional[pulumi.Input['PipelineArtifactStoreArgs']]:
        return pulumi.get(self, "artifact_store")

    @artifact_store.setter
    def artifact_store(self, value: Optional[pulumi.Input['PipelineArtifactStoreArgs']]):
        pulumi.set(self, "artifact_store", value)

    @property
    @pulumi.getter(name="artifactStores")
    def artifact_stores(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PipelineArtifactStoreMapArgs']]]]:
        return pulumi.get(self, "artifact_stores")

    @artifact_stores.setter
    def artifact_stores(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineArtifactStoreMapArgs']]]]):
        pulumi.set(self, "artifact_stores", value)

    @property
    @pulumi.getter(name="disableInboundStageTransitions")
    def disable_inbound_stage_transitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PipelineStageTransitionArgs']]]]:
        return pulumi.get(self, "disable_inbound_stage_transitions")

    @disable_inbound_stage_transitions.setter
    def disable_inbound_stage_transitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineStageTransitionArgs']]]]):
        pulumi.set(self, "disable_inbound_stage_transitions", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="pipelineType")
    def pipeline_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "pipeline_type")

    @pipeline_type.setter
    def pipeline_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pipeline_type", value)

    @property
    @pulumi.getter(name="restartExecutionOnUpdate")
    def restart_execution_on_update(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "restart_execution_on_update")

    @restart_execution_on_update.setter
    def restart_execution_on_update(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "restart_execution_on_update", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PipelineTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PipelineTriggerDeclarationArgs']]]]:
        return pulumi.get(self, "triggers")

    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineTriggerDeclarationArgs']]]]):
        pulumi.set(self, "triggers", value)

    @property
    @pulumi.getter
    def variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PipelineVariableDeclarationArgs']]]]:
        return pulumi.get(self, "variables")

    @variables.setter
    def variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineVariableDeclarationArgs']]]]):
        pulumi.set(self, "variables", value)


warnings.warn("""Pipeline is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Pipeline(pulumi.CustomResource):
    warnings.warn("""Pipeline is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 artifact_store: Optional[pulumi.Input[pulumi.InputType['PipelineArtifactStoreArgs']]] = None,
                 artifact_stores: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineArtifactStoreMapArgs']]]]] = None,
                 disable_inbound_stage_transitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineStageTransitionArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pipeline_type: Optional[pulumi.Input[str]] = None,
                 restart_execution_on_update: Optional[pulumi.Input[bool]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 stages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineStageDeclarationArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineTagArgs']]]]] = None,
                 triggers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineTriggerDeclarationArgs']]]]] = None,
                 variables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineVariableDeclarationArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::CodePipeline::Pipeline

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PipelineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::CodePipeline::Pipeline

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
                 artifact_store: Optional[pulumi.Input[pulumi.InputType['PipelineArtifactStoreArgs']]] = None,
                 artifact_stores: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineArtifactStoreMapArgs']]]]] = None,
                 disable_inbound_stage_transitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineStageTransitionArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pipeline_type: Optional[pulumi.Input[str]] = None,
                 restart_execution_on_update: Optional[pulumi.Input[bool]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 stages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineStageDeclarationArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineTagArgs']]]]] = None,
                 triggers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineTriggerDeclarationArgs']]]]] = None,
                 variables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineVariableDeclarationArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""Pipeline is deprecated: Pipeline is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PipelineArgs.__new__(PipelineArgs)

            __props__.__dict__["artifact_store"] = artifact_store
            __props__.__dict__["artifact_stores"] = artifact_stores
            __props__.__dict__["disable_inbound_stage_transitions"] = disable_inbound_stage_transitions
            __props__.__dict__["name"] = name
            __props__.__dict__["pipeline_type"] = pipeline_type
            __props__.__dict__["restart_execution_on_update"] = restart_execution_on_update
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            if stages is None and not opts.urn:
                raise TypeError("Missing required property 'stages'")
            __props__.__dict__["stages"] = stages
            __props__.__dict__["tags"] = tags
            __props__.__dict__["triggers"] = triggers
            __props__.__dict__["variables"] = variables
            __props__.__dict__["version"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Pipeline, __self__).__init__(
            'aws-native:codepipeline:Pipeline',
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

        __props__.__dict__["artifact_store"] = None
        __props__.__dict__["artifact_stores"] = None
        __props__.__dict__["disable_inbound_stage_transitions"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["pipeline_type"] = None
        __props__.__dict__["restart_execution_on_update"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["stages"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["triggers"] = None
        __props__.__dict__["variables"] = None
        __props__.__dict__["version"] = None
        return Pipeline(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="artifactStore")
    def artifact_store(self) -> pulumi.Output[Optional['outputs.PipelineArtifactStore']]:
        return pulumi.get(self, "artifact_store")

    @property
    @pulumi.getter(name="artifactStores")
    def artifact_stores(self) -> pulumi.Output[Optional[Sequence['outputs.PipelineArtifactStoreMap']]]:
        return pulumi.get(self, "artifact_stores")

    @property
    @pulumi.getter(name="disableInboundStageTransitions")
    def disable_inbound_stage_transitions(self) -> pulumi.Output[Optional[Sequence['outputs.PipelineStageTransition']]]:
        return pulumi.get(self, "disable_inbound_stage_transitions")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pipelineType")
    def pipeline_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "pipeline_type")

    @property
    @pulumi.getter(name="restartExecutionOnUpdate")
    def restart_execution_on_update(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "restart_execution_on_update")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def stages(self) -> pulumi.Output[Sequence['outputs.PipelineStageDeclaration']]:
        return pulumi.get(self, "stages")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.PipelineTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Optional[Sequence['outputs.PipelineTriggerDeclaration']]]:
        return pulumi.get(self, "triggers")

    @property
    @pulumi.getter
    def variables(self) -> pulumi.Output[Optional[Sequence['outputs.PipelineVariableDeclaration']]]:
        return pulumi.get(self, "variables")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "version")

