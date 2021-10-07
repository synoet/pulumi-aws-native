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
    'AliasProvisionedConcurrencyConfiguration',
    'AliasRoutingConfiguration',
    'AliasVersionWeight',
    'CodeSigningConfigAllowedPublishers',
    'CodeSigningConfigCodeSigningPolicies',
    'EventInvokeConfigDestinationConfig',
    'EventInvokeConfigOnFailure',
    'EventInvokeConfigOnSuccess',
    'EventSourceMappingDestinationConfig',
    'EventSourceMappingEndpoints',
    'EventSourceMappingOnFailure',
    'EventSourceMappingSelfManagedEventSource',
    'EventSourceMappingSourceAccessConfiguration',
    'FunctionCode',
    'FunctionDeadLetterConfig',
    'FunctionEnvironment',
    'FunctionFileSystemConfig',
    'FunctionImageConfig',
    'FunctionTag',
    'FunctionTracingConfig',
    'FunctionVpcConfig',
    'LayerVersionContent',
    'VersionProvisionedConcurrencyConfiguration',
]

@pulumi.output_type
class AliasProvisionedConcurrencyConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "provisionedConcurrentExecutions":
            suggest = "provisioned_concurrent_executions"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AliasProvisionedConcurrencyConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AliasProvisionedConcurrencyConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AliasProvisionedConcurrencyConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 provisioned_concurrent_executions: int):
        pulumi.set(__self__, "provisioned_concurrent_executions", provisioned_concurrent_executions)

    @property
    @pulumi.getter(name="provisionedConcurrentExecutions")
    def provisioned_concurrent_executions(self) -> int:
        return pulumi.get(self, "provisioned_concurrent_executions")


@pulumi.output_type
class AliasRoutingConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "additionalVersionWeights":
            suggest = "additional_version_weights"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AliasRoutingConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AliasRoutingConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AliasRoutingConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 additional_version_weights: Sequence['outputs.AliasVersionWeight']):
        pulumi.set(__self__, "additional_version_weights", additional_version_weights)

    @property
    @pulumi.getter(name="additionalVersionWeights")
    def additional_version_weights(self) -> Sequence['outputs.AliasVersionWeight']:
        return pulumi.get(self, "additional_version_weights")


@pulumi.output_type
class AliasVersionWeight(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "functionVersion":
            suggest = "function_version"
        elif key == "functionWeight":
            suggest = "function_weight"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AliasVersionWeight. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AliasVersionWeight.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AliasVersionWeight.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 function_version: str,
                 function_weight: float):
        pulumi.set(__self__, "function_version", function_version)
        pulumi.set(__self__, "function_weight", function_weight)

    @property
    @pulumi.getter(name="functionVersion")
    def function_version(self) -> str:
        return pulumi.get(self, "function_version")

    @property
    @pulumi.getter(name="functionWeight")
    def function_weight(self) -> float:
        return pulumi.get(self, "function_weight")


