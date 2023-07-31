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
    'GetDeliveryChannelResult',
    'AwaitableGetDeliveryChannelResult',
    'get_delivery_channel',
    'get_delivery_channel_output',
]

@pulumi.output_type
class GetDeliveryChannelResult:
    def __init__(__self__, config_snapshot_delivery_properties=None, id=None, s3_bucket_name=None, s3_key_prefix=None, s3_kms_key_arn=None, sns_topic_arn=None):
        if config_snapshot_delivery_properties and not isinstance(config_snapshot_delivery_properties, dict):
            raise TypeError("Expected argument 'config_snapshot_delivery_properties' to be a dict")
        pulumi.set(__self__, "config_snapshot_delivery_properties", config_snapshot_delivery_properties)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if s3_bucket_name and not isinstance(s3_bucket_name, str):
            raise TypeError("Expected argument 's3_bucket_name' to be a str")
        pulumi.set(__self__, "s3_bucket_name", s3_bucket_name)
        if s3_key_prefix and not isinstance(s3_key_prefix, str):
            raise TypeError("Expected argument 's3_key_prefix' to be a str")
        pulumi.set(__self__, "s3_key_prefix", s3_key_prefix)
        if s3_kms_key_arn and not isinstance(s3_kms_key_arn, str):
            raise TypeError("Expected argument 's3_kms_key_arn' to be a str")
        pulumi.set(__self__, "s3_kms_key_arn", s3_kms_key_arn)
        if sns_topic_arn and not isinstance(sns_topic_arn, str):
            raise TypeError("Expected argument 'sns_topic_arn' to be a str")
        pulumi.set(__self__, "sns_topic_arn", sns_topic_arn)

    @property
    @pulumi.getter(name="configSnapshotDeliveryProperties")
    def config_snapshot_delivery_properties(self) -> Optional['outputs.DeliveryChannelConfigSnapshotDeliveryProperties']:
        return pulumi.get(self, "config_snapshot_delivery_properties")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> Optional[str]:
        return pulumi.get(self, "s3_bucket_name")

    @property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[str]:
        return pulumi.get(self, "s3_key_prefix")

    @property
    @pulumi.getter(name="s3KmsKeyArn")
    def s3_kms_key_arn(self) -> Optional[str]:
        return pulumi.get(self, "s3_kms_key_arn")

    @property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[str]:
        return pulumi.get(self, "sns_topic_arn")


class AwaitableGetDeliveryChannelResult(GetDeliveryChannelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeliveryChannelResult(
            config_snapshot_delivery_properties=self.config_snapshot_delivery_properties,
            id=self.id,
            s3_bucket_name=self.s3_bucket_name,
            s3_key_prefix=self.s3_key_prefix,
            s3_kms_key_arn=self.s3_kms_key_arn,
            sns_topic_arn=self.sns_topic_arn)


def get_delivery_channel(id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeliveryChannelResult:
    """
    Resource Type definition for AWS::Config::DeliveryChannel
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:configuration:getDeliveryChannel', __args__, opts=opts, typ=GetDeliveryChannelResult).value

    return AwaitableGetDeliveryChannelResult(
        config_snapshot_delivery_properties=pulumi.get(__ret__, 'config_snapshot_delivery_properties'),
        id=pulumi.get(__ret__, 'id'),
        s3_bucket_name=pulumi.get(__ret__, 's3_bucket_name'),
        s3_key_prefix=pulumi.get(__ret__, 's3_key_prefix'),
        s3_kms_key_arn=pulumi.get(__ret__, 's3_kms_key_arn'),
        sns_topic_arn=pulumi.get(__ret__, 'sns_topic_arn'))


@_utilities.lift_output_func(get_delivery_channel)
def get_delivery_channel_output(id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeliveryChannelResult]:
    """
    Resource Type definition for AWS::Config::DeliveryChannel
    """
    ...
