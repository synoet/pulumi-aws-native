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

__all__ = ['NetworkInsightsPathArgs', 'NetworkInsightsPath']

@pulumi.input_type
class NetworkInsightsPathArgs:
    def __init__(__self__, *,
                 protocol: pulumi.Input['NetworkInsightsPathProtocol'],
                 source: pulumi.Input[str],
                 destination: Optional[pulumi.Input[str]] = None,
                 destination_ip: Optional[pulumi.Input[str]] = None,
                 destination_port: Optional[pulumi.Input[int]] = None,
                 filter_at_destination: Optional[pulumi.Input['NetworkInsightsPathPathFilterArgs']] = None,
                 filter_at_source: Optional[pulumi.Input['NetworkInsightsPathPathFilterArgs']] = None,
                 source_ip: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsPathTagArgs']]]] = None):
        """
        The set of arguments for constructing a NetworkInsightsPath resource.
        """
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "source", source)
        if destination is not None:
            pulumi.set(__self__, "destination", destination)
        if destination_ip is not None:
            pulumi.set(__self__, "destination_ip", destination_ip)
        if destination_port is not None:
            pulumi.set(__self__, "destination_port", destination_port)
        if filter_at_destination is not None:
            pulumi.set(__self__, "filter_at_destination", filter_at_destination)
        if filter_at_source is not None:
            pulumi.set(__self__, "filter_at_source", filter_at_source)
        if source_ip is not None:
            pulumi.set(__self__, "source_ip", source_ip)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input['NetworkInsightsPathProtocol']:
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input['NetworkInsightsPathProtocol']):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[str]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter(name="destinationIp")
    def destination_ip(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "destination_ip")

    @destination_ip.setter
    def destination_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_ip", value)

    @property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "destination_port")

    @destination_port.setter
    def destination_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "destination_port", value)

    @property
    @pulumi.getter(name="filterAtDestination")
    def filter_at_destination(self) -> Optional[pulumi.Input['NetworkInsightsPathPathFilterArgs']]:
        return pulumi.get(self, "filter_at_destination")

    @filter_at_destination.setter
    def filter_at_destination(self, value: Optional[pulumi.Input['NetworkInsightsPathPathFilterArgs']]):
        pulumi.set(self, "filter_at_destination", value)

    @property
    @pulumi.getter(name="filterAtSource")
    def filter_at_source(self) -> Optional[pulumi.Input['NetworkInsightsPathPathFilterArgs']]:
        return pulumi.get(self, "filter_at_source")

    @filter_at_source.setter
    def filter_at_source(self, value: Optional[pulumi.Input['NetworkInsightsPathPathFilterArgs']]):
        pulumi.set(self, "filter_at_source", value)

    @property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_ip")

    @source_ip.setter
    def source_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_ip", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsPathTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsPathTagArgs']]]]):
        pulumi.set(self, "tags", value)


class NetworkInsightsPath(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 destination_ip: Optional[pulumi.Input[str]] = None,
                 destination_port: Optional[pulumi.Input[int]] = None,
                 filter_at_destination: Optional[pulumi.Input[pulumi.InputType['NetworkInsightsPathPathFilterArgs']]] = None,
                 filter_at_source: Optional[pulumi.Input[pulumi.InputType['NetworkInsightsPathPathFilterArgs']]] = None,
                 protocol: Optional[pulumi.Input['NetworkInsightsPathProtocol']] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 source_ip: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInsightsPathTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::EC2::NetworkInsightsPath

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkInsightsPathArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::EC2::NetworkInsightsPath

        :param str resource_name: The name of the resource.
        :param NetworkInsightsPathArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkInsightsPathArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 destination_ip: Optional[pulumi.Input[str]] = None,
                 destination_port: Optional[pulumi.Input[int]] = None,
                 filter_at_destination: Optional[pulumi.Input[pulumi.InputType['NetworkInsightsPathPathFilterArgs']]] = None,
                 filter_at_source: Optional[pulumi.Input[pulumi.InputType['NetworkInsightsPathPathFilterArgs']]] = None,
                 protocol: Optional[pulumi.Input['NetworkInsightsPathProtocol']] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 source_ip: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInsightsPathTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkInsightsPathArgs.__new__(NetworkInsightsPathArgs)

            __props__.__dict__["destination"] = destination
            __props__.__dict__["destination_ip"] = destination_ip
            __props__.__dict__["destination_port"] = destination_port
            __props__.__dict__["filter_at_destination"] = filter_at_destination
            __props__.__dict__["filter_at_source"] = filter_at_source
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__.__dict__["source"] = source
            __props__.__dict__["source_ip"] = source_ip
            __props__.__dict__["tags"] = tags
            __props__.__dict__["created_date"] = None
            __props__.__dict__["destination_arn"] = None
            __props__.__dict__["network_insights_path_arn"] = None
            __props__.__dict__["network_insights_path_id"] = None
            __props__.__dict__["source_arn"] = None
        super(NetworkInsightsPath, __self__).__init__(
            'aws-native:ec2:NetworkInsightsPath',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkInsightsPath':
        """
        Get an existing NetworkInsightsPath resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkInsightsPathArgs.__new__(NetworkInsightsPathArgs)

        __props__.__dict__["created_date"] = None
        __props__.__dict__["destination"] = None
        __props__.__dict__["destination_arn"] = None
        __props__.__dict__["destination_ip"] = None
        __props__.__dict__["destination_port"] = None
        __props__.__dict__["filter_at_destination"] = None
        __props__.__dict__["filter_at_source"] = None
        __props__.__dict__["network_insights_path_arn"] = None
        __props__.__dict__["network_insights_path_id"] = None
        __props__.__dict__["protocol"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["source_arn"] = None
        __props__.__dict__["source_ip"] = None
        __props__.__dict__["tags"] = None
        return NetworkInsightsPath(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "destination_arn")

    @property
    @pulumi.getter(name="destinationIp")
    def destination_ip(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "destination_ip")

    @property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "destination_port")

    @property
    @pulumi.getter(name="filterAtDestination")
    def filter_at_destination(self) -> pulumi.Output[Optional['outputs.NetworkInsightsPathPathFilter']]:
        return pulumi.get(self, "filter_at_destination")

    @property
    @pulumi.getter(name="filterAtSource")
    def filter_at_source(self) -> pulumi.Output[Optional['outputs.NetworkInsightsPathPathFilter']]:
        return pulumi.get(self, "filter_at_source")

    @property
    @pulumi.getter(name="networkInsightsPathArn")
    def network_insights_path_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "network_insights_path_arn")

    @property
    @pulumi.getter(name="networkInsightsPathId")
    def network_insights_path_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "network_insights_path_id")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output['NetworkInsightsPathProtocol']:
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[str]:
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "source_arn")

    @property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "source_ip")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.NetworkInsightsPathTag']]]:
        return pulumi.get(self, "tags")

