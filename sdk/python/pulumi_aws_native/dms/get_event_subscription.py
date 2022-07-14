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
    'GetEventSubscriptionResult',
    'AwaitableGetEventSubscriptionResult',
    'get_event_subscription',
    'get_event_subscription_output',
]

@pulumi.output_type
class GetEventSubscriptionResult:
    def __init__(__self__, enabled=None, event_categories=None, id=None, sns_topic_arn=None, source_type=None):
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if event_categories and not isinstance(event_categories, list):
            raise TypeError("Expected argument 'event_categories' to be a list")
        pulumi.set(__self__, "event_categories", event_categories)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if sns_topic_arn and not isinstance(sns_topic_arn, str):
            raise TypeError("Expected argument 'sns_topic_arn' to be a str")
        pulumi.set(__self__, "sns_topic_arn", sns_topic_arn)
        if source_type and not isinstance(source_type, str):
            raise TypeError("Expected argument 'source_type' to be a str")
        pulumi.set(__self__, "source_type", source_type)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="eventCategories")
    def event_categories(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "event_categories")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[str]:
        return pulumi.get(self, "sns_topic_arn")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[str]:
        return pulumi.get(self, "source_type")


class AwaitableGetEventSubscriptionResult(GetEventSubscriptionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEventSubscriptionResult(
            enabled=self.enabled,
            event_categories=self.event_categories,
            id=self.id,
            sns_topic_arn=self.sns_topic_arn,
            source_type=self.source_type)


def get_event_subscription(id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEventSubscriptionResult:
    """
    Resource Type definition for AWS::DMS::EventSubscription
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:dms:getEventSubscription', __args__, opts=opts, typ=GetEventSubscriptionResult).value

    return AwaitableGetEventSubscriptionResult(
        enabled=__ret__.enabled,
        event_categories=__ret__.event_categories,
        id=__ret__.id,
        sns_topic_arn=__ret__.sns_topic_arn,
        source_type=__ret__.source_type)


@_utilities.lift_output_func(get_event_subscription)
def get_event_subscription_output(id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEventSubscriptionResult]:
    """
    Resource Type definition for AWS::DMS::EventSubscription
    """
    ...
