# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'ServiceAuthenticationConfigurationArgs',
    'ServiceCodeConfigurationValuesArgs',
    'ServiceCodeConfigurationArgs',
    'ServiceCodeRepositoryArgs',
    'ServiceEncryptionConfigurationArgs',
    'ServiceHealthCheckConfigurationArgs',
    'ServiceImageConfigurationArgs',
    'ServiceImageRepositoryArgs',
    'ServiceInstanceConfigurationArgs',
    'ServiceKeyValuePairArgs',
    'ServiceSourceCodeVersionArgs',
    'ServiceSourceConfigurationArgs',
    'ServiceTagArgs',
]

@pulumi.input_type
class ServiceAuthenticationConfigurationArgs:
    def __init__(__self__, *,
                 access_role_arn: Optional[pulumi.Input[str]] = None,
                 connection_arn: Optional[pulumi.Input[str]] = None):
        """
        Authentication Configuration
        :param pulumi.Input[str] access_role_arn: Access Role Arn
        :param pulumi.Input[str] connection_arn: Connection Arn
        """
        if access_role_arn is not None:
            pulumi.set(__self__, "access_role_arn", access_role_arn)
        if connection_arn is not None:
            pulumi.set(__self__, "connection_arn", connection_arn)

    @property
    @pulumi.getter(name="accessRoleArn")
    def access_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Access Role Arn
        """
        return pulumi.get(self, "access_role_arn")

    @access_role_arn.setter
    def access_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_role_arn", value)

    @property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Connection Arn
        """
        return pulumi.get(self, "connection_arn")

    @connection_arn.setter
    def connection_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_arn", value)


