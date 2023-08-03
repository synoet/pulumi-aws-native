# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetVpcEndpointConnectionNotificationResult',
    'AwaitableGetVpcEndpointConnectionNotificationResult',
    'get_vpc_endpoint_connection_notification',
    'get_vpc_endpoint_connection_notification_output',
]

@pulumi.output_type
class GetVpcEndpointConnectionNotificationResult:
    def __init__(__self__, connection_events=None, connection_notification_arn=None, id=None):
        if connection_events and not isinstance(connection_events, list):
            raise TypeError("Expected argument 'connection_events' to be a list")
        pulumi.set(__self__, "connection_events", connection_events)
        if connection_notification_arn and not isinstance(connection_notification_arn, str):
            raise TypeError("Expected argument 'connection_notification_arn' to be a str")
        pulumi.set(__self__, "connection_notification_arn", connection_notification_arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="connectionEvents")
    def connection_events(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "connection_events")

    @property
    @pulumi.getter(name="connectionNotificationArn")
    def connection_notification_arn(self) -> Optional[str]:
        return pulumi.get(self, "connection_notification_arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetVpcEndpointConnectionNotificationResult(GetVpcEndpointConnectionNotificationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcEndpointConnectionNotificationResult(
            connection_events=self.connection_events,
            connection_notification_arn=self.connection_notification_arn,
            id=self.id)


def get_vpc_endpoint_connection_notification(id: Optional[str] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpcEndpointConnectionNotificationResult:
    """
    Resource Type definition for AWS::EC2::VPCEndpointConnectionNotification
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getVpcEndpointConnectionNotification', __args__, opts=opts, typ=GetVpcEndpointConnectionNotificationResult).value

    return AwaitableGetVpcEndpointConnectionNotificationResult(
        connection_events=pulumi.get(__ret__, 'connection_events'),
        connection_notification_arn=pulumi.get(__ret__, 'connection_notification_arn'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_vpc_endpoint_connection_notification)
def get_vpc_endpoint_connection_notification_output(id: Optional[pulumi.Input[str]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVpcEndpointConnectionNotificationResult]:
    """
    Resource Type definition for AWS::EC2::VPCEndpointConnectionNotification
    """
    ...
