# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['TaskDefinitionArgs', 'TaskDefinition']

@pulumi.input_type
class TaskDefinitionArgs:
    def __init__(__self__, *,
                 container_definitions: Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionContainerDefinitionArgs']]]] = None,
                 cpu: Optional[pulumi.Input[str]] = None,
                 ephemeral_storage: Optional[pulumi.Input['TaskDefinitionEphemeralStorageArgs']] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 inference_accelerators: Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionInferenceAcceleratorArgs']]]] = None,
                 ipc_mode: Optional[pulumi.Input[str]] = None,
                 memory: Optional[pulumi.Input[str]] = None,
                 network_mode: Optional[pulumi.Input[str]] = None,
                 pid_mode: Optional[pulumi.Input[str]] = None,
                 placement_constraints: Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionPlacementConstraintArgs']]]] = None,
                 proxy_configuration: Optional[pulumi.Input['TaskDefinitionProxyConfigurationArgs']] = None,
                 requires_compatibilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionTagArgs']]]] = None,
                 task_role_arn: Optional[pulumi.Input[str]] = None,
                 volumes: Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionVolumeArgs']]]] = None):
        """
        The set of arguments for constructing a TaskDefinition resource.
        """
        if container_definitions is not None:
            pulumi.set(__self__, "container_definitions", container_definitions)
        if cpu is not None:
            pulumi.set(__self__, "cpu", cpu)
        if ephemeral_storage is not None:
            pulumi.set(__self__, "ephemeral_storage", ephemeral_storage)
        if execution_role_arn is not None:
            pulumi.set(__self__, "execution_role_arn", execution_role_arn)
        if family is not None:
            pulumi.set(__self__, "family", family)
        if inference_accelerators is not None:
            pulumi.set(__self__, "inference_accelerators", inference_accelerators)
        if ipc_mode is not None:
            pulumi.set(__self__, "ipc_mode", ipc_mode)
        if memory is not None:
            pulumi.set(__self__, "memory", memory)
        if network_mode is not None:
            pulumi.set(__self__, "network_mode", network_mode)
        if pid_mode is not None:
            pulumi.set(__self__, "pid_mode", pid_mode)
        if placement_constraints is not None:
            pulumi.set(__self__, "placement_constraints", placement_constraints)
        if proxy_configuration is not None:
            pulumi.set(__self__, "proxy_configuration", proxy_configuration)
        if requires_compatibilities is not None:
            pulumi.set(__self__, "requires_compatibilities", requires_compatibilities)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if task_role_arn is not None:
            pulumi.set(__self__, "task_role_arn", task_role_arn)
        if volumes is not None:
            pulumi.set(__self__, "volumes", volumes)

    @property
    @pulumi.getter(name="containerDefinitions")
    def container_definitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionContainerDefinitionArgs']]]]:
        return pulumi.get(self, "container_definitions")

    @container_definitions.setter
    def container_definitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionContainerDefinitionArgs']]]]):
        pulumi.set(self, "container_definitions", value)

    @property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cpu")

    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cpu", value)

    @property
    @pulumi.getter(name="ephemeralStorage")
    def ephemeral_storage(self) -> Optional[pulumi.Input['TaskDefinitionEphemeralStorageArgs']]:
        return pulumi.get(self, "ephemeral_storage")

    @ephemeral_storage.setter
    def ephemeral_storage(self, value: Optional[pulumi.Input['TaskDefinitionEphemeralStorageArgs']]):
        pulumi.set(self, "ephemeral_storage", value)

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "execution_role_arn")

    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "execution_role_arn", value)

    @property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "family")

    @family.setter
    def family(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "family", value)

    @property
    @pulumi.getter(name="inferenceAccelerators")
    def inference_accelerators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionInferenceAcceleratorArgs']]]]:
        return pulumi.get(self, "inference_accelerators")

    @inference_accelerators.setter
    def inference_accelerators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionInferenceAcceleratorArgs']]]]):
        pulumi.set(self, "inference_accelerators", value)

    @property
    @pulumi.getter(name="ipcMode")
    def ipc_mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ipc_mode")

    @ipc_mode.setter
    def ipc_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipc_mode", value)

    @property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter(name="networkMode")
    def network_mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "network_mode")

    @network_mode.setter
    def network_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_mode", value)

    @property
    @pulumi.getter(name="pidMode")
    def pid_mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "pid_mode")

    @pid_mode.setter
    def pid_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pid_mode", value)

    @property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionPlacementConstraintArgs']]]]:
        return pulumi.get(self, "placement_constraints")

    @placement_constraints.setter
    def placement_constraints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionPlacementConstraintArgs']]]]):
        pulumi.set(self, "placement_constraints", value)

    @property
    @pulumi.getter(name="proxyConfiguration")
    def proxy_configuration(self) -> Optional[pulumi.Input['TaskDefinitionProxyConfigurationArgs']]:
        return pulumi.get(self, "proxy_configuration")

    @proxy_configuration.setter
    def proxy_configuration(self, value: Optional[pulumi.Input['TaskDefinitionProxyConfigurationArgs']]):
        pulumi.set(self, "proxy_configuration", value)

    @property
    @pulumi.getter(name="requiresCompatibilities")
    def requires_compatibilities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "requires_compatibilities")

    @requires_compatibilities.setter
    def requires_compatibilities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "requires_compatibilities", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="taskRoleArn")
    def task_role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "task_role_arn")

    @task_role_arn.setter
    def task_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "task_role_arn", value)

    @property
    @pulumi.getter
    def volumes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionVolumeArgs']]]]:
        return pulumi.get(self, "volumes")

    @volumes.setter
    def volumes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionVolumeArgs']]]]):
        pulumi.set(self, "volumes", value)


class TaskDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskDefinitionContainerDefinitionArgs']]]]] = None,
                 cpu: Optional[pulumi.Input[str]] = None,
                 ephemeral_storage: Optional[pulumi.Input[pulumi.InputType['TaskDefinitionEphemeralStorageArgs']]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 inference_accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskDefinitionInferenceAcceleratorArgs']]]]] = None,
                 ipc_mode: Optional[pulumi.Input[str]] = None,
                 memory: Optional[pulumi.Input[str]] = None,
                 network_mode: Optional[pulumi.Input[str]] = None,
                 pid_mode: Optional[pulumi.Input[str]] = None,
                 placement_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskDefinitionPlacementConstraintArgs']]]]] = None,
                 proxy_configuration: Optional[pulumi.Input[pulumi.InputType['TaskDefinitionProxyConfigurationArgs']]] = None,
                 requires_compatibilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskDefinitionTagArgs']]]]] = None,
                 task_role_arn: Optional[pulumi.Input[str]] = None,
                 volumes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskDefinitionVolumeArgs']]]]] = None,
                 __props__=None):
        """
        Resource Schema describing various properties for ECS TaskDefinition

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TaskDefinitionArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Schema describing various properties for ECS TaskDefinition

        :param str resource_name: The name of the resource.
        :param TaskDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TaskDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskDefinitionContainerDefinitionArgs']]]]] = None,
                 cpu: Optional[pulumi.Input[str]] = None,
                 ephemeral_storage: Optional[pulumi.Input[pulumi.InputType['TaskDefinitionEphemeralStorageArgs']]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 inference_accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskDefinitionInferenceAcceleratorArgs']]]]] = None,
                 ipc_mode: Optional[pulumi.Input[str]] = None,
                 memory: Optional[pulumi.Input[str]] = None,
                 network_mode: Optional[pulumi.Input[str]] = None,
                 pid_mode: Optional[pulumi.Input[str]] = None,
                 placement_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskDefinitionPlacementConstraintArgs']]]]] = None,
                 proxy_configuration: Optional[pulumi.Input[pulumi.InputType['TaskDefinitionProxyConfigurationArgs']]] = None,
                 requires_compatibilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskDefinitionTagArgs']]]]] = None,
                 task_role_arn: Optional[pulumi.Input[str]] = None,
                 volumes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskDefinitionVolumeArgs']]]]] = None,
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
            __props__ = TaskDefinitionArgs.__new__(TaskDefinitionArgs)

            __props__.__dict__["container_definitions"] = container_definitions
            __props__.__dict__["cpu"] = cpu
            __props__.__dict__["ephemeral_storage"] = ephemeral_storage
            __props__.__dict__["execution_role_arn"] = execution_role_arn
            __props__.__dict__["family"] = family
            __props__.__dict__["inference_accelerators"] = inference_accelerators
            __props__.__dict__["ipc_mode"] = ipc_mode
            __props__.__dict__["memory"] = memory
            __props__.__dict__["network_mode"] = network_mode
            __props__.__dict__["pid_mode"] = pid_mode
            __props__.__dict__["placement_constraints"] = placement_constraints
            __props__.__dict__["proxy_configuration"] = proxy_configuration
            __props__.__dict__["requires_compatibilities"] = requires_compatibilities
            __props__.__dict__["tags"] = tags
            __props__.__dict__["task_role_arn"] = task_role_arn
            __props__.__dict__["volumes"] = volumes
            __props__.__dict__["task_definition_arn"] = None
        super(TaskDefinition, __self__).__init__(
            'aws-native:ecs:TaskDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TaskDefinition':
        """
        Get an existing TaskDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TaskDefinitionArgs.__new__(TaskDefinitionArgs)

        __props__.__dict__["container_definitions"] = None
        __props__.__dict__["cpu"] = None
        __props__.__dict__["ephemeral_storage"] = None
        __props__.__dict__["execution_role_arn"] = None
        __props__.__dict__["family"] = None
        __props__.__dict__["inference_accelerators"] = None
        __props__.__dict__["ipc_mode"] = None
        __props__.__dict__["memory"] = None
        __props__.__dict__["network_mode"] = None
        __props__.__dict__["pid_mode"] = None
        __props__.__dict__["placement_constraints"] = None
        __props__.__dict__["proxy_configuration"] = None
        __props__.__dict__["requires_compatibilities"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["task_definition_arn"] = None
        __props__.__dict__["task_role_arn"] = None
        __props__.__dict__["volumes"] = None
        return TaskDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="containerDefinitions")
    def container_definitions(self) -> pulumi.Output[Optional[Sequence['outputs.TaskDefinitionContainerDefinition']]]:
        return pulumi.get(self, "container_definitions")

    @property
    @pulumi.getter
    def cpu(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "cpu")

    @property
    @pulumi.getter(name="ephemeralStorage")
    def ephemeral_storage(self) -> pulumi.Output[Optional['outputs.TaskDefinitionEphemeralStorage']]:
        return pulumi.get(self, "ephemeral_storage")

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "execution_role_arn")

    @property
    @pulumi.getter
    def family(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "family")

    @property
    @pulumi.getter(name="inferenceAccelerators")
    def inference_accelerators(self) -> pulumi.Output[Optional[Sequence['outputs.TaskDefinitionInferenceAccelerator']]]:
        return pulumi.get(self, "inference_accelerators")

    @property
    @pulumi.getter(name="ipcMode")
    def ipc_mode(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ipc_mode")

    @property
    @pulumi.getter
    def memory(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter(name="networkMode")
    def network_mode(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "network_mode")

    @property
    @pulumi.getter(name="pidMode")
    def pid_mode(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "pid_mode")

    @property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(self) -> pulumi.Output[Optional[Sequence['outputs.TaskDefinitionPlacementConstraint']]]:
        return pulumi.get(self, "placement_constraints")

    @property
    @pulumi.getter(name="proxyConfiguration")
    def proxy_configuration(self) -> pulumi.Output[Optional['outputs.TaskDefinitionProxyConfiguration']]:
        return pulumi.get(self, "proxy_configuration")

    @property
    @pulumi.getter(name="requiresCompatibilities")
    def requires_compatibilities(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "requires_compatibilities")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.TaskDefinitionTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="taskDefinitionArn")
    def task_definition_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the Amazon ECS task definition
        """
        return pulumi.get(self, "task_definition_arn")

    @property
    @pulumi.getter(name="taskRoleArn")
    def task_role_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "task_role_arn")

    @property
    @pulumi.getter
    def volumes(self) -> pulumi.Output[Optional[Sequence['outputs.TaskDefinitionVolume']]]:
        return pulumi.get(self, "volumes")