@pulumi.input_type
class ServiceCodeConfigurationValuesArgs:
    def __init__(__self__, *,
                 runtime: pulumi.Input['ServiceCodeConfigurationValuesRuntime'],
                 build_command: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[str]] = None,
                 runtime_environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceKeyValuePairArgs']]]] = None,
                 start_command: Optional[pulumi.Input[str]] = None):
        """
        Code Configuration Values
        :param pulumi.Input['ServiceCodeConfigurationValuesRuntime'] runtime: Runtime
        :param pulumi.Input[str] build_command: Build Command
        :param pulumi.Input[str] port: Port
        :param pulumi.Input[str] start_command: Start Command
        """
        pulumi.set(__self__, "runtime", runtime)
        if build_command is not None:
            pulumi.set(__self__, "build_command", build_command)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if runtime_environment_variables is not None:
            pulumi.set(__self__, "runtime_environment_variables", runtime_environment_variables)
        if start_command is not None:
            pulumi.set(__self__, "start_command", start_command)

    @property
    @pulumi.getter
    def runtime(self) -> pulumi.Input['ServiceCodeConfigurationValuesRuntime']:
        """
        Runtime
        """
        return pulumi.get(self, "runtime")

    @runtime.setter
    def runtime(self, value: pulumi.Input['ServiceCodeConfigurationValuesRuntime']):
        pulumi.set(self, "runtime", value)

    @property
    @pulumi.getter(name="buildCommand")
    def build_command(self) -> Optional[pulumi.Input[str]]:
        """
        Build Command
        """
        return pulumi.get(self, "build_command")

    @build_command.setter
    def build_command(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "build_command", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[str]]:
        """
        Port
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="runtimeEnvironmentVariables")
    def runtime_environment_variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceKeyValuePairArgs']]]]:
        return pulumi.get(self, "runtime_environment_variables")

    @runtime_environment_variables.setter
    def runtime_environment_variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceKeyValuePairArgs']]]]):
        pulumi.set(self, "runtime_environment_variables", value)

    @property
    @pulumi.getter(name="startCommand")
    def start_command(self) -> Optional[pulumi.Input[str]]:
        """
        Start Command
        """
        return pulumi.get(self, "start_command")

    @start_command.setter
    def start_command(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_command", value)


@pulumi.input_type
class ServiceCodeConfigurationArgs:
    def __init__(__self__, *,
                 configuration_source: pulumi.Input['ServiceCodeConfigurationConfigurationSource'],
                 code_configuration_values: Optional[pulumi.Input['ServiceCodeConfigurationValuesArgs']] = None):
        """
        Code Configuration
        :param pulumi.Input['ServiceCodeConfigurationConfigurationSource'] configuration_source: Configuration Source
        """
        pulumi.set(__self__, "configuration_source", configuration_source)
        if code_configuration_values is not None:
            pulumi.set(__self__, "code_configuration_values", code_configuration_values)

    @property
    @pulumi.getter(name="configurationSource")
    def configuration_source(self) -> pulumi.Input['ServiceCodeConfigurationConfigurationSource']:
        """
        Configuration Source
        """
        return pulumi.get(self, "configuration_source")

    @configuration_source.setter
    def configuration_source(self, value: pulumi.Input['ServiceCodeConfigurationConfigurationSource']):
        pulumi.set(self, "configuration_source", value)

    @property
    @pulumi.getter(name="codeConfigurationValues")
    def code_configuration_values(self) -> Optional[pulumi.Input['ServiceCodeConfigurationValuesArgs']]:
        return pulumi.get(self, "code_configuration_values")

    @code_configuration_values.setter
    def code_configuration_values(self, value: Optional[pulumi.Input['ServiceCodeConfigurationValuesArgs']]):
        pulumi.set(self, "code_configuration_values", value)


@pulumi.input_type
class ServiceCodeRepositoryArgs:
    def __init__(__self__, *,
                 repository_url: pulumi.Input[str],
                 source_code_version: pulumi.Input['ServiceSourceCodeVersionArgs'],
                 code_configuration: Optional[pulumi.Input['ServiceCodeConfigurationArgs']] = None):
        """
        Source Code Repository
        :param pulumi.Input[str] repository_url: Repository Url
        """
        pulumi.set(__self__, "repository_url", repository_url)
        pulumi.set(__self__, "source_code_version", source_code_version)
        if code_configuration is not None:
            pulumi.set(__self__, "code_configuration", code_configuration)

    @property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Input[str]:
        """
        Repository Url
        """
        return pulumi.get(self, "repository_url")

    @repository_url.setter
    def repository_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "repository_url", value)

    @property
    @pulumi.getter(name="sourceCodeVersion")
    def source_code_version(self) -> pulumi.Input['ServiceSourceCodeVersionArgs']:
        return pulumi.get(self, "source_code_version")

    @source_code_version.setter
    def source_code_version(self, value: pulumi.Input['ServiceSourceCodeVersionArgs']):
        pulumi.set(self, "source_code_version", value)

    @property
    @pulumi.getter(name="codeConfiguration")
    def code_configuration(self) -> Optional[pulumi.Input['ServiceCodeConfigurationArgs']]:
        return pulumi.get(self, "code_configuration")

    @code_configuration.setter
    def code_configuration(self, value: Optional[pulumi.Input['ServiceCodeConfigurationArgs']]):
        pulumi.set(self, "code_configuration", value)


@pulumi.input_type
class ServiceEncryptionConfigurationArgs:
    def __init__(__self__, *,
                 kms_key: pulumi.Input[str]):
        """
        Encryption configuration (KMS key)
        :param pulumi.Input[str] kms_key: The KMS Key
        """
        pulumi.set(__self__, "kms_key", kms_key)

    @property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Input[str]:
        """
        The KMS Key
        """
        return pulumi.get(self, "kms_key")

    @kms_key.setter
    def kms_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "kms_key", value)


@pulumi.input_type
class ServiceHealthCheckConfigurationArgs:
    def __init__(__self__, *,
                 healthy_threshold: Optional[pulumi.Input[int]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input['ServiceHealthCheckConfigurationProtocol']] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 unhealthy_threshold: Optional[pulumi.Input[int]] = None):
        """
        Health check configuration
        :param pulumi.Input[int] healthy_threshold: Health check Healthy Threshold
        :param pulumi.Input[int] interval: Health check Interval
        :param pulumi.Input[str] path: Health check Path
        :param pulumi.Input['ServiceHealthCheckConfigurationProtocol'] protocol: Health Check Protocol
        :param pulumi.Input[int] timeout: Health check Timeout
        :param pulumi.Input[int] unhealthy_threshold: Health check Unhealthy Threshold
        """
        if healthy_threshold is not None:
            pulumi.set(__self__, "healthy_threshold", healthy_threshold)
        if interval is not None:
            pulumi.set(__self__, "interval", interval)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)
        if unhealthy_threshold is not None:
            pulumi.set(__self__, "unhealthy_threshold", unhealthy_threshold)

    @property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> Optional[pulumi.Input[int]]:
        """
        Health check Healthy Threshold
        """
        return pulumi.get(self, "healthy_threshold")

    @healthy_threshold.setter
    def healthy_threshold(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "healthy_threshold", value)

    @property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[int]]:
        """
        Health check Interval
        """
        return pulumi.get(self, "interval")

    @interval.setter
    def interval(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "interval", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        Health check Path
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input['ServiceHealthCheckConfigurationProtocol']]:
        """
        Health Check Protocol
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input['ServiceHealthCheckConfigurationProtocol']]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Health check Timeout
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout", value)

    @property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> Optional[pulumi.Input[int]]:
        """
        Health check Unhealthy Threshold
        """
        return pulumi.get(self, "unhealthy_threshold")

    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "unhealthy_threshold", value)