@pulumi.output_type
class CodeSigningConfigAllowedPublishers(dict):
    """
    When the CodeSigningConfig is later on attached to a function, the function code will be expected to be signed by profiles from this list
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "signingProfileVersionArns":
            suggest = "signing_profile_version_arns"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CodeSigningConfigAllowedPublishers. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CodeSigningConfigAllowedPublishers.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CodeSigningConfigAllowedPublishers.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 signing_profile_version_arns: Sequence[str]):
        """
        When the CodeSigningConfig is later on attached to a function, the function code will be expected to be signed by profiles from this list
        :param Sequence[str] signing_profile_version_arns: List of Signing profile version Arns
        """
        pulumi.set(__self__, "signing_profile_version_arns", signing_profile_version_arns)

    @property
    @pulumi.getter(name="signingProfileVersionArns")
    def signing_profile_version_arns(self) -> Sequence[str]:
        """
        List of Signing profile version Arns
        """
        return pulumi.get(self, "signing_profile_version_arns")


@pulumi.output_type
class CodeSigningConfigCodeSigningPolicies(dict):
    """
    Policies to control how to act if a signature is invalid
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "untrustedArtifactOnDeployment":
            suggest = "untrusted_artifact_on_deployment"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CodeSigningConfigCodeSigningPolicies. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CodeSigningConfigCodeSigningPolicies.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CodeSigningConfigCodeSigningPolicies.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 untrusted_artifact_on_deployment: 'CodeSigningConfigCodeSigningPoliciesUntrustedArtifactOnDeployment'):
        """
        Policies to control how to act if a signature is invalid
        :param 'CodeSigningConfigCodeSigningPoliciesUntrustedArtifactOnDeployment' untrusted_artifact_on_deployment: Indicates how Lambda operations involve updating the code artifact will operate. Default to Warn if not provided
        """
        pulumi.set(__self__, "untrusted_artifact_on_deployment", untrusted_artifact_on_deployment)

    @property
    @pulumi.getter(name="untrustedArtifactOnDeployment")
    def untrusted_artifact_on_deployment(self) -> 'CodeSigningConfigCodeSigningPoliciesUntrustedArtifactOnDeployment':
        """
        Indicates how Lambda operations involve updating the code artifact will operate. Default to Warn if not provided
        """
        return pulumi.get(self, "untrusted_artifact_on_deployment")


@pulumi.output_type
class EventInvokeConfigDestinationConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "onFailure":
            suggest = "on_failure"
        elif key == "onSuccess":
            suggest = "on_success"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EventInvokeConfigDestinationConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EventInvokeConfigDestinationConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EventInvokeConfigDestinationConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 on_failure: Optional['outputs.EventInvokeConfigOnFailure'] = None,
                 on_success: Optional['outputs.EventInvokeConfigOnSuccess'] = None):
        if on_failure is not None:
            pulumi.set(__self__, "on_failure", on_failure)
        if on_success is not None:
            pulumi.set(__self__, "on_success", on_success)

    @property
    @pulumi.getter(name="onFailure")
    def on_failure(self) -> Optional['outputs.EventInvokeConfigOnFailure']:
        return pulumi.get(self, "on_failure")

    @property
    @pulumi.getter(name="onSuccess")
    def on_success(self) -> Optional['outputs.EventInvokeConfigOnSuccess']:
        return pulumi.get(self, "on_success")


@pulumi.output_type
class EventInvokeConfigOnFailure(dict):
    def __init__(__self__, *,
                 destination: str):
        pulumi.set(__self__, "destination", destination)

    @property
    @pulumi.getter
    def destination(self) -> str:
        return pulumi.get(self, "destination")


@pulumi.output_type
class EventInvokeConfigOnSuccess(dict):
    def __init__(__self__, *,
                 destination: str):
        pulumi.set(__self__, "destination", destination)

    @property
    @pulumi.getter
    def destination(self) -> str:
        return pulumi.get(self, "destination")


@pulumi.output_type
class EventSourceMappingDestinationConfig(dict):
    """
    (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "onFailure":
            suggest = "on_failure"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EventSourceMappingDestinationConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EventSourceMappingDestinationConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EventSourceMappingDestinationConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 on_failure: Optional['outputs.EventSourceMappingOnFailure'] = None):
        """
        (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.
        :param 'EventSourceMappingOnFailure' on_failure: The destination configuration for failed invocations.
        """
        if on_failure is not None:
            pulumi.set(__self__, "on_failure", on_failure)

    @property
    @pulumi.getter(name="onFailure")
    def on_failure(self) -> Optional['outputs.EventSourceMappingOnFailure']:
        """
        The destination configuration for failed invocations.
        """
        return pulumi.get(self, "on_failure")


@pulumi.output_type
class EventSourceMappingEndpoints(dict):
    """
    The endpoints used by AWS Lambda to access a self-managed event source.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kafkaBootstrapServers":
            suggest = "kafka_bootstrap_servers"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EventSourceMappingEndpoints. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EventSourceMappingEndpoints.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EventSourceMappingEndpoints.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kafka_bootstrap_servers: Optional[Sequence[str]] = None):
        """
        The endpoints used by AWS Lambda to access a self-managed event source.
        :param Sequence[str] kafka_bootstrap_servers: A list of Kafka server endpoints.
        """
        if kafka_bootstrap_servers is not None:
            pulumi.set(__self__, "kafka_bootstrap_servers", kafka_bootstrap_servers)

    @property
    @pulumi.getter(name="kafkaBootstrapServers")
    def kafka_bootstrap_servers(self) -> Optional[Sequence[str]]:
        """
        A list of Kafka server endpoints.
        """
        return pulumi.get(self, "kafka_bootstrap_servers")


