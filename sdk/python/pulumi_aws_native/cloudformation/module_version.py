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

__all__ = ['ModuleVersionArgs', 'ModuleVersion']

@pulumi.input_type
class ModuleVersionArgs:
    def __init__(__self__, *,
                 module_name: pulumi.Input[str],
                 module_package: pulumi.Input[str]):
        """
        The set of arguments for constructing a ModuleVersion resource.
        :param pulumi.Input[str] module_name: The name of the module being registered.
               
               Recommended module naming pattern: company_or_organization::service::type::MODULE.
        :param pulumi.Input[str] module_package: The url to the S3 bucket containing the schema and template fragment for the module you want to register.
        """
        pulumi.set(__self__, "module_name", module_name)
        pulumi.set(__self__, "module_package", module_package)

    @property
    @pulumi.getter(name="moduleName")
    def module_name(self) -> pulumi.Input[str]:
        """
        The name of the module being registered.

        Recommended module naming pattern: company_or_organization::service::type::MODULE.
        """
        return pulumi.get(self, "module_name")

    @module_name.setter
    def module_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "module_name", value)

    @property
    @pulumi.getter(name="modulePackage")
    def module_package(self) -> pulumi.Input[str]:
        """
        The url to the S3 bucket containing the schema and template fragment for the module you want to register.
        """
        return pulumi.get(self, "module_package")

    @module_package.setter
    def module_package(self, value: pulumi.Input[str]):
        pulumi.set(self, "module_package", value)


class ModuleVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 module_name: Optional[pulumi.Input[str]] = None,
                 module_package: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A module that has been registered in the CloudFormation registry.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] module_name: The name of the module being registered.
               
               Recommended module naming pattern: company_or_organization::service::type::MODULE.
        :param pulumi.Input[str] module_package: The url to the S3 bucket containing the schema and template fragment for the module you want to register.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ModuleVersionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A module that has been registered in the CloudFormation registry.

        :param str resource_name: The name of the resource.
        :param ModuleVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ModuleVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 module_name: Optional[pulumi.Input[str]] = None,
                 module_package: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ModuleVersionArgs.__new__(ModuleVersionArgs)

            if module_name is None and not opts.urn:
                raise TypeError("Missing required property 'module_name'")
            __props__.__dict__["module_name"] = module_name
            if module_package is None and not opts.urn:
                raise TypeError("Missing required property 'module_package'")
            __props__.__dict__["module_package"] = module_package
            __props__.__dict__["arn"] = None
            __props__.__dict__["description"] = None
            __props__.__dict__["documentation_url"] = None
            __props__.__dict__["is_default_version"] = None
            __props__.__dict__["schema"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["version_id"] = None
            __props__.__dict__["visibility"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["module_name", "module_package"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ModuleVersion, __self__).__init__(
            'aws-native:cloudformation:ModuleVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ModuleVersion':
        """
        Get an existing ModuleVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ModuleVersionArgs.__new__(ModuleVersionArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["documentation_url"] = None
        __props__.__dict__["is_default_version"] = None
        __props__.__dict__["module_name"] = None
        __props__.__dict__["module_package"] = None
        __props__.__dict__["schema"] = None
        __props__.__dict__["time_created"] = None
        __props__.__dict__["version_id"] = None
        __props__.__dict__["visibility"] = None
        return ModuleVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the module.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the registered module.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="documentationUrl")
    def documentation_url(self) -> pulumi.Output[str]:
        """
        The URL of a page providing detailed documentation for this module.
        """
        return pulumi.get(self, "documentation_url")

    @property
    @pulumi.getter(name="isDefaultVersion")
    def is_default_version(self) -> pulumi.Output[bool]:
        """
        Indicator of whether this module version is the current default version
        """
        return pulumi.get(self, "is_default_version")

    @property
    @pulumi.getter(name="moduleName")
    def module_name(self) -> pulumi.Output[str]:
        """
        The name of the module being registered.

        Recommended module naming pattern: company_or_organization::service::type::MODULE.
        """
        return pulumi.get(self, "module_name")

    @property
    @pulumi.getter(name="modulePackage")
    def module_package(self) -> pulumi.Output[str]:
        """
        The url to the S3 bucket containing the schema and template fragment for the module you want to register.
        """
        return pulumi.get(self, "module_package")

    @property
    @pulumi.getter
    def schema(self) -> pulumi.Output[str]:
        """
        The schema defining input parameters to and resources generated by the module.
        """
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The time that the specified module version was registered.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[str]:
        """
        The version ID of the module represented by this module instance.
        """
        return pulumi.get(self, "version_id")

    @property
    @pulumi.getter
    def visibility(self) -> pulumi.Output['ModuleVersionVisibility']:
        """
        The scope at which the type is visible and usable in CloudFormation operations.

        The only allowed value at present is:

        PRIVATE: The type is only visible and usable within the account in which it is registered. Currently, AWS CloudFormation marks any types you register as PRIVATE.
        """
        return pulumi.get(self, "visibility")

