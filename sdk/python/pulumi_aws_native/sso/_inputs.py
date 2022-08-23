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
    'InstanceAccessControlAttributeConfigurationAccessControlAttributeValueArgs',
    'InstanceAccessControlAttributeConfigurationAccessControlAttributeArgs',
    'InstanceAccessControlAttributeConfigurationPropertiesArgs',
    'PermissionSetCustomerManagedPolicyReferenceArgs',
    'PermissionSetPermissionsBoundaryArgs',
    'PermissionSetTagArgs',
]

@pulumi.input_type
class InstanceAccessControlAttributeConfigurationAccessControlAttributeValueArgs:
    def __init__(__self__, *,
                 source: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(__self__, "source", source)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "source", value)


@pulumi.input_type
class InstanceAccessControlAttributeConfigurationAccessControlAttributeArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input['InstanceAccessControlAttributeConfigurationAccessControlAttributeValueArgs']):
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
    def value(self) -> pulumi.Input['InstanceAccessControlAttributeConfigurationAccessControlAttributeValueArgs']:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input['InstanceAccessControlAttributeConfigurationAccessControlAttributeValueArgs']):
        pulumi.set(self, "value", value)


@pulumi.input_type
class InstanceAccessControlAttributeConfigurationPropertiesArgs:
    def __init__(__self__, *,
                 access_control_attributes: pulumi.Input[Sequence[pulumi.Input['InstanceAccessControlAttributeConfigurationAccessControlAttributeArgs']]]):
        """
        The InstanceAccessControlAttributeConfiguration property has been deprecated but is still supported for backwards compatibility purposes. We recomend that you use  AccessControlAttributes property instead.
        """
        pulumi.set(__self__, "access_control_attributes", access_control_attributes)

    @property
    @pulumi.getter(name="accessControlAttributes")
    def access_control_attributes(self) -> pulumi.Input[Sequence[pulumi.Input['InstanceAccessControlAttributeConfigurationAccessControlAttributeArgs']]]:
        return pulumi.get(self, "access_control_attributes")

    @access_control_attributes.setter
    def access_control_attributes(self, value: pulumi.Input[Sequence[pulumi.Input['InstanceAccessControlAttributeConfigurationAccessControlAttributeArgs']]]):
        pulumi.set(self, "access_control_attributes", value)


@pulumi.input_type
class PermissionSetCustomerManagedPolicyReferenceArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 path: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "name", name)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)


@pulumi.input_type
class PermissionSetPermissionsBoundaryArgs:
    def __init__(__self__, *,
                 customer_managed_policy_reference: Optional[pulumi.Input['PermissionSetCustomerManagedPolicyReferenceArgs']] = None,
                 managed_policy_arn: Optional[pulumi.Input[str]] = None):
        if customer_managed_policy_reference is not None:
            pulumi.set(__self__, "customer_managed_policy_reference", customer_managed_policy_reference)
        if managed_policy_arn is not None:
            pulumi.set(__self__, "managed_policy_arn", managed_policy_arn)

    @property
    @pulumi.getter(name="customerManagedPolicyReference")
    def customer_managed_policy_reference(self) -> Optional[pulumi.Input['PermissionSetCustomerManagedPolicyReferenceArgs']]:
        return pulumi.get(self, "customer_managed_policy_reference")

    @customer_managed_policy_reference.setter
    def customer_managed_policy_reference(self, value: Optional[pulumi.Input['PermissionSetCustomerManagedPolicyReferenceArgs']]):
        pulumi.set(self, "customer_managed_policy_reference", value)

    @property
    @pulumi.getter(name="managedPolicyArn")
    def managed_policy_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "managed_policy_arn")

    @managed_policy_arn.setter
    def managed_policy_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_policy_arn", value)


@pulumi.input_type
class PermissionSetTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        The metadata that you apply to the permission set to help you categorize and organize them.
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


