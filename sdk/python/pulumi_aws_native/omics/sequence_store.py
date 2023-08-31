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
from ._enums import *
from ._inputs import *

__all__ = ['SequenceStoreArgs', 'SequenceStore']

@pulumi.input_type
class SequenceStoreArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 fallback_location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sse_config: Optional[pulumi.Input['SequenceStoreSseConfigArgs']] = None,
                 tags: Optional[pulumi.Input['SequenceStoreTagMapArgs']] = None):
        """
        The set of arguments for constructing a SequenceStore resource.
        :param pulumi.Input[str] description: A description for the store.
        :param pulumi.Input[str] fallback_location: An S3 URI representing the bucket and folder to store failed read set uploads.
        :param pulumi.Input[str] name: A name for the store.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if fallback_location is not None:
            pulumi.set(__self__, "fallback_location", fallback_location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sse_config is not None:
            pulumi.set(__self__, "sse_config", sse_config)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the store.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="fallbackLocation")
    def fallback_location(self) -> Optional[pulumi.Input[str]]:
        """
        An S3 URI representing the bucket and folder to store failed read set uploads.
        """
        return pulumi.get(self, "fallback_location")

    @fallback_location.setter
    def fallback_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fallback_location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A name for the store.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sseConfig")
    def sse_config(self) -> Optional[pulumi.Input['SequenceStoreSseConfigArgs']]:
        return pulumi.get(self, "sse_config")

    @sse_config.setter
    def sse_config(self, value: Optional[pulumi.Input['SequenceStoreSseConfigArgs']]):
        pulumi.set(self, "sse_config", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input['SequenceStoreTagMapArgs']]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input['SequenceStoreTagMapArgs']]):
        pulumi.set(self, "tags", value)


class SequenceStore(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fallback_location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sse_config: Optional[pulumi.Input[pulumi.InputType['SequenceStoreSseConfigArgs']]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['SequenceStoreTagMapArgs']]] = None,
                 __props__=None):
        """
        Definition of AWS::Omics::SequenceStore Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description for the store.
        :param pulumi.Input[str] fallback_location: An S3 URI representing the bucket and folder to store failed read set uploads.
        :param pulumi.Input[str] name: A name for the store.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SequenceStoreArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::Omics::SequenceStore Resource Type

        :param str resource_name: The name of the resource.
        :param SequenceStoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SequenceStoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fallback_location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sse_config: Optional[pulumi.Input[pulumi.InputType['SequenceStoreSseConfigArgs']]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['SequenceStoreTagMapArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SequenceStoreArgs.__new__(SequenceStoreArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["fallback_location"] = fallback_location
            __props__.__dict__["name"] = name
            __props__.__dict__["sse_config"] = sse_config
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["sequence_store_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["description", "fallback_location", "name", "sse_config", "tags"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(SequenceStore, __self__).__init__(
            'aws-native:omics:SequenceStore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SequenceStore':
        """
        Get an existing SequenceStore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SequenceStoreArgs.__new__(SequenceStoreArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["fallback_location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["sequence_store_id"] = None
        __props__.__dict__["sse_config"] = None
        __props__.__dict__["tags"] = None
        return SequenceStore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The store's ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        When the store was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the store.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="fallbackLocation")
    def fallback_location(self) -> pulumi.Output[Optional[str]]:
        """
        An S3 URI representing the bucket and folder to store failed read set uploads.
        """
        return pulumi.get(self, "fallback_location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A name for the store.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sequenceStoreId")
    def sequence_store_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "sequence_store_id")

    @property
    @pulumi.getter(name="sseConfig")
    def sse_config(self) -> pulumi.Output[Optional['outputs.SequenceStoreSseConfig']]:
        return pulumi.get(self, "sse_config")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional['outputs.SequenceStoreTagMap']]:
        return pulumi.get(self, "tags")

