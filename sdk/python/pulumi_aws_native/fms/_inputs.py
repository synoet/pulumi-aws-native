# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'PolicyIEMapArgs',
    'PolicyNetworkFirewallPolicyArgs',
    'PolicyOptionArgs',
    'PolicyResourceTagArgs',
    'PolicySecurityServicePolicyDataArgs',
    'PolicyTagArgs',
    'PolicyThirdPartyFirewallPolicyArgs',
]

@pulumi.input_type
class PolicyIEMapArgs:
    def __init__(__self__, *,
                 a_ccount: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 o_rgunit: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        An FMS includeMap or excludeMap.
        """
        if a_ccount is not None:
            pulumi.set(__self__, "a_ccount", a_ccount)
        if o_rgunit is not None:
            pulumi.set(__self__, "o_rgunit", o_rgunit)

    @property
    @pulumi.getter(name="aCCOUNT")
    def a_ccount(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "a_ccount")

    @a_ccount.setter
    def a_ccount(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "a_ccount", value)

    @property
    @pulumi.getter(name="oRGUNIT")
    def o_rgunit(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "o_rgunit")

    @o_rgunit.setter
    def o_rgunit(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "o_rgunit", value)


@pulumi.input_type
class PolicyNetworkFirewallPolicyArgs:
    def __init__(__self__, *,
                 firewall_deployment_model: pulumi.Input['PolicyFirewallDeploymentModel']):
        """
        Network firewall policy.
        """
        pulumi.set(__self__, "firewall_deployment_model", firewall_deployment_model)

    @property
    @pulumi.getter(name="firewallDeploymentModel")
    def firewall_deployment_model(self) -> pulumi.Input['PolicyFirewallDeploymentModel']:
        return pulumi.get(self, "firewall_deployment_model")

    @firewall_deployment_model.setter
    def firewall_deployment_model(self, value: pulumi.Input['PolicyFirewallDeploymentModel']):
        pulumi.set(self, "firewall_deployment_model", value)


@pulumi.input_type
class PolicyOptionArgs:
    def __init__(__self__, *,
                 network_firewall_policy: Optional[pulumi.Input['PolicyNetworkFirewallPolicyArgs']] = None,
                 third_party_firewall_policy: Optional[pulumi.Input['PolicyThirdPartyFirewallPolicyArgs']] = None):
        """
        Firewall policy option.
        """
        if network_firewall_policy is not None:
            pulumi.set(__self__, "network_firewall_policy", network_firewall_policy)
        if third_party_firewall_policy is not None:
            pulumi.set(__self__, "third_party_firewall_policy", third_party_firewall_policy)

    @property
    @pulumi.getter(name="networkFirewallPolicy")
    def network_firewall_policy(self) -> Optional[pulumi.Input['PolicyNetworkFirewallPolicyArgs']]:
        return pulumi.get(self, "network_firewall_policy")

    @network_firewall_policy.setter
    def network_firewall_policy(self, value: Optional[pulumi.Input['PolicyNetworkFirewallPolicyArgs']]):
        pulumi.set(self, "network_firewall_policy", value)

    @property
    @pulumi.getter(name="thirdPartyFirewallPolicy")
    def third_party_firewall_policy(self) -> Optional[pulumi.Input['PolicyThirdPartyFirewallPolicyArgs']]:
        return pulumi.get(self, "third_party_firewall_policy")

    @third_party_firewall_policy.setter
    def third_party_firewall_policy(self, value: Optional[pulumi.Input['PolicyThirdPartyFirewallPolicyArgs']]):
        pulumi.set(self, "third_party_firewall_policy", value)


@pulumi.input_type
class PolicyResourceTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: Optional[pulumi.Input[str]] = None):
        """
        A resource tag.
        """
        pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class PolicySecurityServicePolicyDataArgs:
    def __init__(__self__, *,
                 type: pulumi.Input['PolicyType'],
                 managed_service_data: Optional[pulumi.Input[str]] = None,
                 policy_option: Optional[pulumi.Input['PolicyOptionArgs']] = None):
        """
        Firewall security service policy data.
        """
        pulumi.set(__self__, "type", type)
        if managed_service_data is not None:
            pulumi.set(__self__, "managed_service_data", managed_service_data)
        if policy_option is not None:
            pulumi.set(__self__, "policy_option", policy_option)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['PolicyType']:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['PolicyType']):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="managedServiceData")
    def managed_service_data(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "managed_service_data")

    @managed_service_data.setter
    def managed_service_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_service_data", value)

    @property
    @pulumi.getter(name="policyOption")
    def policy_option(self) -> Optional[pulumi.Input['PolicyOptionArgs']]:
        return pulumi.get(self, "policy_option")

    @policy_option.setter
    def policy_option(self, value: Optional[pulumi.Input['PolicyOptionArgs']]):
        pulumi.set(self, "policy_option", value)


@pulumi.input_type
class PolicyTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A policy tag.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class PolicyThirdPartyFirewallPolicyArgs:
    def __init__(__self__, *,
                 firewall_deployment_model: pulumi.Input['PolicyFirewallDeploymentModel']):
        """
        Third party firewall policy.
        """
        pulumi.set(__self__, "firewall_deployment_model", firewall_deployment_model)

    @property
    @pulumi.getter(name="firewallDeploymentModel")
    def firewall_deployment_model(self) -> pulumi.Input['PolicyFirewallDeploymentModel']:
        return pulumi.get(self, "firewall_deployment_model")

    @firewall_deployment_model.setter
    def firewall_deployment_model(self, value: pulumi.Input['PolicyFirewallDeploymentModel']):
        pulumi.set(self, "firewall_deployment_model", value)


