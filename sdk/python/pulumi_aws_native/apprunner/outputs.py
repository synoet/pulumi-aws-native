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

__all__ = [
    'ServiceAuthenticationConfiguration',
    'ServiceCodeConfiguration',
    'ServiceCodeConfigurationValues',
    'ServiceCodeRepository',
    'ServiceEncryptionConfiguration',
    'ServiceHealthCheckConfiguration',
    'ServiceImageConfiguration',
    'ServiceImageRepository',
    'ServiceInstanceConfiguration',
    'ServiceKeyValuePair',
    'ServiceSourceCodeVersion',
    'ServiceSourceConfiguration',
    'ServiceTag',
    'VpcConnectorTag',
]

@pulumi.output_type
class ServiceAuthenticationConfiguration(dict):
    """
    Authentication Configuration
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "accessRoleArn":
            suggest = "access_role_arn"
        elif key == "connectionArn":
            suggest = "connection_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceAuthenticationConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceAuthenticationConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceAuthenticationConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 access_role_arn: Optional[str] = None,
                 connection_arn: Optional[str] = None):
        """
        Authentication Configuration
        :param str access_role_arn: Access Role Arn
        :param str connection_arn: Connection Arn
        """
        if access_role_arn is not None:
            pulumi.set(__self__, "access_role_arn", access_role_arn)
        if connection_arn is not None:
            pulumi.set(__self__, "connection_arn", connection_arn)

    @property
    @pulumi.getter(name="accessRoleArn")
    def access_role_arn(self) -> Optional[str]:
        """
        Access Role Arn
        """
        return pulumi.get(self, "access_role_arn")

    @property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> Optional[str]:
        """
        Connection Arn
        """
        return pulumi.get(self, "connection_arn")


@pulumi.output_type
class ServiceCodeConfiguration(dict):
    """
    Code Configuration
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "configurationSource":
            suggest = "configuration_source"
        elif key == "codeConfigurationValues":
            suggest = "code_configuration_values"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceCodeConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceCodeConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceCodeConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 configuration_source: 'ServiceCodeConfigurationConfigurationSource',
                 code_configuration_values: Optional['outputs.ServiceCodeConfigurationValues'] = None):
        """
        Code Configuration
        :param 'ServiceCodeConfigurationConfigurationSource' configuration_source: Configuration Source
        """
        pulumi.set(__self__, "configuration_source", configuration_source)
        if code_configuration_values is not None:
            pulumi.set(__self__, "code_configuration_values", code_configuration_values)

    @property
    @pulumi.getter(name="configurationSource")
    def configuration_source(self) -> 'ServiceCodeConfigurationConfigurationSource':
        """
        Configuration Source
        """
        return pulumi.get(self, "configuration_source")

    @property
    @pulumi.getter(name="codeConfigurationValues")
    def code_configuration_values(self) -> Optional['outputs.ServiceCodeConfigurationValues']:
        return pulumi.get(self, "code_configuration_values")


@pulumi.output_type
class ServiceCodeConfigurationValues(dict):
    """
    Code Configuration Values
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "buildCommand":
            suggest = "build_command"
        elif key == "runtimeEnvironmentVariables":
            suggest = "runtime_environment_variables"
        elif key == "startCommand":
            suggest = "start_command"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceCodeConfigurationValues. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceCodeConfigurationValues.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceCodeConfigurationValues.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 runtime: 'ServiceCodeConfigurationValuesRuntime',
                 build_command: Optional[str] = None,
                 port: Optional[str] = None,
                 runtime_environment_variables: Optional[Sequence['outputs.ServiceKeyValuePair']] = None,
                 start_command: Optional[str] = None):
        """
        Code Configuration Values
        :param 'ServiceCodeConfigurationValuesRuntime' runtime: Runtime
        :param str build_command: Build Command
        :param str port: Port
        :param str start_command: Start Command
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
    def runtime(self) -> 'ServiceCodeConfigurationValuesRuntime':
        """
        Runtime
        """
        return pulumi.get(self, "runtime")

    @property
    @pulumi.getter(name="buildCommand")
    def build_command(self) -> Optional[str]:
        """
        Build Command
        """
        return pulumi.get(self, "build_command")

    @property
    @pulumi.getter
    def port(self) -> Optional[str]:
        """
        Port
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="runtimeEnvironmentVariables")
    def runtime_environment_variables(self) -> Optional[Sequence['outputs.ServiceKeyValuePair']]:
        return pulumi.get(self, "runtime_environment_variables")

    @property
    @pulumi.getter(name="startCommand")
    def start_command(self) -> Optional[str]:
        """
        Start Command
        """
        return pulumi.get(self, "start_command")


@pulumi.output_type
class ServiceCodeRepository(dict):
    """
    Source Code Repository
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "repositoryUrl":
            suggest = "repository_url"
        elif key == "sourceCodeVersion":
            suggest = "source_code_version"
        elif key == "codeConfiguration":
            suggest = "code_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceCodeRepository. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceCodeRepository.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceCodeRepository.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 repository_url: str,
                 source_code_version: 'outputs.ServiceSourceCodeVersion',
                 code_configuration: Optional['outputs.ServiceCodeConfiguration'] = None):
        """
        Source Code Repository
        :param str repository_url: Repository Url
        """
        pulumi.set(__self__, "repository_url", repository_url)
        pulumi.set(__self__, "source_code_version", source_code_version)
        if code_configuration is not None:
            pulumi.set(__self__, "code_configuration", code_configuration)

    @property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> str:
        """
        Repository Url
        """
        return pulumi.get(self, "repository_url")

    @property
    @pulumi.getter(name="sourceCodeVersion")
    def source_code_version(self) -> 'outputs.ServiceSourceCodeVersion':
        return pulumi.get(self, "source_code_version")

    @property
    @pulumi.getter(name="codeConfiguration")
    def code_configuration(self) -> Optional['outputs.ServiceCodeConfiguration']:
        return pulumi.get(self, "code_configuration")


