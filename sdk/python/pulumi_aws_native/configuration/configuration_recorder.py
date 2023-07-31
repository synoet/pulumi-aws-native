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

__all__ = ['ConfigurationRecorderArgs', 'ConfigurationRecorder']

@pulumi.input_type
class ConfigurationRecorderArgs:
    def __init__(__self__, *,
                 role_arn: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 recording_group: Optional[pulumi.Input['ConfigurationRecorderRecordingGroupArgs']] = None):
        """
        The set of arguments for constructing a ConfigurationRecorder resource.
        """
        pulumi.set(__self__, "role_arn", role_arn)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if recording_group is not None:
            pulumi.set(__self__, "recording_group", recording_group)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="recordingGroup")
    def recording_group(self) -> Optional[pulumi.Input['ConfigurationRecorderRecordingGroupArgs']]:
        return pulumi.get(self, "recording_group")

    @recording_group.setter
    def recording_group(self, value: Optional[pulumi.Input['ConfigurationRecorderRecordingGroupArgs']]):
        pulumi.set(self, "recording_group", value)


warnings.warn("""ConfigurationRecorder is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ConfigurationRecorder(pulumi.CustomResource):
    warnings.warn("""ConfigurationRecorder is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recording_group: Optional[pulumi.Input[pulumi.InputType['ConfigurationRecorderRecordingGroupArgs']]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Config::ConfigurationRecorder

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigurationRecorderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Config::ConfigurationRecorder

        :param str resource_name: The name of the resource.
        :param ConfigurationRecorderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigurationRecorderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recording_group: Optional[pulumi.Input[pulumi.InputType['ConfigurationRecorderRecordingGroupArgs']]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""ConfigurationRecorder is deprecated: ConfigurationRecorder is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigurationRecorderArgs.__new__(ConfigurationRecorderArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["recording_group"] = recording_group
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
        super(ConfigurationRecorder, __self__).__init__(
            'aws-native:configuration:ConfigurationRecorder',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConfigurationRecorder':
        """
        Get an existing ConfigurationRecorder resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConfigurationRecorderArgs.__new__(ConfigurationRecorderArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["recording_group"] = None
        __props__.__dict__["role_arn"] = None
        return ConfigurationRecorder(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recordingGroup")
    def recording_group(self) -> pulumi.Output[Optional['outputs.ConfigurationRecorderRecordingGroup']]:
        return pulumi.get(self, "recording_group")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "role_arn")

