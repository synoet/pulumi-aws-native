# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['LaunchTemplateArgs', 'LaunchTemplate']

@pulumi.input_type
class LaunchTemplateArgs:
    def __init__(__self__, *,
                 launch_template_data: Optional[pulumi.Input['LaunchTemplateDataArgs']] = None,
                 launch_template_name: Optional[pulumi.Input[str]] = None,
                 tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input['LaunchTemplateTagSpecificationArgs']]]] = None):
        """
        The set of arguments for constructing a LaunchTemplate resource.
        """
        if launch_template_data is not None:
            pulumi.set(__self__, "launch_template_data", launch_template_data)
        if launch_template_name is not None:
            pulumi.set(__self__, "launch_template_name", launch_template_name)
        if tag_specifications is not None:
            pulumi.set(__self__, "tag_specifications", tag_specifications)

    @property
    @pulumi.getter(name="launchTemplateData")
    def launch_template_data(self) -> Optional[pulumi.Input['LaunchTemplateDataArgs']]:
        return pulumi.get(self, "launch_template_data")

    @launch_template_data.setter
    def launch_template_data(self, value: Optional[pulumi.Input['LaunchTemplateDataArgs']]):
        pulumi.set(self, "launch_template_data", value)

    @property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "launch_template_name")

    @launch_template_name.setter
    def launch_template_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "launch_template_name", value)

    @property
    @pulumi.getter(name="tagSpecifications")
    def tag_specifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LaunchTemplateTagSpecificationArgs']]]]:
        return pulumi.get(self, "tag_specifications")

    @tag_specifications.setter
    def tag_specifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LaunchTemplateTagSpecificationArgs']]]]):
        pulumi.set(self, "tag_specifications", value)


warnings.warn("""LaunchTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class LaunchTemplate(pulumi.CustomResource):
    warnings.warn("""LaunchTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 launch_template_data: Optional[pulumi.Input[pulumi.InputType['LaunchTemplateDataArgs']]] = None,
                 launch_template_name: Optional[pulumi.Input[str]] = None,
                 tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LaunchTemplateTagSpecificationArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::LaunchTemplate

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[LaunchTemplateArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::LaunchTemplate

        :param str resource_name: The name of the resource.
        :param LaunchTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LaunchTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 launch_template_data: Optional[pulumi.Input[pulumi.InputType['LaunchTemplateDataArgs']]] = None,
                 launch_template_name: Optional[pulumi.Input[str]] = None,
                 tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LaunchTemplateTagSpecificationArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""LaunchTemplate is deprecated: LaunchTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LaunchTemplateArgs.__new__(LaunchTemplateArgs)

            __props__.__dict__["launch_template_data"] = launch_template_data
            __props__.__dict__["launch_template_name"] = launch_template_name
            __props__.__dict__["tag_specifications"] = tag_specifications
            __props__.__dict__["default_version_number"] = None
            __props__.__dict__["latest_version_number"] = None
        super(LaunchTemplate, __self__).__init__(
            'aws-native:ec2:LaunchTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LaunchTemplate':
        """
        Get an existing LaunchTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LaunchTemplateArgs.__new__(LaunchTemplateArgs)

        __props__.__dict__["default_version_number"] = None
        __props__.__dict__["latest_version_number"] = None
        __props__.__dict__["launch_template_data"] = None
        __props__.__dict__["launch_template_name"] = None
        __props__.__dict__["tag_specifications"] = None
        return LaunchTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultVersionNumber")
    def default_version_number(self) -> pulumi.Output[str]:
        return pulumi.get(self, "default_version_number")

    @property
    @pulumi.getter(name="latestVersionNumber")
    def latest_version_number(self) -> pulumi.Output[str]:
        return pulumi.get(self, "latest_version_number")

    @property
    @pulumi.getter(name="launchTemplateData")
    def launch_template_data(self) -> pulumi.Output[Optional['outputs.LaunchTemplateData']]:
        return pulumi.get(self, "launch_template_data")

    @property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "launch_template_name")

    @property
    @pulumi.getter(name="tagSpecifications")
    def tag_specifications(self) -> pulumi.Output[Optional[Sequence['outputs.LaunchTemplateTagSpecification']]]:
        return pulumi.get(self, "tag_specifications")

