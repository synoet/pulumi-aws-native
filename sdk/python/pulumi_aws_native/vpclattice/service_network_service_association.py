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

__all__ = ['ServiceNetworkServiceAssociationArgs', 'ServiceNetworkServiceAssociation']

@pulumi.input_type
class ServiceNetworkServiceAssociationArgs:
    def __init__(__self__, *,
                 dns_entry: Optional[pulumi.Input['ServiceNetworkServiceAssociationDnsEntryArgs']] = None,
                 service_identifier: Optional[pulumi.Input[str]] = None,
                 service_network_identifier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceNetworkServiceAssociationTagArgs']]]] = None):
        """
        The set of arguments for constructing a ServiceNetworkServiceAssociation resource.
        """
        if dns_entry is not None:
            pulumi.set(__self__, "dns_entry", dns_entry)
        if service_identifier is not None:
            pulumi.set(__self__, "service_identifier", service_identifier)
        if service_network_identifier is not None:
            pulumi.set(__self__, "service_network_identifier", service_network_identifier)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dnsEntry")
    def dns_entry(self) -> Optional[pulumi.Input['ServiceNetworkServiceAssociationDnsEntryArgs']]:
        return pulumi.get(self, "dns_entry")

    @dns_entry.setter
    def dns_entry(self, value: Optional[pulumi.Input['ServiceNetworkServiceAssociationDnsEntryArgs']]):
        pulumi.set(self, "dns_entry", value)

    @property
    @pulumi.getter(name="serviceIdentifier")
    def service_identifier(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "service_identifier")

    @service_identifier.setter
    def service_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_identifier", value)

    @property
    @pulumi.getter(name="serviceNetworkIdentifier")
    def service_network_identifier(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "service_network_identifier")

    @service_network_identifier.setter
    def service_network_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_network_identifier", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceNetworkServiceAssociationTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceNetworkServiceAssociationTagArgs']]]]):
        pulumi.set(self, "tags", value)


class ServiceNetworkServiceAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_entry: Optional[pulumi.Input[pulumi.InputType['ServiceNetworkServiceAssociationDnsEntryArgs']]] = None,
                 service_identifier: Optional[pulumi.Input[str]] = None,
                 service_network_identifier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceNetworkServiceAssociationTagArgs']]]]] = None,
                 __props__=None):
        """
        Association between a Service Network and Service to allow the Service to be exposed within the ServiceNetwork

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ServiceNetworkServiceAssociationArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Association between a Service Network and Service to allow the Service to be exposed within the ServiceNetwork

        :param str resource_name: The name of the resource.
        :param ServiceNetworkServiceAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceNetworkServiceAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_entry: Optional[pulumi.Input[pulumi.InputType['ServiceNetworkServiceAssociationDnsEntryArgs']]] = None,
                 service_identifier: Optional[pulumi.Input[str]] = None,
                 service_network_identifier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceNetworkServiceAssociationTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceNetworkServiceAssociationArgs.__new__(ServiceNetworkServiceAssociationArgs)

            __props__.__dict__["dns_entry"] = dns_entry
            __props__.__dict__["service_identifier"] = service_identifier
            __props__.__dict__["service_network_identifier"] = service_network_identifier
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["service_arn"] = None
            __props__.__dict__["service_id"] = None
            __props__.__dict__["service_name"] = None
            __props__.__dict__["service_network_arn"] = None
            __props__.__dict__["service_network_id"] = None
            __props__.__dict__["service_network_name"] = None
            __props__.__dict__["status"] = None
        super(ServiceNetworkServiceAssociation, __self__).__init__(
            'aws-native:vpclattice:ServiceNetworkServiceAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServiceNetworkServiceAssociation':
        """
        Get an existing ServiceNetworkServiceAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServiceNetworkServiceAssociationArgs.__new__(ServiceNetworkServiceAssociationArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["dns_entry"] = None
        __props__.__dict__["service_arn"] = None
        __props__.__dict__["service_id"] = None
        __props__.__dict__["service_identifier"] = None
        __props__.__dict__["service_name"] = None
        __props__.__dict__["service_network_arn"] = None
        __props__.__dict__["service_network_id"] = None
        __props__.__dict__["service_network_identifier"] = None
        __props__.__dict__["service_network_name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        return ServiceNetworkServiceAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="dnsEntry")
    def dns_entry(self) -> pulumi.Output[Optional['outputs.ServiceNetworkServiceAssociationDnsEntry']]:
        return pulumi.get(self, "dns_entry")

    @property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "service_arn")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter(name="serviceIdentifier")
    def service_identifier(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "service_identifier")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="serviceNetworkArn")
    def service_network_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "service_network_arn")

    @property
    @pulumi.getter(name="serviceNetworkId")
    def service_network_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "service_network_id")

    @property
    @pulumi.getter(name="serviceNetworkIdentifier")
    def service_network_identifier(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "service_network_identifier")

    @property
    @pulumi.getter(name="serviceNetworkName")
    def service_network_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "service_network_name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['ServiceNetworkServiceAssociationStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceNetworkServiceAssociationTag']]]:
        return pulumi.get(self, "tags")

