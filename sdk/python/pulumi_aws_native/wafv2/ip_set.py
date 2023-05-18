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

__all__ = ['IPSetArgs', 'IPSet']

@pulumi.input_type
class IPSetArgs:
    def __init__(__self__, *,
                 addresses: pulumi.Input[Sequence[pulumi.Input[str]]],
                 i_p_address_version: pulumi.Input['IPSetIPAddressVersion'],
                 scope: pulumi.Input['IPSetScope'],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['IPSetTagArgs']]]] = None):
        """
        The set of arguments for constructing a IPSet resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] addresses: List of IPAddresses.
        """
        pulumi.set(__self__, "addresses", addresses)
        pulumi.set(__self__, "i_p_address_version", i_p_address_version)
        pulumi.set(__self__, "scope", scope)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def addresses(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of IPAddresses.
        """
        return pulumi.get(self, "addresses")

    @addresses.setter
    def addresses(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "addresses", value)

    @property
    @pulumi.getter(name="iPAddressVersion")
    def i_p_address_version(self) -> pulumi.Input['IPSetIPAddressVersion']:
        return pulumi.get(self, "i_p_address_version")

    @i_p_address_version.setter
    def i_p_address_version(self, value: pulumi.Input['IPSetIPAddressVersion']):
        pulumi.set(self, "i_p_address_version", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input['IPSetScope']:
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input['IPSetScope']):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IPSetTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IPSetTagArgs']]]]):
        pulumi.set(self, "tags", value)


class IPSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 i_p_address_version: Optional[pulumi.Input['IPSetIPAddressVersion']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input['IPSetScope']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IPSetTagArgs']]]]] = None,
                 __props__=None):
        """
        Contains a list of IP addresses. This can be either IPV4 or IPV6. The list will be mutually

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] addresses: List of IPAddresses.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IPSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Contains a list of IP addresses. This can be either IPV4 or IPV6. The list will be mutually

        :param str resource_name: The name of the resource.
        :param IPSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IPSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 i_p_address_version: Optional[pulumi.Input['IPSetIPAddressVersion']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input['IPSetScope']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IPSetTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IPSetArgs.__new__(IPSetArgs)

            if addresses is None and not opts.urn:
                raise TypeError("Missing required property 'addresses'")
            __props__.__dict__["addresses"] = addresses
            __props__.__dict__["description"] = description
            if i_p_address_version is None and not opts.urn:
                raise TypeError("Missing required property 'i_p_address_version'")
            __props__.__dict__["i_p_address_version"] = i_p_address_version
            __props__.__dict__["name"] = name
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        super(IPSet, __self__).__init__(
            'aws-native:wafv2:IPSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IPSet':
        """
        Get an existing IPSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IPSetArgs.__new__(IPSetArgs)

        __props__.__dict__["addresses"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["i_p_address_version"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["tags"] = None
        return IPSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        List of IPAddresses.
        """
        return pulumi.get(self, "addresses")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="iPAddressVersion")
    def i_p_address_version(self) -> pulumi.Output['IPSetIPAddressVersion']:
        return pulumi.get(self, "i_p_address_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output['IPSetScope']:
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.IPSetTag']]]:
        return pulumi.get(self, "tags")

