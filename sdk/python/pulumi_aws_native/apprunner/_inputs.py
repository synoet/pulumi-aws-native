# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'ObservabilityConfigurationTagArgs',
    'ObservabilityConfigurationTraceConfigurationArgs',
    'ServiceAuthenticationConfigurationArgs',
    'ServiceCodeConfigurationValuesArgs',
    'ServiceCodeConfigurationArgs',
    'ServiceCodeRepositoryArgs',
    'ServiceEgressConfigurationArgs',
    'ServiceEncryptionConfigurationArgs',
    'ServiceHealthCheckConfigurationArgs',
    'ServiceImageConfigurationArgs',
    'ServiceImageRepositoryArgs',
    'ServiceIngressConfigurationArgs',
    'ServiceInstanceConfigurationArgs',
    'ServiceKeyValuePairArgs',
    'ServiceNetworkConfigurationArgs',
    'ServiceObservabilityConfigurationArgs',
    'ServiceSourceCodeVersionArgs',
    'ServiceSourceConfigurationArgs',
    'ServiceTagArgs',
    'VpcConnectorTagArgs',
    'VpcIngressConnectionIngressVpcConfigurationArgs',
    'VpcIngressConnectionTagArgs',
]

@pulumi.input_type
class ObservabilityConfigurationTagArgs:
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


