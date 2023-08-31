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

__all__ = ['ConnectAttachmentArgs', 'ConnectAttachment']

@pulumi.input_type
class ConnectAttachmentArgs:
    def __init__(__self__, *,
                 core_network_id: pulumi.Input[str],
                 edge_location: pulumi.Input[str],
                 options: pulumi.Input['ConnectAttachmentOptionsArgs'],
                 transport_attachment_id: pulumi.Input[str],
                 proposed_segment_change: Optional[pulumi.Input['ConnectAttachmentProposedSegmentChangeArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectAttachmentTagArgs']]]] = None):
        """
        The set of arguments for constructing a ConnectAttachment resource.
        :param pulumi.Input[str] core_network_id: ID of the CoreNetwork that the attachment will be attached to.
        :param pulumi.Input[str] edge_location: Edge location of the attachment.
        :param pulumi.Input['ConnectAttachmentOptionsArgs'] options: Protocol options for connect attachment
        :param pulumi.Input[str] transport_attachment_id: Id of transport attachment
        :param pulumi.Input['ConnectAttachmentProposedSegmentChangeArgs'] proposed_segment_change: The attachment to move from one segment to another.
        :param pulumi.Input[Sequence[pulumi.Input['ConnectAttachmentTagArgs']]] tags: Tags for the attachment.
        """
        pulumi.set(__self__, "core_network_id", core_network_id)
        pulumi.set(__self__, "edge_location", edge_location)
        pulumi.set(__self__, "options", options)
        pulumi.set(__self__, "transport_attachment_id", transport_attachment_id)
        if proposed_segment_change is not None:
            pulumi.set(__self__, "proposed_segment_change", proposed_segment_change)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> pulumi.Input[str]:
        """
        ID of the CoreNetwork that the attachment will be attached to.
        """
        return pulumi.get(self, "core_network_id")

    @core_network_id.setter
    def core_network_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "core_network_id", value)

    @property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> pulumi.Input[str]:
        """
        Edge location of the attachment.
        """
        return pulumi.get(self, "edge_location")

    @edge_location.setter
    def edge_location(self, value: pulumi.Input[str]):
        pulumi.set(self, "edge_location", value)

    @property
    @pulumi.getter
    def options(self) -> pulumi.Input['ConnectAttachmentOptionsArgs']:
        """
        Protocol options for connect attachment
        """
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: pulumi.Input['ConnectAttachmentOptionsArgs']):
        pulumi.set(self, "options", value)

    @property
    @pulumi.getter(name="transportAttachmentId")
    def transport_attachment_id(self) -> pulumi.Input[str]:
        """
        Id of transport attachment
        """
        return pulumi.get(self, "transport_attachment_id")

    @transport_attachment_id.setter
    def transport_attachment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "transport_attachment_id", value)

    @property
    @pulumi.getter(name="proposedSegmentChange")
    def proposed_segment_change(self) -> Optional[pulumi.Input['ConnectAttachmentProposedSegmentChangeArgs']]:
        """
        The attachment to move from one segment to another.
        """
        return pulumi.get(self, "proposed_segment_change")

    @proposed_segment_change.setter
    def proposed_segment_change(self, value: Optional[pulumi.Input['ConnectAttachmentProposedSegmentChangeArgs']]):
        pulumi.set(self, "proposed_segment_change", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConnectAttachmentTagArgs']]]]:
        """
        Tags for the attachment.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectAttachmentTagArgs']]]]):
        pulumi.set(self, "tags", value)


class ConnectAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 core_network_id: Optional[pulumi.Input[str]] = None,
                 edge_location: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['ConnectAttachmentOptionsArgs']]] = None,
                 proposed_segment_change: Optional[pulumi.Input[pulumi.InputType['ConnectAttachmentProposedSegmentChangeArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectAttachmentTagArgs']]]]] = None,
                 transport_attachment_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        AWS::NetworkManager::ConnectAttachment Resource Type Definition

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] core_network_id: ID of the CoreNetwork that the attachment will be attached to.
        :param pulumi.Input[str] edge_location: Edge location of the attachment.
        :param pulumi.Input[pulumi.InputType['ConnectAttachmentOptionsArgs']] options: Protocol options for connect attachment
        :param pulumi.Input[pulumi.InputType['ConnectAttachmentProposedSegmentChangeArgs']] proposed_segment_change: The attachment to move from one segment to another.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectAttachmentTagArgs']]]] tags: Tags for the attachment.
        :param pulumi.Input[str] transport_attachment_id: Id of transport attachment
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        AWS::NetworkManager::ConnectAttachment Resource Type Definition

        :param str resource_name: The name of the resource.
        :param ConnectAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 core_network_id: Optional[pulumi.Input[str]] = None,
                 edge_location: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['ConnectAttachmentOptionsArgs']]] = None,
                 proposed_segment_change: Optional[pulumi.Input[pulumi.InputType['ConnectAttachmentProposedSegmentChangeArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectAttachmentTagArgs']]]]] = None,
                 transport_attachment_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectAttachmentArgs.__new__(ConnectAttachmentArgs)

            if core_network_id is None and not opts.urn:
                raise TypeError("Missing required property 'core_network_id'")
            __props__.__dict__["core_network_id"] = core_network_id
            if edge_location is None and not opts.urn:
                raise TypeError("Missing required property 'edge_location'")
            __props__.__dict__["edge_location"] = edge_location
            if options is None and not opts.urn:
                raise TypeError("Missing required property 'options'")
            __props__.__dict__["options"] = options
            __props__.__dict__["proposed_segment_change"] = proposed_segment_change
            __props__.__dict__["tags"] = tags
            if transport_attachment_id is None and not opts.urn:
                raise TypeError("Missing required property 'transport_attachment_id'")
            __props__.__dict__["transport_attachment_id"] = transport_attachment_id
            __props__.__dict__["attachment_id"] = None
            __props__.__dict__["attachment_policy_rule_number"] = None
            __props__.__dict__["attachment_type"] = None
            __props__.__dict__["core_network_arn"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["owner_account_id"] = None
            __props__.__dict__["resource_arn"] = None
            __props__.__dict__["segment_name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["updated_at"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["core_network_id", "edge_location", "options", "transport_attachment_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ConnectAttachment, __self__).__init__(
            'aws-native:networkmanager:ConnectAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConnectAttachment':
        """
        Get an existing ConnectAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectAttachmentArgs.__new__(ConnectAttachmentArgs)

        __props__.__dict__["attachment_id"] = None
        __props__.__dict__["attachment_policy_rule_number"] = None
        __props__.__dict__["attachment_type"] = None
        __props__.__dict__["core_network_arn"] = None
        __props__.__dict__["core_network_id"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["edge_location"] = None
        __props__.__dict__["options"] = None
        __props__.__dict__["owner_account_id"] = None
        __props__.__dict__["proposed_segment_change"] = None
        __props__.__dict__["resource_arn"] = None
        __props__.__dict__["segment_name"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["transport_attachment_id"] = None
        __props__.__dict__["updated_at"] = None
        return ConnectAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> pulumi.Output[str]:
        """
        The ID of the attachment.
        """
        return pulumi.get(self, "attachment_id")

    @property
    @pulumi.getter(name="attachmentPolicyRuleNumber")
    def attachment_policy_rule_number(self) -> pulumi.Output[int]:
        """
        The policy rule number associated with the attachment.
        """
        return pulumi.get(self, "attachment_policy_rule_number")

    @property
    @pulumi.getter(name="attachmentType")
    def attachment_type(self) -> pulumi.Output[str]:
        """
        The type of attachment.
        """
        return pulumi.get(self, "attachment_type")

    @property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> pulumi.Output[str]:
        """
        The ARN of a core network for the VPC attachment.
        """
        return pulumi.get(self, "core_network_arn")

    @property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> pulumi.Output[str]:
        """
        ID of the CoreNetwork that the attachment will be attached to.
        """
        return pulumi.get(self, "core_network_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Creation time of the attachment.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> pulumi.Output[str]:
        """
        Edge location of the attachment.
        """
        return pulumi.get(self, "edge_location")

    @property
    @pulumi.getter
    def options(self) -> pulumi.Output['outputs.ConnectAttachmentOptions']:
        """
        Protocol options for connect attachment
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> pulumi.Output[str]:
        """
        The ID of the attachment account owner.
        """
        return pulumi.get(self, "owner_account_id")

    @property
    @pulumi.getter(name="proposedSegmentChange")
    def proposed_segment_change(self) -> pulumi.Output[Optional['outputs.ConnectAttachmentProposedSegmentChange']]:
        """
        The attachment to move from one segment to another.
        """
        return pulumi.get(self, "proposed_segment_change")

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[str]:
        """
        The attachment resource ARN.
        """
        return pulumi.get(self, "resource_arn")

    @property
    @pulumi.getter(name="segmentName")
    def segment_name(self) -> pulumi.Output[str]:
        """
        The name of the segment attachment.
        """
        return pulumi.get(self, "segment_name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the attachment.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ConnectAttachmentTag']]]:
        """
        Tags for the attachment.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="transportAttachmentId")
    def transport_attachment_id(self) -> pulumi.Output[str]:
        """
        Id of transport attachment
        """
        return pulumi.get(self, "transport_attachment_id")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Last update time of the attachment.
        """
        return pulumi.get(self, "updated_at")

