# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'CanaryArtifactConfigArgs',
    'CanaryBaseScreenshotArgs',
    'CanaryCodeArgs',
    'CanaryRunConfigArgs',
    'CanaryS3EncryptionArgs',
    'CanaryScheduleArgs',
    'CanaryTagArgs',
    'CanaryVPCConfigArgs',
    'CanaryVisualReferenceArgs',
    'GroupTagArgs',
]

@pulumi.input_type
class CanaryArtifactConfigArgs:
    def __init__(__self__, *,
                 s3_encryption: Optional[pulumi.Input['CanaryS3EncryptionArgs']] = None):
        """
        :param pulumi.Input['CanaryS3EncryptionArgs'] s3_encryption: Encryption configuration for uploading artifacts to S3
        """
        if s3_encryption is not None:
            pulumi.set(__self__, "s3_encryption", s3_encryption)

    @property
    @pulumi.getter(name="s3Encryption")
    def s3_encryption(self) -> Optional[pulumi.Input['CanaryS3EncryptionArgs']]:
        """
        Encryption configuration for uploading artifacts to S3
        """
        return pulumi.get(self, "s3_encryption")

    @s3_encryption.setter
    def s3_encryption(self, value: Optional[pulumi.Input['CanaryS3EncryptionArgs']]):
        pulumi.set(self, "s3_encryption", value)


@pulumi.input_type
class CanaryBaseScreenshotArgs:
    def __init__(__self__, *,
                 screenshot_name: pulumi.Input[str],
                 ignore_coordinates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] screenshot_name: Name of the screenshot to be used as base reference for visual testing
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ignore_coordinates: List of coordinates of rectangles to be ignored during visual testing
        """
        pulumi.set(__self__, "screenshot_name", screenshot_name)
        if ignore_coordinates is not None:
            pulumi.set(__self__, "ignore_coordinates", ignore_coordinates)

    @property
    @pulumi.getter(name="screenshotName")
    def screenshot_name(self) -> pulumi.Input[str]:
        """
        Name of the screenshot to be used as base reference for visual testing
        """
        return pulumi.get(self, "screenshot_name")

    @screenshot_name.setter
    def screenshot_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "screenshot_name", value)

    @property
    @pulumi.getter(name="ignoreCoordinates")
    def ignore_coordinates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of coordinates of rectangles to be ignored during visual testing
        """
        return pulumi.get(self, "ignore_coordinates")

    @ignore_coordinates.setter
    def ignore_coordinates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ignore_coordinates", value)


@pulumi.input_type
class CanaryCodeArgs:
    def __init__(__self__, *,
                 handler: pulumi.Input[str],
                 s3_bucket: Optional[pulumi.Input[str]] = None,
                 s3_key: Optional[pulumi.Input[str]] = None,
                 s3_object_version: Optional[pulumi.Input[str]] = None,
                 script: Optional[pulumi.Input[str]] = None,
                 source_location_arn: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "handler", handler)
        if s3_bucket is not None:
            pulumi.set(__self__, "s3_bucket", s3_bucket)
        if s3_key is not None:
            pulumi.set(__self__, "s3_key", s3_key)
        if s3_object_version is not None:
            pulumi.set(__self__, "s3_object_version", s3_object_version)
        if script is not None:
            pulumi.set(__self__, "script", script)
        if source_location_arn is not None:
            pulumi.set(__self__, "source_location_arn", source_location_arn)

    @property
    @pulumi.getter
    def handler(self) -> pulumi.Input[str]:
        return pulumi.get(self, "handler")

    @handler.setter
    def handler(self, value: pulumi.Input[str]):
        pulumi.set(self, "handler", value)

    @property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "s3_bucket")

    @s3_bucket.setter
    def s3_bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "s3_bucket", value)

    @property
    @pulumi.getter(name="s3Key")
    def s3_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "s3_key")

    @s3_key.setter
    def s3_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "s3_key", value)

    @property
    @pulumi.getter(name="s3ObjectVersion")
    def s3_object_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "s3_object_version")

    @s3_object_version.setter
    def s3_object_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "s3_object_version", value)

    @property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "script")

    @script.setter
    def script(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "script", value)

    @property
    @pulumi.getter(name="sourceLocationArn")
    def source_location_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_location_arn")

    @source_location_arn.setter
    def source_location_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_location_arn", value)