@pulumi.output_type
class EventSourceMappingOnFailure(dict):
    """
    A destination for events that failed processing.
    """
    def __init__(__self__, *,
                 destination: Optional[str] = None):
        """
        A destination for events that failed processing.
        :param str destination: The Amazon Resource Name (ARN) of the destination resource.
        """
        if destination is not None:
            pulumi.set(__self__, "destination", destination)

    @property
    @pulumi.getter
    def destination(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the destination resource.
        """
        return pulumi.get(self, "destination")


@pulumi.output_type
class EventSourceMappingSelfManagedEventSource(dict):
    """
    The configuration used by AWS Lambda to access a self-managed event source.
    """
    def __init__(__self__, *,
                 endpoints: Optional['outputs.EventSourceMappingEndpoints'] = None):
        """
        The configuration used by AWS Lambda to access a self-managed event source.
        :param 'EventSourceMappingEndpoints' endpoints: The endpoints for a self-managed event source.
        """
        if endpoints is not None:
            pulumi.set(__self__, "endpoints", endpoints)

    @property
    @pulumi.getter
    def endpoints(self) -> Optional['outputs.EventSourceMappingEndpoints']:
        """
        The endpoints for a self-managed event source.
        """
        return pulumi.get(self, "endpoints")


@pulumi.output_type
class EventSourceMappingSourceAccessConfiguration(dict):
    """
    The configuration used by AWS Lambda to access event source
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "uRI":
            suggest = "u_ri"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EventSourceMappingSourceAccessConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EventSourceMappingSourceAccessConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EventSourceMappingSourceAccessConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: Optional['EventSourceMappingSourceAccessConfigurationType'] = None,
                 u_ri: Optional[str] = None):
        """
        The configuration used by AWS Lambda to access event source
        :param 'EventSourceMappingSourceAccessConfigurationType' type: The type of source access configuration.
        :param str u_ri: The URI for the source access configuration resource.
        """
        if type is not None:
            pulumi.set(__self__, "type", type)
        if u_ri is not None:
            pulumi.set(__self__, "u_ri", u_ri)

    @property
    @pulumi.getter
    def type(self) -> Optional['EventSourceMappingSourceAccessConfigurationType']:
        """
        The type of source access configuration.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uRI")
    def u_ri(self) -> Optional[str]:
        """
        The URI for the source access configuration resource.
        """
        return pulumi.get(self, "u_ri")


@pulumi.output_type
class FunctionCode(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "imageUri":
            suggest = "image_uri"
        elif key == "s3Bucket":
            suggest = "s3_bucket"
        elif key == "s3Key":
            suggest = "s3_key"
        elif key == "s3ObjectVersion":
            suggest = "s3_object_version"
        elif key == "zipFile":
            suggest = "zip_file"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FunctionCode. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FunctionCode.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FunctionCode.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 image_uri: Optional[str] = None,
                 s3_bucket: Optional[str] = None,
                 s3_key: Optional[str] = None,
                 s3_object_version: Optional[str] = None,
                 zip_file: Optional[str] = None):
        """
        :param str image_uri: ImageUri.
        :param str s3_bucket: An Amazon S3 bucket in the same AWS Region as your function. The bucket can be in a different AWS account.
        :param str s3_key: The Amazon S3 key of the deployment package.
        :param str s3_object_version: For versioned objects, the version of the deployment package object to use.
        :param str zip_file: The source code of your Lambda function. If you include your function source inline with this parameter, AWS CloudFormation places it in a file named index and zips it to create a deployment package..
        """
        if image_uri is not None:
            pulumi.set(__self__, "image_uri", image_uri)
        if s3_bucket is not None:
            pulumi.set(__self__, "s3_bucket", s3_bucket)
        if s3_key is not None:
            pulumi.set(__self__, "s3_key", s3_key)
        if s3_object_version is not None:
            pulumi.set(__self__, "s3_object_version", s3_object_version)
        if zip_file is not None:
            pulumi.set(__self__, "zip_file", zip_file)

    @property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[str]:
        """
        ImageUri.
        """
        return pulumi.get(self, "image_uri")

    @property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> Optional[str]:
        """
        An Amazon S3 bucket in the same AWS Region as your function. The bucket can be in a different AWS account.
        """
        return pulumi.get(self, "s3_bucket")

    @property
    @pulumi.getter(name="s3Key")
    def s3_key(self) -> Optional[str]:
        """
        The Amazon S3 key of the deployment package.
        """
        return pulumi.get(self, "s3_key")

    @property
    @pulumi.getter(name="s3ObjectVersion")
    def s3_object_version(self) -> Optional[str]:
        """
        For versioned objects, the version of the deployment package object to use.
        """
        return pulumi.get(self, "s3_object_version")

    @property
    @pulumi.getter(name="zipFile")
    def zip_file(self) -> Optional[str]:
        """
        The source code of your Lambda function. If you include your function source inline with this parameter, AWS CloudFormation places it in a file named index and zips it to create a deployment package..
        """
        return pulumi.get(self, "zip_file")


@pulumi.output_type
class FunctionDeadLetterConfig(dict):
    """
    The dead-letter queue for failed asynchronous invocations.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "targetArn":
            suggest = "target_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FunctionDeadLetterConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FunctionDeadLetterConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FunctionDeadLetterConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 target_arn: Optional[str] = None):
        """
        The dead-letter queue for failed asynchronous invocations.
        :param str target_arn: The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
        """
        if target_arn is not None:
            pulumi.set(__self__, "target_arn", target_arn)

    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
        """
        return pulumi.get(self, "target_arn")


@pulumi.output_type
class FunctionEnvironment(dict):
    """
    A function's environment variable settings.
    """
    def __init__(__self__, *,
                 variables: Optional[Any] = None):
        """
        A function's environment variable settings.
        :param Any variables: Environment variable key-value pairs.
        """
        if variables is not None:
            pulumi.set(__self__, "variables", variables)

    @property
    @pulumi.getter
    def variables(self) -> Optional[Any]:
        """
        Environment variable key-value pairs.
        """
        return pulumi.get(self, "variables")


@pulumi.output_type
class FunctionFileSystemConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "localMountPath":
            suggest = "local_mount_path"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FunctionFileSystemConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FunctionFileSystemConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FunctionFileSystemConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 arn: str,
                 local_mount_path: str):
        """
        :param str arn: The Amazon Resource Name (ARN) of the Amazon EFS access point that provides access to the file system.
        :param str local_mount_path: The path where the function can access the file system, starting with /mnt/.
        """
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "local_mount_path", local_mount_path)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the Amazon EFS access point that provides access to the file system.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="localMountPath")
    def local_mount_path(self) -> str:
        """
        The path where the function can access the file system, starting with /mnt/.
        """
        return pulumi.get(self, "local_mount_path")


@pulumi.output_type
class FunctionImageConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "entryPoint":
            suggest = "entry_point"
        elif key == "workingDirectory":
            suggest = "working_directory"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FunctionImageConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FunctionImageConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FunctionImageConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 command: Optional[Sequence[str]] = None,
                 entry_point: Optional[Sequence[str]] = None,
                 working_directory: Optional[str] = None):
        """
        :param Sequence[str] command: Command.
        :param Sequence[str] entry_point: EntryPoint.
        :param str working_directory: WorkingDirectory.
        """
        if command is not None:
            pulumi.set(__self__, "command", command)
        if entry_point is not None:
            pulumi.set(__self__, "entry_point", entry_point)
        if working_directory is not None:
            pulumi.set(__self__, "working_directory", working_directory)

    @property
    @pulumi.getter
    def command(self) -> Optional[Sequence[str]]:
        """
        Command.
        """
        return pulumi.get(self, "command")

    @property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> Optional[Sequence[str]]:
        """
        EntryPoint.
        """
        return pulumi.get(self, "entry_point")

    @property
    @pulumi.getter(name="workingDirectory")
    def working_directory(self) -> Optional[str]:
        """
        WorkingDirectory.
        """
        return pulumi.get(self, "working_directory")


@pulumi.output_type
class FunctionTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: Optional[str] = None):
        """
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param str value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class FunctionTracingConfig(dict):
    """
    The function's AWS X-Ray tracing configuration. To sample and record incoming requests, set Mode to Active.
    """
    def __init__(__self__, *,
                 mode: Optional['FunctionTracingConfigMode'] = None):
        """
        The function's AWS X-Ray tracing configuration. To sample and record incoming requests, set Mode to Active.
        :param 'FunctionTracingConfigMode' mode: The tracing mode.
        """
        if mode is not None:
            pulumi.set(__self__, "mode", mode)

    @property
    @pulumi.getter
    def mode(self) -> Optional['FunctionTracingConfigMode']:
        """
        The tracing mode.
        """
        return pulumi.get(self, "mode")


