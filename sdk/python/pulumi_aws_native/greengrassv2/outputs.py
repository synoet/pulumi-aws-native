# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'ComponentVersionComponentPlatform',
    'ComponentVersionLambdaContainerParams',
    'ComponentVersionLambdaDeviceMount',
    'ComponentVersionLambdaEventSource',
    'ComponentVersionLambdaExecutionParameters',
    'ComponentVersionLambdaFunctionRecipeSource',
    'ComponentVersionLambdaLinuxProcessParams',
    'ComponentVersionLambdaVolumeMount',
]

@pulumi.output_type
class ComponentVersionComponentPlatform(dict):
    def __init__(__self__, *,
                 attributes: Optional[Any] = None,
                 name: Optional[str] = None):
        if attributes is not None:
            pulumi.set(__self__, "attributes", attributes)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[Any]:
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")


@pulumi.output_type
class ComponentVersionLambdaContainerParams(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "memorySizeInKB":
            suggest = "memory_size_in_kb"
        elif key == "mountROSysfs":
            suggest = "mount_ro_sysfs"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ComponentVersionLambdaContainerParams. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ComponentVersionLambdaContainerParams.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ComponentVersionLambdaContainerParams.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 devices: Optional[Sequence['outputs.ComponentVersionLambdaDeviceMount']] = None,
                 memory_size_in_kb: Optional[int] = None,
                 mount_ro_sysfs: Optional[bool] = None,
                 volumes: Optional[Sequence['outputs.ComponentVersionLambdaVolumeMount']] = None):
        if devices is not None:
            pulumi.set(__self__, "devices", devices)
        if memory_size_in_kb is not None:
            pulumi.set(__self__, "memory_size_in_kb", memory_size_in_kb)
        if mount_ro_sysfs is not None:
            pulumi.set(__self__, "mount_ro_sysfs", mount_ro_sysfs)
        if volumes is not None:
            pulumi.set(__self__, "volumes", volumes)

    @property
    @pulumi.getter
    def devices(self) -> Optional[Sequence['outputs.ComponentVersionLambdaDeviceMount']]:
        return pulumi.get(self, "devices")

    @property
    @pulumi.getter(name="memorySizeInKB")
    def memory_size_in_kb(self) -> Optional[int]:
        return pulumi.get(self, "memory_size_in_kb")

    @property
    @pulumi.getter(name="mountROSysfs")
    def mount_ro_sysfs(self) -> Optional[bool]:
        return pulumi.get(self, "mount_ro_sysfs")

    @property
    @pulumi.getter
    def volumes(self) -> Optional[Sequence['outputs.ComponentVersionLambdaVolumeMount']]:
        return pulumi.get(self, "volumes")


@pulumi.output_type
class ComponentVersionLambdaDeviceMount(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "addGroupOwner":
            suggest = "add_group_owner"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ComponentVersionLambdaDeviceMount. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ComponentVersionLambdaDeviceMount.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ComponentVersionLambdaDeviceMount.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 add_group_owner: Optional[bool] = None,
                 path: Optional[str] = None,
                 permission: Optional['ComponentVersionLambdaFilesystemPermission'] = None):
        if add_group_owner is not None:
            pulumi.set(__self__, "add_group_owner", add_group_owner)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if permission is not None:
            pulumi.set(__self__, "permission", permission)

    @property
    @pulumi.getter(name="addGroupOwner")
    def add_group_owner(self) -> Optional[bool]:
        return pulumi.get(self, "add_group_owner")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def permission(self) -> Optional['ComponentVersionLambdaFilesystemPermission']:
        return pulumi.get(self, "permission")


@pulumi.output_type
class ComponentVersionLambdaEventSource(dict):
    def __init__(__self__, *,
                 topic: Optional[str] = None,
                 type: Optional['ComponentVersionLambdaEventSourceType'] = None):
        if topic is not None:
            pulumi.set(__self__, "topic", topic)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def topic(self) -> Optional[str]:
        return pulumi.get(self, "topic")

    @property
    @pulumi.getter
    def type(self) -> Optional['ComponentVersionLambdaEventSourceType']:
        return pulumi.get(self, "type")


