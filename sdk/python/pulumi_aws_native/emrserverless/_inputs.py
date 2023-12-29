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
    'ApplicationAutoStartConfigurationArgs',
    'ApplicationAutoStopConfigurationArgs',
    'ApplicationCloudWatchLoggingConfigurationArgs',
    'ApplicationConfigurationObjectArgs',
    'ApplicationImageConfigurationInputArgs',
    'ApplicationInitialCapacityConfigKeyValuePairArgs',
    'ApplicationInitialCapacityConfigArgs',
    'ApplicationLogTypeMapKeyValuePairArgs',
    'ApplicationManagedPersistenceMonitoringConfigurationArgs',
    'ApplicationMaximumAllowedResourcesArgs',
    'ApplicationMonitoringConfigurationArgs',
    'ApplicationNetworkConfigurationArgs',
    'ApplicationS3MonitoringConfigurationArgs',
    'ApplicationTagArgs',
    'ApplicationWorkerConfigurationArgs',
    'ApplicationWorkerTypeSpecificationInputMapArgs',
]

@pulumi.input_type
class ApplicationAutoStartConfigurationArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None):
        """
        Configuration for Auto Start of Application
        :param pulumi.Input[bool] enabled: If set to true, the Application will automatically start. Defaults to true.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to true, the Application will automatically start. Defaults to true.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)


@pulumi.input_type
class ApplicationAutoStopConfigurationArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 idle_timeout_minutes: Optional[pulumi.Input[int]] = None):
        """
        Configuration for Auto Stop of Application
        :param pulumi.Input[bool] enabled: If set to true, the Application will automatically stop after being idle. Defaults to true.
        :param pulumi.Input[int] idle_timeout_minutes: The amount of time [in minutes] to wait before auto stopping the Application when idle. Defaults to 15 minutes.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if idle_timeout_minutes is not None:
            pulumi.set(__self__, "idle_timeout_minutes", idle_timeout_minutes)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to true, the Application will automatically stop after being idle. Defaults to true.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="idleTimeoutMinutes")
    def idle_timeout_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        The amount of time [in minutes] to wait before auto stopping the Application when idle. Defaults to 15 minutes.
        """
        return pulumi.get(self, "idle_timeout_minutes")

    @idle_timeout_minutes.setter
    def idle_timeout_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "idle_timeout_minutes", value)


@pulumi.input_type
class ApplicationCloudWatchLoggingConfigurationArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 encryption_key_arn: Optional[pulumi.Input[str]] = None,
                 log_group_name: Optional[pulumi.Input[str]] = None,
                 log_stream_name_prefix: Optional[pulumi.Input[str]] = None,
                 log_type_map: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationLogTypeMapKeyValuePairArgs']]]] = None):
        """
        :param pulumi.Input[bool] enabled: If set to false, CloudWatch logging will be turned off. Defaults to false.
        :param pulumi.Input[str] encryption_key_arn: KMS key ARN to encrypt the logs stored in given CloudWatch log-group.
        :param pulumi.Input[str] log_group_name: Log-group name to produce log-streams on CloudWatch. If undefined, logs will be produced in a default log-group /aws/emr-serverless
        :param pulumi.Input[str] log_stream_name_prefix: Log-stream name prefix by which log-stream names will start in the CloudWatch Log-group.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationLogTypeMapKeyValuePairArgs']]] log_type_map: The specific log-streams which need to be uploaded to CloudWatch.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if encryption_key_arn is not None:
            pulumi.set(__self__, "encryption_key_arn", encryption_key_arn)
        if log_group_name is not None:
            pulumi.set(__self__, "log_group_name", log_group_name)
        if log_stream_name_prefix is not None:
            pulumi.set(__self__, "log_stream_name_prefix", log_stream_name_prefix)
        if log_type_map is not None:
            pulumi.set(__self__, "log_type_map", log_type_map)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to false, CloudWatch logging will be turned off. Defaults to false.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="encryptionKeyArn")
    def encryption_key_arn(self) -> Optional[pulumi.Input[str]]:
        """
        KMS key ARN to encrypt the logs stored in given CloudWatch log-group.
        """
        return pulumi.get(self, "encryption_key_arn")

    @encryption_key_arn.setter
    def encryption_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_key_arn", value)

    @property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Log-group name to produce log-streams on CloudWatch. If undefined, logs will be produced in a default log-group /aws/emr-serverless
        """
        return pulumi.get(self, "log_group_name")

    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_group_name", value)

    @property
    @pulumi.getter(name="logStreamNamePrefix")
    def log_stream_name_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Log-stream name prefix by which log-stream names will start in the CloudWatch Log-group.
        """
        return pulumi.get(self, "log_stream_name_prefix")

    @log_stream_name_prefix.setter
    def log_stream_name_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_stream_name_prefix", value)

    @property
    @pulumi.getter(name="logTypeMap")
    def log_type_map(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationLogTypeMapKeyValuePairArgs']]]]:
        """
        The specific log-streams which need to be uploaded to CloudWatch.
        """
        return pulumi.get(self, "log_type_map")

    @log_type_map.setter
    def log_type_map(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationLogTypeMapKeyValuePairArgs']]]]):
        pulumi.set(self, "log_type_map", value)


@pulumi.input_type
class ApplicationConfigurationObjectArgs:
    def __init__(__self__, *,
                 classification: pulumi.Input[str],
                 configurations: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationConfigurationObjectArgs']]]] = None,
                 properties: Optional[Any] = None):
        """
        Configuration for a JobRun.
        :param pulumi.Input[str] classification: String with a maximum length of 1024.
        """
        pulumi.set(__self__, "classification", classification)
        if configurations is not None:
            pulumi.set(__self__, "configurations", configurations)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter
    def classification(self) -> pulumi.Input[str]:
        """
        String with a maximum length of 1024.
        """
        return pulumi.get(self, "classification")

    @classification.setter
    def classification(self, value: pulumi.Input[str]):
        pulumi.set(self, "classification", value)

    @property
    @pulumi.getter
    def configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationConfigurationObjectArgs']]]]:
        return pulumi.get(self, "configurations")

    @configurations.setter
    def configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationConfigurationObjectArgs']]]]):
        pulumi.set(self, "configurations", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[Any]:
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[Any]):
        pulumi.set(self, "properties", value)


@pulumi.input_type
class ApplicationImageConfigurationInputArgs:
    def __init__(__self__, *,
                 image_uri: Optional[pulumi.Input[str]] = None):
        """
        The image configuration.
        :param pulumi.Input[str] image_uri: The URI of an image in the Amazon ECR registry. This field is required when you create a new application. If you leave this field blank in an update, Amazon EMR will remove the image configuration.
        """
        if image_uri is not None:
            pulumi.set(__self__, "image_uri", image_uri)

    @property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The URI of an image in the Amazon ECR registry. This field is required when you create a new application. If you leave this field blank in an update, Amazon EMR will remove the image configuration.
        """
        return pulumi.get(self, "image_uri")

    @image_uri.setter
    def image_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_uri", value)


@pulumi.input_type
class ApplicationInitialCapacityConfigKeyValuePairArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input['ApplicationInitialCapacityConfigArgs']):
        """
        :param pulumi.Input[str] key: Worker type for an analytics framework.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Worker type for an analytics framework.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input['ApplicationInitialCapacityConfigArgs']:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input['ApplicationInitialCapacityConfigArgs']):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ApplicationInitialCapacityConfigArgs:
    def __init__(__self__, *,
                 worker_configuration: pulumi.Input['ApplicationWorkerConfigurationArgs'],
                 worker_count: pulumi.Input[int]):
        """
        :param pulumi.Input[int] worker_count: Initial count of workers to be initialized when an Application is started. This count will be continued to be maintained until the Application is stopped
        """
        pulumi.set(__self__, "worker_configuration", worker_configuration)
        pulumi.set(__self__, "worker_count", worker_count)

    @property
    @pulumi.getter(name="workerConfiguration")
    def worker_configuration(self) -> pulumi.Input['ApplicationWorkerConfigurationArgs']:
        return pulumi.get(self, "worker_configuration")

    @worker_configuration.setter
    def worker_configuration(self, value: pulumi.Input['ApplicationWorkerConfigurationArgs']):
        pulumi.set(self, "worker_configuration", value)

    @property
    @pulumi.getter(name="workerCount")
    def worker_count(self) -> pulumi.Input[int]:
        """
        Initial count of workers to be initialized when an Application is started. This count will be continued to be maintained until the Application is stopped
        """
        return pulumi.get(self, "worker_count")

    @worker_count.setter
    def worker_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "worker_count", value)


