# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SubscriptionArgs', 'Subscription']

@pulumi.input_type
class SubscriptionArgs:
    def __init__(__self__, *,
                 protocol: pulumi.Input[str],
                 topic_arn: pulumi.Input[str],
                 delivery_policy: Optional[Any] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 filter_policy: Optional[Any] = None,
                 raw_message_delivery: Optional[pulumi.Input[bool]] = None,
                 redrive_policy: Optional[Any] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 subscription_role_arn: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Subscription resource.
        """
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "topic_arn", topic_arn)
        if delivery_policy is not None:
            pulumi.set(__self__, "delivery_policy", delivery_policy)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if filter_policy is not None:
            pulumi.set(__self__, "filter_policy", filter_policy)
        if raw_message_delivery is not None:
            pulumi.set(__self__, "raw_message_delivery", raw_message_delivery)
        if redrive_policy is not None:
            pulumi.set(__self__, "redrive_policy", redrive_policy)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if subscription_role_arn is not None:
            pulumi.set(__self__, "subscription_role_arn", subscription_role_arn)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[str]:
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "topic_arn")

    @topic_arn.setter
    def topic_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "topic_arn", value)

    @property
    @pulumi.getter(name="deliveryPolicy")
    def delivery_policy(self) -> Optional[Any]:
        return pulumi.get(self, "delivery_policy")

    @delivery_policy.setter
    def delivery_policy(self, value: Optional[Any]):
        pulumi.set(self, "delivery_policy", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter(name="filterPolicy")
    def filter_policy(self) -> Optional[Any]:
        return pulumi.get(self, "filter_policy")

    @filter_policy.setter
    def filter_policy(self, value: Optional[Any]):
        pulumi.set(self, "filter_policy", value)

    @property
    @pulumi.getter(name="rawMessageDelivery")
    def raw_message_delivery(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "raw_message_delivery")

    @raw_message_delivery.setter
    def raw_message_delivery(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "raw_message_delivery", value)

    @property
    @pulumi.getter(name="redrivePolicy")
    def redrive_policy(self) -> Optional[Any]:
        return pulumi.get(self, "redrive_policy")

    @redrive_policy.setter
    def redrive_policy(self, value: Optional[Any]):
        pulumi.set(self, "redrive_policy", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="subscriptionRoleArn")
    def subscription_role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "subscription_role_arn")

    @subscription_role_arn.setter
    def subscription_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_role_arn", value)


warnings.warn("""Subscription is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Subscription(pulumi.CustomResource):
    warnings.warn("""Subscription is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delivery_policy: Optional[Any] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 filter_policy: Optional[Any] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 raw_message_delivery: Optional[pulumi.Input[bool]] = None,
                 redrive_policy: Optional[Any] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 subscription_role_arn: Optional[pulumi.Input[str]] = None,
                 topic_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SNS::Subscription

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubscriptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SNS::Subscription

        :param str resource_name: The name of the resource.
        :param SubscriptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubscriptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delivery_policy: Optional[Any] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 filter_policy: Optional[Any] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 raw_message_delivery: Optional[pulumi.Input[bool]] = None,
                 redrive_policy: Optional[Any] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 subscription_role_arn: Optional[pulumi.Input[str]] = None,
                 topic_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Subscription is deprecated: Subscription is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SubscriptionArgs.__new__(SubscriptionArgs)

            __props__.__dict__["delivery_policy"] = delivery_policy
            __props__.__dict__["endpoint"] = endpoint
            __props__.__dict__["filter_policy"] = filter_policy
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
            __props__.__dict__["raw_message_delivery"] = raw_message_delivery
            __props__.__dict__["redrive_policy"] = redrive_policy
            __props__.__dict__["region"] = region
            __props__.__dict__["subscription_role_arn"] = subscription_role_arn
            if topic_arn is None and not opts.urn:
                raise TypeError("Missing required property 'topic_arn'")
            __props__.__dict__["topic_arn"] = topic_arn
        super(Subscription, __self__).__init__(
            'aws-native:sns:Subscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Subscription':
        """
        Get an existing Subscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SubscriptionArgs.__new__(SubscriptionArgs)

        __props__.__dict__["delivery_policy"] = None
        __props__.__dict__["endpoint"] = None
        __props__.__dict__["filter_policy"] = None
        __props__.__dict__["protocol"] = None
        __props__.__dict__["raw_message_delivery"] = None
        __props__.__dict__["redrive_policy"] = None
        __props__.__dict__["region"] = None
        __props__.__dict__["subscription_role_arn"] = None
        __props__.__dict__["topic_arn"] = None
        return Subscription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deliveryPolicy")
    def delivery_policy(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "delivery_policy")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="filterPolicy")
    def filter_policy(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "filter_policy")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="rawMessageDelivery")
    def raw_message_delivery(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "raw_message_delivery")

    @property
    @pulumi.getter(name="redrivePolicy")
    def redrive_policy(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "redrive_policy")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="subscriptionRoleArn")
    def subscription_role_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "subscription_role_arn")

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "topic_arn")

