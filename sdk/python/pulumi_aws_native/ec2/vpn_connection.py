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

__all__ = ['VpnConnectionArgs', 'VpnConnection']

@pulumi.input_type
class VpnConnectionArgs:
    def __init__(__self__, *,
                 customer_gateway_id: pulumi.Input[str],
                 type: pulumi.Input[str],
                 static_routes_only: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['VpnConnectionTagArgs']]]] = None,
                 transit_gateway_id: Optional[pulumi.Input[str]] = None,
                 vpn_gateway_id: Optional[pulumi.Input[str]] = None,
                 vpn_tunnel_options_specifications: Optional[pulumi.Input[Sequence[pulumi.Input['VpnConnectionVpnTunnelOptionsSpecificationArgs']]]] = None):
        """
        The set of arguments for constructing a VpnConnection resource.
        :param pulumi.Input[str] customer_gateway_id: The ID of the customer gateway at your end of the VPN connection.
        :param pulumi.Input[str] type: The type of VPN connection.
        :param pulumi.Input[bool] static_routes_only: Indicates whether the VPN connection uses static routes only.
        :param pulumi.Input[Sequence[pulumi.Input['VpnConnectionTagArgs']]] tags: Any tags assigned to the VPN connection.
        :param pulumi.Input[str] transit_gateway_id: The ID of the transit gateway associated with the VPN connection.
        :param pulumi.Input[str] vpn_gateway_id: The ID of the virtual private gateway at the AWS side of the VPN connection.
        :param pulumi.Input[Sequence[pulumi.Input['VpnConnectionVpnTunnelOptionsSpecificationArgs']]] vpn_tunnel_options_specifications: The tunnel options for the VPN connection.
        """
        pulumi.set(__self__, "customer_gateway_id", customer_gateway_id)
        pulumi.set(__self__, "type", type)
        if static_routes_only is not None:
            pulumi.set(__self__, "static_routes_only", static_routes_only)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if transit_gateway_id is not None:
            pulumi.set(__self__, "transit_gateway_id", transit_gateway_id)
        if vpn_gateway_id is not None:
            pulumi.set(__self__, "vpn_gateway_id", vpn_gateway_id)
        if vpn_tunnel_options_specifications is not None:
            pulumi.set(__self__, "vpn_tunnel_options_specifications", vpn_tunnel_options_specifications)

    @property
    @pulumi.getter(name="customerGatewayId")
    def customer_gateway_id(self) -> pulumi.Input[str]:
        """
        The ID of the customer gateway at your end of the VPN connection.
        """
        return pulumi.get(self, "customer_gateway_id")

    @customer_gateway_id.setter
    def customer_gateway_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "customer_gateway_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of VPN connection.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="staticRoutesOnly")
    def static_routes_only(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the VPN connection uses static routes only.
        """
        return pulumi.get(self, "static_routes_only")

    @static_routes_only.setter
    def static_routes_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "static_routes_only", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpnConnectionTagArgs']]]]:
        """
        Any tags assigned to the VPN connection.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpnConnectionTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the transit gateway associated with the VPN connection.
        """
        return pulumi.get(self, "transit_gateway_id")

    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transit_gateway_id", value)

    @property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the virtual private gateway at the AWS side of the VPN connection.
        """
        return pulumi.get(self, "vpn_gateway_id")

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpn_gateway_id", value)

    @property
    @pulumi.getter(name="vpnTunnelOptionsSpecifications")
    def vpn_tunnel_options_specifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpnConnectionVpnTunnelOptionsSpecificationArgs']]]]:
        """
        The tunnel options for the VPN connection.
        """
        return pulumi.get(self, "vpn_tunnel_options_specifications")

    @vpn_tunnel_options_specifications.setter
    def vpn_tunnel_options_specifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpnConnectionVpnTunnelOptionsSpecificationArgs']]]]):
        pulumi.set(self, "vpn_tunnel_options_specifications", value)


class VpnConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 customer_gateway_id: Optional[pulumi.Input[str]] = None,
                 static_routes_only: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnConnectionTagArgs']]]]] = None,
                 transit_gateway_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vpn_gateway_id: Optional[pulumi.Input[str]] = None,
                 vpn_tunnel_options_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnConnectionVpnTunnelOptionsSpecificationArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::VPNConnection

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] customer_gateway_id: The ID of the customer gateway at your end of the VPN connection.
        :param pulumi.Input[bool] static_routes_only: Indicates whether the VPN connection uses static routes only.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnConnectionTagArgs']]]] tags: Any tags assigned to the VPN connection.
        :param pulumi.Input[str] transit_gateway_id: The ID of the transit gateway associated with the VPN connection.
        :param pulumi.Input[str] type: The type of VPN connection.
        :param pulumi.Input[str] vpn_gateway_id: The ID of the virtual private gateway at the AWS side of the VPN connection.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnConnectionVpnTunnelOptionsSpecificationArgs']]]] vpn_tunnel_options_specifications: The tunnel options for the VPN connection.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpnConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::VPNConnection

        :param str resource_name: The name of the resource.
        :param VpnConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpnConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 customer_gateway_id: Optional[pulumi.Input[str]] = None,
                 static_routes_only: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnConnectionTagArgs']]]]] = None,
                 transit_gateway_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vpn_gateway_id: Optional[pulumi.Input[str]] = None,
                 vpn_tunnel_options_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnConnectionVpnTunnelOptionsSpecificationArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpnConnectionArgs.__new__(VpnConnectionArgs)

            if customer_gateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'customer_gateway_id'")
            __props__.__dict__["customer_gateway_id"] = customer_gateway_id
            __props__.__dict__["static_routes_only"] = static_routes_only
            __props__.__dict__["tags"] = tags
            __props__.__dict__["transit_gateway_id"] = transit_gateway_id
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["vpn_gateway_id"] = vpn_gateway_id
            __props__.__dict__["vpn_tunnel_options_specifications"] = vpn_tunnel_options_specifications
            __props__.__dict__["vpn_connection_id"] = None
        super(VpnConnection, __self__).__init__(
            'aws-native:ec2:VpnConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VpnConnection':
        """
        Get an existing VpnConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VpnConnectionArgs.__new__(VpnConnectionArgs)

        __props__.__dict__["customer_gateway_id"] = None
        __props__.__dict__["static_routes_only"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["transit_gateway_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vpn_connection_id"] = None
        __props__.__dict__["vpn_gateway_id"] = None
        __props__.__dict__["vpn_tunnel_options_specifications"] = None
        return VpnConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customerGatewayId")
    def customer_gateway_id(self) -> pulumi.Output[str]:
        """
        The ID of the customer gateway at your end of the VPN connection.
        """
        return pulumi.get(self, "customer_gateway_id")

    @property
    @pulumi.getter(name="staticRoutesOnly")
    def static_routes_only(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the VPN connection uses static routes only.
        """
        return pulumi.get(self, "static_routes_only")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.VpnConnectionTag']]]:
        """
        Any tags assigned to the VPN connection.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the transit gateway associated with the VPN connection.
        """
        return pulumi.get(self, "transit_gateway_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of VPN connection.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vpnConnectionId")
    def vpn_connection_id(self) -> pulumi.Output[str]:
        """
        The provider-assigned unique ID for this managed resource
        """
        return pulumi.get(self, "vpn_connection_id")

    @property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the virtual private gateway at the AWS side of the VPN connection.
        """
        return pulumi.get(self, "vpn_gateway_id")

    @property
    @pulumi.getter(name="vpnTunnelOptionsSpecifications")
    def vpn_tunnel_options_specifications(self) -> pulumi.Output[Optional[Sequence['outputs.VpnConnectionVpnTunnelOptionsSpecification']]]:
        """
        The tunnel options for the VPN connection.
        """
        return pulumi.get(self, "vpn_tunnel_options_specifications")