@pulumi.input_type
class ServiceImageConfigurationArgs:
    def __init__(__self__, *,
                 port: Optional[pulumi.Input[str]] = None,
                 runtime_environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceKeyValuePairArgs']]]] = None,
                 start_command: Optional[pulumi.Input[str]] = None):
        """
        Image Configuration
        :param pulumi.Input[str] port: Port
        :param pulumi.Input[str] start_command: Start Command
        """
        if port is not None:
            pulumi.set(__self__, "port", port)
        if runtime_environment_variables is not None:
            pulumi.set(__self__, "runtime_environment_variables", runtime_environment_variables)
        if start_command is not None:
            pulumi.set(__self__, "start_command", start_command)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[str]]:
        """
        Port
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="runtimeEnvironmentVariables")
    def runtime_environment_variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceKeyValuePairArgs']]]]:
        return pulumi.get(self, "runtime_environment_variables")

    @runtime_environment_variables.setter
    def runtime_environment_variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceKeyValuePairArgs']]]]):
        pulumi.set(self, "runtime_environment_variables", value)

    @property
    @pulumi.getter(name="startCommand")
    def start_command(self) -> Optional[pulumi.Input[str]]:
        """
        Start Command
        """
        return pulumi.get(self, "start_command")

    @start_command.setter
    def start_command(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_command", value)


@pulumi.input_type
class ServiceImageRepositoryArgs:
    def __init__(__self__, *,
                 image_identifier: pulumi.Input[str],
                 image_repository_type: pulumi.Input['ServiceImageRepositoryImageRepositoryType'],
                 image_configuration: Optional[pulumi.Input['ServiceImageConfigurationArgs']] = None):
        """
        Image Repository
        :param pulumi.Input[str] image_identifier: Image Identifier
        :param pulumi.Input['ServiceImageRepositoryImageRepositoryType'] image_repository_type: Image Repository Type
        """
        pulumi.set(__self__, "image_identifier", image_identifier)
        pulumi.set(__self__, "image_repository_type", image_repository_type)
        if image_configuration is not None:
            pulumi.set(__self__, "image_configuration", image_configuration)

    @property
    @pulumi.getter(name="imageIdentifier")
    def image_identifier(self) -> pulumi.Input[str]:
        """
        Image Identifier
        """
        return pulumi.get(self, "image_identifier")

    @image_identifier.setter
    def image_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "image_identifier", value)

    @property
    @pulumi.getter(name="imageRepositoryType")
    def image_repository_type(self) -> pulumi.Input['ServiceImageRepositoryImageRepositoryType']:
        """
        Image Repository Type
        """
        return pulumi.get(self, "image_repository_type")

    @image_repository_type.setter
    def image_repository_type(self, value: pulumi.Input['ServiceImageRepositoryImageRepositoryType']):
        pulumi.set(self, "image_repository_type", value)

    @property
    @pulumi.getter(name="imageConfiguration")
    def image_configuration(self) -> Optional[pulumi.Input['ServiceImageConfigurationArgs']]:
        return pulumi.get(self, "image_configuration")

    @image_configuration.setter
    def image_configuration(self, value: Optional[pulumi.Input['ServiceImageConfigurationArgs']]):
        pulumi.set(self, "image_configuration", value)


@pulumi.input_type
class ServiceInstanceConfigurationArgs:
    def __init__(__self__, *,
                 cpu: Optional[pulumi.Input[str]] = None,
                 instance_role_arn: Optional[pulumi.Input[str]] = None,
                 memory: Optional[pulumi.Input[str]] = None):
        """
        Instance Configuration
        :param pulumi.Input[str] cpu: CPU
        :param pulumi.Input[str] instance_role_arn: Instance Role Arn
        :param pulumi.Input[str] memory: Memory
        """
        if cpu is not None:
            pulumi.set(__self__, "cpu", cpu)
        if instance_role_arn is not None:
            pulumi.set(__self__, "instance_role_arn", instance_role_arn)
        if memory is not None:
            pulumi.set(__self__, "memory", memory)

    @property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[str]]:
        """
        CPU
        """
        return pulumi.get(self, "cpu")

    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cpu", value)

    @property
    @pulumi.getter(name="instanceRoleArn")
    def instance_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Instance Role Arn
        """
        return pulumi.get(self, "instance_role_arn")

    @instance_role_arn.setter
    def instance_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_role_arn", value)

    @property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[str]]:
        """
        Memory
        """
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "memory", value)


