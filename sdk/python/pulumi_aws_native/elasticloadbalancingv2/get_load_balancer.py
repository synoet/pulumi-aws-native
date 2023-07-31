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

__all__ = [
    'GetLoadBalancerResult',
    'AwaitableGetLoadBalancerResult',
    'get_load_balancer',
    'get_load_balancer_output',
]

@pulumi.output_type
class GetLoadBalancerResult:
    def __init__(__self__, canonical_hosted_zone_id=None, dns_name=None, id=None, ip_address_type=None, load_balancer_attributes=None, load_balancer_full_name=None, load_balancer_name=None, security_groups=None, subnet_mappings=None, subnets=None, tags=None):
        if canonical_hosted_zone_id and not isinstance(canonical_hosted_zone_id, str):
            raise TypeError("Expected argument 'canonical_hosted_zone_id' to be a str")
        pulumi.set(__self__, "canonical_hosted_zone_id", canonical_hosted_zone_id)
        if dns_name and not isinstance(dns_name, str):
            raise TypeError("Expected argument 'dns_name' to be a str")
        pulumi.set(__self__, "dns_name", dns_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_address_type and not isinstance(ip_address_type, str):
            raise TypeError("Expected argument 'ip_address_type' to be a str")
        pulumi.set(__self__, "ip_address_type", ip_address_type)
        if load_balancer_attributes and not isinstance(load_balancer_attributes, list):
            raise TypeError("Expected argument 'load_balancer_attributes' to be a list")
        pulumi.set(__self__, "load_balancer_attributes", load_balancer_attributes)
        if load_balancer_full_name and not isinstance(load_balancer_full_name, str):
            raise TypeError("Expected argument 'load_balancer_full_name' to be a str")
        pulumi.set(__self__, "load_balancer_full_name", load_balancer_full_name)
        if load_balancer_name and not isinstance(load_balancer_name, str):
            raise TypeError("Expected argument 'load_balancer_name' to be a str")
        pulumi.set(__self__, "load_balancer_name", load_balancer_name)
        if security_groups and not isinstance(security_groups, list):
            raise TypeError("Expected argument 'security_groups' to be a list")
        pulumi.set(__self__, "security_groups", security_groups)
        if subnet_mappings and not isinstance(subnet_mappings, list):
            raise TypeError("Expected argument 'subnet_mappings' to be a list")
        pulumi.set(__self__, "subnet_mappings", subnet_mappings)
        if subnets and not isinstance(subnets, list):
            raise TypeError("Expected argument 'subnets' to be a list")
        pulumi.set(__self__, "subnets", subnets)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="canonicalHostedZoneId")
    def canonical_hosted_zone_id(self) -> Optional[str]:
        return pulumi.get(self, "canonical_hosted_zone_id")

    @property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[str]:
        return pulumi.get(self, "dns_name")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[str]:
        return pulumi.get(self, "ip_address_type")

    @property
    @pulumi.getter(name="loadBalancerAttributes")
    def load_balancer_attributes(self) -> Optional[Sequence['outputs.LoadBalancerAttribute']]:
        return pulumi.get(self, "load_balancer_attributes")

    @property
    @pulumi.getter(name="loadBalancerFullName")
    def load_balancer_full_name(self) -> Optional[str]:
        return pulumi.get(self, "load_balancer_full_name")

    @property
    @pulumi.getter(name="loadBalancerName")
    def load_balancer_name(self) -> Optional[str]:
        return pulumi.get(self, "load_balancer_name")

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "security_groups")

    @property
    @pulumi.getter(name="subnetMappings")
    def subnet_mappings(self) -> Optional[Sequence['outputs.LoadBalancerSubnetMapping']]:
        return pulumi.get(self, "subnet_mappings")

    @property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "subnets")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.LoadBalancerTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetLoadBalancerResult(GetLoadBalancerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLoadBalancerResult(
            canonical_hosted_zone_id=self.canonical_hosted_zone_id,
            dns_name=self.dns_name,
            id=self.id,
            ip_address_type=self.ip_address_type,
            load_balancer_attributes=self.load_balancer_attributes,
            load_balancer_full_name=self.load_balancer_full_name,
            load_balancer_name=self.load_balancer_name,
            security_groups=self.security_groups,
            subnet_mappings=self.subnet_mappings,
            subnets=self.subnets,
            tags=self.tags)


def get_load_balancer(id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLoadBalancerResult:
    """
    Resource Type definition for AWS::ElasticLoadBalancingV2::LoadBalancer
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:elasticloadbalancingv2:getLoadBalancer', __args__, opts=opts, typ=GetLoadBalancerResult).value

    return AwaitableGetLoadBalancerResult(
        canonical_hosted_zone_id=pulumi.get(__ret__, 'canonical_hosted_zone_id'),
        dns_name=pulumi.get(__ret__, 'dns_name'),
        id=pulumi.get(__ret__, 'id'),
        ip_address_type=pulumi.get(__ret__, 'ip_address_type'),
        load_balancer_attributes=pulumi.get(__ret__, 'load_balancer_attributes'),
        load_balancer_full_name=pulumi.get(__ret__, 'load_balancer_full_name'),
        load_balancer_name=pulumi.get(__ret__, 'load_balancer_name'),
        security_groups=pulumi.get(__ret__, 'security_groups'),
        subnet_mappings=pulumi.get(__ret__, 'subnet_mappings'),
        subnets=pulumi.get(__ret__, 'subnets'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_load_balancer)
def get_load_balancer_output(id: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLoadBalancerResult]:
    """
    Resource Type definition for AWS::ElasticLoadBalancingV2::LoadBalancer
    """
    ...
