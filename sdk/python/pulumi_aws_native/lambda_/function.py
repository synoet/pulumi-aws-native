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
from ._inputs import *

__all__ = ['FunctionArgs', 'Function']

@pulumi.input_type
class FunctionArgs:
    def __init__(__self__, *,
                 code: pulumi.Input['FunctionCodeArgs'],
                 role: pulumi.Input[str],
                 code_signing_config_arn: Optional[pulumi.Input[str]] = None,
                 dead_letter_config: Optional[pulumi.Input['FunctionDeadLetterConfigArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input['FunctionEnvironmentArgs']] = None,
                 file_system_configs: Optional[pulumi.Input[Sequence[pulumi.Input['FunctionFileSystemConfigArgs']]]] = None,
                 function_name: Optional[pulumi.Input[str]] = None,
                 handler: Optional[pulumi.Input[str]] = None,
                 image_config: Optional[pulumi.Input['FunctionImageConfigArgs']] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 layers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 memory_size: Optional[pulumi.Input[int]] = None,
                 package_type: Optional[pulumi.Input['FunctionPackageType']] = None,
                 reserved_concurrent_executions: Optional[pulumi.Input[int]] = None,
                 runtime: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['FunctionTagArgs']]]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 tracing_config: Optional[pulumi.Input['FunctionTracingConfigArgs']] = None,
                 vpc_config: Optional[pulumi.Input['FunctionVpcConfigArgs']] = None):
        """
        The set of arguments for constructing a Function resource.
        :param pulumi.Input['FunctionCodeArgs'] code: The code for the function.
        :param pulumi.Input[str] role: The Amazon Resource Name (ARN) of the function's execution role.
        :param pulumi.Input[str] code_signing_config_arn: A unique Arn for CodeSigningConfig resource
        :param pulumi.Input['FunctionDeadLetterConfigArgs'] dead_letter_config: A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing.
        :param pulumi.Input[str] description: A description of the function.
        :param pulumi.Input['FunctionEnvironmentArgs'] environment: Environment variables that are accessible from function code during execution.
        :param pulumi.Input[Sequence[pulumi.Input['FunctionFileSystemConfigArgs']]] file_system_configs: Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an AWS::EFS::MountTarget resource, you must also specify a DependsOn attribute to ensure that the mount target is created or updated before the function.
        :param pulumi.Input[str] function_name: The name of the Lambda function, up to 64 characters in length. If you don't specify a name, AWS CloudFormation generates one.
        :param pulumi.Input[str] handler: The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime
        :param pulumi.Input['FunctionImageConfigArgs'] image_config: ImageConfig
        :param pulumi.Input[str] kms_key_arn: The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] layers: A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version.
        :param pulumi.Input[int] memory_size: The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.
        :param pulumi.Input['FunctionPackageType'] package_type: PackageType.
        :param pulumi.Input[int] reserved_concurrent_executions: The number of simultaneous executions to reserve for the function.
        :param pulumi.Input[str] runtime: The identifier of the function's runtime.
        :param pulumi.Input[Sequence[pulumi.Input['FunctionTagArgs']]] tags: A list of tags to apply to the function.
        :param pulumi.Input[int] timeout: The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.
        :param pulumi.Input['FunctionTracingConfigArgs'] tracing_config: Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.
        :param pulumi.Input['FunctionVpcConfigArgs'] vpc_config: For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC.
        """
        pulumi.set(__self__, "code", code)
        pulumi.set(__self__, "role", role)
        if code_signing_config_arn is not None:
            pulumi.set(__self__, "code_signing_config_arn", code_signing_config_arn)
        if dead_letter_config is not None:
            pulumi.set(__self__, "dead_letter_config", dead_letter_config)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if environment is not None:
            pulumi.set(__self__, "environment", environment)
        if file_system_configs is not None:
            pulumi.set(__self__, "file_system_configs", file_system_configs)
        if function_name is not None:
            pulumi.set(__self__, "function_name", function_name)
        if handler is not None:
            pulumi.set(__self__, "handler", handler)
        if image_config is not None:
            pulumi.set(__self__, "image_config", image_config)
        if kms_key_arn is not None:
            pulumi.set(__self__, "kms_key_arn", kms_key_arn)
        if layers is not None:
            pulumi.set(__self__, "layers", layers)
        if memory_size is not None:
            pulumi.set(__self__, "memory_size", memory_size)
        if package_type is not None:
            pulumi.set(__self__, "package_type", package_type)
        if reserved_concurrent_executions is not None:
            pulumi.set(__self__, "reserved_concurrent_executions", reserved_concurrent_executions)
        if runtime is not None:
            pulumi.set(__self__, "runtime", runtime)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)
        if tracing_config is not None:
            pulumi.set(__self__, "tracing_config", tracing_config)
        if vpc_config is not None:
            pulumi.set(__self__, "vpc_config", vpc_config)

    @property
    @pulumi.getter
    def code(self) -> pulumi.Input['FunctionCodeArgs']:
        """
        The code for the function.
        """
        return pulumi.get(self, "code")

    @code.setter
    def code(self, value: pulumi.Input['FunctionCodeArgs']):
        pulumi.set(self, "code", value)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the function's execution role.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="codeSigningConfigArn")
    def code_signing_config_arn(self) -> Optional[pulumi.Input[str]]:
        """
        A unique Arn for CodeSigningConfig resource
        """
        return pulumi.get(self, "code_signing_config_arn")

    @code_signing_config_arn.setter
    def code_signing_config_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "code_signing_config_arn", value)

    @property
    @pulumi.getter(name="deadLetterConfig")
    def dead_letter_config(self) -> Optional[pulumi.Input['FunctionDeadLetterConfigArgs']]:
        """
        A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing.
        """
        return pulumi.get(self, "dead_letter_config")

    @dead_letter_config.setter
    def dead_letter_config(self, value: Optional[pulumi.Input['FunctionDeadLetterConfigArgs']]):
        pulumi.set(self, "dead_letter_config", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the function.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input['FunctionEnvironmentArgs']]:
        """
        Environment variables that are accessible from function code during execution.
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input['FunctionEnvironmentArgs']]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter(name="fileSystemConfigs")
    def file_system_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FunctionFileSystemConfigArgs']]]]:
        """
        Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an AWS::EFS::MountTarget resource, you must also specify a DependsOn attribute to ensure that the mount target is created or updated before the function.
        """
        return pulumi.get(self, "file_system_configs")

    @file_system_configs.setter
    def file_system_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FunctionFileSystemConfigArgs']]]]):
        pulumi.set(self, "file_system_configs", value)

    @property
    @pulumi.getter(name="functionName")
    def function_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Lambda function, up to 64 characters in length. If you don't specify a name, AWS CloudFormation generates one.
        """
        return pulumi.get(self, "function_name")

    @function_name.setter
    def function_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "function_name", value)

    @property
    @pulumi.getter
    def handler(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime
        """
        return pulumi.get(self, "handler")

    @handler.setter
    def handler(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "handler", value)

    @property
    @pulumi.getter(name="imageConfig")
    def image_config(self) -> Optional[pulumi.Input['FunctionImageConfigArgs']]:
        """
        ImageConfig
        """
        return pulumi.get(self, "image_config")

    @image_config.setter
    def image_config(self, value: Optional[pulumi.Input['FunctionImageConfigArgs']]):
        pulumi.set(self, "image_config", value)

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
        """
        return pulumi.get(self, "kms_key_arn")

    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_arn", value)

    @property
    @pulumi.getter
    def layers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version.
        """
        return pulumi.get(self, "layers")

    @layers.setter
    def layers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "layers", value)

    @property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> Optional[pulumi.Input[int]]:
        """
        The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.
        """
        return pulumi.get(self, "memory_size")

    @memory_size.setter
    def memory_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "memory_size", value)

    @property
    @pulumi.getter(name="packageType")
    def package_type(self) -> Optional[pulumi.Input['FunctionPackageType']]:
        """
        PackageType.
        """
        return pulumi.get(self, "package_type")

    @package_type.setter
    def package_type(self, value: Optional[pulumi.Input['FunctionPackageType']]):
        pulumi.set(self, "package_type", value)

    @property
    @pulumi.getter(name="reservedConcurrentExecutions")
    def reserved_concurrent_executions(self) -> Optional[pulumi.Input[int]]:
        """
        The number of simultaneous executions to reserve for the function.
        """
        return pulumi.get(self, "reserved_concurrent_executions")

    @reserved_concurrent_executions.setter
    def reserved_concurrent_executions(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "reserved_concurrent_executions", value)

    @property
    @pulumi.getter
    def runtime(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the function's runtime.
        """
        return pulumi.get(self, "runtime")

    @runtime.setter
    def runtime(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "runtime", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FunctionTagArgs']]]]:
        """
        A list of tags to apply to the function.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FunctionTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[int]]:
        """
        The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout", value)

    @property
    @pulumi.getter(name="tracingConfig")
    def tracing_config(self) -> Optional[pulumi.Input['FunctionTracingConfigArgs']]:
        """
        Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.
        """
        return pulumi.get(self, "tracing_config")

    @tracing_config.setter
    def tracing_config(self, value: Optional[pulumi.Input['FunctionTracingConfigArgs']]):
        pulumi.set(self, "tracing_config", value)

    @property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input['FunctionVpcConfigArgs']]:
        """
        For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC.
        """
        return pulumi.get(self, "vpc_config")

    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input['FunctionVpcConfigArgs']]):
        pulumi.set(self, "vpc_config", value)


