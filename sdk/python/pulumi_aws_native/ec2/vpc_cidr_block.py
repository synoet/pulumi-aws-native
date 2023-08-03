# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['VpcCidrBlockArgs', 'VpcCidrBlock']

@pulumi.input_type
class VpcCidrBlockArgs:
    def __init__(__self__, *,
                 vpc_id: pulumi.Input[str],
                 amazon_provided_ipv6_cidr_block: Optional[pulumi.Input[bool]] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 ipv4_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv4_netmask_length: Optional[pulumi.Input[int]] = None,
                 ipv6_cidr_block: Optional[pulumi.Input[str]] = None,
                 ipv6_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv6_netmask_length: Optional[pulumi.Input[int]] = None,
                 ipv6_pool: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VpcCidrBlock resource.
        """
        pulumi.set(__self__, "vpc_id", vpc_id)
        if amazon_provided_ipv6_cidr_block is not None:
            pulumi.set(__self__, "amazon_provided_ipv6_cidr_block", amazon_provided_ipv6_cidr_block)
        if cidr_block is not None:
            pulumi.set(__self__, "cidr_block", cidr_block)
        if ipv4_ipam_pool_id is not None:
            pulumi.set(__self__, "ipv4_ipam_pool_id", ipv4_ipam_pool_id)
        if ipv4_netmask_length is not None:
            pulumi.set(__self__, "ipv4_netmask_length", ipv4_netmask_length)
        if ipv6_cidr_block is not None:
            pulumi.set(__self__, "ipv6_cidr_block", ipv6_cidr_block)
        if ipv6_ipam_pool_id is not None:
            pulumi.set(__self__, "ipv6_ipam_pool_id", ipv6_ipam_pool_id)
        if ipv6_netmask_length is not None:
            pulumi.set(__self__, "ipv6_netmask_length", ipv6_netmask_length)
        if ipv6_pool is not None:
            pulumi.set(__self__, "ipv6_pool", ipv6_pool)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter(name="amazonProvidedIpv6CidrBlock")
    def amazon_provided_ipv6_cidr_block(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "amazon_provided_ipv6_cidr_block")

    @amazon_provided_ipv6_cidr_block.setter
    def amazon_provided_ipv6_cidr_block(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "amazon_provided_ipv6_cidr_block", value)

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cidr_block")

    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr_block", value)

    @property
    @pulumi.getter(name="ipv4IpamPoolId")
    def ipv4_ipam_pool_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ipv4_ipam_pool_id")

    @ipv4_ipam_pool_id.setter
    def ipv4_ipam_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv4_ipam_pool_id", value)

    @property
    @pulumi.getter(name="ipv4NetmaskLength")
    def ipv4_netmask_length(self) -> Optional[pulumi.Input[int]]:
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
    @pulumi.getter(name="ipv6IpamPoolId")
    def ipv6_ipam_pool_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ipv6_ipam_pool_id")

    @ipv6_ipam_pool_id.setter
    def ipv6_ipam_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_ipam_pool_id", value)

    @property
    @pulumi.getter(name="ipv6NetmaskLength")
    def ipv6_netmask_length(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "ipv6_netmask_length")

    @ipv6_netmask_length.setter
    def ipv6_netmask_length(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ipv6_netmask_length", value)

    @property
    @pulumi.getter(name="ipv6Pool")
    def ipv6_pool(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ipv6_pool")

    @ipv6_pool.setter
    def ipv6_pool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_pool", value)


warnings.warn("""VpcCidrBlock is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class VpcCidrBlock(pulumi.CustomResource):
    warnings.warn("""VpcCidrBlock is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 amazon_provided_ipv6_cidr_block: Optional[pulumi.Input[bool]] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 ipv4_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv4_netmask_length: Optional[pulumi.Input[int]] = None,
                 ipv6_cidr_block: Optional[pulumi.Input[str]] = None,
                 ipv6_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv6_netmask_length: Optional[pulumi.Input[int]] = None,
                 ipv6_pool: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::VPCCidrBlock

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpcCidrBlockArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::VPCCidrBlock

        :param str resource_name: The name of the resource.
        :param VpcCidrBlockArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpcCidrBlockArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 amazon_provided_ipv6_cidr_block: Optional[pulumi.Input[bool]] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 ipv4_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv4_netmask_length: Optional[pulumi.Input[int]] = None,
                 ipv6_cidr_block: Optional[pulumi.Input[str]] = None,
                 ipv6_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv6_netmask_length: Optional[pulumi.Input[int]] = None,
                 ipv6_pool: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""VpcCidrBlock is deprecated: VpcCidrBlock is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpcCidrBlockArgs.__new__(VpcCidrBlockArgs)

            __props__.__dict__["amazon_provided_ipv6_cidr_block"] = amazon_provided_ipv6_cidr_block
            __props__.__dict__["cidr_block"] = cidr_block
            __props__.__dict__["ipv4_ipam_pool_id"] = ipv4_ipam_pool_id
            __props__.__dict__["ipv4_netmask_length"] = ipv4_netmask_length
            __props__.__dict__["ipv6_cidr_block"] = ipv6_cidr_block
            __props__.__dict__["ipv6_ipam_pool_id"] = ipv6_ipam_pool_id
            __props__.__dict__["ipv6_netmask_length"] = ipv6_netmask_length
            __props__.__dict__["ipv6_pool"] = ipv6_pool
            if vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_id'")
            __props__.__dict__["vpc_id"] = vpc_id
        super(VpcCidrBlock, __self__).__init__(
            'aws-native:ec2:VpcCidrBlock',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VpcCidrBlock':
        """
        Get an existing VpcCidrBlock resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VpcCidrBlockArgs.__new__(VpcCidrBlockArgs)

        __props__.__dict__["amazon_provided_ipv6_cidr_block"] = None
        __props__.__dict__["cidr_block"] = None
        __props__.__dict__["ipv4_ipam_pool_id"] = None
        __props__.__dict__["ipv4_netmask_length"] = None
        __props__.__dict__["ipv6_cidr_block"] = None
        __props__.__dict__["ipv6_ipam_pool_id"] = None
        __props__.__dict__["ipv6_netmask_length"] = None
        __props__.__dict__["ipv6_pool"] = None
        __props__.__dict__["vpc_id"] = None
        return VpcCidrBlock(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="amazonProvidedIpv6CidrBlock")
    def amazon_provided_ipv6_cidr_block(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "amazon_provided_ipv6_cidr_block")

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "cidr_block")

    @property
    @pulumi.getter(name="ipv4IpamPoolId")
    def ipv4_ipam_pool_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ipv4_ipam_pool_id")

    @property
    @pulumi.getter(name="ipv4NetmaskLength")
    def ipv4_netmask_length(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "ipv4_netmask_length")

    @property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ipv6_cidr_block")

    @property
    @pulumi.getter(name="ipv6IpamPoolId")
    def ipv6_ipam_pool_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ipv6_ipam_pool_id")

    @property
    @pulumi.getter(name="ipv6NetmaskLength")
    def ipv6_netmask_length(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "ipv6_netmask_length")

    @property
    @pulumi.getter(name="ipv6Pool")
    def ipv6_pool(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ipv6_pool")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "vpc_id")