@pulumi.input_type
class ObservabilityConfigurationTraceConfigurationArgs:
    def __init__(__self__, *,
                 vendor: pulumi.Input['ObservabilityConfigurationTraceConfigurationVendor']):
        """
        Describes the configuration of the tracing feature within an AWS App Runner observability configuration.
        :param pulumi.Input['ObservabilityConfigurationTraceConfigurationVendor'] vendor: The implementation provider chosen for tracing App Runner services.
        """
        pulumi.set(__self__, "vendor", vendor)

    @property
    @pulumi.getter
    def vendor(self) -> pulumi.Input['ObservabilityConfigurationTraceConfigurationVendor']:
        """
        The implementation provider chosen for tracing App Runner services.
        """
        return pulumi.get(self, "vendor")

    @vendor.setter
    def vendor(self, value: pulumi.Input['ObservabilityConfigurationTraceConfigurationVendor']):
        pulumi.set(self, "vendor", value)


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
                 runtime_environment_secrets: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceKeyValuePairArgs']]]] = None,
                 runtime_environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceKeyValuePairArgs']]]] = None,
                 start_command: Optional[pulumi.Input[str]] = None):
        """
        Code Configuration Values
        :param pulumi.Input['ServiceCodeConfigurationValuesRuntime'] runtime: Runtime
        :param pulumi.Input[str] build_command: Build Command
        :param pulumi.Input[str] port: Port
        :param pulumi.Input[Sequence[pulumi.Input['ServiceKeyValuePairArgs']]] runtime_environment_secrets: The secrets and parameters that get referenced by your service as environment variables
        :param pulumi.Input[str] start_command: Start Command
        """
        pulumi.set(__self__, "runtime", runtime)
        if build_command is not None:
            pulumi.set(__self__, "build_command", build_command)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if runtime_environment_secrets is not None:
            pulumi.set(__self__, "runtime_environment_secrets", runtime_environment_secrets)
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
    @pulumi.getter(name="runtimeEnvironmentSecrets")
    def runtime_environment_secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceKeyValuePairArgs']]]]:
        """
        The secrets and parameters that get referenced by your service as environment variables
        """
        return pulumi.get(self, "runtime_environment_secrets")

    @runtime_environment_secrets.setter
    def runtime_environment_secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceKeyValuePairArgs']]]]):
        pulumi.set(self, "runtime_environment_secrets", value)

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
class ServiceEgressConfigurationArgs:
    def __init__(__self__, *,
                 egress_type: pulumi.Input['ServiceEgressConfigurationEgressType'],
                 vpc_connector_arn: Optional[pulumi.Input[str]] = None):
        """
        Network egress configuration
        :param pulumi.Input['ServiceEgressConfigurationEgressType'] egress_type: Network egress type.
        :param pulumi.Input[str] vpc_connector_arn: The Amazon Resource Name (ARN) of the App Runner VpcConnector.
        """
        pulumi.set(__self__, "egress_type", egress_type)
        if vpc_connector_arn is not None:
            pulumi.set(__self__, "vpc_connector_arn", vpc_connector_arn)

    @property
    @pulumi.getter(name="egressType")
    def egress_type(self) -> pulumi.Input['ServiceEgressConfigurationEgressType']:
        """
        Network egress type.
        """
        return pulumi.get(self, "egress_type")

    @egress_type.setter
    def egress_type(self, value: pulumi.Input['ServiceEgressConfigurationEgressType']):
        pulumi.set(self, "egress_type", value)

    @property
    @pulumi.getter(name="vpcConnectorArn")
    def vpc_connector_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the App Runner VpcConnector.
        """
        return pulumi.get(self, "vpc_connector_arn")

    @vpc_connector_arn.setter
    def vpc_connector_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_connector_arn", value)


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
                 runtime_environment_secrets: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceKeyValuePairArgs']]]] = None,
                 runtime_environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceKeyValuePairArgs']]]] = None,
                 start_command: Optional[pulumi.Input[str]] = None):
        """
        Image Configuration
        :param pulumi.Input[str] port: Port
        :param pulumi.Input[Sequence[pulumi.Input['ServiceKeyValuePairArgs']]] runtime_environment_secrets: The secrets and parameters that get referenced by your service as environment variables
        :param pulumi.Input[str] start_command: Start Command
        """
        if port is not None:
            pulumi.set(__self__, "port", port)
        if runtime_environment_secrets is not None:
            pulumi.set(__self__, "runtime_environment_secrets", runtime_environment_secrets)
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
    @pulumi.getter(name="runtimeEnvironmentSecrets")
    def runtime_environment_secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceKeyValuePairArgs']]]]:
        """
        The secrets and parameters that get referenced by your service as environment variables
        """
        return pulumi.get(self, "runtime_environment_secrets")

    @runtime_environment_secrets.setter
    def runtime_environment_secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceKeyValuePairArgs']]]]):
        pulumi.set(self, "runtime_environment_secrets", value)

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
class ServiceIngressConfigurationArgs:
    def __init__(__self__, *,
                 is_publicly_accessible: pulumi.Input[bool]):
        """
        Network ingress configuration
        :param pulumi.Input[bool] is_publicly_accessible: It's set to true if the Apprunner service is publicly accessible. It's set to false otherwise.
        """
        pulumi.set(__self__, "is_publicly_accessible", is_publicly_accessible)

    @property
    @pulumi.getter(name="isPubliclyAccessible")
    def is_publicly_accessible(self) -> pulumi.Input[bool]:
        """
        It's set to true if the Apprunner service is publicly accessible. It's set to false otherwise.
        """
        return pulumi.get(self, "is_publicly_accessible")

    @is_publicly_accessible.setter
    def is_publicly_accessible(self, value: pulumi.Input[bool]):
        pulumi.set(self, "is_publicly_accessible", value)


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
class ServiceNetworkConfigurationArgs:
    def __init__(__self__, *,
                 egress_configuration: Optional[pulumi.Input['ServiceEgressConfigurationArgs']] = None,
                 ingress_configuration: Optional[pulumi.Input['ServiceIngressConfigurationArgs']] = None):
        """
        Network configuration
        """
        if egress_configuration is not None:
            pulumi.set(__self__, "egress_configuration", egress_configuration)
        if ingress_configuration is not None:
            pulumi.set(__self__, "ingress_configuration", ingress_configuration)

    @property
    @pulumi.getter(name="egressConfiguration")
    def egress_configuration(self) -> Optional[pulumi.Input['ServiceEgressConfigurationArgs']]:
        return pulumi.get(self, "egress_configuration")

    @egress_configuration.setter
    def egress_configuration(self, value: Optional[pulumi.Input['ServiceEgressConfigurationArgs']]):
        pulumi.set(self, "egress_configuration", value)

    @property
    @pulumi.getter(name="ingressConfiguration")
    def ingress_configuration(self) -> Optional[pulumi.Input['ServiceIngressConfigurationArgs']]:
        return pulumi.get(self, "ingress_configuration")

    @ingress_configuration.setter
    def ingress_configuration(self, value: Optional[pulumi.Input['ServiceIngressConfigurationArgs']]):
        pulumi.set(self, "ingress_configuration", value)


@pulumi.input_type
class ServiceObservabilityConfigurationArgs:
    def __init__(__self__, *,
                 observability_enabled: pulumi.Input[bool],
                 observability_configuration_arn: Optional[pulumi.Input[str]] = None):
        """
        Service observability configuration
        :param pulumi.Input[bool] observability_enabled: Observability enabled
        :param pulumi.Input[str] observability_configuration_arn: The Amazon Resource Name (ARN) of the App Runner ObservabilityConfiguration.
        """
        pulumi.set(__self__, "observability_enabled", observability_enabled)
        if observability_configuration_arn is not None:
            pulumi.set(__self__, "observability_configuration_arn", observability_configuration_arn)

    @property
    @pulumi.getter(name="observabilityEnabled")
    def observability_enabled(self) -> pulumi.Input[bool]:
        """
        Observability enabled
        """
        return pulumi.get(self, "observability_enabled")

    @observability_enabled.setter
    def observability_enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "observability_enabled", value)

    @property
    @pulumi.getter(name="observabilityConfigurationArn")
    def observability_configuration_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the App Runner ObservabilityConfiguration.
        """
        return pulumi.get(self, "observability_configuration_arn")

    @observability_configuration_arn.setter
    def observability_configuration_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "observability_configuration_arn", value)


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


@pulumi.input_type
class VpcConnectorTagArgs:
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


@pulumi.input_type
class VpcIngressConnectionIngressVpcConfigurationArgs:
    def __init__(__self__, *,
                 vpc_endpoint_id: pulumi.Input[str],
                 vpc_id: pulumi.Input[str]):
        """
        The configuration of customer’s VPC and related VPC endpoint
        :param pulumi.Input[str] vpc_endpoint_id: The ID of the VPC endpoint that your App Runner service connects to.
        :param pulumi.Input[str] vpc_id: The ID of the VPC that the VPC endpoint is used in.
        """
        pulumi.set(__self__, "vpc_endpoint_id", vpc_endpoint_id)
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> pulumi.Input[str]:
        """
        The ID of the VPC endpoint that your App Runner service connects to.
        """
        return pulumi.get(self, "vpc_endpoint_id")

    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_endpoint_id", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        """
        The ID of the VPC that the VPC endpoint is used in.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)


@pulumi.input_type
class VpcIngressConnectionTagArgs:
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