@pulumi.input_type
class ApplicationLogTypeMapKeyValuePairArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ApplicationManagedPersistenceMonitoringConfigurationArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 encryption_key_arn: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] enabled: If set to false, managed logging will be turned off. Defaults to true.
        :param pulumi.Input[str] encryption_key_arn: KMS key ARN to encrypt the logs stored in managed persistence
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if encryption_key_arn is not None:
            pulumi.set(__self__, "encryption_key_arn", encryption_key_arn)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to false, managed logging will be turned off. Defaults to true.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="encryptionKeyArn")
    def encryption_key_arn(self) -> Optional[pulumi.Input[str]]:
        """
        KMS key ARN to encrypt the logs stored in managed persistence
        """
        return pulumi.get(self, "encryption_key_arn")

    @encryption_key_arn.setter
    def encryption_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_key_arn", value)


@pulumi.input_type
class ApplicationMaximumAllowedResourcesArgs:
    def __init__(__self__, *,
                 cpu: pulumi.Input[str],
                 memory: pulumi.Input[str],
                 disk: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] cpu: Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        :param pulumi.Input[str] memory: Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        :param pulumi.Input[str] disk: Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        """
        pulumi.set(__self__, "cpu", cpu)
        pulumi.set(__self__, "memory", memory)
        if disk is not None:
            pulumi.set(__self__, "disk", disk)

    @property
    @pulumi.getter
    def cpu(self) -> pulumi.Input[str]:
        """
        Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        """
        return pulumi.get(self, "cpu")

    @cpu.setter
    def cpu(self, value: pulumi.Input[str]):
        pulumi.set(self, "cpu", value)

    @property
    @pulumi.getter
    def memory(self) -> pulumi.Input[str]:
        """
        Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        """
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: pulumi.Input[str]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter
    def disk(self) -> Optional[pulumi.Input[str]]:
        """
        Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        """
        return pulumi.get(self, "disk")

    @disk.setter
    def disk(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk", value)


@pulumi.input_type
class ApplicationMonitoringConfigurationArgs:
    def __init__(__self__, *,
                 cloud_watch_logging_configuration: Optional[pulumi.Input['ApplicationCloudWatchLoggingConfigurationArgs']] = None,
                 managed_persistence_monitoring_configuration: Optional[pulumi.Input['ApplicationManagedPersistenceMonitoringConfigurationArgs']] = None,
                 s3_monitoring_configuration: Optional[pulumi.Input['ApplicationS3MonitoringConfigurationArgs']] = None):
        """
        Monitoring configuration for batch and interactive JobRun.
        :param pulumi.Input['ApplicationCloudWatchLoggingConfigurationArgs'] cloud_watch_logging_configuration: CloudWatch logging configurations for a JobRun.
        :param pulumi.Input['ApplicationManagedPersistenceMonitoringConfigurationArgs'] managed_persistence_monitoring_configuration: Managed log persistence configurations for a JobRun.
        :param pulumi.Input['ApplicationS3MonitoringConfigurationArgs'] s3_monitoring_configuration: S3 monitoring configurations for a JobRun.
        """
        if cloud_watch_logging_configuration is not None:
            pulumi.set(__self__, "cloud_watch_logging_configuration", cloud_watch_logging_configuration)
        if managed_persistence_monitoring_configuration is not None:
            pulumi.set(__self__, "managed_persistence_monitoring_configuration", managed_persistence_monitoring_configuration)
        if s3_monitoring_configuration is not None:
            pulumi.set(__self__, "s3_monitoring_configuration", s3_monitoring_configuration)

    @property
    @pulumi.getter(name="cloudWatchLoggingConfiguration")
    def cloud_watch_logging_configuration(self) -> Optional[pulumi.Input['ApplicationCloudWatchLoggingConfigurationArgs']]:
        """
        CloudWatch logging configurations for a JobRun.
        """
        return pulumi.get(self, "cloud_watch_logging_configuration")

    @cloud_watch_logging_configuration.setter
    def cloud_watch_logging_configuration(self, value: Optional[pulumi.Input['ApplicationCloudWatchLoggingConfigurationArgs']]):
        pulumi.set(self, "cloud_watch_logging_configuration", value)

    @property
    @pulumi.getter(name="managedPersistenceMonitoringConfiguration")
    def managed_persistence_monitoring_configuration(self) -> Optional[pulumi.Input['ApplicationManagedPersistenceMonitoringConfigurationArgs']]:
        """
        Managed log persistence configurations for a JobRun.
        """
        return pulumi.get(self, "managed_persistence_monitoring_configuration")

    @managed_persistence_monitoring_configuration.setter
    def managed_persistence_monitoring_configuration(self, value: Optional[pulumi.Input['ApplicationManagedPersistenceMonitoringConfigurationArgs']]):
        pulumi.set(self, "managed_persistence_monitoring_configuration", value)

    @property
    @pulumi.getter(name="s3MonitoringConfiguration")
    def s3_monitoring_configuration(self) -> Optional[pulumi.Input['ApplicationS3MonitoringConfigurationArgs']]:
        """
        S3 monitoring configurations for a JobRun.
        """
        return pulumi.get(self, "s3_monitoring_configuration")

    @s3_monitoring_configuration.setter
    def s3_monitoring_configuration(self, value: Optional[pulumi.Input['ApplicationS3MonitoringConfigurationArgs']]):
        pulumi.set(self, "s3_monitoring_configuration", value)


@pulumi.input_type
class ApplicationNetworkConfigurationArgs:
    def __init__(__self__, *,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: The ID of the security groups in the VPC to which you want to connect your job or application.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: The ID of the subnets in the VPC to which you want to connect your job or application.
        """
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The ID of the security groups in the VPC to which you want to connect your job or application.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The ID of the subnets in the VPC to which you want to connect your job or application.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnet_ids", value)