@pulumi.output_type
class ServiceEncryptionConfiguration(dict):
    """
    Encryption configuration (KMS key)
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kmsKey":
            suggest = "kms_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceEncryptionConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceEncryptionConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceEncryptionConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kms_key: str):
        """
        Encryption configuration (KMS key)
        :param str kms_key: The KMS Key
        """
        pulumi.set(__self__, "kms_key", kms_key)

    @property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> str:
        """
        The KMS Key
        """
        return pulumi.get(self, "kms_key")


@pulumi.output_type
class ServiceHealthCheckConfiguration(dict):
    """
    Health check configuration
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "healthyThreshold":
            suggest = "healthy_threshold"
        elif key == "unhealthyThreshold":
            suggest = "unhealthy_threshold"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceHealthCheckConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceHealthCheckConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceHealthCheckConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 healthy_threshold: Optional[int] = None,
                 interval: Optional[int] = None,
                 path: Optional[str] = None,
                 protocol: Optional['ServiceHealthCheckConfigurationProtocol'] = None,
                 timeout: Optional[int] = None,
                 unhealthy_threshold: Optional[int] = None):
        """
        Health check configuration
        :param int healthy_threshold: Health check Healthy Threshold
        :param int interval: Health check Interval
        :param str path: Health check Path
        :param 'ServiceHealthCheckConfigurationProtocol' protocol: Health Check Protocol
        :param int timeout: Health check Timeout
        :param int unhealthy_threshold: Health check Unhealthy Threshold
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
    def healthy_threshold(self) -> Optional[int]:
        """
        Health check Healthy Threshold
        """
        return pulumi.get(self, "healthy_threshold")

    @property
    @pulumi.getter
    def interval(self) -> Optional[int]:
        """
        Health check Interval
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        """
        Health check Path
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def protocol(self) -> Optional['ServiceHealthCheckConfigurationProtocol']:
        """
        Health Check Protocol
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def timeout(self) -> Optional[int]:
        """
        Health check Timeout
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> Optional[int]:
        """
        Health check Unhealthy Threshold
        """
        return pulumi.get(self, "unhealthy_threshold")


@pulumi.output_type
class ServiceImageConfiguration(dict):
    """
    Image Configuration
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "runtimeEnvironmentVariables":
            suggest = "runtime_environment_variables"
        elif key == "startCommand":
            suggest = "start_command"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceImageConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceImageConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceImageConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 port: Optional[str] = None,
                 runtime_environment_variables: Optional[Sequence['outputs.ServiceKeyValuePair']] = None,
                 start_command: Optional[str] = None):
        """
        Image Configuration
        :param str port: Port
        :param str start_command: Start Command
        """
        if port is not None:
            pulumi.set(__self__, "port", port)
        if runtime_environment_variables is not None:
            pulumi.set(__self__, "runtime_environment_variables", runtime_environment_variables)
        if start_command is not None:
            pulumi.set(__self__, "start_command", start_command)

    @property
    @pulumi.getter
    def port(self) -> Optional[str]:
        """
        Port
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="runtimeEnvironmentVariables")
    def runtime_environment_variables(self) -> Optional[Sequence['outputs.ServiceKeyValuePair']]:
        return pulumi.get(self, "runtime_environment_variables")

    @property
    @pulumi.getter(name="startCommand")
    def start_command(self) -> Optional[str]:
        """
        Start Command
        """
        return pulumi.get(self, "start_command")


@pulumi.output_type
class ServiceImageRepository(dict):
    """
    Image Repository
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "imageIdentifier":
            suggest = "image_identifier"
        elif key == "imageRepositoryType":
            suggest = "image_repository_type"
        elif key == "imageConfiguration":
            suggest = "image_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceImageRepository. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceImageRepository.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceImageRepository.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 image_identifier: str,
                 image_repository_type: 'ServiceImageRepositoryImageRepositoryType',
                 image_configuration: Optional['outputs.ServiceImageConfiguration'] = None):
        """
        Image Repository
        :param str image_identifier: Image Identifier
        :param 'ServiceImageRepositoryImageRepositoryType' image_repository_type: Image Repository Type
        """
        pulumi.set(__self__, "image_identifier", image_identifier)
        pulumi.set(__self__, "image_repository_type", image_repository_type)
        if image_configuration is not None:
            pulumi.set(__self__, "image_configuration", image_configuration)

    @property
    @pulumi.getter(name="imageIdentifier")
    def image_identifier(self) -> str:
        """
        Image Identifier
        """
        return pulumi.get(self, "image_identifier")

    @property
    @pulumi.getter(name="imageRepositoryType")
    def image_repository_type(self) -> 'ServiceImageRepositoryImageRepositoryType':
        """
        Image Repository Type
        """
        return pulumi.get(self, "image_repository_type")

    @property
    @pulumi.getter(name="imageConfiguration")
    def image_configuration(self) -> Optional['outputs.ServiceImageConfiguration']:
        return pulumi.get(self, "image_configuration")


