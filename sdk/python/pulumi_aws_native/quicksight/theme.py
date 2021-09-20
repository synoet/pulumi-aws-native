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

__all__ = ['ThemeArgs', 'Theme']

@pulumi.input_type
class ThemeArgs:
    def __init__(__self__, *,
                 aws_account_id: pulumi.Input[str],
                 theme_id: pulumi.Input[str],
                 base_theme_id: Optional[pulumi.Input[str]] = None,
                 configuration: Optional[pulumi.Input['ThemeThemeConfigurationArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input['ThemeResourcePermissionArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ThemeTagArgs']]]] = None,
                 version_description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Theme resource.
        :param pulumi.Input[str] base_theme_id: <p>The ID of the theme that a custom theme will inherit from. All themes inherit from one of
               			the starting themes defined by Amazon QuickSight. For a list of the starting themes, use
               				<code>ListThemes</code> or choose <b>Themes</b> from
               			within a QuickSight analysis. </p>
        :param pulumi.Input[str] name: <p>A display name for the theme.</p>
        :param pulumi.Input[Sequence[pulumi.Input['ThemeResourcePermissionArgs']]] permissions: <p>A valid grouping of resource permissions to apply to the new theme.
               			</p>
        :param pulumi.Input[Sequence[pulumi.Input['ThemeTagArgs']]] tags: <p>A map of the key-value pairs for the resource tag or tags that you want to add to the
               			resource.</p>
        :param pulumi.Input[str] version_description: <p>A description of the first version of the theme that you're creating. Every time
               				<code>UpdateTheme</code> is called, a new version is created. Each version of the
               			theme has a description of the version in the <code>VersionDescription</code>
               			field.</p>
        """
        pulumi.set(__self__, "aws_account_id", aws_account_id)
        pulumi.set(__self__, "theme_id", theme_id)
        if base_theme_id is not None:
            pulumi.set(__self__, "base_theme_id", base_theme_id)
        if configuration is not None:
            pulumi.set(__self__, "configuration", configuration)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if version_description is not None:
            pulumi.set(__self__, "version_description", version_description)

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "aws_account_id")

    @aws_account_id.setter
    def aws_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "aws_account_id", value)

    @property
    @pulumi.getter(name="themeId")
    def theme_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "theme_id")

    @theme_id.setter
    def theme_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "theme_id", value)

    @property
    @pulumi.getter(name="baseThemeId")
    def base_theme_id(self) -> Optional[pulumi.Input[str]]:
        """
        <p>The ID of the theme that a custom theme will inherit from. All themes inherit from one of
        			the starting themes defined by Amazon QuickSight. For a list of the starting themes, use
        				<code>ListThemes</code> or choose <b>Themes</b> from
        			within a QuickSight analysis. </p>
        """
        return pulumi.get(self, "base_theme_id")

    @base_theme_id.setter
    def base_theme_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_theme_id", value)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input['ThemeThemeConfigurationArgs']]:
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input['ThemeThemeConfigurationArgs']]):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        <p>A display name for the theme.</p>
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ThemeResourcePermissionArgs']]]]:
        """
        <p>A valid grouping of resource permissions to apply to the new theme.
        			</p>
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ThemeResourcePermissionArgs']]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ThemeTagArgs']]]]:
        """
        <p>A map of the key-value pairs for the resource tag or tags that you want to add to the
        			resource.</p>
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ThemeTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> Optional[pulumi.Input[str]]:
        """
        <p>A description of the first version of the theme that you're creating. Every time
        				<code>UpdateTheme</code> is called, a new version is created. Each version of the
        			theme has a description of the version in the <code>VersionDescription</code>
        			field.</p>
        """
        return pulumi.get(self, "version_description")

    @version_description.setter
    def version_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_description", value)


class Theme(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 base_theme_id: Optional[pulumi.Input[str]] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['ThemeThemeConfigurationArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThemeResourcePermissionArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThemeTagArgs']]]]] = None,
                 theme_id: Optional[pulumi.Input[str]] = None,
                 version_description: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Definition of the AWS::QuickSight::Theme Resource Type.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_theme_id: <p>The ID of the theme that a custom theme will inherit from. All themes inherit from one of
               			the starting themes defined by Amazon QuickSight. For a list of the starting themes, use
               				<code>ListThemes</code> or choose <b>Themes</b> from
               			within a QuickSight analysis. </p>
        :param pulumi.Input[str] name: <p>A display name for the theme.</p>
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThemeResourcePermissionArgs']]]] permissions: <p>A valid grouping of resource permissions to apply to the new theme.
               			</p>
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThemeTagArgs']]]] tags: <p>A map of the key-value pairs for the resource tag or tags that you want to add to the
               			resource.</p>
        :param pulumi.Input[str] version_description: <p>A description of the first version of the theme that you're creating. Every time
               				<code>UpdateTheme</code> is called, a new version is created. Each version of the
               			theme has a description of the version in the <code>VersionDescription</code>
               			field.</p>
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ThemeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of the AWS::QuickSight::Theme Resource Type.

        :param str resource_name: The name of the resource.
        :param ThemeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ThemeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 base_theme_id: Optional[pulumi.Input[str]] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['ThemeThemeConfigurationArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThemeResourcePermissionArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThemeTagArgs']]]]] = None,
                 theme_id: Optional[pulumi.Input[str]] = None,
                 version_description: Optional[pulumi.Input[str]] = None,
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
            __props__ = ThemeArgs.__new__(ThemeArgs)

            if aws_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'aws_account_id'")
            __props__.__dict__["aws_account_id"] = aws_account_id
            __props__.__dict__["base_theme_id"] = base_theme_id
            __props__.__dict__["configuration"] = configuration
            __props__.__dict__["name"] = name
            __props__.__dict__["permissions"] = permissions
            __props__.__dict__["tags"] = tags
            if theme_id is None and not opts.urn:
                raise TypeError("Missing required property 'theme_id'")
            __props__.__dict__["theme_id"] = theme_id
            __props__.__dict__["version_description"] = version_description
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_time"] = None
            __props__.__dict__["last_updated_time"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["version"] = None
        super(Theme, __self__).__init__(
            'aws-native:quicksight:Theme',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Theme':
        """
        Get an existing Theme resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ThemeArgs.__new__(ThemeArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["aws_account_id"] = None
        __props__.__dict__["base_theme_id"] = None
        __props__.__dict__["configuration"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["last_updated_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["permissions"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["theme_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        __props__.__dict__["version_description"] = None
        return Theme(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        <p>The Amazon Resource Name (ARN) of the theme.</p>
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "aws_account_id")

    @property
    @pulumi.getter(name="baseThemeId")
    def base_theme_id(self) -> pulumi.Output[Optional[str]]:
        """
        <p>The ID of the theme that a custom theme will inherit from. All themes inherit from one of
        			the starting themes defined by Amazon QuickSight. For a list of the starting themes, use
        				<code>ListThemes</code> or choose <b>Themes</b> from
        			within a QuickSight analysis. </p>
        """
        return pulumi.get(self, "base_theme_id")

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[Optional['outputs.ThemeThemeConfiguration']]:
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        """
        <p>The date and time that the theme was created.</p>
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[str]:
        """
        <p>The date and time that the theme was last updated.</p>
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        <p>A display name for the theme.</p>
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[Sequence['outputs.ThemeResourcePermission']]]:
        """
        <p>A valid grouping of resource permissions to apply to the new theme.
        			</p>
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ThemeTag']]]:
        """
        <p>A map of the key-value pairs for the resource tag or tags that you want to add to the
        			resource.</p>
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="themeId")
    def theme_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "theme_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output['ThemeThemeType']:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output['outputs.ThemeThemeVersion']:
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> pulumi.Output[Optional[str]]:
        """
        <p>A description of the first version of the theme that you're creating. Every time
        				<code>UpdateTheme</code> is called, a new version is created. Each version of the
        			theme has a description of the version in the <code>VersionDescription</code>
        			field.</p>
        """
        return pulumi.get(self, "version_description")