@pulumi.input_type
class CanaryRunConfigArgs:
    def __init__(__self__, *,
                 active_tracing: Optional[pulumi.Input[bool]] = None,
                 environment_variables: Optional[Any] = None,
                 memory_in_mb: Optional[pulumi.Input[int]] = None,
                 timeout_in_seconds: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[bool] active_tracing: Enable active tracing if set to true
        :param Any environment_variables: Environment variable key-value pairs.
        :param pulumi.Input[int] memory_in_mb: Provide maximum memory available for canary in MB
        :param pulumi.Input[int] timeout_in_seconds: Provide maximum canary timeout per run in seconds
        """
        if active_tracing is not None:
            pulumi.set(__self__, "active_tracing", active_tracing)
        if environment_variables is not None:
            pulumi.set(__self__, "environment_variables", environment_variables)
        if memory_in_mb is not None:
            pulumi.set(__self__, "memory_in_mb", memory_in_mb)
        if timeout_in_seconds is not None:
            pulumi.set(__self__, "timeout_in_seconds", timeout_in_seconds)

    @property
    @pulumi.getter(name="activeTracing")
    def active_tracing(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable active tracing if set to true
        """
        return pulumi.get(self, "active_tracing")

    @active_tracing.setter
    def active_tracing(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active_tracing", value)

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Any]:
        """
        Environment variable key-value pairs.
        """
        return pulumi.get(self, "environment_variables")

    @environment_variables.setter
    def environment_variables(self, value: Optional[Any]):
        pulumi.set(self, "environment_variables", value)

    @property
    @pulumi.getter(name="memoryInMb")
    def memory_in_mb(self) -> Optional[pulumi.Input[int]]:
        """
        Provide maximum memory available for canary in MB
        """
        return pulumi.get(self, "memory_in_mb")

    @memory_in_mb.setter
    def memory_in_mb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "memory_in_mb", value)

    @property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Provide maximum canary timeout per run in seconds
        """
        return pulumi.get(self, "timeout_in_seconds")

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout_in_seconds", value)


@pulumi.input_type
class CanaryS3EncryptionArgs:
    def __init__(__self__, *,
                 encryption_mode: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] encryption_mode: Encryption mode for encrypting artifacts when uploading to S3. Valid values: SSE_S3 and SSE_KMS.
        :param pulumi.Input[str] kms_key_arn: KMS key Arn for encrypting artifacts when uploading to S3. You must specify KMS key Arn for SSE_KMS encryption mode only.
        """
        if encryption_mode is not None:
            pulumi.set(__self__, "encryption_mode", encryption_mode)
        if kms_key_arn is not None:
            pulumi.set(__self__, "kms_key_arn", kms_key_arn)

    @property
    @pulumi.getter(name="encryptionMode")
    def encryption_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Encryption mode for encrypting artifacts when uploading to S3. Valid values: SSE_S3 and SSE_KMS.
        """
        return pulumi.get(self, "encryption_mode")

    @encryption_mode.setter
    def encryption_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_mode", value)

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[str]]:
        """
        KMS key Arn for encrypting artifacts when uploading to S3. You must specify KMS key Arn for SSE_KMS encryption mode only.
        """
        return pulumi.get(self, "kms_key_arn")

    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_arn", value)


@pulumi.input_type
class CanaryScheduleArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 duration_in_seconds: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        if duration_in_seconds is not None:
            pulumi.set(__self__, "duration_in_seconds", duration_in_seconds)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter(name="durationInSeconds")
    def duration_in_seconds(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "duration_in_seconds")

    @duration_in_seconds.setter
    def duration_in_seconds(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "duration_in_seconds", value)


@pulumi.input_type
class CanaryTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class CanaryVPCConfigArgs:
    def __init__(__self__, *,
                 security_group_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 vpc_id: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "security_group_ids", security_group_ids)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


@pulumi.input_type
class CanaryVisualReferenceArgs:
    def __init__(__self__, *,
                 base_canary_run_id: pulumi.Input[str],
                 base_screenshots: Optional[pulumi.Input[Sequence[pulumi.Input['CanaryBaseScreenshotArgs']]]] = None):
        """
        :param pulumi.Input[str] base_canary_run_id: Canary run id to be used as base reference for visual testing
        :param pulumi.Input[Sequence[pulumi.Input['CanaryBaseScreenshotArgs']]] base_screenshots: List of screenshots used as base reference for visual testing
        """
        pulumi.set(__self__, "base_canary_run_id", base_canary_run_id)
        if base_screenshots is not None:
            pulumi.set(__self__, "base_screenshots", base_screenshots)

    @property
    @pulumi.getter(name="baseCanaryRunId")
    def base_canary_run_id(self) -> pulumi.Input[str]:
        """
        Canary run id to be used as base reference for visual testing
        """
        return pulumi.get(self, "base_canary_run_id")

    @base_canary_run_id.setter
    def base_canary_run_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "base_canary_run_id", value)

    @property
    @pulumi.getter(name="baseScreenshots")
    def base_screenshots(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CanaryBaseScreenshotArgs']]]]:
        """
        List of screenshots used as base reference for visual testing
        """
        return pulumi.get(self, "base_screenshots")

    @base_screenshots.setter
    def base_screenshots(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CanaryBaseScreenshotArgs']]]]):
        pulumi.set(self, "base_screenshots", value)


@pulumi.input_type
class GroupTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


