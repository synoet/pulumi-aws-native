# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['EventStreamArgs', 'EventStream']

@pulumi.input_type
class EventStreamArgs:
    def __init__(__self__, *,
                 application_id: pulumi.Input[str],
                 destination_stream_arn: pulumi.Input[str],
                 role_arn: pulumi.Input[str]):
        """
        The set of arguments for constructing a EventStream resource.
        """
        pulumi.set(__self__, "application_id", application_id)
        pulumi.set(__self__, "destination_stream_arn", destination_stream_arn)
        pulumi.set(__self__, "role_arn", role_arn)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter(name="destinationStreamArn")
    def destination_stream_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "destination_stream_arn")

    @destination_stream_arn.setter
    def destination_stream_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination_stream_arn", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)


warnings.warn("""EventStream is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class EventStream(pulumi.CustomResource):
    warnings.warn("""EventStream is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 destination_stream_arn: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Pinpoint::EventStream

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EventStreamArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Pinpoint::EventStream

        :param str resource_name: The name of the resource.
        :param EventStreamArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EventStreamArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 destination_stream_arn: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""EventStream is deprecated: EventStream is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EventStreamArgs.__new__(EventStreamArgs)

            if application_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_id'")
            __props__.__dict__["application_id"] = application_id
            if destination_stream_arn is None and not opts.urn:
                raise TypeError("Missing required property 'destination_stream_arn'")
            __props__.__dict__["destination_stream_arn"] = destination_stream_arn
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
        super(EventStream, __self__).__init__(
            'aws-native:pinpoint:EventStream',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EventStream':
        """
        Get an existing EventStream resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EventStreamArgs.__new__(EventStreamArgs)

        __props__.__dict__["application_id"] = None
        __props__.__dict__["destination_stream_arn"] = None
        __props__.__dict__["role_arn"] = None
        return EventStream(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="destinationStreamArn")
    def destination_stream_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "destination_stream_arn")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "role_arn")

