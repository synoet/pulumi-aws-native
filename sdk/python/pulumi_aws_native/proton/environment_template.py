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

__all__ = ['EnvironmentTemplateArgs', 'EnvironmentTemplate']

@pulumi.input_type
class EnvironmentTemplateArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 encryption_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioning: Optional[pulumi.Input['EnvironmentTemplateProvisioning']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentTemplateTagArgs']]]] = None):
        """
        The set of arguments for constructing a EnvironmentTemplate resource.
        :param pulumi.Input[str] description: <p>A description of the environment template.</p>
        :param pulumi.Input[str] display_name: <p>The environment template name as displayed in the developer interface.</p>
        :param pulumi.Input[str] encryption_key: <p>A customer provided encryption key that Proton uses to encrypt data.</p>
        :param pulumi.Input[Sequence[pulumi.Input['EnvironmentTemplateTagArgs']]] tags: <p>An optional list of metadata items that you can associate with the Proton environment template. A tag is a key-value pair.</p>
                        <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the
                       <i>Proton User Guide</i>.</p>
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if encryption_key is not None:
            pulumi.set(__self__, "encryption_key", encryption_key)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if provisioning is not None:
            pulumi.set(__self__, "provisioning", provisioning)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        <p>A description of the environment template.</p>
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        <p>The environment template name as displayed in the developer interface.</p>
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[pulumi.Input[str]]:
        """
        <p>A customer provided encryption key that Proton uses to encrypt data.</p>
        """
        return pulumi.get(self, "encryption_key")

    @encryption_key.setter
    def encryption_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def provisioning(self) -> Optional[pulumi.Input['EnvironmentTemplateProvisioning']]:
        return pulumi.get(self, "provisioning")

    @provisioning.setter
    def provisioning(self, value: Optional[pulumi.Input['EnvironmentTemplateProvisioning']]):
        pulumi.set(self, "provisioning", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentTemplateTagArgs']]]]:
        """
        <p>An optional list of metadata items that you can associate with the Proton environment template. A tag is a key-value pair.</p>
                 <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the
                <i>Proton User Guide</i>.</p>
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentTemplateTagArgs']]]]):
        pulumi.set(self, "tags", value)


class EnvironmentTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 encryption_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioning: Optional[pulumi.Input['EnvironmentTemplateProvisioning']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentTemplateTagArgs']]]]] = None,
                 __props__=None):
        """
        Definition of AWS::Proton::EnvironmentTemplate Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: <p>A description of the environment template.</p>
        :param pulumi.Input[str] display_name: <p>The environment template name as displayed in the developer interface.</p>
        :param pulumi.Input[str] encryption_key: <p>A customer provided encryption key that Proton uses to encrypt data.</p>
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentTemplateTagArgs']]]] tags: <p>An optional list of metadata items that you can associate with the Proton environment template. A tag is a key-value pair.</p>
                        <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the
                       <i>Proton User Guide</i>.</p>
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[EnvironmentTemplateArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::Proton::EnvironmentTemplate Resource Type

        :param str resource_name: The name of the resource.
        :param EnvironmentTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnvironmentTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 encryption_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioning: Optional[pulumi.Input['EnvironmentTemplateProvisioning']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentTemplateTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EnvironmentTemplateArgs.__new__(EnvironmentTemplateArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["encryption_key"] = encryption_key
            __props__.__dict__["name"] = name
            __props__.__dict__["provisioning"] = provisioning
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["encryption_key", "name", "provisioning"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(EnvironmentTemplate, __self__).__init__(
            'aws-native:proton:EnvironmentTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EnvironmentTemplate':
        """
        Get an existing EnvironmentTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EnvironmentTemplateArgs.__new__(EnvironmentTemplateArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["encryption_key"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning"] = None
        __props__.__dict__["tags"] = None
        return EnvironmentTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        <p>The Amazon Resource Name (ARN) of the environment template.</p>
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        <p>A description of the environment template.</p>
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        <p>The environment template name as displayed in the developer interface.</p>
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> pulumi.Output[Optional[str]]:
        """
        <p>A customer provided encryption key that Proton uses to encrypt data.</p>
        """
        return pulumi.get(self, "encryption_key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def provisioning(self) -> pulumi.Output[Optional['EnvironmentTemplateProvisioning']]:
        return pulumi.get(self, "provisioning")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.EnvironmentTemplateTag']]]:
        """
        <p>An optional list of metadata items that you can associate with the Proton environment template. A tag is a key-value pair.</p>
                 <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the
                <i>Proton User Guide</i>.</p>
        """
        return pulumi.get(self, "tags")

