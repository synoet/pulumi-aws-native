# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['StudioArgs', 'Studio']

@pulumi.input_type
class StudioArgs:
    def __init__(__self__, *,
                 admin_role_arn: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 studio_name: pulumi.Input[str],
                 user_role_arn: pulumi.Input[str],
                 studio_encryption_configuration: Optional[pulumi.Input['StudioEncryptionConfigurationArgs']] = None,
                 tags: Optional[Any] = None):
        """
        The set of arguments for constructing a Studio resource.
        """
        pulumi.set(__self__, "admin_role_arn", admin_role_arn)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "studio_name", studio_name)
        pulumi.set(__self__, "user_role_arn", user_role_arn)
        if studio_encryption_configuration is not None:
            pulumi.set(__self__, "studio_encryption_configuration", studio_encryption_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="adminRoleArn")
    def admin_role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "admin_role_arn")

    @admin_role_arn.setter
    def admin_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "admin_role_arn", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="studioName")
    def studio_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "studio_name")

    @studio_name.setter
    def studio_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "studio_name", value)

    @property
    @pulumi.getter(name="userRoleArn")
    def user_role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "user_role_arn")

    @user_role_arn.setter
    def user_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_role_arn", value)

    @property
    @pulumi.getter(name="studioEncryptionConfiguration")
    def studio_encryption_configuration(self) -> Optional[pulumi.Input['StudioEncryptionConfigurationArgs']]:
        return pulumi.get(self, "studio_encryption_configuration")

    @studio_encryption_configuration.setter
    def studio_encryption_configuration(self, value: Optional[pulumi.Input['StudioEncryptionConfigurationArgs']]):
        pulumi.set(self, "studio_encryption_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)


class Studio(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_role_arn: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 studio_encryption_configuration: Optional[pulumi.Input[pulumi.InputType['StudioEncryptionConfigurationArgs']]] = None,
                 studio_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 user_role_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource schema for AWS::NimbleStudio::Studio.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StudioArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::NimbleStudio::Studio.

        :param str resource_name: The name of the resource.
        :param StudioArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StudioArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_role_arn: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 studio_encryption_configuration: Optional[pulumi.Input[pulumi.InputType['StudioEncryptionConfigurationArgs']]] = None,
                 studio_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 user_role_arn: Optional[pulumi.Input[str]] = None,
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
            __props__ = StudioArgs.__new__(StudioArgs)

            if admin_role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'admin_role_arn'")
            __props__.__dict__["admin_role_arn"] = admin_role_arn
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["studio_encryption_configuration"] = studio_encryption_configuration
            if studio_name is None and not opts.urn:
                raise TypeError("Missing required property 'studio_name'")
            __props__.__dict__["studio_name"] = studio_name
            __props__.__dict__["tags"] = tags
            if user_role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'user_role_arn'")
            __props__.__dict__["user_role_arn"] = user_role_arn
            __props__.__dict__["home_region"] = None
            __props__.__dict__["sso_client_id"] = None
            __props__.__dict__["studio_id"] = None
            __props__.__dict__["studio_url"] = None
        super(Studio, __self__).__init__(
            'aws-native:nimblestudio:Studio',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Studio':
        """
        Get an existing Studio resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StudioArgs.__new__(StudioArgs)

        __props__.__dict__["admin_role_arn"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["home_region"] = None
        __props__.__dict__["sso_client_id"] = None
        __props__.__dict__["studio_encryption_configuration"] = None
        __props__.__dict__["studio_id"] = None
        __props__.__dict__["studio_name"] = None
        __props__.__dict__["studio_url"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["user_role_arn"] = None
        return Studio(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminRoleArn")
    def admin_role_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "admin_role_arn")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="homeRegion")
    def home_region(self) -> pulumi.Output[str]:
        return pulumi.get(self, "home_region")

    @property
    @pulumi.getter(name="ssoClientId")
    def sso_client_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "sso_client_id")

    @property
    @pulumi.getter(name="studioEncryptionConfiguration")
    def studio_encryption_configuration(self) -> pulumi.Output[Optional['outputs.StudioEncryptionConfiguration']]:
        return pulumi.get(self, "studio_encryption_configuration")

    @property
    @pulumi.getter(name="studioId")
    def studio_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "studio_id")

    @property
    @pulumi.getter(name="studioName")
    def studio_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "studio_name")

    @property
    @pulumi.getter(name="studioUrl")
    def studio_url(self) -> pulumi.Output[str]:
        return pulumi.get(self, "studio_url")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userRoleArn")
    def user_role_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "user_role_arn")