@pulumi.output_type
class ComponentVersionLambdaExecutionParameters(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "environmentVariables":
            suggest = "environment_variables"
        elif key == "eventSources":
            suggest = "event_sources"
        elif key == "execArgs":
            suggest = "exec_args"
        elif key == "inputPayloadEncodingType":
            suggest = "input_payload_encoding_type"
        elif key == "linuxProcessParams":
            suggest = "linux_process_params"
        elif key == "maxIdleTimeInSeconds":
            suggest = "max_idle_time_in_seconds"
        elif key == "maxInstancesCount":
            suggest = "max_instances_count"
        elif key == "maxQueueSize":
            suggest = "max_queue_size"
        elif key == "statusTimeoutInSeconds":
            suggest = "status_timeout_in_seconds"
        elif key == "timeoutInSeconds":
            suggest = "timeout_in_seconds"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ComponentVersionLambdaExecutionParameters. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ComponentVersionLambdaExecutionParameters.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ComponentVersionLambdaExecutionParameters.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 environment_variables: Optional[Any] = None,
                 event_sources: Optional[Sequence['outputs.ComponentVersionLambdaEventSource']] = None,
                 exec_args: Optional[Sequence[str]] = None,
                 input_payload_encoding_type: Optional['ComponentVersionLambdaExecutionParametersInputPayloadEncodingType'] = None,
                 linux_process_params: Optional['outputs.ComponentVersionLambdaLinuxProcessParams'] = None,
                 max_idle_time_in_seconds: Optional[int] = None,
                 max_instances_count: Optional[int] = None,
                 max_queue_size: Optional[int] = None,
                 pinned: Optional[bool] = None,
                 status_timeout_in_seconds: Optional[int] = None,
                 timeout_in_seconds: Optional[int] = None):
        if environment_variables is not None:
            pulumi.set(__self__, "environment_variables", environment_variables)
        if event_sources is not None:
            pulumi.set(__self__, "event_sources", event_sources)
        if exec_args is not None:
            pulumi.set(__self__, "exec_args", exec_args)
        if input_payload_encoding_type is not None:
            pulumi.set(__self__, "input_payload_encoding_type", input_payload_encoding_type)
        if linux_process_params is not None:
            pulumi.set(__self__, "linux_process_params", linux_process_params)
        if max_idle_time_in_seconds is not None:
            pulumi.set(__self__, "max_idle_time_in_seconds", max_idle_time_in_seconds)
        if max_instances_count is not None:
            pulumi.set(__self__, "max_instances_count", max_instances_count)
        if max_queue_size is not None:
            pulumi.set(__self__, "max_queue_size", max_queue_size)
        if pinned is not None:
            pulumi.set(__self__, "pinned", pinned)
        if status_timeout_in_seconds is not None:
            pulumi.set(__self__, "status_timeout_in_seconds", status_timeout_in_seconds)
        if timeout_in_seconds is not None:
            pulumi.set(__self__, "timeout_in_seconds", timeout_in_seconds)

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Any]:
        return pulumi.get(self, "environment_variables")

    @property
    @pulumi.getter(name="eventSources")
    def event_sources(self) -> Optional[Sequence['outputs.ComponentVersionLambdaEventSource']]:
        return pulumi.get(self, "event_sources")

    @property
    @pulumi.getter(name="execArgs")
    def exec_args(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "exec_args")

    @property
    @pulumi.getter(name="inputPayloadEncodingType")
    def input_payload_encoding_type(self) -> Optional['ComponentVersionLambdaExecutionParametersInputPayloadEncodingType']:
        return pulumi.get(self, "input_payload_encoding_type")

    @property
    @pulumi.getter(name="linuxProcessParams")
    def linux_process_params(self) -> Optional['outputs.ComponentVersionLambdaLinuxProcessParams']:
        return pulumi.get(self, "linux_process_params")

    @property
    @pulumi.getter(name="maxIdleTimeInSeconds")
    def max_idle_time_in_seconds(self) -> Optional[int]:
        return pulumi.get(self, "max_idle_time_in_seconds")

    @property
    @pulumi.getter(name="maxInstancesCount")
    def max_instances_count(self) -> Optional[int]:
        return pulumi.get(self, "max_instances_count")

    @property
    @pulumi.getter(name="maxQueueSize")
    def max_queue_size(self) -> Optional[int]:
        return pulumi.get(self, "max_queue_size")

    @property
    @pulumi.getter
    def pinned(self) -> Optional[bool]:
        return pulumi.get(self, "pinned")

    @property
    @pulumi.getter(name="statusTimeoutInSeconds")
    def status_timeout_in_seconds(self) -> Optional[int]:
        return pulumi.get(self, "status_timeout_in_seconds")

    @property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[int]:
        return pulumi.get(self, "timeout_in_seconds")


