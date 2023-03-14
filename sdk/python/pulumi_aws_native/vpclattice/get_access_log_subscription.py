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
    'GetAccessLogSubscriptionResult',
    'AwaitableGetAccessLogSubscriptionResult',
    'get_access_log_subscription',
    'get_access_log_subscription_output',
]

@pulumi.output_type
class GetAccessLogSubscriptionResult:
    def __init__(__self__, arn=None, destination_arn=None, id=None, resource_arn=None, resource_id=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if destination_arn and not isinstance(destination_arn, str):
            raise TypeError("Expected argument 'destination_arn' to be a str")
        pulumi.set(__self__, "destination_arn", destination_arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if resource_arn and not isinstance(resource_arn, str):
            raise TypeError("Expected argument 'resource_arn' to be a str")
        pulumi.set(__self__, "resource_arn", resource_arn)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> Optional[str]:
        return pulumi.get(self, "destination_arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[str]:
        return pulumi.get(self, "resource_arn")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.AccessLogSubscriptionTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetAccessLogSubscriptionResult(GetAccessLogSubscriptionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccessLogSubscriptionResult(
            arn=self.arn,
            destination_arn=self.destination_arn,
            id=self.id,
            resource_arn=self.resource_arn,
            resource_id=self.resource_id,
            tags=self.tags)


def get_access_log_subscription(arn: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccessLogSubscriptionResult:
    """
    Delivers logs from a Mesh or Service to the provided destination
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:vpclattice:getAccessLogSubscription', __args__, opts=opts, typ=GetAccessLogSubscriptionResult).value

    return AwaitableGetAccessLogSubscriptionResult(
        arn=__ret__.arn,
        destination_arn=__ret__.destination_arn,
        id=__ret__.id,
        resource_arn=__ret__.resource_arn,
        resource_id=__ret__.resource_id,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_access_log_subscription)
def get_access_log_subscription_output(arn: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccessLogSubscriptionResult]:
    """
    Delivers logs from a Mesh or Service to the provided destination
    """
    ...
