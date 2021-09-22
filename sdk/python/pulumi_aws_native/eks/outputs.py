# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'AddonTag',
    'ClusterEncryptionConfig',
    'ClusterKubernetesNetworkConfig',
    'ClusterProvider',
    'ClusterResourcesVpcConfig',
    'FargateProfileLabel',
    'FargateProfileSelector',
    'FargateProfileTag',
    'NodegroupLaunchTemplateSpecification',
    'NodegroupRemoteAccess',
    'NodegroupScalingConfig',
    'NodegroupTaint',
    'NodegroupUpdateConfig',
]

@pulumi.output_type
class AddonTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param str value: The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class ClusterEncryptionConfig(dict):
    def __init__(__self__, *,
                 provider: Optional['outputs.ClusterProvider'] = None,
                 resources: Optional[Sequence[str]] = None):
        if provider is not None:
            pulumi.set(__self__, "provider", provider)
        if resources is not None:
            pulumi.set(__self__, "resources", resources)

    @property
    @pulumi.getter
    def provider(self) -> Optional['outputs.ClusterProvider']:
        return pulumi.get(self, "provider")

    @property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "resources")


@pulumi.output_type
class ClusterKubernetesNetworkConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "serviceIpv4Cidr":
            suggest = "service_ipv4_cidr"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterKubernetesNetworkConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterKubernetesNetworkConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterKubernetesNetworkConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 service_ipv4_cidr: Optional[str] = None):
        if service_ipv4_cidr is not None:
            pulumi.set(__self__, "service_ipv4_cidr", service_ipv4_cidr)

    @property
    @pulumi.getter(name="serviceIpv4Cidr")
    def service_ipv4_cidr(self) -> Optional[str]:
        return pulumi.get(self, "service_ipv4_cidr")


@pulumi.output_type
class ClusterProvider(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyArn":
            suggest = "key_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterProvider. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterProvider.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterProvider.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 key_arn: Optional[str] = None):
        if key_arn is not None:
            pulumi.set(__self__, "key_arn", key_arn)

    @property
    @pulumi.getter(name="keyArn")
    def key_arn(self) -> Optional[str]:
        return pulumi.get(self, "key_arn")


@pulumi.output_type
class ClusterResourcesVpcConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subnetIds":
            suggest = "subnet_ids"
        elif key == "securityGroupIds":
            suggest = "security_group_ids"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterResourcesVpcConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterResourcesVpcConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterResourcesVpcConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 subnet_ids: Sequence[str],
                 security_group_ids: Optional[Sequence[str]] = None):
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[str]:
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "security_group_ids")


@pulumi.output_type
class FargateProfileLabel(dict):
    """
    A key-value pair to associate with a pod.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a pod.
        :param str key: The key name of the label.
        :param str value: The value for the label. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the label.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the label. 
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class FargateProfileSelector(dict):
    def __init__(__self__, *,
                 namespace: str,
                 labels: Optional[Sequence['outputs.FargateProfileLabel']] = None):
        pulumi.set(__self__, "namespace", namespace)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Sequence['outputs.FargateProfileLabel']]:
        return pulumi.get(self, "labels")


@pulumi.output_type
class FargateProfileTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param str value: The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class NodegroupLaunchTemplateSpecification(dict):
    def __init__(__self__, *,
                 id: Optional[str] = None,
                 name: Optional[str] = None,
                 version: Optional[str] = None):
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        return pulumi.get(self, "version")


@pulumi.output_type
class NodegroupRemoteAccess(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ec2SshKey":
            suggest = "ec2_ssh_key"
        elif key == "sourceSecurityGroups":
            suggest = "source_security_groups"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NodegroupRemoteAccess. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NodegroupRemoteAccess.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NodegroupRemoteAccess.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 ec2_ssh_key: str,
                 source_security_groups: Optional[Sequence[str]] = None):
        pulumi.set(__self__, "ec2_ssh_key", ec2_ssh_key)
        if source_security_groups is not None:
            pulumi.set(__self__, "source_security_groups", source_security_groups)

    @property
    @pulumi.getter(name="ec2SshKey")
    def ec2_ssh_key(self) -> str:
        return pulumi.get(self, "ec2_ssh_key")

    @property
    @pulumi.getter(name="sourceSecurityGroups")
    def source_security_groups(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "source_security_groups")


@pulumi.output_type
class NodegroupScalingConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "desiredSize":
            suggest = "desired_size"
        elif key == "maxSize":
            suggest = "max_size"
        elif key == "minSize":
            suggest = "min_size"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NodegroupScalingConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NodegroupScalingConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NodegroupScalingConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 desired_size: Optional[float] = None,
                 max_size: Optional[float] = None,
                 min_size: Optional[float] = None):
        if desired_size is not None:
            pulumi.set(__self__, "desired_size", desired_size)
        if max_size is not None:
            pulumi.set(__self__, "max_size", max_size)
        if min_size is not None:
            pulumi.set(__self__, "min_size", min_size)

    @property
    @pulumi.getter(name="desiredSize")
    def desired_size(self) -> Optional[float]:
        return pulumi.get(self, "desired_size")

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[float]:
        return pulumi.get(self, "max_size")

    @property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[float]:
        return pulumi.get(self, "min_size")


@pulumi.output_type
class NodegroupTaint(dict):
    def __init__(__self__, *,
                 effect: Optional[str] = None,
                 key: Optional[str] = None,
                 value: Optional[str] = None):
        if effect is not None:
            pulumi.set(__self__, "effect", effect)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def effect(self) -> Optional[str]:
        return pulumi.get(self, "effect")

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


@pulumi.output_type
class NodegroupUpdateConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "maxUnavailable":
            suggest = "max_unavailable"
        elif key == "maxUnavailablePercentage":
            suggest = "max_unavailable_percentage"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NodegroupUpdateConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NodegroupUpdateConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NodegroupUpdateConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 max_unavailable: Optional[float] = None,
                 max_unavailable_percentage: Optional[float] = None):
        if max_unavailable is not None:
            pulumi.set(__self__, "max_unavailable", max_unavailable)
        if max_unavailable_percentage is not None:
            pulumi.set(__self__, "max_unavailable_percentage", max_unavailable_percentage)

    @property
    @pulumi.getter(name="maxUnavailable")
    def max_unavailable(self) -> Optional[float]:
        return pulumi.get(self, "max_unavailable")

    @property
    @pulumi.getter(name="maxUnavailablePercentage")
    def max_unavailable_percentage(self) -> Optional[float]:
        return pulumi.get(self, "max_unavailable_percentage")


