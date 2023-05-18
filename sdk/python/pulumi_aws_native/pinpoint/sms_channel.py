# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SMSChannelArgs', 'SMSChannel']

@pulumi.input_type
class SMSChannelArgs:
    def __init__(__self__, *,
                 application_id: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 sender_id: Optional[pulumi.Input[str]] = None,
                 short_code: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SMSChannel resource.
        """
        pulumi.set(__self__, "application_id", application_id)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if sender_id is not None:
            pulumi.set(__self__, "sender_id", sender_id)
        if short_code is not None:
            pulumi.set(__self__, "short_code", short_code)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="senderId")
    def sender_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sender_id")

    @sender_id.setter
    def sender_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sender_id", value)

    @property
    @pulumi.getter(name="shortCode")
    def short_code(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "short_code")

    @short_code.setter
    def short_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "short_code", value)


warnings.warn("""SMSChannel is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class SMSChannel(pulumi.CustomResource):
    warnings.warn("""SMSChannel is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 sender_id: Optional[pulumi.Input[str]] = None,
                 short_code: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Pinpoint::SMSChannel

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SMSChannelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Pinpoint::SMSChannel

        :param str resource_name: The name of the resource.
        :param SMSChannelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SMSChannelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 sender_id: Optional[pulumi.Input[str]] = None,
                 short_code: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""SMSChannel is deprecated: SMSChannel is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SMSChannelArgs.__new__(SMSChannelArgs)

            if application_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_id'")
            __props__.__dict__["application_id"] = application_id
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["sender_id"] = sender_id
            __props__.__dict__["short_code"] = short_code
        super(SMSChannel, __self__).__init__(
            'aws-native:pinpoint:SMSChannel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SMSChannel':
        """
        Get an existing SMSChannel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SMSChannelArgs.__new__(SMSChannelArgs)

        __props__.__dict__["application_id"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["sender_id"] = None
        __props__.__dict__["short_code"] = None
        return SMSChannel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="senderId")
    def sender_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "sender_id")

    @property
    @pulumi.getter(name="shortCode")
    def short_code(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "short_code")

