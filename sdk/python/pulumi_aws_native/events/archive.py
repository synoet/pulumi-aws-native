# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ArchiveArgs', 'Archive']

@pulumi.input_type
class ArchiveArgs:
    def __init__(__self__, *,
                 source_arn: pulumi.Input[str],
                 archive_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 event_pattern: Optional[Any] = None,
                 retention_days: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Archive resource.
        """
        pulumi.set(__self__, "source_arn", source_arn)
        if archive_name is not None:
            pulumi.set(__self__, "archive_name", archive_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if event_pattern is not None:
            pulumi.set(__self__, "event_pattern", event_pattern)
        if retention_days is not None:
            pulumi.set(__self__, "retention_days", retention_days)

    @property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source_arn")

    @source_arn.setter
    def source_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_arn", value)

    @property
    @pulumi.getter(name="archiveName")
    def archive_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "archive_name")

    @archive_name.setter
    def archive_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "archive_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="eventPattern")
    def event_pattern(self) -> Optional[Any]:
        return pulumi.get(self, "event_pattern")

    @event_pattern.setter
    def event_pattern(self, value: Optional[Any]):
        pulumi.set(self, "event_pattern", value)

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "retention_days")

    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_days", value)


class Archive(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 archive_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 event_pattern: Optional[Any] = None,
                 retention_days: Optional[pulumi.Input[int]] = None,
                 source_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Events::Archive

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ArchiveArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Events::Archive

        :param str resource_name: The name of the resource.
        :param ArchiveArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ArchiveArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 archive_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 event_pattern: Optional[Any] = None,
                 retention_days: Optional[pulumi.Input[int]] = None,
                 source_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ArchiveArgs.__new__(ArchiveArgs)

            __props__.__dict__["archive_name"] = archive_name
            __props__.__dict__["description"] = description
            __props__.__dict__["event_pattern"] = event_pattern
            __props__.__dict__["retention_days"] = retention_days
            if source_arn is None and not opts.urn:
                raise TypeError("Missing required property 'source_arn'")
            __props__.__dict__["source_arn"] = source_arn
            __props__.__dict__["arn"] = None
        super(Archive, __self__).__init__(
            'aws-native:events:Archive',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Archive':
        """
        Get an existing Archive resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ArchiveArgs.__new__(ArchiveArgs)

        __props__.__dict__["archive_name"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["event_pattern"] = None
        __props__.__dict__["retention_days"] = None
        __props__.__dict__["source_arn"] = None
        return Archive(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="archiveName")
    def archive_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "archive_name")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="eventPattern")
    def event_pattern(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "event_pattern")

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "retention_days")

    @property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "source_arn")

