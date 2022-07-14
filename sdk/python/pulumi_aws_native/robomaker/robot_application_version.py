# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['RobotApplicationVersionArgs', 'RobotApplicationVersion']

@pulumi.input_type
class RobotApplicationVersionArgs:
    def __init__(__self__, *,
                 application: pulumi.Input[str],
                 current_revision_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RobotApplicationVersion resource.
        :param pulumi.Input[str] current_revision_id: The revision ID of robot application.
        """
        pulumi.set(__self__, "application", application)
        if current_revision_id is not None:
            pulumi.set(__self__, "current_revision_id", current_revision_id)

    @property
    @pulumi.getter
    def application(self) -> pulumi.Input[str]:
        return pulumi.get(self, "application")

    @application.setter
    def application(self, value: pulumi.Input[str]):
        pulumi.set(self, "application", value)

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


class RobotApplicationVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application: Optional[pulumi.Input[str]] = None,
                 current_revision_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        AWS::RoboMaker::RobotApplicationVersion resource creates an AWS RoboMaker RobotApplicationVersion. This helps you control which code your robot uses.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] current_revision_id: The revision ID of robot application.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RobotApplicationVersionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        AWS::RoboMaker::RobotApplicationVersion resource creates an AWS RoboMaker RobotApplicationVersion. This helps you control which code your robot uses.

        :param str resource_name: The name of the resource.
        :param RobotApplicationVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RobotApplicationVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application: Optional[pulumi.Input[str]] = None,
                 current_revision_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RobotApplicationVersionArgs.__new__(RobotApplicationVersionArgs)

            if application is None and not opts.urn:
                raise TypeError("Missing required property 'application'")
            __props__.__dict__["application"] = application
            __props__.__dict__["current_revision_id"] = current_revision_id
            __props__.__dict__["application_version"] = None
            __props__.__dict__["arn"] = None
        super(RobotApplicationVersion, __self__).__init__(
            'aws-native:robomaker:RobotApplicationVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RobotApplicationVersion':
        """
        Get an existing RobotApplicationVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RobotApplicationVersionArgs.__new__(RobotApplicationVersionArgs)

        __props__.__dict__["application"] = None
        __props__.__dict__["application_version"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["current_revision_id"] = None
        return RobotApplicationVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def application(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application")

    @property
    @pulumi.getter(name="applicationVersion")
    def application_version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_version")

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

