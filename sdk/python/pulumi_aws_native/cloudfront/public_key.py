# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['PublicKeyArgs', 'PublicKey']

@pulumi.input_type
class PublicKeyArgs:
    def __init__(__self__, *,
                 public_key_config: pulumi.Input['PublicKeyPublicKeyConfigArgs']):
        """
        The set of arguments for constructing a PublicKey resource.
        :param pulumi.Input['PublicKeyPublicKeyConfigArgs'] public_key_config: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-publickey.html#cfn-cloudfront-publickey-publickeyconfig
        """
        pulumi.set(__self__, "public_key_config", public_key_config)

    @property
    @pulumi.getter(name="publicKeyConfig")
    def public_key_config(self) -> pulumi.Input['PublicKeyPublicKeyConfigArgs']:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-publickey.html#cfn-cloudfront-publickey-publickeyconfig
        """
        return pulumi.get(self, "public_key_config")

    @public_key_config.setter
    def public_key_config(self, value: pulumi.Input['PublicKeyPublicKeyConfigArgs']):
        pulumi.set(self, "public_key_config", value)


class PublicKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 public_key_config: Optional[pulumi.Input[pulumi.InputType['PublicKeyPublicKeyConfigArgs']]] = None,
                 __props__=None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-publickey.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['PublicKeyPublicKeyConfigArgs']] public_key_config: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-publickey.html#cfn-cloudfront-publickey-publickeyconfig
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PublicKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-publickey.html

        :param str resource_name: The name of the resource.
        :param PublicKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PublicKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 public_key_config: Optional[pulumi.Input[pulumi.InputType['PublicKeyPublicKeyConfigArgs']]] = None,
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
            __props__ = PublicKeyArgs.__new__(PublicKeyArgs)

            if public_key_config is None and not opts.urn:
                raise TypeError("Missing required property 'public_key_config'")
            __props__.__dict__["public_key_config"] = public_key_config
            __props__.__dict__["created_time"] = None
            __props__.__dict__["id"] = None
        super(PublicKey, __self__).__init__(
            'aws-native:cloudfront:PublicKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PublicKey':
        """
        Get an existing PublicKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PublicKeyArgs.__new__(PublicKeyArgs)

        __props__.__dict__["created_time"] = None
        __props__.__dict__["id"] = None
        __props__.__dict__["public_key_config"] = None
        return PublicKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="publicKeyConfig")
    def public_key_config(self) -> pulumi.Output['outputs.PublicKeyPublicKeyConfig']:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-publickey.html#cfn-cloudfront-publickey-publickeyconfig
        """
        return pulumi.get(self, "public_key_config")

