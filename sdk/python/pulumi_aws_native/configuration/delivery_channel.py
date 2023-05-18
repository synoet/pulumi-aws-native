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
from ._inputs import *

__all__ = ['DeliveryChannelArgs', 'DeliveryChannel']

@pulumi.input_type
class DeliveryChannelArgs:
    def __init__(__self__, *,
                 s3_bucket_name: pulumi.Input[str],
                 config_snapshot_delivery_properties: Optional[pulumi.Input['DeliveryChannelConfigSnapshotDeliveryPropertiesArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 s3_key_prefix: Optional[pulumi.Input[str]] = None,
                 s3_kms_key_arn: Optional[pulumi.Input[str]] = None,
                 sns_topic_arn: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DeliveryChannel resource.
        """
        pulumi.set(__self__, "s3_bucket_name", s3_bucket_name)
        if config_snapshot_delivery_properties is not None:
            pulumi.set(__self__, "config_snapshot_delivery_properties", config_snapshot_delivery_properties)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if s3_key_prefix is not None:
            pulumi.set(__self__, "s3_key_prefix", s3_key_prefix)
        if s3_kms_key_arn is not None:
            pulumi.set(__self__, "s3_kms_key_arn", s3_kms_key_arn)
        if sns_topic_arn is not None:
            pulumi.set(__self__, "sns_topic_arn", sns_topic_arn)

    @property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "s3_bucket_name")

    @s3_bucket_name.setter
    def s3_bucket_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "s3_bucket_name", value)

    @property
    @pulumi.getter(name="configSnapshotDeliveryProperties")
    def config_snapshot_delivery_properties(self) -> Optional[pulumi.Input['DeliveryChannelConfigSnapshotDeliveryPropertiesArgs']]:
        return pulumi.get(self, "config_snapshot_delivery_properties")

    @config_snapshot_delivery_properties.setter
    def config_snapshot_delivery_properties(self, value: Optional[pulumi.Input['DeliveryChannelConfigSnapshotDeliveryPropertiesArgs']]):
        pulumi.set(self, "config_snapshot_delivery_properties", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "s3_key_prefix")

    @s3_key_prefix.setter
    def s3_key_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "s3_key_prefix", value)

    @property
    @pulumi.getter(name="s3KmsKeyArn")
    def s3_kms_key_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "s3_kms_key_arn")

    @s3_kms_key_arn.setter
    def s3_kms_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "s3_kms_key_arn", value)

    @property
    @pulumi.getter(name="snsTopicARN")
    def sns_topic_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sns_topic_arn")

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sns_topic_arn", value)


warnings.warn("""DeliveryChannel is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class DeliveryChannel(pulumi.CustomResource):
    warnings.warn("""DeliveryChannel is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config_snapshot_delivery_properties: Optional[pulumi.Input[pulumi.InputType['DeliveryChannelConfigSnapshotDeliveryPropertiesArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 s3_bucket_name: Optional[pulumi.Input[str]] = None,
                 s3_key_prefix: Optional[pulumi.Input[str]] = None,
                 s3_kms_key_arn: Optional[pulumi.Input[str]] = None,
                 sns_topic_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Config::DeliveryChannel

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeliveryChannelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Config::DeliveryChannel

        :param str resource_name: The name of the resource.
        :param DeliveryChannelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeliveryChannelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config_snapshot_delivery_properties: Optional[pulumi.Input[pulumi.InputType['DeliveryChannelConfigSnapshotDeliveryPropertiesArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 s3_bucket_name: Optional[pulumi.Input[str]] = None,
                 s3_key_prefix: Optional[pulumi.Input[str]] = None,
                 s3_kms_key_arn: Optional[pulumi.Input[str]] = None,
                 sns_topic_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""DeliveryChannel is deprecated: DeliveryChannel is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeliveryChannelArgs.__new__(DeliveryChannelArgs)

            __props__.__dict__["config_snapshot_delivery_properties"] = config_snapshot_delivery_properties
            __props__.__dict__["name"] = name
            if s3_bucket_name is None and not opts.urn:
                raise TypeError("Missing required property 's3_bucket_name'")
            __props__.__dict__["s3_bucket_name"] = s3_bucket_name
            __props__.__dict__["s3_key_prefix"] = s3_key_prefix
            __props__.__dict__["s3_kms_key_arn"] = s3_kms_key_arn
            __props__.__dict__["sns_topic_arn"] = sns_topic_arn
        super(DeliveryChannel, __self__).__init__(
            'aws-native:configuration:DeliveryChannel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DeliveryChannel':
        """
        Get an existing DeliveryChannel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DeliveryChannelArgs.__new__(DeliveryChannelArgs)

        __props__.__dict__["config_snapshot_delivery_properties"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["s3_bucket_name"] = None
        __props__.__dict__["s3_key_prefix"] = None
        __props__.__dict__["s3_kms_key_arn"] = None
        __props__.__dict__["sns_topic_arn"] = None
        return DeliveryChannel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="configSnapshotDeliveryProperties")
    def config_snapshot_delivery_properties(self) -> pulumi.Output[Optional['outputs.DeliveryChannelConfigSnapshotDeliveryProperties']]:
        return pulumi.get(self, "config_snapshot_delivery_properties")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "s3_bucket_name")

    @property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "s3_key_prefix")

    @property
    @pulumi.getter(name="s3KmsKeyArn")
    def s3_kms_key_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "s3_kms_key_arn")

    @property
    @pulumi.getter(name="snsTopicARN")
    def sns_topic_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "sns_topic_arn")

