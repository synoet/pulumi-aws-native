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

__all__ = ['ApplicationArgs', 'Application']

@pulumi.input_type
class ApplicationArgs:
    def __init__(__self__, *,
                 app_block_arn: pulumi.Input[str],
                 icon_s3_location: pulumi.Input['ApplicationS3LocationArgs'],
                 instance_families: pulumi.Input[Sequence[pulumi.Input[str]]],
                 launch_path: pulumi.Input[str],
                 platforms: pulumi.Input[Sequence[pulumi.Input[str]]],
                 attributes_to_delete: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 launch_parameters: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationTagArgs']]]] = None,
                 working_directory: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Application resource.
        """
        pulumi.set(__self__, "app_block_arn", app_block_arn)
        pulumi.set(__self__, "icon_s3_location", icon_s3_location)
        pulumi.set(__self__, "instance_families", instance_families)
        pulumi.set(__self__, "launch_path", launch_path)
        pulumi.set(__self__, "platforms", platforms)
        if attributes_to_delete is not None:
            pulumi.set(__self__, "attributes_to_delete", attributes_to_delete)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if launch_parameters is not None:
            pulumi.set(__self__, "launch_parameters", launch_parameters)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if working_directory is not None:
            pulumi.set(__self__, "working_directory", working_directory)

    @property
    @pulumi.getter(name="appBlockArn")
    def app_block_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "app_block_arn")

    @app_block_arn.setter
    def app_block_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_block_arn", value)

    @property
    @pulumi.getter(name="iconS3Location")
    def icon_s3_location(self) -> pulumi.Input['ApplicationS3LocationArgs']:
        return pulumi.get(self, "icon_s3_location")

    @icon_s3_location.setter
    def icon_s3_location(self, value: pulumi.Input['ApplicationS3LocationArgs']):
        pulumi.set(self, "icon_s3_location", value)

    @property
    @pulumi.getter(name="instanceFamilies")
    def instance_families(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "instance_families")

    @instance_families.setter
    def instance_families(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "instance_families", value)

    @property
    @pulumi.getter(name="launchPath")
    def launch_path(self) -> pulumi.Input[str]:
        return pulumi.get(self, "launch_path")

    @launch_path.setter
    def launch_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "launch_path", value)

    @property
    @pulumi.getter
    def platforms(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "platforms")

    @platforms.setter
    def platforms(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "platforms", value)

    @property
    @pulumi.getter(name="attributesToDelete")
    def attributes_to_delete(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "attributes_to_delete")

    @attributes_to_delete.setter
    def attributes_to_delete(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "attributes_to_delete", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="launchParameters")
    def launch_parameters(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "launch_parameters")

    @launch_parameters.setter
    def launch_parameters(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "launch_parameters", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="workingDirectory")
    def working_directory(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "working_directory")

    @working_directory.setter
    def working_directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "working_directory", value)


class Application(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_block_arn: Optional[pulumi.Input[str]] = None,
                 attributes_to_delete: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 icon_s3_location: Optional[pulumi.Input[pulumi.InputType['ApplicationS3LocationArgs']]] = None,
                 instance_families: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 launch_parameters: Optional[pulumi.Input[str]] = None,
                 launch_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 platforms: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationTagArgs']]]]] = None,
                 working_directory: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::AppStream::Application

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::AppStream::Application

        :param str resource_name: The name of the resource.
        :param ApplicationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_block_arn: Optional[pulumi.Input[str]] = None,
                 attributes_to_delete: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 icon_s3_location: Optional[pulumi.Input[pulumi.InputType['ApplicationS3LocationArgs']]] = None,
                 instance_families: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 launch_parameters: Optional[pulumi.Input[str]] = None,
                 launch_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 platforms: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationTagArgs']]]]] = None,
                 working_directory: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationArgs.__new__(ApplicationArgs)

            if app_block_arn is None and not opts.urn:
                raise TypeError("Missing required property 'app_block_arn'")
            __props__.__dict__["app_block_arn"] = app_block_arn
            __props__.__dict__["attributes_to_delete"] = attributes_to_delete
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if icon_s3_location is None and not opts.urn:
                raise TypeError("Missing required property 'icon_s3_location'")
            __props__.__dict__["icon_s3_location"] = icon_s3_location
            if instance_families is None and not opts.urn:
                raise TypeError("Missing required property 'instance_families'")
            __props__.__dict__["instance_families"] = instance_families
            __props__.__dict__["launch_parameters"] = launch_parameters
            if launch_path is None and not opts.urn:
                raise TypeError("Missing required property 'launch_path'")
            __props__.__dict__["launch_path"] = launch_path
            __props__.__dict__["name"] = name
            if platforms is None and not opts.urn:
                raise TypeError("Missing required property 'platforms'")
            __props__.__dict__["platforms"] = platforms
            __props__.__dict__["tags"] = tags
            __props__.__dict__["working_directory"] = working_directory
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_time"] = None
        super(Application, __self__).__init__(
            'aws-native:appstream:Application',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Application':
        """
        Get an existing Application resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApplicationArgs.__new__(ApplicationArgs)

        __props__.__dict__["app_block_arn"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["attributes_to_delete"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["icon_s3_location"] = None
        __props__.__dict__["instance_families"] = None
        __props__.__dict__["launch_parameters"] = None
        __props__.__dict__["launch_path"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["platforms"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["working_directory"] = None
        return Application(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appBlockArn")
    def app_block_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "app_block_arn")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="attributesToDelete")
    def attributes_to_delete(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "attributes_to_delete")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="iconS3Location")
    def icon_s3_location(self) -> pulumi.Output['outputs.ApplicationS3Location']:
        return pulumi.get(self, "icon_s3_location")

    @property
    @pulumi.getter(name="instanceFamilies")
    def instance_families(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "instance_families")

    @property
    @pulumi.getter(name="launchParameters")
    def launch_parameters(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "launch_parameters")

    @property
    @pulumi.getter(name="launchPath")
    def launch_path(self) -> pulumi.Output[str]:
        return pulumi.get(self, "launch_path")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def platforms(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "platforms")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="workingDirectory")
    def working_directory(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "working_directory")

