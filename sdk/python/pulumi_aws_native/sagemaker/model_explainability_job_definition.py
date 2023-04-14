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

__all__ = ['ModelExplainabilityJobDefinitionArgs', 'ModelExplainabilityJobDefinition']

@pulumi.input_type
class ModelExplainabilityJobDefinitionArgs:
    def __init__(__self__, *,
                 job_resources: pulumi.Input['ModelExplainabilityJobDefinitionMonitoringResourcesArgs'],
                 model_explainability_app_specification: pulumi.Input['ModelExplainabilityJobDefinitionModelExplainabilityAppSpecificationArgs'],
                 model_explainability_job_input: pulumi.Input['ModelExplainabilityJobDefinitionModelExplainabilityJobInputArgs'],
                 model_explainability_job_output_config: pulumi.Input['ModelExplainabilityJobDefinitionMonitoringOutputConfigArgs'],
                 role_arn: pulumi.Input[str],
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 job_definition_name: Optional[pulumi.Input[str]] = None,
                 model_explainability_baseline_config: Optional[pulumi.Input['ModelExplainabilityJobDefinitionModelExplainabilityBaselineConfigArgs']] = None,
                 network_config: Optional[pulumi.Input['ModelExplainabilityJobDefinitionNetworkConfigArgs']] = None,
                 stopping_condition: Optional[pulumi.Input['ModelExplainabilityJobDefinitionStoppingConditionArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ModelExplainabilityJobDefinitionTagArgs']]]] = None):
        """
        The set of arguments for constructing a ModelExplainabilityJobDefinition resource.
        :param pulumi.Input[str] role_arn: The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
        :param pulumi.Input[Sequence[pulumi.Input['ModelExplainabilityJobDefinitionTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "job_resources", job_resources)
        pulumi.set(__self__, "model_explainability_app_specification", model_explainability_app_specification)
        pulumi.set(__self__, "model_explainability_job_input", model_explainability_job_input)
        pulumi.set(__self__, "model_explainability_job_output_config", model_explainability_job_output_config)
        pulumi.set(__self__, "role_arn", role_arn)
        if endpoint_name is not None:
            pulumi.set(__self__, "endpoint_name", endpoint_name)
        if job_definition_name is not None:
            pulumi.set(__self__, "job_definition_name", job_definition_name)
        if model_explainability_baseline_config is not None:
            pulumi.set(__self__, "model_explainability_baseline_config", model_explainability_baseline_config)
        if network_config is not None:
            pulumi.set(__self__, "network_config", network_config)
        if stopping_condition is not None:
            pulumi.set(__self__, "stopping_condition", stopping_condition)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="jobResources")
    def job_resources(self) -> pulumi.Input['ModelExplainabilityJobDefinitionMonitoringResourcesArgs']:
        return pulumi.get(self, "job_resources")

    @job_resources.setter
    def job_resources(self, value: pulumi.Input['ModelExplainabilityJobDefinitionMonitoringResourcesArgs']):
        pulumi.set(self, "job_resources", value)

    @property
    @pulumi.getter(name="modelExplainabilityAppSpecification")
    def model_explainability_app_specification(self) -> pulumi.Input['ModelExplainabilityJobDefinitionModelExplainabilityAppSpecificationArgs']:
        return pulumi.get(self, "model_explainability_app_specification")

    @model_explainability_app_specification.setter
    def model_explainability_app_specification(self, value: pulumi.Input['ModelExplainabilityJobDefinitionModelExplainabilityAppSpecificationArgs']):
        pulumi.set(self, "model_explainability_app_specification", value)

    @property
    @pulumi.getter(name="modelExplainabilityJobInput")
    def model_explainability_job_input(self) -> pulumi.Input['ModelExplainabilityJobDefinitionModelExplainabilityJobInputArgs']:
        return pulumi.get(self, "model_explainability_job_input")

    @model_explainability_job_input.setter
    def model_explainability_job_input(self, value: pulumi.Input['ModelExplainabilityJobDefinitionModelExplainabilityJobInputArgs']):
        pulumi.set(self, "model_explainability_job_input", value)

    @property
    @pulumi.getter(name="modelExplainabilityJobOutputConfig")
    def model_explainability_job_output_config(self) -> pulumi.Input['ModelExplainabilityJobDefinitionMonitoringOutputConfigArgs']:
        return pulumi.get(self, "model_explainability_job_output_config")

    @model_explainability_job_output_config.setter
    def model_explainability_job_output_config(self, value: pulumi.Input['ModelExplainabilityJobDefinitionMonitoringOutputConfigArgs']):
        pulumi.set(self, "model_explainability_job_output_config", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "endpoint_name")

    @endpoint_name.setter
    def endpoint_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_name", value)

    @property
    @pulumi.getter(name="jobDefinitionName")
    def job_definition_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "job_definition_name")

    @job_definition_name.setter
    def job_definition_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "job_definition_name", value)

    @property
    @pulumi.getter(name="modelExplainabilityBaselineConfig")
    def model_explainability_baseline_config(self) -> Optional[pulumi.Input['ModelExplainabilityJobDefinitionModelExplainabilityBaselineConfigArgs']]:
        return pulumi.get(self, "model_explainability_baseline_config")

    @model_explainability_baseline_config.setter
    def model_explainability_baseline_config(self, value: Optional[pulumi.Input['ModelExplainabilityJobDefinitionModelExplainabilityBaselineConfigArgs']]):
        pulumi.set(self, "model_explainability_baseline_config", value)

    @property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input['ModelExplainabilityJobDefinitionNetworkConfigArgs']]:
        return pulumi.get(self, "network_config")

    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input['ModelExplainabilityJobDefinitionNetworkConfigArgs']]):
        pulumi.set(self, "network_config", value)

    @property
    @pulumi.getter(name="stoppingCondition")
    def stopping_condition(self) -> Optional[pulumi.Input['ModelExplainabilityJobDefinitionStoppingConditionArgs']]:
        return pulumi.get(self, "stopping_condition")

    @stopping_condition.setter
    def stopping_condition(self, value: Optional[pulumi.Input['ModelExplainabilityJobDefinitionStoppingConditionArgs']]):
        pulumi.set(self, "stopping_condition", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ModelExplainabilityJobDefinitionTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ModelExplainabilityJobDefinitionTagArgs']]]]):
        pulumi.set(self, "tags", value)


class ModelExplainabilityJobDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 job_definition_name: Optional[pulumi.Input[str]] = None,
                 job_resources: Optional[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionMonitoringResourcesArgs']]] = None,
                 model_explainability_app_specification: Optional[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionModelExplainabilityAppSpecificationArgs']]] = None,
                 model_explainability_baseline_config: Optional[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionModelExplainabilityBaselineConfigArgs']]] = None,
                 model_explainability_job_input: Optional[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionModelExplainabilityJobInputArgs']]] = None,
                 model_explainability_job_output_config: Optional[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionMonitoringOutputConfigArgs']]] = None,
                 network_config: Optional[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionNetworkConfigArgs']]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 stopping_condition: Optional[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionStoppingConditionArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SageMaker::ModelExplainabilityJobDefinition

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] role_arn: The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ModelExplainabilityJobDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SageMaker::ModelExplainabilityJobDefinition

        :param str resource_name: The name of the resource.
        :param ModelExplainabilityJobDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ModelExplainabilityJobDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 job_definition_name: Optional[pulumi.Input[str]] = None,
                 job_resources: Optional[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionMonitoringResourcesArgs']]] = None,
                 model_explainability_app_specification: Optional[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionModelExplainabilityAppSpecificationArgs']]] = None,
                 model_explainability_baseline_config: Optional[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionModelExplainabilityBaselineConfigArgs']]] = None,
                 model_explainability_job_input: Optional[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionModelExplainabilityJobInputArgs']]] = None,
                 model_explainability_job_output_config: Optional[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionMonitoringOutputConfigArgs']]] = None,
                 network_config: Optional[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionNetworkConfigArgs']]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 stopping_condition: Optional[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionStoppingConditionArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ModelExplainabilityJobDefinitionTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ModelExplainabilityJobDefinitionArgs.__new__(ModelExplainabilityJobDefinitionArgs)

            __props__.__dict__["endpoint_name"] = endpoint_name
            __props__.__dict__["job_definition_name"] = job_definition_name
            if job_resources is None and not opts.urn:
                raise TypeError("Missing required property 'job_resources'")
            __props__.__dict__["job_resources"] = job_resources
            if model_explainability_app_specification is None and not opts.urn:
                raise TypeError("Missing required property 'model_explainability_app_specification'")
            __props__.__dict__["model_explainability_app_specification"] = model_explainability_app_specification
            __props__.__dict__["model_explainability_baseline_config"] = model_explainability_baseline_config
            if model_explainability_job_input is None and not opts.urn:
                raise TypeError("Missing required property 'model_explainability_job_input'")
            __props__.__dict__["model_explainability_job_input"] = model_explainability_job_input
            if model_explainability_job_output_config is None and not opts.urn:
                raise TypeError("Missing required property 'model_explainability_job_output_config'")
            __props__.__dict__["model_explainability_job_output_config"] = model_explainability_job_output_config
            __props__.__dict__["network_config"] = network_config
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["stopping_condition"] = stopping_condition
            __props__.__dict__["tags"] = tags
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["job_definition_arn"] = None
        super(ModelExplainabilityJobDefinition, __self__).__init__(
            'aws-native:sagemaker:ModelExplainabilityJobDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ModelExplainabilityJobDefinition':
        """
        Get an existing ModelExplainabilityJobDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ModelExplainabilityJobDefinitionArgs.__new__(ModelExplainabilityJobDefinitionArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["endpoint_name"] = None
        __props__.__dict__["job_definition_arn"] = None
        __props__.__dict__["job_definition_name"] = None
        __props__.__dict__["job_resources"] = None
        __props__.__dict__["model_explainability_app_specification"] = None
        __props__.__dict__["model_explainability_baseline_config"] = None
        __props__.__dict__["model_explainability_job_input"] = None
        __props__.__dict__["model_explainability_job_output_config"] = None
        __props__.__dict__["network_config"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["stopping_condition"] = None
        __props__.__dict__["tags"] = None
        return ModelExplainabilityJobDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        The time at which the job definition was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "endpoint_name")

    @property
    @pulumi.getter(name="jobDefinitionArn")
    def job_definition_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of job definition.
        """
        return pulumi.get(self, "job_definition_arn")

    @property
    @pulumi.getter(name="jobDefinitionName")
    def job_definition_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "job_definition_name")

    @property
    @pulumi.getter(name="jobResources")
    def job_resources(self) -> pulumi.Output['outputs.ModelExplainabilityJobDefinitionMonitoringResources']:
        return pulumi.get(self, "job_resources")

    @property
    @pulumi.getter(name="modelExplainabilityAppSpecification")
    def model_explainability_app_specification(self) -> pulumi.Output['outputs.ModelExplainabilityJobDefinitionModelExplainabilityAppSpecification']:
        return pulumi.get(self, "model_explainability_app_specification")

    @property
    @pulumi.getter(name="modelExplainabilityBaselineConfig")
    def model_explainability_baseline_config(self) -> pulumi.Output[Optional['outputs.ModelExplainabilityJobDefinitionModelExplainabilityBaselineConfig']]:
        return pulumi.get(self, "model_explainability_baseline_config")

    @property
    @pulumi.getter(name="modelExplainabilityJobInput")
    def model_explainability_job_input(self) -> pulumi.Output['outputs.ModelExplainabilityJobDefinitionModelExplainabilityJobInput']:
        return pulumi.get(self, "model_explainability_job_input")

    @property
    @pulumi.getter(name="modelExplainabilityJobOutputConfig")
    def model_explainability_job_output_config(self) -> pulumi.Output['outputs.ModelExplainabilityJobDefinitionMonitoringOutputConfig']:
        return pulumi.get(self, "model_explainability_job_output_config")

    @property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> pulumi.Output[Optional['outputs.ModelExplainabilityJobDefinitionNetworkConfig']]:
        return pulumi.get(self, "network_config")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="stoppingCondition")
    def stopping_condition(self) -> pulumi.Output[Optional['outputs.ModelExplainabilityJobDefinitionStoppingCondition']]:
        return pulumi.get(self, "stopping_condition")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ModelExplainabilityJobDefinitionTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

