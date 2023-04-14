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

__all__ = ['PublicTypeVersionArgs', 'PublicTypeVersion']

@pulumi.input_type
class PublicTypeVersionArgs:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 log_delivery_bucket: Optional[pulumi.Input[str]] = None,
                 public_version_number: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['PublicTypeVersionType']] = None,
                 type_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PublicTypeVersion resource.
        :param pulumi.Input[str] arn: The Amazon Resource Number (ARN) of the extension.
        :param pulumi.Input[str] log_delivery_bucket: A url to the S3 bucket where logs for the testType run will be available
        :param pulumi.Input[str] public_version_number: The version number of a public third-party extension
        :param pulumi.Input['PublicTypeVersionType'] type: The kind of extension
        :param pulumi.Input[str] type_name: The name of the type being registered.
               
               We recommend that type names adhere to the following pattern: company_or_organization::service::type.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if log_delivery_bucket is not None:
            pulumi.set(__self__, "log_delivery_bucket", log_delivery_bucket)
        if public_version_number is not None:
            pulumi.set(__self__, "public_version_number", public_version_number)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if type_name is not None:
            pulumi.set(__self__, "type_name", type_name)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Number (ARN) of the extension.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="logDeliveryBucket")
    def log_delivery_bucket(self) -> Optional[pulumi.Input[str]]:
        """
        A url to the S3 bucket where logs for the testType run will be available
        """
        return pulumi.get(self, "log_delivery_bucket")

    @log_delivery_bucket.setter
    def log_delivery_bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_delivery_bucket", value)

    @property
    @pulumi.getter(name="publicVersionNumber")
    def public_version_number(self) -> Optional[pulumi.Input[str]]:
        """
        The version number of a public third-party extension
        """
        return pulumi.get(self, "public_version_number")

    @public_version_number.setter
    def public_version_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_version_number", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['PublicTypeVersionType']]:
        """
        The kind of extension
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['PublicTypeVersionType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="typeName")
    def type_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the type being registered.

        We recommend that type names adhere to the following pattern: company_or_organization::service::type.
        """
        return pulumi.get(self, "type_name")

    @type_name.setter
    def type_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type_name", value)


class PublicTypeVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 log_delivery_bucket: Optional[pulumi.Input[str]] = None,
                 public_version_number: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['PublicTypeVersionType']] = None,
                 type_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Test and Publish a resource that has been registered in the CloudFormation Registry.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Number (ARN) of the extension.
        :param pulumi.Input[str] log_delivery_bucket: A url to the S3 bucket where logs for the testType run will be available
        :param pulumi.Input[str] public_version_number: The version number of a public third-party extension
        :param pulumi.Input['PublicTypeVersionType'] type: The kind of extension
        :param pulumi.Input[str] type_name: The name of the type being registered.
               
               We recommend that type names adhere to the following pattern: company_or_organization::service::type.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[PublicTypeVersionArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Test and Publish a resource that has been registered in the CloudFormation Registry.

        :param str resource_name: The name of the resource.
        :param PublicTypeVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PublicTypeVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 log_delivery_bucket: Optional[pulumi.Input[str]] = None,
                 public_version_number: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['PublicTypeVersionType']] = None,
                 type_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PublicTypeVersionArgs.__new__(PublicTypeVersionArgs)

            __props__.__dict__["arn"] = arn
            __props__.__dict__["log_delivery_bucket"] = log_delivery_bucket
            __props__.__dict__["public_version_number"] = public_version_number
            __props__.__dict__["type"] = type
            __props__.__dict__["type_name"] = type_name
            __props__.__dict__["public_type_arn"] = None
            __props__.__dict__["publisher_id"] = None
            __props__.__dict__["type_version_arn"] = None
        super(PublicTypeVersion, __self__).__init__(
            'aws-native:cloudformation:PublicTypeVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PublicTypeVersion':
        """
        Get an existing PublicTypeVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PublicTypeVersionArgs.__new__(PublicTypeVersionArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["log_delivery_bucket"] = None
        __props__.__dict__["public_type_arn"] = None
        __props__.__dict__["public_version_number"] = None
        __props__.__dict__["publisher_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["type_name"] = None
        __props__.__dict__["type_version_arn"] = None
        return PublicTypeVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Number (ARN) of the extension.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="logDeliveryBucket")
    def log_delivery_bucket(self) -> pulumi.Output[Optional[str]]:
        """
        A url to the S3 bucket where logs for the testType run will be available
        """
        return pulumi.get(self, "log_delivery_bucket")

    @property
    @pulumi.getter(name="publicTypeArn")
    def public_type_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Number (ARN) assigned to the public extension upon publication
        """
        return pulumi.get(self, "public_type_arn")

    @property
    @pulumi.getter(name="publicVersionNumber")
    def public_version_number(self) -> pulumi.Output[Optional[str]]:
        """
        The version number of a public third-party extension
        """
        return pulumi.get(self, "public_version_number")

    @property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> pulumi.Output[str]:
        """
        The publisher id assigned by CloudFormation for publishing in this region.
        """
        return pulumi.get(self, "publisher_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional['PublicTypeVersionType']]:
        """
        The kind of extension
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the type being registered.

        We recommend that type names adhere to the following pattern: company_or_organization::service::type.
        """
        return pulumi.get(self, "type_name")

    @property
    @pulumi.getter(name="typeVersionArn")
    def type_version_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Number (ARN) of the extension with the versionId.
        """
        return pulumi.get(self, "type_version_arn")