@pulumi.output_type
class ComponentVersionLambdaFunctionRecipeSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "componentDependencies":
            suggest = "component_dependencies"
        elif key == "componentLambdaParameters":
            suggest = "component_lambda_parameters"
        elif key == "componentName":
            suggest = "component_name"
        elif key == "componentPlatforms":
            suggest = "component_platforms"
        elif key == "componentVersion":
            suggest = "component_version"
        elif key == "lambdaArn":
            suggest = "lambda_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ComponentVersionLambdaFunctionRecipeSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ComponentVersionLambdaFunctionRecipeSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ComponentVersionLambdaFunctionRecipeSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 component_dependencies: Optional[Any] = None,
                 component_lambda_parameters: Optional['outputs.ComponentVersionLambdaExecutionParameters'] = None,
                 component_name: Optional[str] = None,
                 component_platforms: Optional[Sequence['outputs.ComponentVersionComponentPlatform']] = None,
                 component_version: Optional[str] = None,
                 lambda_arn: Optional[str] = None):
        if component_dependencies is not None:
            pulumi.set(__self__, "component_dependencies", component_dependencies)
        if component_lambda_parameters is not None:
            pulumi.set(__self__, "component_lambda_parameters", component_lambda_parameters)
        if component_name is not None:
            pulumi.set(__self__, "component_name", component_name)
        if component_platforms is not None:
            pulumi.set(__self__, "component_platforms", component_platforms)
        if component_version is not None:
            pulumi.set(__self__, "component_version", component_version)
        if lambda_arn is not None:
            pulumi.set(__self__, "lambda_arn", lambda_arn)

    @property
    @pulumi.getter(name="componentDependencies")
    def component_dependencies(self) -> Optional[Any]:
        return pulumi.get(self, "component_dependencies")

    @property
    @pulumi.getter(name="componentLambdaParameters")
    def component_lambda_parameters(self) -> Optional['outputs.ComponentVersionLambdaExecutionParameters']:
        return pulumi.get(self, "component_lambda_parameters")

    @property
    @pulumi.getter(name="componentName")
    def component_name(self) -> Optional[str]:
        return pulumi.get(self, "component_name")

    @property
    @pulumi.getter(name="componentPlatforms")
    def component_platforms(self) -> Optional[Sequence['outputs.ComponentVersionComponentPlatform']]:
        return pulumi.get(self, "component_platforms")

    @property
    @pulumi.getter(name="componentVersion")
    def component_version(self) -> Optional[str]:
        return pulumi.get(self, "component_version")

    @property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> Optional[str]:
        return pulumi.get(self, "lambda_arn")


@pulumi.output_type
class ComponentVersionLambdaLinuxProcessParams(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "containerParams":
            suggest = "container_params"
        elif key == "isolationMode":
            suggest = "isolation_mode"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ComponentVersionLambdaLinuxProcessParams. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ComponentVersionLambdaLinuxProcessParams.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ComponentVersionLambdaLinuxProcessParams.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 container_params: Optional['outputs.ComponentVersionLambdaContainerParams'] = None,
                 isolation_mode: Optional['ComponentVersionLambdaLinuxProcessParamsIsolationMode'] = None):
        if container_params is not None:
            pulumi.set(__self__, "container_params", container_params)
        if isolation_mode is not None:
            pulumi.set(__self__, "isolation_mode", isolation_mode)

    @property
    @pulumi.getter(name="containerParams")
    def container_params(self) -> Optional['outputs.ComponentVersionLambdaContainerParams']:
        return pulumi.get(self, "container_params")

    @property
    @pulumi.getter(name="isolationMode")
    def isolation_mode(self) -> Optional['ComponentVersionLambdaLinuxProcessParamsIsolationMode']:
        return pulumi.get(self, "isolation_mode")


@pulumi.output_type
class ComponentVersionLambdaVolumeMount(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "addGroupOwner":
            suggest = "add_group_owner"
        elif key == "destinationPath":
            suggest = "destination_path"
        elif key == "sourcePath":
            suggest = "source_path"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ComponentVersionLambdaVolumeMount. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ComponentVersionLambdaVolumeMount.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ComponentVersionLambdaVolumeMount.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 add_group_owner: Optional[bool] = None,
                 destination_path: Optional[str] = None,
                 permission: Optional['ComponentVersionLambdaFilesystemPermission'] = None,
                 source_path: Optional[str] = None):
        if add_group_owner is not None:
            pulumi.set(__self__, "add_group_owner", add_group_owner)
        if destination_path is not None:
            pulumi.set(__self__, "destination_path", destination_path)
        if permission is not None:
            pulumi.set(__self__, "permission", permission)
        if source_path is not None:
            pulumi.set(__self__, "source_path", source_path)

    @property
    @pulumi.getter(name="addGroupOwner")
    def add_group_owner(self) -> Optional[bool]:
        return pulumi.get(self, "add_group_owner")

    @property
    @pulumi.getter(name="destinationPath")
    def destination_path(self) -> Optional[str]:
        return pulumi.get(self, "destination_path")

    @property
    @pulumi.getter
    def permission(self) -> Optional['ComponentVersionLambdaFilesystemPermission']:
        return pulumi.get(self, "permission")

    @property
    @pulumi.getter(name="sourcePath")
    def source_path(self) -> Optional[str]:
        return pulumi.get(self, "source_path")


