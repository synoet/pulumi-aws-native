# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['IPAMPoolCidrArgs', 'IPAMPoolCidr']

@pulumi.input_type
class IPAMPoolCidrArgs:
    def __init__(__self__, *,
                 ipam_pool_id: pulumi.Input[str],
                 cidr: Optional[pulumi.Input[str]] = None,
                 netmask_length: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a IPAMPoolCidr resource.
        :param pulumi.Input[str] ipam_pool_id: Id of the IPAM Pool.
        :param pulumi.Input[str] cidr: Represents a single IPv4 or IPv6 CIDR
        :param pulumi.Input[int] netmask_length: The desired netmask length of the provision. If set, IPAM will choose a block of free space with this size and return the CIDR representing it.
        """
        pulumi.set(__self__, "ipam_pool_id", ipam_pool_id)
        if cidr is not None:
            pulumi.set(__self__, "cidr", cidr)
        if netmask_length is not None:
            pulumi.set(__self__, "netmask_length", netmask_length)

    @property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> pulumi.Input[str]:
        """
        Id of the IPAM Pool.
        """
        return pulumi.get(self, "ipam_pool_id")

    @ipam_pool_id.setter
    def ipam_pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "ipam_pool_id", value)

    @property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[str]]:
        """
        Represents a single IPv4 or IPv6 CIDR
        """
        return pulumi.get(self, "cidr")

    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr", value)

    @property
    @pulumi.getter(name="netmaskLength")
    def netmask_length(self) -> Optional[pulumi.Input[int]]:
        """
        The desired netmask length of the provision. If set, IPAM will choose a block of free space with this size and return the CIDR representing it.
        """
        return pulumi.get(self, "netmask_length")

    @netmask_length.setter
    def netmask_length(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "netmask_length", value)


class IPAMPoolCidr(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr: Optional[pulumi.Input[str]] = None,
                 ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 netmask_length: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Resource Schema of AWS::EC2::IPAMPoolCidr Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cidr: Represents a single IPv4 or IPv6 CIDR
        :param pulumi.Input[str] ipam_pool_id: Id of the IPAM Pool.
        :param pulumi.Input[int] netmask_length: The desired netmask length of the provision. If set, IPAM will choose a block of free space with this size and return the CIDR representing it.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IPAMPoolCidrArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Schema of AWS::EC2::IPAMPoolCidr Type

        :param str resource_name: The name of the resource.
        :param IPAMPoolCidrArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IPAMPoolCidrArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr: Optional[pulumi.Input[str]] = None,
                 ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 netmask_length: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IPAMPoolCidrArgs.__new__(IPAMPoolCidrArgs)

            __props__.__dict__["cidr"] = cidr
            if ipam_pool_id is None and not opts.urn:
                raise TypeError("Missing required property 'ipam_pool_id'")
            __props__.__dict__["ipam_pool_id"] = ipam_pool_id
            __props__.__dict__["netmask_length"] = netmask_length
            __props__.__dict__["ipam_pool_cidr_id"] = None
            __props__.__dict__["state"] = None
        super(IPAMPoolCidr, __self__).__init__(
            'aws-native:ec2:IPAMPoolCidr',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IPAMPoolCidr':
        """
        Get an existing IPAMPoolCidr resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IPAMPoolCidrArgs.__new__(IPAMPoolCidrArgs)

        __props__.__dict__["cidr"] = None
        __props__.__dict__["ipam_pool_cidr_id"] = None
        __props__.__dict__["ipam_pool_id"] = None
        __props__.__dict__["netmask_length"] = None
        __props__.__dict__["state"] = None
        return IPAMPoolCidr(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cidr(self) -> pulumi.Output[Optional[str]]:
        """
        Represents a single IPv4 or IPv6 CIDR
        """
        return pulumi.get(self, "cidr")

    @property
    @pulumi.getter(name="ipamPoolCidrId")
    def ipam_pool_cidr_id(self) -> pulumi.Output[str]:
        """
        Id of the IPAM Pool Cidr.
        """
        return pulumi.get(self, "ipam_pool_cidr_id")

    @property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> pulumi.Output[str]:
        """
        Id of the IPAM Pool.
        """
        return pulumi.get(self, "ipam_pool_id")

    @property
    @pulumi.getter(name="netmaskLength")
    def netmask_length(self) -> pulumi.Output[Optional[int]]:
        """
        The desired netmask length of the provision. If set, IPAM will choose a block of free space with this size and return the CIDR representing it.
        """
        return pulumi.get(self, "netmask_length")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Provisioned state of the cidr.
        """
        return pulumi.get(self, "state")

