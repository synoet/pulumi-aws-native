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

__all__ = ['ProvisioningTemplateArgs', 'ProvisioningTemplate']

@pulumi.input_type
class ProvisioningTemplateArgs:
    def __init__(__self__, *,
                 provisioning_role_arn: pulumi.Input[str],
                 template_body: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 pre_provisioning_hook: Optional[pulumi.Input['ProvisioningTemplateProvisioningHookArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 template_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ProvisioningTemplate resource.
        :param pulumi.Input[str] provisioning_role_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-provisioningrolearn
        :param pulumi.Input[str] template_body: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatebody
        :param pulumi.Input[str] description: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-description
        :param pulumi.Input[bool] enabled: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-enabled
        :param pulumi.Input['ProvisioningTemplateProvisioningHookArgs'] pre_provisioning_hook: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-preprovisioninghook
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-tags
        :param pulumi.Input[str] template_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatename
        """
        pulumi.set(__self__, "provisioning_role_arn", provisioning_role_arn)
        pulumi.set(__self__, "template_body", template_body)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if pre_provisioning_hook is not None:
            pulumi.set(__self__, "pre_provisioning_hook", pre_provisioning_hook)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if template_name is not None:
            pulumi.set(__self__, "template_name", template_name)

    @property
    @pulumi.getter(name="provisioningRoleArn")
    def provisioning_role_arn(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-provisioningrolearn
        """
        return pulumi.get(self, "provisioning_role_arn")

    @provisioning_role_arn.setter
    def provisioning_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "provisioning_role_arn", value)

    @property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatebody
        """
        return pulumi.get(self, "template_body")

    @template_body.setter
    def template_body(self, value: pulumi.Input[str]):
        pulumi.set(self, "template_body", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-enabled
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="preProvisioningHook")
    def pre_provisioning_hook(self) -> Optional[pulumi.Input['ProvisioningTemplateProvisioningHookArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-preprovisioninghook
        """
        return pulumi.get(self, "pre_provisioning_hook")

    @pre_provisioning_hook.setter
    def pre_provisioning_hook(self, value: Optional[pulumi.Input['ProvisioningTemplateProvisioningHookArgs']]):
        pulumi.set(self, "pre_provisioning_hook", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatename
        """
        return pulumi.get(self, "template_name")

    @template_name.setter
    def template_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_name", value)


class ProvisioningTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 pre_provisioning_hook: Optional[pulumi.Input[pulumi.InputType['ProvisioningTemplateProvisioningHookArgs']]] = None,
                 provisioning_role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 template_body: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-description
        :param pulumi.Input[bool] enabled: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-enabled
        :param pulumi.Input[pulumi.InputType['ProvisioningTemplateProvisioningHookArgs']] pre_provisioning_hook: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-preprovisioninghook
        :param pulumi.Input[str] provisioning_role_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-provisioningrolearn
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-tags
        :param pulumi.Input[str] template_body: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatebody
        :param pulumi.Input[str] template_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatename
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProvisioningTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html

        :param str resource_name: The name of the resource.
        :param ProvisioningTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProvisioningTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 pre_provisioning_hook: Optional[pulumi.Input[pulumi.InputType['ProvisioningTemplateProvisioningHookArgs']]] = None,
                 provisioning_role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 template_body: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ProvisioningTemplateArgs.__new__(ProvisioningTemplateArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["pre_provisioning_hook"] = pre_provisioning_hook
            if provisioning_role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'provisioning_role_arn'")
            __props__.__dict__["provisioning_role_arn"] = provisioning_role_arn
            __props__.__dict__["tags"] = tags
            if template_body is None and not opts.urn:
                raise TypeError("Missing required property 'template_body'")
            __props__.__dict__["template_body"] = template_body
            __props__.__dict__["template_name"] = template_name
            __props__.__dict__["template_arn"] = None
        super(ProvisioningTemplate, __self__).__init__(
            'aws-native:iot:ProvisioningTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ProvisioningTemplate':
        """
        Get an existing ProvisioningTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProvisioningTemplateArgs.__new__(ProvisioningTemplateArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["pre_provisioning_hook"] = None
        __props__.__dict__["provisioning_role_arn"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["template_arn"] = None
        __props__.__dict__["template_body"] = None
        __props__.__dict__["template_name"] = None
        return ProvisioningTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-enabled
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="preProvisioningHook")
    def pre_provisioning_hook(self) -> pulumi.Output[Optional['outputs.ProvisioningTemplateProvisioningHook']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-preprovisioninghook
        """
        return pulumi.get(self, "pre_provisioning_hook")

    @property
    @pulumi.getter(name="provisioningRoleArn")
    def provisioning_role_arn(self) -> pulumi.Output[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-provisioningrolearn
        """
        return pulumi.get(self, "provisioning_role_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateArn")
    def template_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "template_arn")

    @property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> pulumi.Output[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatebody
        """
        return pulumi.get(self, "template_body")

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatename
        """
        return pulumi.get(self, "template_name")

