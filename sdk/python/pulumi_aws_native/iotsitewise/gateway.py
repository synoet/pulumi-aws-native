# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._inputs import *

__all__ = ['GatewayArgs', 'Gateway']

@pulumi.input_type
class GatewayArgs:
    def __init__(__self__, *,
                 gateway_name: pulumi.Input[str],
                 gateway_platform: pulumi.Input['GatewayGatewayPlatformArgs'],
                 gateway_capability_summaries: Optional[pulumi.Input[Sequence[pulumi.Input['GatewayGatewayCapabilitySummaryArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Gateway resource.
        :param pulumi.Input[str] gateway_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayname
        :param pulumi.Input['GatewayGatewayPlatformArgs'] gateway_platform: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayplatform
        :param pulumi.Input[Sequence[pulumi.Input['GatewayGatewayCapabilitySummaryArgs']]] gateway_capability_summaries: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewaycapabilitysummaries
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-tags
        """
        pulumi.set(__self__, "gateway_name", gateway_name)
        pulumi.set(__self__, "gateway_platform", gateway_platform)
        if gateway_capability_summaries is not None:
            pulumi.set(__self__, "gateway_capability_summaries", gateway_capability_summaries)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayname
        """
        return pulumi.get(self, "gateway_name")

    @gateway_name.setter
    def gateway_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "gateway_name", value)

    @property
    @pulumi.getter(name="gatewayPlatform")
    def gateway_platform(self) -> pulumi.Input['GatewayGatewayPlatformArgs']:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayplatform
        """
        return pulumi.get(self, "gateway_platform")

    @gateway_platform.setter
    def gateway_platform(self, value: pulumi.Input['GatewayGatewayPlatformArgs']):
        pulumi.set(self, "gateway_platform", value)

    @property
    @pulumi.getter(name="gatewayCapabilitySummaries")
    def gateway_capability_summaries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GatewayGatewayCapabilitySummaryArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewaycapabilitysummaries
        """
        return pulumi.get(self, "gateway_capability_summaries")

    @gateway_capability_summaries.setter
    def gateway_capability_summaries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GatewayGatewayCapabilitySummaryArgs']]]]):
        pulumi.set(self, "gateway_capability_summaries", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Gateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 gateway_capability_summaries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GatewayGatewayCapabilitySummaryArgs']]]]] = None,
                 gateway_name: Optional[pulumi.Input[str]] = None,
                 gateway_platform: Optional[pulumi.Input[pulumi.InputType['GatewayGatewayPlatformArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GatewayGatewayCapabilitySummaryArgs']]]] gateway_capability_summaries: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewaycapabilitysummaries
        :param pulumi.Input[str] gateway_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayname
        :param pulumi.Input[pulumi.InputType['GatewayGatewayPlatformArgs']] gateway_platform: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayplatform
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html

        :param str resource_name: The name of the resource.
        :param GatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 gateway_capability_summaries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GatewayGatewayCapabilitySummaryArgs']]]]] = None,
                 gateway_name: Optional[pulumi.Input[str]] = None,
                 gateway_platform: Optional[pulumi.Input[pulumi.InputType['GatewayGatewayPlatformArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GatewayArgs.__new__(GatewayArgs)

            __props__.__dict__["gateway_capability_summaries"] = gateway_capability_summaries
            if gateway_name is None and not opts.urn:
                raise TypeError("Missing required property 'gateway_name'")
            __props__.__dict__["gateway_name"] = gateway_name
            if gateway_platform is None and not opts.urn:
                raise TypeError("Missing required property 'gateway_platform'")
            __props__.__dict__["gateway_platform"] = gateway_platform
            __props__.__dict__["tags"] = tags
            __props__.__dict__["gateway_id"] = None
        super(Gateway, __self__).__init__(
            'aws-native:iotsitewise:Gateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Gateway':
        """
        Get an existing Gateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GatewayArgs.__new__(GatewayArgs)

        __props__.__dict__["gateway_capability_summaries"] = None
        __props__.__dict__["gateway_id"] = None
        __props__.__dict__["gateway_name"] = None
        __props__.__dict__["gateway_platform"] = None
        __props__.__dict__["tags"] = None
        return Gateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="gatewayCapabilitySummaries")
    def gateway_capability_summaries(self) -> pulumi.Output[Optional[Sequence['outputs.GatewayGatewayCapabilitySummary']]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewaycapabilitysummaries
        """
        return pulumi.get(self, "gateway_capability_summaries")

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "gateway_id")

    @property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> pulumi.Output[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayname
        """
        return pulumi.get(self, "gateway_name")

    @property
    @pulumi.getter(name="gatewayPlatform")
    def gateway_platform(self) -> pulumi.Output['outputs.GatewayGatewayPlatform']:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayplatform
        """
        return pulumi.get(self, "gateway_platform")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-tags
        """
        return pulumi.get(self, "tags")