@pulumi.input_type
class ServiceKeyValuePairArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        if name is not None:
            pulumi.set(__self__, "name", name)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ServiceSourceCodeVersionArgs:
    def __init__(__self__, *,
                 type: pulumi.Input['ServiceSourceCodeVersionType'],
                 value: pulumi.Input[str]):
        """
        Source Code Version
        :param pulumi.Input['ServiceSourceCodeVersionType'] type: Source Code Version Type
        :param pulumi.Input[str] value: Source Code Version Value
        """
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['ServiceSourceCodeVersionType']:
        """
        Source Code Version Type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['ServiceSourceCodeVersionType']):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        Source Code Version Value
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ServiceSourceConfigurationArgs:
    def __init__(__self__, *,
                 authentication_configuration: Optional[pulumi.Input['ServiceAuthenticationConfigurationArgs']] = None,
                 auto_deployments_enabled: Optional[pulumi.Input[bool]] = None,
                 code_repository: Optional[pulumi.Input['ServiceCodeRepositoryArgs']] = None,
                 image_repository: Optional[pulumi.Input['ServiceImageRepositoryArgs']] = None):
        """
        Source Code configuration
        :param pulumi.Input[bool] auto_deployments_enabled: Auto Deployment enabled
        """
        if authentication_configuration is not None:
            pulumi.set(__self__, "authentication_configuration", authentication_configuration)
        if auto_deployments_enabled is not None:
            pulumi.set(__self__, "auto_deployments_enabled", auto_deployments_enabled)
        if code_repository is not None:
            pulumi.set(__self__, "code_repository", code_repository)
        if image_repository is not None:
            pulumi.set(__self__, "image_repository", image_repository)

    @property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(self) -> Optional[pulumi.Input['ServiceAuthenticationConfigurationArgs']]:
        return pulumi.get(self, "authentication_configuration")

    @authentication_configuration.setter
    def authentication_configuration(self, value: Optional[pulumi.Input['ServiceAuthenticationConfigurationArgs']]):
        pulumi.set(self, "authentication_configuration", value)

    @property
    @pulumi.getter(name="autoDeploymentsEnabled")
    def auto_deployments_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Auto Deployment enabled
        """
        return pulumi.get(self, "auto_deployments_enabled")

    @auto_deployments_enabled.setter
    def auto_deployments_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_deployments_enabled", value)

    @property
    @pulumi.getter(name="codeRepository")
    def code_repository(self) -> Optional[pulumi.Input['ServiceCodeRepositoryArgs']]:
        return pulumi.get(self, "code_repository")

    @code_repository.setter
    def code_repository(self, value: Optional[pulumi.Input['ServiceCodeRepositoryArgs']]):
        pulumi.set(self, "code_repository", value)

    @property
    @pulumi.getter(name="imageRepository")
    def image_repository(self) -> Optional[pulumi.Input['ServiceImageRepositoryArgs']]:
        return pulumi.get(self, "image_repository")

    @image_repository.setter
    def image_repository(self, value: Optional[pulumi.Input['ServiceImageRepositoryArgs']]):
        pulumi.set(self, "image_repository", value)


@pulumi.input_type
class ServiceTagArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


