# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._inputs import *

__all__ = ['LocationS3Args', 'LocationS3']

@pulumi.input_type
class LocationS3Args:
    def __init__(__self__, *,
                 s3_bucket_arn: pulumi.Input[str],
                 s3_config: pulumi.Input['LocationS3S3ConfigArgs'],
                 s3_storage_class: Optional[pulumi.Input[str]] = None,
                 subdirectory: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a LocationS3 resource.
        :param pulumi.Input[str] s3_bucket_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3bucketarn
        :param pulumi.Input['LocationS3S3ConfigArgs'] s3_config: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3config
        :param pulumi.Input[str] s3_storage_class: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3storageclass
        :param pulumi.Input[str] subdirectory: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-subdirectory
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-tags
        """
        pulumi.set(__self__, "s3_bucket_arn", s3_bucket_arn)
        pulumi.set(__self__, "s3_config", s3_config)
        if s3_storage_class is not None:
            pulumi.set(__self__, "s3_storage_class", s3_storage_class)
        if subdirectory is not None:
            pulumi.set(__self__, "subdirectory", subdirectory)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="s3BucketArn")
    def s3_bucket_arn(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3bucketarn
        """
        return pulumi.get(self, "s3_bucket_arn")

    @s3_bucket_arn.setter
    def s3_bucket_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "s3_bucket_arn", value)

    @property
    @pulumi.getter(name="s3Config")
    def s3_config(self) -> pulumi.Input['LocationS3S3ConfigArgs']:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3config
        """
        return pulumi.get(self, "s3_config")

    @s3_config.setter
    def s3_config(self, value: pulumi.Input['LocationS3S3ConfigArgs']):
        pulumi.set(self, "s3_config", value)

    @property
    @pulumi.getter(name="s3StorageClass")
    def s3_storage_class(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3storageclass
        """
        return pulumi.get(self, "s3_storage_class")

    @s3_storage_class.setter
    def s3_storage_class(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "s3_storage_class", value)

    @property
    @pulumi.getter
    def subdirectory(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-subdirectory
        """
        return pulumi.get(self, "subdirectory")

    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subdirectory", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class LocationS3(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 s3_bucket_arn: Optional[pulumi.Input[str]] = None,
                 s3_config: Optional[pulumi.Input[pulumi.InputType['LocationS3S3ConfigArgs']]] = None,
                 s3_storage_class: Optional[pulumi.Input[str]] = None,
                 subdirectory: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] s3_bucket_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3bucketarn
        :param pulumi.Input[pulumi.InputType['LocationS3S3ConfigArgs']] s3_config: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3config
        :param pulumi.Input[str] s3_storage_class: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3storageclass
        :param pulumi.Input[str] subdirectory: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-subdirectory
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LocationS3Args,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html

        :param str resource_name: The name of the resource.
        :param LocationS3Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LocationS3Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 s3_bucket_arn: Optional[pulumi.Input[str]] = None,
                 s3_config: Optional[pulumi.Input[pulumi.InputType['LocationS3S3ConfigArgs']]] = None,
                 s3_storage_class: Optional[pulumi.Input[str]] = None,
                 subdirectory: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LocationS3Args.__new__(LocationS3Args)

            if s3_bucket_arn is None and not opts.urn:
                raise TypeError("Missing required property 's3_bucket_arn'")
            __props__.__dict__["s3_bucket_arn"] = s3_bucket_arn
            if s3_config is None and not opts.urn:
                raise TypeError("Missing required property 's3_config'")
            __props__.__dict__["s3_config"] = s3_config
            __props__.__dict__["s3_storage_class"] = s3_storage_class
            __props__.__dict__["subdirectory"] = subdirectory
            __props__.__dict__["tags"] = tags
            __props__.__dict__["location_arn"] = None
            __props__.__dict__["location_uri"] = None
        super(LocationS3, __self__).__init__(
            'aws-native:datasync:LocationS3',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LocationS3':
        """
        Get an existing LocationS3 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LocationS3Args.__new__(LocationS3Args)

        __props__.__dict__["location_arn"] = None
        __props__.__dict__["location_uri"] = None
        __props__.__dict__["s3_bucket_arn"] = None
        __props__.__dict__["s3_config"] = None
        __props__.__dict__["s3_storage_class"] = None
        __props__.__dict__["subdirectory"] = None
        __props__.__dict__["tags"] = None
        return LocationS3(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="locationArn")
    def location_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location_arn")

    @property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location_uri")

    @property
    @pulumi.getter(name="s3BucketArn")
    def s3_bucket_arn(self) -> pulumi.Output[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3bucketarn
        """
        return pulumi.get(self, "s3_bucket_arn")

    @property
    @pulumi.getter(name="s3Config")
    def s3_config(self) -> pulumi.Output['outputs.LocationS3S3Config']:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3config
        """
        return pulumi.get(self, "s3_config")

    @property
    @pulumi.getter(name="s3StorageClass")
    def s3_storage_class(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3storageclass
        """
        return pulumi.get(self, "s3_storage_class")

    @property
    @pulumi.getter
    def subdirectory(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-subdirectory
        """
        return pulumi.get(self, "subdirectory")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-tags
        """
        return pulumi.get(self, "tags")

