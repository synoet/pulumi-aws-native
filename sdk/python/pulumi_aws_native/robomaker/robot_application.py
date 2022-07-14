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
from ._enums import *
from ._inputs import *

__all__ = ['RobotApplicationArgs', 'RobotApplication']

@pulumi.input_type
class RobotApplicationArgs:
    def __init__(__self__, *,
                 robot_software_suite: pulumi.Input['RobotApplicationRobotSoftwareSuiteArgs'],
                 current_revision_id: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input['RobotApplicationSourceConfigArgs']]]] = None,
                 tags: Optional[pulumi.Input['RobotApplicationTagsArgs']] = None):
        """
        The set of arguments for constructing a RobotApplication resource.
        :param pulumi.Input[str] current_revision_id: The revision ID of robot application.
        :param pulumi.Input[str] environment: The URI of the Docker image for the robot application.
        :param pulumi.Input[str] name: The name of the robot application.
        :param pulumi.Input[Sequence[pulumi.Input['RobotApplicationSourceConfigArgs']]] sources: The sources of the robot application.
        """
        pulumi.set(__self__, "robot_software_suite", robot_software_suite)
        if current_revision_id is not None:
            pulumi.set(__self__, "current_revision_id", current_revision_id)
        if environment is not None:
            pulumi.set(__self__, "environment", environment)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sources is not None:
            pulumi.set(__self__, "sources", sources)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="robotSoftwareSuite")
    def robot_software_suite(self) -> pulumi.Input['RobotApplicationRobotSoftwareSuiteArgs']:
        return pulumi.get(self, "robot_software_suite")

    @robot_software_suite.setter
    def robot_software_suite(self, value: pulumi.Input['RobotApplicationRobotSoftwareSuiteArgs']):
        pulumi.set(self, "robot_software_suite", value)

    @property
    @pulumi.getter(name="currentRevisionId")
    def current_revision_id(self) -> Optional[pulumi.Input[str]]:
        """
        The revision ID of robot application.
        """
        return pulumi.get(self, "current_revision_id")

    @current_revision_id.setter
    def current_revision_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "current_revision_id", value)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[str]]:
        """
        The URI of the Docker image for the robot application.
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the robot application.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RobotApplicationSourceConfigArgs']]]]:
        """
        The sources of the robot application.
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RobotApplicationSourceConfigArgs']]]]):
        pulumi.set(self, "sources", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input['RobotApplicationTagsArgs']]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input['RobotApplicationTagsArgs']]):
        pulumi.set(self, "tags", value)


class RobotApplication(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 current_revision_id: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 robot_software_suite: Optional[pulumi.Input[pulumi.InputType['RobotApplicationRobotSoftwareSuiteArgs']]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RobotApplicationSourceConfigArgs']]]]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['RobotApplicationTagsArgs']]] = None,
                 __props__=None):
        """
        AWS::RoboMaker::RobotApplication resource creates an AWS RoboMaker RobotApplication. Robot application can be used in AWS RoboMaker Simulation Jobs.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] current_revision_id: The revision ID of robot application.
        :param pulumi.Input[str] environment: The URI of the Docker image for the robot application.
        :param pulumi.Input[str] name: The name of the robot application.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RobotApplicationSourceConfigArgs']]]] sources: The sources of the robot application.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RobotApplicationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        AWS::RoboMaker::RobotApplication resource creates an AWS RoboMaker RobotApplication. Robot application can be used in AWS RoboMaker Simulation Jobs.

        :param str resource_name: The name of the resource.
        :param RobotApplicationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RobotApplicationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 current_revision_id: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 robot_software_suite: Optional[pulumi.Input[pulumi.InputType['RobotApplicationRobotSoftwareSuiteArgs']]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RobotApplicationSourceConfigArgs']]]]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['RobotApplicationTagsArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RobotApplicationArgs.__new__(RobotApplicationArgs)

            __props__.__dict__["current_revision_id"] = current_revision_id
            __props__.__dict__["environment"] = environment
            __props__.__dict__["name"] = name
            if robot_software_suite is None and not opts.urn:
                raise TypeError("Missing required property 'robot_software_suite'")
            __props__.__dict__["robot_software_suite"] = robot_software_suite
            __props__.__dict__["sources"] = sources
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        super(RobotApplication, __self__).__init__(
            'aws-native:robomaker:RobotApplication',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RobotApplication':
        """
        Get an existing RobotApplication resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RobotApplicationArgs.__new__(RobotApplicationArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["current_revision_id"] = None
        __props__.__dict__["environment"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["robot_software_suite"] = None
        __props__.__dict__["sources"] = None
        __props__.__dict__["tags"] = None
        return RobotApplication(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="currentRevisionId")
    def current_revision_id(self) -> pulumi.Output[Optional[str]]:
        """
        The revision ID of robot application.
        """
        return pulumi.get(self, "current_revision_id")

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Output[Optional[str]]:
        """
        The URI of the Docker image for the robot application.
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the robot application.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="robotSoftwareSuite")
    def robot_software_suite(self) -> pulumi.Output['outputs.RobotApplicationRobotSoftwareSuite']:
        return pulumi.get(self, "robot_software_suite")

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Output[Optional[Sequence['outputs.RobotApplicationSourceConfig']]]:
        """
        The sources of the robot application.
        """
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional['outputs.RobotApplicationTags']]:
        return pulumi.get(self, "tags")

