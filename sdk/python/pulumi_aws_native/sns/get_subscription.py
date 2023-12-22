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
    'GetSubscriptionResult',
    'AwaitableGetSubscriptionResult',
    'get_subscription',
    'get_subscription_output',
]

@pulumi.output_type
class GetSubscriptionResult:
    def __init__(__self__, delivery_policy=None, filter_policy=None, filter_policy_scope=None, id=None, raw_message_delivery=None, redrive_policy=None, region=None, replay_policy=None, subscription_role_arn=None):
        if delivery_policy and not isinstance(delivery_policy, dict):
            raise TypeError("Expected argument 'delivery_policy' to be a dict")
        pulumi.set(__self__, "delivery_policy", delivery_policy)
        if filter_policy and not isinstance(filter_policy, dict):
            raise TypeError("Expected argument 'filter_policy' to be a dict")
        pulumi.set(__self__, "filter_policy", filter_policy)
        if filter_policy_scope and not isinstance(filter_policy_scope, str):
            raise TypeError("Expected argument 'filter_policy_scope' to be a str")
        pulumi.set(__self__, "filter_policy_scope", filter_policy_scope)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if raw_message_delivery and not isinstance(raw_message_delivery, bool):
            raise TypeError("Expected argument 'raw_message_delivery' to be a bool")
        pulumi.set(__self__, "raw_message_delivery", raw_message_delivery)
        if redrive_policy and not isinstance(redrive_policy, dict):
            raise TypeError("Expected argument 'redrive_policy' to be a dict")
        pulumi.set(__self__, "redrive_policy", redrive_policy)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if replay_policy and not isinstance(replay_policy, dict):
            raise TypeError("Expected argument 'replay_policy' to be a dict")
        pulumi.set(__self__, "replay_policy", replay_policy)
        if subscription_role_arn and not isinstance(subscription_role_arn, str):
            raise TypeError("Expected argument 'subscription_role_arn' to be a str")
        pulumi.set(__self__, "subscription_role_arn", subscription_role_arn)

    @property
    @pulumi.getter(name="deliveryPolicy")
    def delivery_policy(self) -> Optional[Any]:
        return pulumi.get(self, "delivery_policy")

    @property
    @pulumi.getter(name="filterPolicy")
    def filter_policy(self) -> Optional[Any]:
        return pulumi.get(self, "filter_policy")

    @property
    @pulumi.getter(name="filterPolicyScope")
    def filter_policy_scope(self) -> Optional[str]:
        return pulumi.get(self, "filter_policy_scope")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="rawMessageDelivery")
    def raw_message_delivery(self) -> Optional[bool]:
        return pulumi.get(self, "raw_message_delivery")

    @property
    @pulumi.getter(name="redrivePolicy")
    def redrive_policy(self) -> Optional[Any]:
        return pulumi.get(self, "redrive_policy")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="replayPolicy")
    def replay_policy(self) -> Optional[Any]:
        return pulumi.get(self, "replay_policy")

    @property
    @pulumi.getter(name="subscriptionRoleArn")
    def subscription_role_arn(self) -> Optional[str]:
        return pulumi.get(self, "subscription_role_arn")


class AwaitableGetSubscriptionResult(GetSubscriptionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSubscriptionResult(
            delivery_policy=self.delivery_policy,
            filter_policy=self.filter_policy,
            filter_policy_scope=self.filter_policy_scope,
            id=self.id,
            raw_message_delivery=self.raw_message_delivery,
            redrive_policy=self.redrive_policy,
            region=self.region,
            replay_policy=self.replay_policy,
            subscription_role_arn=self.subscription_role_arn)


def get_subscription(id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSubscriptionResult:
    """
    Resource Type definition for AWS::SNS::Subscription
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:sns:getSubscription', __args__, opts=opts, typ=GetSubscriptionResult).value

    return AwaitableGetSubscriptionResult(
        delivery_policy=pulumi.get(__ret__, 'delivery_policy'),
        filter_policy=pulumi.get(__ret__, 'filter_policy'),
        filter_policy_scope=pulumi.get(__ret__, 'filter_policy_scope'),
        id=pulumi.get(__ret__, 'id'),
        raw_message_delivery=pulumi.get(__ret__, 'raw_message_delivery'),
        redrive_policy=pulumi.get(__ret__, 'redrive_policy'),
        region=pulumi.get(__ret__, 'region'),
        replay_policy=pulumi.get(__ret__, 'replay_policy'),
        subscription_role_arn=pulumi.get(__ret__, 'subscription_role_arn'))


@_utilities.lift_output_func(get_subscription)
def get_subscription_output(id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSubscriptionResult]:
    """
    Resource Type definition for AWS::SNS::Subscription
    """
    ...