@pulumi.input_type
class ApplicationS3MonitoringConfigurationArgs:
    def __init__(__self__, *,
                 encryption_key_arn: Optional[pulumi.Input[str]] = None,
                 log_uri: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] encryption_key_arn: KMS key ARN to encrypt the logs stored in given s3
        """
        if encryption_key_arn is not None:
            pulumi.set(__self__, "encryption_key_arn", encryption_key_arn)
        if log_uri is not None:
            pulumi.set(__self__, "log_uri", log_uri)

    @property
    @pulumi.getter(name="encryptionKeyArn")
    def encryption_key_arn(self) -> Optional[pulumi.Input[str]]:
        """
        KMS key ARN to encrypt the logs stored in given s3
        """
        return pulumi.get(self, "encryption_key_arn")

    @encryption_key_arn.setter
    def encryption_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_key_arn", value)

    @property
    @pulumi.getter(name="logUri")
    def log_uri(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "log_uri")

    @log_uri.setter
    def log_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_uri", value)


@pulumi.input_type
class ApplicationTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The value for the tag. You can specify a value that is 1 to 128 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 1 to 128 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ApplicationWorkerConfigurationArgs:
    def __init__(__self__, *,
                 cpu: pulumi.Input[str],
                 memory: pulumi.Input[str],
                 disk: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] cpu: Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        :param pulumi.Input[str] memory: Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        :param pulumi.Input[str] disk: Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        """
        pulumi.set(__self__, "cpu", cpu)
        pulumi.set(__self__, "memory", memory)
        if disk is not None:
            pulumi.set(__self__, "disk", disk)

    @property
    @pulumi.getter
    def cpu(self) -> pulumi.Input[str]:
        """
        Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        """
        return pulumi.get(self, "cpu")

    @cpu.setter
    def cpu(self, value: pulumi.Input[str]):
        pulumi.set(self, "cpu", value)

    @property
    @pulumi.getter
    def memory(self) -> pulumi.Input[str]:
        """
        Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        """
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: pulumi.Input[str]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter
    def disk(self) -> Optional[pulumi.Input[str]]:
        """
        Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        """
        return pulumi.get(self, "disk")

    @disk.setter
    def disk(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk", value)


@pulumi.input_type
class ApplicationWorkerTypeSpecificationInputMapArgs:
    def __init__(__self__):
        pass


