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
    'AcceleratorTag',
    'EndpointGroupEndpointConfiguration',
    'EndpointGroupPortOverride',
    'ListenerPortRange',
]

@pulumi.output_type
class AcceleratorTag(dict):
    """
    Tag is a key-value pair associated with accelerator.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        Tag is a key-value pair associated with accelerator.
        :param str key: Key of the tag. Value can be 1 to 127 characters.
        :param str value: Value for the tag. Value can be 1 to 255 characters.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Key of the tag. Value can be 1 to 127 characters.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Value for the tag. Value can be 1 to 255 characters.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class EndpointGroupEndpointConfiguration(dict):
    """
    The configuration for a given endpoint
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endpointId":
            suggest = "endpoint_id"
        elif key == "clientIpPreservationEnabled":
            suggest = "client_ip_preservation_enabled"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EndpointGroupEndpointConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EndpointGroupEndpointConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EndpointGroupEndpointConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 endpoint_id: str,
                 client_ip_preservation_enabled: Optional[bool] = None,
                 weight: Optional[int] = None):
        """
        The configuration for a given endpoint
        :param str endpoint_id: Id of the endpoint. For Network/Application Load Balancer this value is the ARN.  For EIP, this value is the allocation ID.  For EC2 instances, this is the EC2 instance ID
        :param bool client_ip_preservation_enabled: true if client ip should be preserved
        :param int weight: The weight for the endpoint.
        """
        pulumi.set(__self__, "endpoint_id", endpoint_id)
        if client_ip_preservation_enabled is not None:
            pulumi.set(__self__, "client_ip_preservation_enabled", client_ip_preservation_enabled)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> str:
        """
        Id of the endpoint. For Network/Application Load Balancer this value is the ARN.  For EIP, this value is the allocation ID.  For EC2 instances, this is the EC2 instance ID
        """
        return pulumi.get(self, "endpoint_id")

    @property
    @pulumi.getter(name="clientIpPreservationEnabled")
    def client_ip_preservation_enabled(self) -> Optional[bool]:
        """
        true if client ip should be preserved
        """
        return pulumi.get(self, "client_ip_preservation_enabled")

    @property
    @pulumi.getter
    def weight(self) -> Optional[int]:
        """
        The weight for the endpoint.
        """
        return pulumi.get(self, "weight")


@pulumi.output_type
class EndpointGroupPortOverride(dict):
    """
    listener to endpoint port mapping.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endpointPort":
            suggest = "endpoint_port"
        elif key == "listenerPort":
            suggest = "listener_port"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EndpointGroupPortOverride. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EndpointGroupPortOverride.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EndpointGroupPortOverride.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 endpoint_port: int,
                 listener_port: int):
        """
        listener to endpoint port mapping.
        """
        pulumi.set(__self__, "endpoint_port", endpoint_port)
        pulumi.set(__self__, "listener_port", listener_port)

    @property
    @pulumi.getter(name="endpointPort")
    def endpoint_port(self) -> int:
        return pulumi.get(self, "endpoint_port")

    @property
    @pulumi.getter(name="listenerPort")
    def listener_port(self) -> int:
        return pulumi.get(self, "listener_port")


@pulumi.output_type
class ListenerPortRange(dict):
    """
    A port range to support for connections from  clients to your accelerator.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fromPort":
            suggest = "from_port"
        elif key == "toPort":
            suggest = "to_port"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ListenerPortRange. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ListenerPortRange.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ListenerPortRange.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 from_port: int,
                 to_port: int):
        """
        A port range to support for connections from  clients to your accelerator.
        """
        pulumi.set(__self__, "from_port", from_port)
        pulumi.set(__self__, "to_port", to_port)

    @property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> int:
        return pulumi.get(self, "from_port")

    @property
    @pulumi.getter(name="toPort")
    def to_port(self) -> int:
        return pulumi.get(self, "to_port")


