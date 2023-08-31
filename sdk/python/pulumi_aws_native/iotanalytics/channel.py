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

__all__ = ['ChannelArgs', 'Channel']

@pulumi.input_type
class ChannelArgs:
    def __init__(__self__, *,
                 channel_name: Optional[pulumi.Input[str]] = None,
                 channel_storage: Optional[pulumi.Input['ChannelStorageArgs']] = None,
                 retention_period: Optional[pulumi.Input['ChannelRetentionPeriodArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ChannelTagArgs']]]] = None):
        """
        The set of arguments for constructing a Channel resource.
        """
        if channel_name is not None:
            pulumi.set(__self__, "channel_name", channel_name)
        if channel_storage is not None:
            pulumi.set(__self__, "channel_storage", channel_storage)
        if retention_period is not None:
            pulumi.set(__self__, "retention_period", retention_period)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "channel_name")

    @channel_name.setter
    def channel_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "channel_name", value)

    @property
    @pulumi.getter(name="channelStorage")
    def channel_storage(self) -> Optional[pulumi.Input['ChannelStorageArgs']]:
        return pulumi.get(self, "channel_storage")

    @channel_storage.setter
    def channel_storage(self, value: Optional[pulumi.Input['ChannelStorageArgs']]):
        pulumi.set(self, "channel_storage", value)

    @property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input['ChannelRetentionPeriodArgs']]:
        return pulumi.get(self, "retention_period")

    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input['ChannelRetentionPeriodArgs']]):
        pulumi.set(self, "retention_period", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ChannelTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ChannelTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Channel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 channel_name: Optional[pulumi.Input[str]] = None,
                 channel_storage: Optional[pulumi.Input[pulumi.InputType['ChannelStorageArgs']]] = None,
                 retention_period: Optional[pulumi.Input[pulumi.InputType['ChannelRetentionPeriodArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChannelTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::IoTAnalytics::Channel

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ChannelArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::IoTAnalytics::Channel

        :param str resource_name: The name of the resource.
        :param ChannelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ChannelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 channel_name: Optional[pulumi.Input[str]] = None,
                 channel_storage: Optional[pulumi.Input[pulumi.InputType['ChannelStorageArgs']]] = None,
                 retention_period: Optional[pulumi.Input[pulumi.InputType['ChannelRetentionPeriodArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChannelTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ChannelArgs.__new__(ChannelArgs)

            __props__.__dict__["channel_name"] = channel_name
            __props__.__dict__["channel_storage"] = channel_storage
            __props__.__dict__["retention_period"] = retention_period
            __props__.__dict__["tags"] = tags
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["channel_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Channel, __self__).__init__(
            'aws-native:iotanalytics:Channel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Channel':
        """
        Get an existing Channel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ChannelArgs.__new__(ChannelArgs)

        __props__.__dict__["channel_name"] = None
        __props__.__dict__["channel_storage"] = None
        __props__.__dict__["retention_period"] = None
        __props__.__dict__["tags"] = None
        return Channel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "channel_name")

    @property
    @pulumi.getter(name="channelStorage")
    def channel_storage(self) -> pulumi.Output[Optional['outputs.ChannelStorage']]:
        return pulumi.get(self, "channel_storage")

    @property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> pulumi.Output[Optional['outputs.ChannelRetentionPeriod']]:
        return pulumi.get(self, "retention_period")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ChannelTag']]]:
        return pulumi.get(self, "tags")

