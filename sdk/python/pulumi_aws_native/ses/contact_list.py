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

__all__ = ['ContactListArgs', 'ContactList']

@pulumi.input_type
class ContactListArgs:
    def __init__(__self__, *,
                 contact_list_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 topics: Optional[pulumi.Input[Sequence[pulumi.Input['ContactListTopicArgs']]]] = None):
        """
        The set of arguments for constructing a ContactList resource.
        :param pulumi.Input[str] contact_list_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-contactlistname
        :param pulumi.Input[str] description: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-description
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-tags
        :param pulumi.Input[Sequence[pulumi.Input['ContactListTopicArgs']]] topics: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-topics
        """
        if contact_list_name is not None:
            pulumi.set(__self__, "contact_list_name", contact_list_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if topics is not None:
            pulumi.set(__self__, "topics", topics)

    @property
    @pulumi.getter(name="contactListName")
    def contact_list_name(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-contactlistname
        """
        return pulumi.get(self, "contact_list_name")

    @contact_list_name.setter
    def contact_list_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "contact_list_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def topics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ContactListTopicArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-topics
        """
        return pulumi.get(self, "topics")

    @topics.setter
    def topics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ContactListTopicArgs']]]]):
        pulumi.set(self, "topics", value)


class ContactList(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_list_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 topics: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContactListTopicArgs']]]]] = None,
                 __props__=None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] contact_list_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-contactlistname
        :param pulumi.Input[str] description: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-description
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-tags
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContactListTopicArgs']]]] topics: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-topics
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ContactListArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html

        :param str resource_name: The name of the resource.
        :param ContactListArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContactListArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_list_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 topics: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContactListTopicArgs']]]]] = None,
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
            __props__ = ContactListArgs.__new__(ContactListArgs)

            __props__.__dict__["contact_list_name"] = contact_list_name
            __props__.__dict__["description"] = description
            __props__.__dict__["tags"] = tags
            __props__.__dict__["topics"] = topics
        super(ContactList, __self__).__init__(
            'aws-native:ses:ContactList',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ContactList':
        """
        Get an existing ContactList resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ContactListArgs.__new__(ContactListArgs)

        __props__.__dict__["contact_list_name"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["topics"] = None
        return ContactList(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contactListName")
    def contact_list_name(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-contactlistname
        """
        return pulumi.get(self, "contact_list_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def topics(self) -> pulumi.Output[Optional[Sequence['outputs.ContactListTopic']]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-topics
        """
        return pulumi.get(self, "topics")

