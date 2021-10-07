# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['SegmentArgs', 'Segment']

@pulumi.input_type
class SegmentArgs:
    def __init__(__self__, *,
                 application_id: pulumi.Input[str],
                 name: pulumi.Input[str],
                 dimensions: Optional[pulumi.Input['SegmentDimensionsArgs']] = None,
                 segment_groups: Optional[pulumi.Input['SegmentGroupsArgs']] = None,
                 tags: Optional[Any] = None):
        """
        The set of arguments for constructing a Segment resource.
        """
        pulumi.set(__self__, "application_id", application_id)
        pulumi.set(__self__, "name", name)
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if segment_groups is not None:
            pulumi.set(__self__, "segment_groups", segment_groups)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input['SegmentDimensionsArgs']]:
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input['SegmentDimensionsArgs']]):
        pulumi.set(self, "dimensions", value)

    @property
    @pulumi.getter(name="segmentGroups")
    def segment_groups(self) -> Optional[pulumi.Input['SegmentGroupsArgs']]:
        return pulumi.get(self, "segment_groups")

    @segment_groups.setter
    def segment_groups(self, value: Optional[pulumi.Input['SegmentGroupsArgs']]):
        pulumi.set(self, "segment_groups", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)


warnings.warn("""Segment is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Segment(pulumi.CustomResource):
    warnings.warn("""Segment is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 dimensions: Optional[pulumi.Input[pulumi.InputType['SegmentDimensionsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 segment_groups: Optional[pulumi.Input[pulumi.InputType['SegmentGroupsArgs']]] = None,
                 tags: Optional[Any] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Pinpoint::Segment

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SegmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Pinpoint::Segment

        :param str resource_name: The name of the resource.
        :param SegmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SegmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 dimensions: Optional[pulumi.Input[pulumi.InputType['SegmentDimensionsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 segment_groups: Optional[pulumi.Input[pulumi.InputType['SegmentGroupsArgs']]] = None,
                 tags: Optional[Any] = None,
                 __props__=None):
        pulumi.log.warn("""Segment is deprecated: Segment is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SegmentArgs.__new__(SegmentArgs)

            if application_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_id'")
            __props__.__dict__["application_id"] = application_id
            __props__.__dict__["dimensions"] = dimensions
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["segment_groups"] = segment_groups
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["segment_id"] = None
        super(Segment, __self__).__init__(
            'aws-native:pinpoint:Segment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Segment':
        """
        Get an existing Segment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SegmentArgs.__new__(SegmentArgs)

        __props__.__dict__["application_id"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["dimensions"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["segment_groups"] = None
        __props__.__dict__["segment_id"] = None
        __props__.__dict__["tags"] = None
        return Segment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def dimensions(self) -> pulumi.Output[Optional['outputs.SegmentDimensions']]:
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="segmentGroups")
    def segment_groups(self) -> pulumi.Output[Optional['outputs.SegmentGroups']]:
        return pulumi.get(self, "segment_groups")

    @property
    @pulumi.getter(name="segmentId")
    def segment_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "segment_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "tags")