@pulumi.output_type
class FunctionVpcConfig(dict):
    """
    The VPC security groups and subnets that are attached to a Lambda function. When you connect a function to a VPC, Lambda creates an elastic network interface for each combination of security group and subnet in the function's VPC configuration. The function can only access resources and the internet through that VPC.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "securityGroupIds":
            suggest = "security_group_ids"
        elif key == "subnetIds":
            suggest = "subnet_ids"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FunctionVpcConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FunctionVpcConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FunctionVpcConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 security_group_ids: Optional[Sequence[str]] = None,
                 subnet_ids: Optional[Sequence[str]] = None):
        """
        The VPC security groups and subnets that are attached to a Lambda function. When you connect a function to a VPC, Lambda creates an elastic network interface for each combination of security group and subnet in the function's VPC configuration. The function can only access resources and the internet through that VPC.
        :param Sequence[str] security_group_ids: A list of VPC security groups IDs.
        :param Sequence[str] subnet_ids: A list of VPC subnet IDs.
        """
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[str]]:
        """
        A list of VPC security groups IDs.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[str]]:
        """
        A list of VPC subnet IDs.
        """
        return pulumi.get(self, "subnet_ids")


@pulumi.output_type
class LayerVersionContent(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "s3Bucket":
            suggest = "s3_bucket"
        elif key == "s3Key":
            suggest = "s3_key"
        elif key == "s3ObjectVersion":
            suggest = "s3_object_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LayerVersionContent. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LayerVersionContent.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LayerVersionContent.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 s3_bucket: str,
                 s3_key: str,
                 s3_object_version: Optional[str] = None):
        pulumi.set(__self__, "s3_bucket", s3_bucket)
        pulumi.set(__self__, "s3_key", s3_key)
        if s3_object_version is not None:
            pulumi.set(__self__, "s3_object_version", s3_object_version)

    @property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> str:
        return pulumi.get(self, "s3_bucket")

    @property
    @pulumi.getter(name="s3Key")
    def s3_key(self) -> str:
        return pulumi.get(self, "s3_key")

    @property
    @pulumi.getter(name="s3ObjectVersion")
    def s3_object_version(self) -> Optional[str]:
        return pulumi.get(self, "s3_object_version")


@pulumi.output_type
class VersionProvisionedConcurrencyConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "provisionedConcurrentExecutions":
            suggest = "provisioned_concurrent_executions"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VersionProvisionedConcurrencyConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VersionProvisionedConcurrencyConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VersionProvisionedConcurrencyConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 provisioned_concurrent_executions: int):
        pulumi.set(__self__, "provisioned_concurrent_executions", provisioned_concurrent_executions)

    @property
    @pulumi.getter(name="provisionedConcurrentExecutions")
    def provisioned_concurrent_executions(self) -> int:
        return pulumi.get(self, "provisioned_concurrent_executions")