class Function(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 code: Optional[pulumi.Input[pulumi.InputType['FunctionCodeArgs']]] = None,
                 code_signing_config_arn: Optional[pulumi.Input[str]] = None,
                 dead_letter_config: Optional[pulumi.Input[pulumi.InputType['FunctionDeadLetterConfigArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[pulumi.InputType['FunctionEnvironmentArgs']]] = None,
                 file_system_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FunctionFileSystemConfigArgs']]]]] = None,
                 function_name: Optional[pulumi.Input[str]] = None,
                 handler: Optional[pulumi.Input[str]] = None,
                 image_config: Optional[pulumi.Input[pulumi.InputType['FunctionImageConfigArgs']]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 layers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 memory_size: Optional[pulumi.Input[int]] = None,
                 package_type: Optional[pulumi.Input['FunctionPackageType']] = None,
                 reserved_concurrent_executions: Optional[pulumi.Input[int]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 runtime: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FunctionTagArgs']]]]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 tracing_config: Optional[pulumi.Input[pulumi.InputType['FunctionTracingConfigArgs']]] = None,
                 vpc_config: Optional[pulumi.Input[pulumi.InputType['FunctionVpcConfigArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Lambda::Function

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['FunctionCodeArgs']] code: The code for the function.
        :param pulumi.Input[str] code_signing_config_arn: A unique Arn for CodeSigningConfig resource
        :param pulumi.Input[pulumi.InputType['FunctionDeadLetterConfigArgs']] dead_letter_config: A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing.
        :param pulumi.Input[str] description: A description of the function.
        :param pulumi.Input[pulumi.InputType['FunctionEnvironmentArgs']] environment: Environment variables that are accessible from function code during execution.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FunctionFileSystemConfigArgs']]]] file_system_configs: Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an AWS::EFS::MountTarget resource, you must also specify a DependsOn attribute to ensure that the mount target is created or updated before the function.
        :param pulumi.Input[str] function_name: The name of the Lambda function, up to 64 characters in length. If you don't specify a name, AWS CloudFormation generates one.
        :param pulumi.Input[str] handler: The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime
        :param pulumi.Input[pulumi.InputType['FunctionImageConfigArgs']] image_config: ImageConfig
        :param pulumi.Input[str] kms_key_arn: The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] layers: A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version.
        :param pulumi.Input[int] memory_size: The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.
        :param pulumi.Input['FunctionPackageType'] package_type: PackageType.
        :param pulumi.Input[int] reserved_concurrent_executions: The number of simultaneous executions to reserve for the function.
        :param pulumi.Input[str] role: The Amazon Resource Name (ARN) of the function's execution role.
        :param pulumi.Input[str] runtime: The identifier of the function's runtime.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FunctionTagArgs']]]] tags: A list of tags to apply to the function.
        :param pulumi.Input[int] timeout: The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.
        :param pulumi.Input[pulumi.InputType['FunctionTracingConfigArgs']] tracing_config: Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.
        :param pulumi.Input[pulumi.InputType['FunctionVpcConfigArgs']] vpc_config: For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FunctionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Lambda::Function

        :param str resource_name: The name of the resource.
        :param FunctionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FunctionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 code: Optional[pulumi.Input[pulumi.InputType['FunctionCodeArgs']]] = None,
                 code_signing_config_arn: Optional[pulumi.Input[str]] = None,
                 dead_letter_config: Optional[pulumi.Input[pulumi.InputType['FunctionDeadLetterConfigArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[pulumi.InputType['FunctionEnvironmentArgs']]] = None,
                 file_system_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FunctionFileSystemConfigArgs']]]]] = None,
                 function_name: Optional[pulumi.Input[str]] = None,
                 handler: Optional[pulumi.Input[str]] = None,
                 image_config: Optional[pulumi.Input[pulumi.InputType['FunctionImageConfigArgs']]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 layers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 memory_size: Optional[pulumi.Input[int]] = None,
                 package_type: Optional[pulumi.Input['FunctionPackageType']] = None,
                 reserved_concurrent_executions: Optional[pulumi.Input[int]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 runtime: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FunctionTagArgs']]]]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 tracing_config: Optional[pulumi.Input[pulumi.InputType['FunctionTracingConfigArgs']]] = None,
                 vpc_config: Optional[pulumi.Input[pulumi.InputType['FunctionVpcConfigArgs']]] = None,
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
            __props__ = FunctionArgs.__new__(FunctionArgs)

            if code is None and not opts.urn:
                raise TypeError("Missing required property 'code'")
            __props__.__dict__["code"] = code
            __props__.__dict__["code_signing_config_arn"] = code_signing_config_arn
            __props__.__dict__["dead_letter_config"] = dead_letter_config
            __props__.__dict__["description"] = description
            __props__.__dict__["environment"] = environment
            __props__.__dict__["file_system_configs"] = file_system_configs
            __props__.__dict__["function_name"] = function_name
            __props__.__dict__["handler"] = handler
            __props__.__dict__["image_config"] = image_config
            __props__.__dict__["kms_key_arn"] = kms_key_arn
            __props__.__dict__["layers"] = layers
            __props__.__dict__["memory_size"] = memory_size
            __props__.__dict__["package_type"] = package_type
            __props__.__dict__["reserved_concurrent_executions"] = reserved_concurrent_executions
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            __props__.__dict__["runtime"] = runtime
            __props__.__dict__["tags"] = tags
            __props__.__dict__["timeout"] = timeout
            __props__.__dict__["tracing_config"] = tracing_config
            __props__.__dict__["vpc_config"] = vpc_config
            __props__.__dict__["arn"] = None
        super(Function, __self__).__init__(
            'aws-native:lambda:Function',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Function':
        """
        Get an existing Function resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FunctionArgs.__new__(FunctionArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["code"] = None
        __props__.__dict__["code_signing_config_arn"] = None
        __props__.__dict__["dead_letter_config"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["environment"] = None
        __props__.__dict__["file_system_configs"] = None
        __props__.__dict__["function_name"] = None
        __props__.__dict__["handler"] = None
        __props__.__dict__["image_config"] = None
        __props__.__dict__["kms_key_arn"] = None
        __props__.__dict__["layers"] = None
        __props__.__dict__["memory_size"] = None
        __props__.__dict__["package_type"] = None
        __props__.__dict__["reserved_concurrent_executions"] = None
        __props__.__dict__["role"] = None
        __props__.__dict__["runtime"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["timeout"] = None
        __props__.__dict__["tracing_config"] = None
        __props__.__dict__["vpc_config"] = None
        return Function(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Unique identifier for function resources
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def code(self) -> pulumi.Output['outputs.FunctionCode']:
        """
        The code for the function.
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter(name="codeSigningConfigArn")
    def code_signing_config_arn(self) -> pulumi.Output[Optional[str]]:
        """
        A unique Arn for CodeSigningConfig resource
        """
        return pulumi.get(self, "code_signing_config_arn")

    @property
    @pulumi.getter(name="deadLetterConfig")
    def dead_letter_config(self) -> pulumi.Output[Optional['outputs.FunctionDeadLetterConfig']]:
        """
        A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing.
        """
        return pulumi.get(self, "dead_letter_config")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the function.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Output[Optional['outputs.FunctionEnvironment']]:
        """
        Environment variables that are accessible from function code during execution.
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter(name="fileSystemConfigs")
    def file_system_configs(self) -> pulumi.Output[Optional[Sequence['outputs.FunctionFileSystemConfig']]]:
        """
        Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an AWS::EFS::MountTarget resource, you must also specify a DependsOn attribute to ensure that the mount target is created or updated before the function.
        """
        return pulumi.get(self, "file_system_configs")

    @property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the Lambda function, up to 64 characters in length. If you don't specify a name, AWS CloudFormation generates one.
        """
        return pulumi.get(self, "function_name")

    @property
    @pulumi.getter
    def handler(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime
        """
        return pulumi.get(self, "handler")

    @property
    @pulumi.getter(name="imageConfig")
    def image_config(self) -> pulumi.Output[Optional['outputs.FunctionImageConfig']]:
        """
        ImageConfig
        """
        return pulumi.get(self, "image_config")

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
        """
        return pulumi.get(self, "kms_key_arn")

    @property
    @pulumi.getter
    def layers(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version.
        """
        return pulumi.get(self, "layers")

    @property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> pulumi.Output[Optional[int]]:
        """
        The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.
        """
        return pulumi.get(self, "memory_size")

    @property
    @pulumi.getter(name="packageType")
    def package_type(self) -> pulumi.Output[Optional['FunctionPackageType']]:
        """
        PackageType.
        """
        return pulumi.get(self, "package_type")

    @property
    @pulumi.getter(name="reservedConcurrentExecutions")
    def reserved_concurrent_executions(self) -> pulumi.Output[Optional[int]]:
        """
        The number of simultaneous executions to reserve for the function.
        """
        return pulumi.get(self, "reserved_concurrent_executions")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the function's execution role.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter
    def runtime(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier of the function's runtime.
        """
        return pulumi.get(self, "runtime")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.FunctionTag']]]:
        """
        A list of tags to apply to the function.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional[int]]:
        """
        The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter(name="tracingConfig")
    def tracing_config(self) -> pulumi.Output[Optional['outputs.FunctionTracingConfig']]:
        """
        Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.
        """
        return pulumi.get(self, "tracing_config")

    @property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Output[Optional['outputs.FunctionVpcConfig']]:
        """
        For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC.
        """
        return pulumi.get(self, "vpc_config")

