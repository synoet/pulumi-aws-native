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

__all__ = ['SubnetArgs', 'Subnet']

@pulumi.input_type
class SubnetArgs:
    def __init__(__self__, *,
                 vpc_id: pulumi.Input[str],
                 assign_ipv6_address_on_creation: Optional[pulumi.Input[bool]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 availability_zone_id: Optional[pulumi.Input[str]] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 enable_dns64: Optional[pulumi.Input[bool]] = None,
                 ipv4_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv4_netmask_length: Optional[pulumi.Input[int]] = None,
                 ipv6_cidr_block: Optional[pulumi.Input[str]] = None,
                 ipv6_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ipv6_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv6_native: Optional[pulumi.Input[bool]] = None,
                 ipv6_netmask_length: Optional[pulumi.Input[int]] = None,
                 map_public_ip_on_launch: Optional[pulumi.Input[bool]] = None,
                 outpost_arn: Optional[pulumi.Input[str]] = None,
                 private_dns_name_options_on_launch: Optional[pulumi.Input['PrivateDnsNameOptionsOnLaunchPropertiesArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetTagArgs']]]] = None):
        """
        The set of arguments for constructing a Subnet resource.
        :param pulumi.Input[str] ipv4_ipam_pool_id: The ID of an IPv4 IPAM pool you want to use for allocating this subnet's CIDR
        :param pulumi.Input[int] ipv4_netmask_length: The netmask length of the IPv4 CIDR you want to allocate to this subnet from an Amazon VPC IP Address Manager (IPAM) pool
        :param pulumi.Input[str] ipv6_ipam_pool_id: The ID of an IPv6 IPAM pool you want to use for allocating this subnet's CIDR
        :param pulumi.Input[int] ipv6_netmask_length: The netmask length of the IPv6 CIDR you want to allocate to this subnet from an Amazon VPC IP Address Manager (IPAM) pool
        """
        pulumi.set(__self__, "vpc_id", vpc_id)
        if assign_ipv6_address_on_creation is not None:
            pulumi.set(__self__, "assign_ipv6_address_on_creation", assign_ipv6_address_on_creation)
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if availability_zone_id is not None:
            pulumi.set(__self__, "availability_zone_id", availability_zone_id)
        if cidr_block is not None:
            pulumi.set(__self__, "cidr_block", cidr_block)
        if enable_dns64 is not None:
            pulumi.set(__self__, "enable_dns64", enable_dns64)
        if ipv4_ipam_pool_id is not None:
            pulumi.set(__self__, "ipv4_ipam_pool_id", ipv4_ipam_pool_id)
        if ipv4_netmask_length is not None:
            pulumi.set(__self__, "ipv4_netmask_length", ipv4_netmask_length)
        if ipv6_cidr_block is not None:
            pulumi.set(__self__, "ipv6_cidr_block", ipv6_cidr_block)
        if ipv6_cidr_blocks is not None:
            pulumi.set(__self__, "ipv6_cidr_blocks", ipv6_cidr_blocks)
        if ipv6_ipam_pool_id is not None:
            pulumi.set(__self__, "ipv6_ipam_pool_id", ipv6_ipam_pool_id)
        if ipv6_native is not None:
            pulumi.set(__self__, "ipv6_native", ipv6_native)
        if ipv6_netmask_length is not None:
            pulumi.set(__self__, "ipv6_netmask_length", ipv6_netmask_length)
        if map_public_ip_on_launch is not None:
            pulumi.set(__self__, "map_public_ip_on_launch", map_public_ip_on_launch)
        if outpost_arn is not None:
            pulumi.set(__self__, "outpost_arn", outpost_arn)
        if private_dns_name_options_on_launch is not None:
            pulumi.set(__self__, "private_dns_name_options_on_launch", private_dns_name_options_on_launch)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter(name="assignIpv6AddressOnCreation")
    def assign_ipv6_address_on_creation(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "assign_ipv6_address_on_creation")

    @assign_ipv6_address_on_creation.setter
    def assign_ipv6_address_on_creation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "assign_ipv6_address_on_creation", value)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "availability_zone_id")

    @availability_zone_id.setter
    def availability_zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone_id", value)

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cidr_block")

    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr_block", value)

    @property
    @pulumi.getter(name="enableDns64")
    def enable_dns64(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_dns64")

    @enable_dns64.setter
    def enable_dns64(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_dns64", value)

    @property
    @pulumi.getter(name="ipv4IpamPoolId")
    def ipv4_ipam_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of an IPv4 IPAM pool you want to use for allocating this subnet's CIDR
        """
        return pulumi.get(self, "ipv4_ipam_pool_id")

    @ipv4_ipam_pool_id.setter
    def ipv4_ipam_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv4_ipam_pool_id", value)

    @property
    @pulumi.getter(name="ipv4NetmaskLength")
    def ipv4_netmask_length(self) -> Optional[pulumi.Input[int]]:
        """
        The netmask length of the IPv4 CIDR you want to allocate to this subnet from an Amazon VPC IP Address Manager (IPAM) pool
        """
        return pulumi.get(self, "ipv4_netmask_length")

    @ipv4_netmask_length.setter
    def ipv4_netmask_length(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ipv4_netmask_length", value)

    @property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ipv6_cidr_block")

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_cidr_block", value)

    @property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "ipv6_cidr_blocks")

    @ipv6_cidr_blocks.setter
    def ipv6_cidr_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ipv6_cidr_blocks", value)

    @property
    @pulumi.getter(name="ipv6IpamPoolId")
    def ipv6_ipam_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of an IPv6 IPAM pool you want to use for allocating this subnet's CIDR
        """
        return pulumi.get(self, "ipv6_ipam_pool_id")

    @ipv6_ipam_pool_id.setter
    def ipv6_ipam_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_ipam_pool_id", value)

    @property
    @pulumi.getter(name="ipv6Native")
    def ipv6_native(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "ipv6_native")

    @ipv6_native.setter
    def ipv6_native(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ipv6_native", value)

    @property
    @pulumi.getter(name="ipv6NetmaskLength")
    def ipv6_netmask_length(self) -> Optional[pulumi.Input[int]]:
        """
        The netmask length of the IPv6 CIDR you want to allocate to this subnet from an Amazon VPC IP Address Manager (IPAM) pool
        """
        return pulumi.get(self, "ipv6_netmask_length")

    @ipv6_netmask_length.setter
    def ipv6_netmask_length(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ipv6_netmask_length", value)

    @property
    @pulumi.getter(name="mapPublicIpOnLaunch")
    def map_public_ip_on_launch(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "map_public_ip_on_launch")

    @map_public_ip_on_launch.setter
    def map_public_ip_on_launch(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "map_public_ip_on_launch", value)

    @property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "outpost_arn")

    @outpost_arn.setter
    def outpost_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "outpost_arn", value)

    @property
    @pulumi.getter(name="privateDnsNameOptionsOnLaunch")
    def private_dns_name_options_on_launch(self) -> Optional[pulumi.Input['PrivateDnsNameOptionsOnLaunchPropertiesArgs']]:
        return pulumi.get(self, "private_dns_name_options_on_launch")

    @private_dns_name_options_on_launch.setter
    def private_dns_name_options_on_launch(self, value: Optional[pulumi.Input['PrivateDnsNameOptionsOnLaunchPropertiesArgs']]):
        pulumi.set(self, "private_dns_name_options_on_launch", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubnetTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Subnet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assign_ipv6_address_on_creation: Optional[pulumi.Input[bool]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 availability_zone_id: Optional[pulumi.Input[str]] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 enable_dns64: Optional[pulumi.Input[bool]] = None,
                 ipv4_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv4_netmask_length: Optional[pulumi.Input[int]] = None,
                 ipv6_cidr_block: Optional[pulumi.Input[str]] = None,
                 ipv6_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ipv6_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv6_native: Optional[pulumi.Input[bool]] = None,
                 ipv6_netmask_length: Optional[pulumi.Input[int]] = None,
                 map_public_ip_on_launch: Optional[pulumi.Input[bool]] = None,
                 outpost_arn: Optional[pulumi.Input[str]] = None,
                 private_dns_name_options_on_launch: Optional[pulumi.Input[pulumi.InputType['PrivateDnsNameOptionsOnLaunchPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetTagArgs']]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::Subnet

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ipv4_ipam_pool_id: The ID of an IPv4 IPAM pool you want to use for allocating this subnet's CIDR
        :param pulumi.Input[int] ipv4_netmask_length: The netmask length of the IPv4 CIDR you want to allocate to this subnet from an Amazon VPC IP Address Manager (IPAM) pool
        :param pulumi.Input[str] ipv6_ipam_pool_id: The ID of an IPv6 IPAM pool you want to use for allocating this subnet's CIDR
        :param pulumi.Input[int] ipv6_netmask_length: The netmask length of the IPv6 CIDR you want to allocate to this subnet from an Amazon VPC IP Address Manager (IPAM) pool
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubnetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::Subnet

        :param str resource_name: The name of the resource.
        :param SubnetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubnetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assign_ipv6_address_on_creation: Optional[pulumi.Input[bool]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 availability_zone_id: Optional[pulumi.Input[str]] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 enable_dns64: Optional[pulumi.Input[bool]] = None,
                 ipv4_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv4_netmask_length: Optional[pulumi.Input[int]] = None,
                 ipv6_cidr_block: Optional[pulumi.Input[str]] = None,
                 ipv6_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ipv6_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv6_native: Optional[pulumi.Input[bool]] = None,
                 ipv6_netmask_length: Optional[pulumi.Input[int]] = None,
                 map_public_ip_on_launch: Optional[pulumi.Input[bool]] = None,
                 outpost_arn: Optional[pulumi.Input[str]] = None,
                 private_dns_name_options_on_launch: Optional[pulumi.Input[pulumi.InputType['PrivateDnsNameOptionsOnLaunchPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetTagArgs']]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SubnetArgs.__new__(SubnetArgs)

            __props__.__dict__["assign_ipv6_address_on_creation"] = assign_ipv6_address_on_creation
            __props__.__dict__["availability_zone"] = availability_zone
            __props__.__dict__["availability_zone_id"] = availability_zone_id
            __props__.__dict__["cidr_block"] = cidr_block
            __props__.__dict__["enable_dns64"] = enable_dns64
            __props__.__dict__["ipv4_ipam_pool_id"] = ipv4_ipam_pool_id
            __props__.__dict__["ipv4_netmask_length"] = ipv4_netmask_length
            __props__.__dict__["ipv6_cidr_block"] = ipv6_cidr_block
            __props__.__dict__["ipv6_cidr_blocks"] = ipv6_cidr_blocks
            __props__.__dict__["ipv6_ipam_pool_id"] = ipv6_ipam_pool_id
            __props__.__dict__["ipv6_native"] = ipv6_native
            __props__.__dict__["ipv6_netmask_length"] = ipv6_netmask_length
            __props__.__dict__["map_public_ip_on_launch"] = map_public_ip_on_launch
            __props__.__dict__["outpost_arn"] = outpost_arn
            __props__.__dict__["private_dns_name_options_on_launch"] = private_dns_name_options_on_launch
            __props__.__dict__["tags"] = tags
            if vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_id'")
            __props__.__dict__["vpc_id"] = vpc_id
            __props__.__dict__["network_acl_association_id"] = None
            __props__.__dict__["subnet_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["availability_zone", "availability_zone_id", "cidr_block", "ipv4_ipam_pool_id", "ipv4_netmask_length", "ipv6_ipam_pool_id", "ipv6_native", "ipv6_netmask_length", "outpost_arn", "vpc_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Subnet, __self__).__init__(
            'aws-native:ec2:Subnet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Subnet':
        """
        Get an existing Subnet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SubnetArgs.__new__(SubnetArgs)

        __props__.__dict__["assign_ipv6_address_on_creation"] = None
        __props__.__dict__["availability_zone"] = None
        __props__.__dict__["availability_zone_id"] = None
        __props__.__dict__["cidr_block"] = None
        __props__.__dict__["enable_dns64"] = None
        __props__.__dict__["ipv4_ipam_pool_id"] = None
        __props__.__dict__["ipv4_netmask_length"] = None
        __props__.__dict__["ipv6_cidr_block"] = None
        __props__.__dict__["ipv6_cidr_blocks"] = None
        __props__.__dict__["ipv6_ipam_pool_id"] = None
        __props__.__dict__["ipv6_native"] = None
        __props__.__dict__["ipv6_netmask_length"] = None
        __props__.__dict__["map_public_ip_on_launch"] = None
        __props__.__dict__["network_acl_association_id"] = None
        __props__.__dict__["outpost_arn"] = None
        __props__.__dict__["private_dns_name_options_on_launch"] = None
        __props__.__dict__["subnet_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpc_id"] = None
        return Subnet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assignIpv6AddressOnCreation")
    def assign_ipv6_address_on_creation(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "assign_ipv6_address_on_creation")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "availability_zone_id")

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "cidr_block")

    @property
    @pulumi.getter(name="enableDns64")
    def enable_dns64(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enable_dns64")

    @property
    @pulumi.getter(name="ipv4IpamPoolId")
    def ipv4_ipam_pool_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of an IPv4 IPAM pool you want to use for allocating this subnet's CIDR
        """
        return pulumi.get(self, "ipv4_ipam_pool_id")

    @property
    @pulumi.getter(name="ipv4NetmaskLength")
    def ipv4_netmask_length(self) -> pulumi.Output[Optional[int]]:
        """
        The netmask length of the IPv4 CIDR you want to allocate to this subnet from an Amazon VPC IP Address Manager (IPAM) pool
        """
        return pulumi.get(self, "ipv4_netmask_length")

    @property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ipv6_cidr_block")

    @property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "ipv6_cidr_blocks")

    @property
    @pulumi.getter(name="ipv6IpamPoolId")
    def ipv6_ipam_pool_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of an IPv6 IPAM pool you want to use for allocating this subnet's CIDR
        """
        return pulumi.get(self, "ipv6_ipam_pool_id")

    @property
    @pulumi.getter(name="ipv6Native")
    def ipv6_native(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "ipv6_native")

    @property
    @pulumi.getter(name="ipv6NetmaskLength")
    def ipv6_netmask_length(self) -> pulumi.Output[Optional[int]]:
        """
        The netmask length of the IPv6 CIDR you want to allocate to this subnet from an Amazon VPC IP Address Manager (IPAM) pool
        """
        return pulumi.get(self, "ipv6_netmask_length")

    @property
    @pulumi.getter(name="mapPublicIpOnLaunch")
    def map_public_ip_on_launch(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "map_public_ip_on_launch")

    @property
    @pulumi.getter(name="networkAclAssociationId")
    def network_acl_association_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "network_acl_association_id")

    @property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "outpost_arn")

    @property
    @pulumi.getter(name="privateDnsNameOptionsOnLaunch")
    def private_dns_name_options_on_launch(self) -> pulumi.Output[Optional['outputs.PrivateDnsNameOptionsOnLaunchProperties']]:
        return pulumi.get(self, "private_dns_name_options_on_launch")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.SubnetTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "vpc_id")

