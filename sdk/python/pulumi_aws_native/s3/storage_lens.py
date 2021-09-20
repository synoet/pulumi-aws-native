# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['StorageLensArgs', 'StorageLens']

@pulumi.input_type
class StorageLensArgs:
    def __init__(__self__, *,
                 storage_lens_configuration: pulumi.Input['StorageLensStorageLensConfigurationArgs'],
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['StorageLensTagArgs']]]] = None):
        """
        The set of arguments for constructing a StorageLens resource.
        :param pulumi.Input[Sequence[pulumi.Input['StorageLensTagArgs']]] tags: A set of tags (key-value pairs) for this Amazon S3 Storage Lens configuration.
        """
        pulumi.set(__self__, "storage_lens_configuration", storage_lens_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="storageLensConfiguration")
    def storage_lens_configuration(self) -> pulumi.Input['StorageLensStorageLensConfigurationArgs']:
        return pulumi.get(self, "storage_lens_configuration")

    @storage_lens_configuration.setter
    def storage_lens_configuration(self, value: pulumi.Input['StorageLensStorageLensConfigurationArgs']):
        pulumi.set(self, "storage_lens_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StorageLensTagArgs']]]]:
        """
        A set of tags (key-value pairs) for this Amazon S3 Storage Lens configuration.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StorageLensTagArgs']]]]):
        pulumi.set(self, "tags", value)


class StorageLens(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 storage_lens_configuration: Optional[pulumi.Input[pulumi.InputType['StorageLensStorageLensConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StorageLensTagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::S3::StorageLens resource is an Amazon S3 resource type that you can use to create Storage Lens configurations.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StorageLensTagArgs']]]] tags: A set of tags (key-value pairs) for this Amazon S3 Storage Lens configuration.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StorageLensArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::S3::StorageLens resource is an Amazon S3 resource type that you can use to create Storage Lens configurations.

        :param str resource_name: The name of the resource.
        :param StorageLensArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StorageLensArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 storage_lens_configuration: Optional[pulumi.Input[pulumi.InputType['StorageLensStorageLensConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StorageLensTagArgs']]]]] = None,
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
            __props__ = StorageLensArgs.__new__(StorageLensArgs)

            if storage_lens_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'storage_lens_configuration'")
            __props__.__dict__["storage_lens_configuration"] = storage_lens_configuration
            __props__.__dict__["tags"] = tags
        super(StorageLens, __self__).__init__(
            'aws-native:s3:StorageLens',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StorageLens':
        """
        Get an existing StorageLens resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StorageLensArgs.__new__(StorageLensArgs)

        __props__.__dict__["storage_lens_configuration"] = None
        __props__.__dict__["tags"] = None
        return StorageLens(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="storageLensConfiguration")
    def storage_lens_configuration(self) -> pulumi.Output['outputs.StorageLensStorageLensConfiguration']:
        return pulumi.get(self, "storage_lens_configuration")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.StorageLensTag']]]:
        """
        A set of tags (key-value pairs) for this Amazon S3 Storage Lens configuration.
        """
        return pulumi.get(self, "tags")

