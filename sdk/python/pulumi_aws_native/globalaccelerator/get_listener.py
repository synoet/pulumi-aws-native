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

__all__ = [
    'GetListenerResult',
    'AwaitableGetListenerResult',
    'get_listener',
    'get_listener_output',
]

@pulumi.output_type
class GetListenerResult:
    def __init__(__self__, client_affinity=None, listener_arn=None, port_ranges=None, protocol=None):
        if client_affinity and not isinstance(client_affinity, str):
            raise TypeError("Expected argument 'client_affinity' to be a str")
        pulumi.set(__self__, "client_affinity", client_affinity)
        if listener_arn and not isinstance(listener_arn, str):
            raise TypeError("Expected argument 'listener_arn' to be a str")
        pulumi.set(__self__, "listener_arn", listener_arn)
        if port_ranges and not isinstance(port_ranges, list):
            raise TypeError("Expected argument 'port_ranges' to be a list")
        pulumi.set(__self__, "port_ranges", port_ranges)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter(name="clientAffinity")
    def client_affinity(self) -> Optional['ListenerClientAffinity']:
        """
        Client affinity lets you direct all requests from a user to the same endpoint.
        """
        return pulumi.get(self, "client_affinity")

    @property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the listener.
        """
        return pulumi.get(self, "listener_arn")

    @property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[Sequence['outputs.ListenerPortRange']]:
        return pulumi.get(self, "port_ranges")

    @property
    @pulumi.getter
    def protocol(self) -> Optional['ListenerProtocol']:
        """
        The protocol for the listener.
        """
        return pulumi.get(self, "protocol")


class AwaitableGetListenerResult(GetListenerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetListenerResult(
            client_affinity=self.client_affinity,
            listener_arn=self.listener_arn,
            port_ranges=self.port_ranges,
            protocol=self.protocol)


def get_listener(listener_arn: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetListenerResult:
    """
    Resource Type definition for AWS::GlobalAccelerator::Listener


    :param str listener_arn: The Amazon Resource Name (ARN) of the listener.
    """
    __args__ = dict()
    __args__['listenerArn'] = listener_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:globalaccelerator:getListener', __args__, opts=opts, typ=GetListenerResult).value

    return AwaitableGetListenerResult(
        client_affinity=__ret__.client_affinity,
        listener_arn=__ret__.listener_arn,
        port_ranges=__ret__.port_ranges,
        protocol=__ret__.protocol)


@_utilities.lift_output_func(get_listener)
def get_listener_output(listener_arn: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetListenerResult]:
    """
    Resource Type definition for AWS::GlobalAccelerator::Listener


    :param str listener_arn: The Amazon Resource Name (ARN) of the listener.
    """
    ...
