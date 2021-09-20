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

__all__ = ['TypeActivationArgs', 'TypeActivation']

@pulumi.input_type
class TypeActivationArgs:
    def __init__(__self__, *,
                 auto_update: Optional[pulumi.Input[bool]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 logging_config: Optional[pulumi.Input['TypeActivationLoggingConfigArgs']] = None,
                 major_version: Optional[pulumi.Input[str]] = None,
                 public_type_arn: Optional[pulumi.Input[str]] = None,
                 publisher_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['TypeActivationType']] = None,
                 type_name: Optional[pulumi.Input[str]] = None,
                 type_name_alias: Optional[pulumi.Input[str]] = None,
                 version_bump: Optional[pulumi.Input['TypeActivationVersionBump']] = None):
        """
        The set of arguments for constructing a TypeActivation resource.
        :param pulumi.Input[bool] auto_update: Whether to automatically update the extension in this account and region when a new minor version is published by the extension publisher. Major versions released by the publisher must be manually updated.
        :param pulumi.Input[str] execution_role_arn: The Amazon Resource Name (ARN) of the IAM execution role to use to register the type. If your resource type calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your resource type with the appropriate credentials.
        :param pulumi.Input['TypeActivationLoggingConfigArgs'] logging_config: Specifies logging configuration information for a type.
        :param pulumi.Input[str] major_version: The Major Version of the type you want to enable
        :param pulumi.Input[str] public_type_arn: The Amazon Resource Number (ARN) assigned to the public extension upon publication
        :param pulumi.Input[str] publisher_id: The publisher id assigned by CloudFormation for publishing in this region.
        :param pulumi.Input['TypeActivationType'] type: The kind of extension
        :param pulumi.Input[str] type_name: The name of the type being registered.
               
               We recommend that type names adhere to the following pattern: company_or_organization::service::type.
        :param pulumi.Input[str] type_name_alias: An alias to assign to the public extension in this account and region. If you specify an alias for the extension, you must then use the alias to refer to the extension in your templates.
        :param pulumi.Input['TypeActivationVersionBump'] version_bump: Manually updates a previously-enabled type to a new major or minor version, if available. You can also use this parameter to update the value of AutoUpdateEnabled
        """
        if auto_update is not None:
            pulumi.set(__self__, "auto_update", auto_update)
        if execution_role_arn is not None:
            pulumi.set(__self__, "execution_role_arn", execution_role_arn)
        if logging_config is not None:
            pulumi.set(__self__, "logging_config", logging_config)
        if major_version is not None:
            pulumi.set(__self__, "major_version", major_version)
        if public_type_arn is not None:
            pulumi.set(__self__, "public_type_arn", public_type_arn)
        if publisher_id is not None:
            pulumi.set(__self__, "publisher_id", publisher_id)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if type_name is not None:
            pulumi.set(__self__, "type_name", type_name)
        if type_name_alias is not None:
            pulumi.set(__self__, "type_name_alias", type_name_alias)
        if version_bump is not None:
            pulumi.set(__self__, "version_bump", version_bump)

    @property
    @pulumi.getter(name="autoUpdate")
    def auto_update(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to automatically update the extension in this account and region when a new minor version is published by the extension publisher. Major versions released by the publisher must be manually updated.
        """
        return pulumi.get(self, "auto_update")

    @auto_update.setter
    def auto_update(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_update", value)

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the IAM execution role to use to register the type. If your resource type calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your resource type with the appropriate credentials.
        """
        return pulumi.get(self, "execution_role_arn")

    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "execution_role_arn", value)

    @property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input['TypeActivationLoggingConfigArgs']]:
        """
        Specifies logging configuration information for a type.
        """
        return pulumi.get(self, "logging_config")

    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input['TypeActivationLoggingConfigArgs']]):
        pulumi.set(self, "logging_config", value)

    @property
    @pulumi.getter(name="majorVersion")
    def major_version(self) -> Optional[pulumi.Input[str]]:
        """
        The Major Version of the type you want to enable
        """
        return pulumi.get(self, "major_version")

    @major_version.setter
    def major_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "major_version", value)

    @property
    @pulumi.getter(name="publicTypeArn")
    def public_type_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Number (ARN) assigned to the public extension upon publication
        """
        return pulumi.get(self, "public_type_arn")

    @public_type_arn.setter
    def public_type_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_type_arn", value)

    @property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> Optional[pulumi.Input[str]]:
        """
        The publisher id assigned by CloudFormation for publishing in this region.
        """
        return pulumi.get(self, "publisher_id")

    @publisher_id.setter
    def publisher_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "publisher_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['TypeActivationType']]:
        """
        The kind of extension
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['TypeActivationType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="typeName")
    def type_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the type being registered.

        We recommend that type names adhere to the following pattern: company_or_organization::service::type.
        """
        return pulumi.get(self, "type_name")

    @type_name.setter
    def type_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type_name", value)

    @property
    @pulumi.getter(name="typeNameAlias")
    def type_name_alias(self) -> Optional[pulumi.Input[str]]:
        """
        An alias to assign to the public extension in this account and region. If you specify an alias for the extension, you must then use the alias to refer to the extension in your templates.
        """
        return pulumi.get(self, "type_name_alias")

    @type_name_alias.setter
    def type_name_alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type_name_alias", value)

    @property
    @pulumi.getter(name="versionBump")
    def version_bump(self) -> Optional[pulumi.Input['TypeActivationVersionBump']]:
        """
        Manually updates a previously-enabled type to a new major or minor version, if available. You can also use this parameter to update the value of AutoUpdateEnabled
        """
        return pulumi.get(self, "version_bump")

    @version_bump.setter
    def version_bump(self, value: Optional[pulumi.Input['TypeActivationVersionBump']]):
        pulumi.set(self, "version_bump", value)


class TypeActivation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_update: Optional[pulumi.Input[bool]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 logging_config: Optional[pulumi.Input[pulumi.InputType['TypeActivationLoggingConfigArgs']]] = None,
                 major_version: Optional[pulumi.Input[str]] = None,
                 public_type_arn: Optional[pulumi.Input[str]] = None,
                 publisher_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['TypeActivationType']] = None,
                 type_name: Optional[pulumi.Input[str]] = None,
                 type_name_alias: Optional[pulumi.Input[str]] = None,
                 version_bump: Optional[pulumi.Input['TypeActivationVersionBump']] = None,
                 __props__=None):
        """
        Enable a resource that has been published in the CloudFormation Registry.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_update: Whether to automatically update the extension in this account and region when a new minor version is published by the extension publisher. Major versions released by the publisher must be manually updated.
        :param pulumi.Input[str] execution_role_arn: The Amazon Resource Name (ARN) of the IAM execution role to use to register the type. If your resource type calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your resource type with the appropriate credentials.
        :param pulumi.Input[pulumi.InputType['TypeActivationLoggingConfigArgs']] logging_config: Specifies logging configuration information for a type.
        :param pulumi.Input[str] major_version: The Major Version of the type you want to enable
        :param pulumi.Input[str] public_type_arn: The Amazon Resource Number (ARN) assigned to the public extension upon publication
        :param pulumi.Input[str] publisher_id: The publisher id assigned by CloudFormation for publishing in this region.
        :param pulumi.Input['TypeActivationType'] type: The kind of extension
        :param pulumi.Input[str] type_name: The name of the type being registered.
               
               We recommend that type names adhere to the following pattern: company_or_organization::service::type.
        :param pulumi.Input[str] type_name_alias: An alias to assign to the public extension in this account and region. If you specify an alias for the extension, you must then use the alias to refer to the extension in your templates.
        :param pulumi.Input['TypeActivationVersionBump'] version_bump: Manually updates a previously-enabled type to a new major or minor version, if available. You can also use this parameter to update the value of AutoUpdateEnabled
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TypeActivationArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Enable a resource that has been published in the CloudFormation Registry.

        :param str resource_name: The name of the resource.
        :param TypeActivationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TypeActivationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_update: Optional[pulumi.Input[bool]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 logging_config: Optional[pulumi.Input[pulumi.InputType['TypeActivationLoggingConfigArgs']]] = None,
                 major_version: Optional[pulumi.Input[str]] = None,
                 public_type_arn: Optional[pulumi.Input[str]] = None,
                 publisher_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['TypeActivationType']] = None,
                 type_name: Optional[pulumi.Input[str]] = None,
                 type_name_alias: Optional[pulumi.Input[str]] = None,
                 version_bump: Optional[pulumi.Input['TypeActivationVersionBump']] = None,
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
            __props__ = TypeActivationArgs.__new__(TypeActivationArgs)

            __props__.__dict__["auto_update"] = auto_update
            __props__.__dict__["execution_role_arn"] = execution_role_arn
            __props__.__dict__["logging_config"] = logging_config
            __props__.__dict__["major_version"] = major_version
            __props__.__dict__["public_type_arn"] = public_type_arn
            __props__.__dict__["publisher_id"] = publisher_id
            __props__.__dict__["type"] = type
            __props__.__dict__["type_name"] = type_name
            __props__.__dict__["type_name_alias"] = type_name_alias
            __props__.__dict__["version_bump"] = version_bump
            __props__.__dict__["arn"] = None
        super(TypeActivation, __self__).__init__(
            'aws-native:cloudformation:TypeActivation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TypeActivation':
        """
        Get an existing TypeActivation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TypeActivationArgs.__new__(TypeActivationArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["auto_update"] = None
        __props__.__dict__["execution_role_arn"] = None
        __props__.__dict__["logging_config"] = None
        __props__.__dict__["major_version"] = None
        __props__.__dict__["public_type_arn"] = None
        __props__.__dict__["publisher_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["type_name"] = None
        __props__.__dict__["type_name_alias"] = None
        __props__.__dict__["version_bump"] = None
        return TypeActivation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the extension.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="autoUpdate")
    def auto_update(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to automatically update the extension in this account and region when a new minor version is published by the extension publisher. Major versions released by the publisher must be manually updated.
        """
        return pulumi.get(self, "auto_update")

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Name (ARN) of the IAM execution role to use to register the type. If your resource type calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your resource type with the appropriate credentials.
        """
        return pulumi.get(self, "execution_role_arn")

    @property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> pulumi.Output[Optional['outputs.TypeActivationLoggingConfig']]:
        """
        Specifies logging configuration information for a type.
        """
        return pulumi.get(self, "logging_config")

    @property
    @pulumi.getter(name="majorVersion")
    def major_version(self) -> pulumi.Output[Optional[str]]:
        """
        The Major Version of the type you want to enable
        """
        return pulumi.get(self, "major_version")

    @property
    @pulumi.getter(name="publicTypeArn")
    def public_type_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Number (ARN) assigned to the public extension upon publication
        """
        return pulumi.get(self, "public_type_arn")

    @property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> pulumi.Output[Optional[str]]:
        """
        The publisher id assigned by CloudFormation for publishing in this region.
        """
        return pulumi.get(self, "publisher_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional['TypeActivationType']]:
        """
        The kind of extension
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the type being registered.

        We recommend that type names adhere to the following pattern: company_or_organization::service::type.
        """
        return pulumi.get(self, "type_name")

    @property
    @pulumi.getter(name="typeNameAlias")
    def type_name_alias(self) -> pulumi.Output[Optional[str]]:
        """
        An alias to assign to the public extension in this account and region. If you specify an alias for the extension, you must then use the alias to refer to the extension in your templates.
        """
        return pulumi.get(self, "type_name_alias")

    @property
    @pulumi.getter(name="versionBump")
    def version_bump(self) -> pulumi.Output[Optional['TypeActivationVersionBump']]:
        """
        Manually updates a previously-enabled type to a new major or minor version, if available. You can also use this parameter to update the value of AutoUpdateEnabled
        """
        return pulumi.get(self, "version_bump")

