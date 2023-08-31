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

__all__ = ['ResourceSpecificLoggingArgs', 'ResourceSpecificLogging']

@pulumi.input_type
class ResourceSpecificLoggingArgs:
    def __init__(__self__, *,
                 log_level: pulumi.Input['ResourceSpecificLoggingLogLevel'],
                 target_name: pulumi.Input[str],
                 target_type: pulumi.Input['ResourceSpecificLoggingTargetType']):
        """
        The set of arguments for constructing a ResourceSpecificLogging resource.
        :param pulumi.Input['ResourceSpecificLoggingLogLevel'] log_level: The log level for a specific target. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.
        :param pulumi.Input[str] target_name: The target name.
        :param pulumi.Input['ResourceSpecificLoggingTargetType'] target_type: The target type. Value must be THING_GROUP, CLIENT_ID, SOURCE_IP, PRINCIPAL_ID, or EVENT_TYPE.
        """
        pulumi.set(__self__, "log_level", log_level)
        pulumi.set(__self__, "target_name", target_name)
        pulumi.set(__self__, "target_type", target_type)

    @property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> pulumi.Input['ResourceSpecificLoggingLogLevel']:
        """
        The log level for a specific target. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.
        """
        return pulumi.get(self, "log_level")

    @log_level.setter
    def log_level(self, value: pulumi.Input['ResourceSpecificLoggingLogLevel']):
        pulumi.set(self, "log_level", value)

    @property
    @pulumi.getter(name="targetName")
    def target_name(self) -> pulumi.Input[str]:
        """
        The target name.
        """
        return pulumi.get(self, "target_name")

    @target_name.setter
    def target_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_name", value)

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Input['ResourceSpecificLoggingTargetType']:
        """
        The target type. Value must be THING_GROUP, CLIENT_ID, SOURCE_IP, PRINCIPAL_ID, or EVENT_TYPE.
        """
        return pulumi.get(self, "target_type")

    @target_type.setter
    def target_type(self, value: pulumi.Input['ResourceSpecificLoggingTargetType']):
        pulumi.set(self, "target_type", value)


class ResourceSpecificLogging(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 log_level: Optional[pulumi.Input['ResourceSpecificLoggingLogLevel']] = None,
                 target_name: Optional[pulumi.Input[str]] = None,
                 target_type: Optional[pulumi.Input['ResourceSpecificLoggingTargetType']] = None,
                 __props__=None):
        """
        Resource-specific logging allows you to specify a logging level for a specific thing group.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['ResourceSpecificLoggingLogLevel'] log_level: The log level for a specific target. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.
        :param pulumi.Input[str] target_name: The target name.
        :param pulumi.Input['ResourceSpecificLoggingTargetType'] target_type: The target type. Value must be THING_GROUP, CLIENT_ID, SOURCE_IP, PRINCIPAL_ID, or EVENT_TYPE.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResourceSpecificLoggingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource-specific logging allows you to specify a logging level for a specific thing group.

        :param str resource_name: The name of the resource.
        :param ResourceSpecificLoggingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResourceSpecificLoggingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 log_level: Optional[pulumi.Input['ResourceSpecificLoggingLogLevel']] = None,
                 target_name: Optional[pulumi.Input[str]] = None,
                 target_type: Optional[pulumi.Input['ResourceSpecificLoggingTargetType']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResourceSpecificLoggingArgs.__new__(ResourceSpecificLoggingArgs)

            if log_level is None and not opts.urn:
                raise TypeError("Missing required property 'log_level'")
            __props__.__dict__["log_level"] = log_level
            if target_name is None and not opts.urn:
                raise TypeError("Missing required property 'target_name'")
            __props__.__dict__["target_name"] = target_name
            if target_type is None and not opts.urn:
                raise TypeError("Missing required property 'target_type'")
            __props__.__dict__["target_type"] = target_type
            __props__.__dict__["target_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["target_name", "target_type"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ResourceSpecificLogging, __self__).__init__(
            'aws-native:iot:ResourceSpecificLogging',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ResourceSpecificLogging':
        """
        Get an existing ResourceSpecificLogging resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ResourceSpecificLoggingArgs.__new__(ResourceSpecificLoggingArgs)

        __props__.__dict__["log_level"] = None
        __props__.__dict__["target_id"] = None
        __props__.__dict__["target_name"] = None
        __props__.__dict__["target_type"] = None
        return ResourceSpecificLogging(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> pulumi.Output['ResourceSpecificLoggingLogLevel']:
        """
        The log level for a specific target. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.
        """
        return pulumi.get(self, "log_level")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Output[str]:
        """
        Unique Id for a Target (TargetType:TargetName), this will be internally built to serve as primary identifier for a log target.
        """
        return pulumi.get(self, "target_id")

    @property
    @pulumi.getter(name="targetName")
    def target_name(self) -> pulumi.Output[str]:
        """
        The target name.
        """
        return pulumi.get(self, "target_name")

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Output['ResourceSpecificLoggingTargetType']:
        """
        The target type. Value must be THING_GROUP, CLIENT_ID, SOURCE_IP, PRINCIPAL_ID, or EVENT_TYPE.
        """
        return pulumi.get(self, "target_type")