@pulumi.output_type
class ServiceInstanceConfiguration(dict):
    """
    Instance Configuration
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "instanceRoleArn":
            suggest = "instance_role_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceInstanceConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceInstanceConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceInstanceConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cpu: Optional[str] = None,
                 instance_role_arn: Optional[str] = None,
                 memory: Optional[str] = None):
        """
        Instance Configuration
        :param str cpu: CPU
        :param str instance_role_arn: Instance Role Arn
        :param str memory: Memory
        """
        if cpu is not None:
            pulumi.set(__self__, "cpu", cpu)
        if instance_role_arn is not None:
            pulumi.set(__self__, "instance_role_arn", instance_role_arn)
        if memory is not None:
            pulumi.set(__self__, "memory", memory)

    @property
    @pulumi.getter
    def cpu(self) -> Optional[str]:
        """
        CPU
        """
        return pulumi.get(self, "cpu")

    @property
    @pulumi.getter(name="instanceRoleArn")
    def instance_role_arn(self) -> Optional[str]:
        """
        Instance Role Arn
        """
        return pulumi.get(self, "instance_role_arn")

    @property
    @pulumi.getter
    def memory(self) -> Optional[str]:
        """
        Memory
        """
        return pulumi.get(self, "memory")


@pulumi.output_type
class ServiceKeyValuePair(dict):
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 value: Optional[str] = None):
        if name is not None:
            pulumi.set(__self__, "name", name)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


@pulumi.output_type
class ServiceSourceCodeVersion(dict):
    """
    Source Code Version
    """
    def __init__(__self__, *,
                 type: 'ServiceSourceCodeVersionType',
                 value: str):
        """
        Source Code Version
        :param 'ServiceSourceCodeVersionType' type: Source Code Version Type
        :param str value: Source Code Version Value
        """
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> 'ServiceSourceCodeVersionType':
        """
        Source Code Version Type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Source Code Version Value
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class ServiceSourceConfiguration(dict):
    """
    Source Code configuration
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "authenticationConfiguration":
            suggest = "authentication_configuration"
        elif key == "autoDeploymentsEnabled":
            suggest = "auto_deployments_enabled"
        elif key == "codeRepository":
            suggest = "code_repository"
        elif key == "imageRepository":
            suggest = "image_repository"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceSourceConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceSourceConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceSourceConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 authentication_configuration: Optional['outputs.ServiceAuthenticationConfiguration'] = None,
                 auto_deployments_enabled: Optional[bool] = None,
                 code_repository: Optional['outputs.ServiceCodeRepository'] = None,
                 image_repository: Optional['outputs.ServiceImageRepository'] = None):
        """
        Source Code configuration
        :param bool auto_deployments_enabled: Auto Deployment enabled
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
    def authentication_configuration(self) -> Optional['outputs.ServiceAuthenticationConfiguration']:
        return pulumi.get(self, "authentication_configuration")

    @property
    @pulumi.getter(name="autoDeploymentsEnabled")
    def auto_deployments_enabled(self) -> Optional[bool]:
        """
        Auto Deployment enabled
        """
        return pulumi.get(self, "auto_deployments_enabled")

    @property
    @pulumi.getter(name="codeRepository")
    def code_repository(self) -> Optional['outputs.ServiceCodeRepository']:
        return pulumi.get(self, "code_repository")

    @property
    @pulumi.getter(name="imageRepository")
    def image_repository(self) -> Optional['outputs.ServiceImageRepository']:
        return pulumi.get(self, "image_repository")


@pulumi.output_type
class ServiceTag(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 value: Optional[str] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


@pulumi.output_type
class VpcConnectorTag(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 value: Optional[str] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


