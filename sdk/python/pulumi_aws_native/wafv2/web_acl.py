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

__all__ = ['WebACLArgs', 'WebACL']

@pulumi.input_type
class WebACLArgs:
    def __init__(__self__, *,
                 default_action: pulumi.Input['WebACLDefaultActionArgs'],
                 scope: pulumi.Input['WebACLScope'],
                 visibility_config: pulumi.Input['WebACLVisibilityConfigArgs'],
                 custom_response_bodies: Optional[pulumi.Input['WebACLCustomResponseBodiesArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['WebACLRuleArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['WebACLTagArgs']]]] = None):
        """
        The set of arguments for constructing a WebACL resource.
        :param pulumi.Input[Sequence[pulumi.Input['WebACLRuleArgs']]] rules: Collection of Rules.
        """
        pulumi.set(__self__, "default_action", default_action)
        pulumi.set(__self__, "scope", scope)
        pulumi.set(__self__, "visibility_config", visibility_config)
        if custom_response_bodies is not None:
            pulumi.set(__self__, "custom_response_bodies", custom_response_bodies)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Input['WebACLDefaultActionArgs']:
        return pulumi.get(self, "default_action")

    @default_action.setter
    def default_action(self, value: pulumi.Input['WebACLDefaultActionArgs']):
        pulumi.set(self, "default_action", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input['WebACLScope']:
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input['WebACLScope']):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="visibilityConfig")
    def visibility_config(self) -> pulumi.Input['WebACLVisibilityConfigArgs']:
        return pulumi.get(self, "visibility_config")

    @visibility_config.setter
    def visibility_config(self, value: pulumi.Input['WebACLVisibilityConfigArgs']):
        pulumi.set(self, "visibility_config", value)

    @property
    @pulumi.getter(name="customResponseBodies")
    def custom_response_bodies(self) -> Optional[pulumi.Input['WebACLCustomResponseBodiesArgs']]:
        return pulumi.get(self, "custom_response_bodies")

    @custom_response_bodies.setter
    def custom_response_bodies(self, value: Optional[pulumi.Input['WebACLCustomResponseBodiesArgs']]):
        pulumi.set(self, "custom_response_bodies", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WebACLRuleArgs']]]]:
        """
        Collection of Rules.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WebACLRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WebACLTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WebACLTagArgs']]]]):
        pulumi.set(self, "tags", value)


class WebACL(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_response_bodies: Optional[pulumi.Input[pulumi.InputType['WebACLCustomResponseBodiesArgs']]] = None,
                 default_action: Optional[pulumi.Input[pulumi.InputType['WebACLDefaultActionArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WebACLRuleArgs']]]]] = None,
                 scope: Optional[pulumi.Input['WebACLScope']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WebACLTagArgs']]]]] = None,
                 visibility_config: Optional[pulumi.Input[pulumi.InputType['WebACLVisibilityConfigArgs']]] = None,
                 __props__=None):
        """
        Contains the Rules that identify the requests that you want to allow, block, or count. In a WebACL, you also specify a default action (ALLOW or BLOCK), and the action for each Rule that you add to a WebACL, for example, block requests from specified IP addresses or block requests from specified referrers. You also associate the WebACL with a CloudFront distribution to identify the requests that you want AWS WAF to filter. If you add more than one Rule to a WebACL, a request needs to match only one of the specifications to be allowed, blocked, or counted.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WebACLRuleArgs']]]] rules: Collection of Rules.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebACLArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Contains the Rules that identify the requests that you want to allow, block, or count. In a WebACL, you also specify a default action (ALLOW or BLOCK), and the action for each Rule that you add to a WebACL, for example, block requests from specified IP addresses or block requests from specified referrers. You also associate the WebACL with a CloudFront distribution to identify the requests that you want AWS WAF to filter. If you add more than one Rule to a WebACL, a request needs to match only one of the specifications to be allowed, blocked, or counted.

        :param str resource_name: The name of the resource.
        :param WebACLArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebACLArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_response_bodies: Optional[pulumi.Input[pulumi.InputType['WebACLCustomResponseBodiesArgs']]] = None,
                 default_action: Optional[pulumi.Input[pulumi.InputType['WebACLDefaultActionArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WebACLRuleArgs']]]]] = None,
                 scope: Optional[pulumi.Input['WebACLScope']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WebACLTagArgs']]]]] = None,
                 visibility_config: Optional[pulumi.Input[pulumi.InputType['WebACLVisibilityConfigArgs']]] = None,
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
            __props__ = WebACLArgs.__new__(WebACLArgs)

            __props__.__dict__["custom_response_bodies"] = custom_response_bodies
            if default_action is None and not opts.urn:
                raise TypeError("Missing required property 'default_action'")
            __props__.__dict__["default_action"] = default_action
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["rules"] = rules
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["tags"] = tags
            if visibility_config is None and not opts.urn:
                raise TypeError("Missing required property 'visibility_config'")
            __props__.__dict__["visibility_config"] = visibility_config
            __props__.__dict__["arn"] = None
            __props__.__dict__["capacity"] = None
            __props__.__dict__["label_namespace"] = None
        super(WebACL, __self__).__init__(
            'aws-native:wafv2:WebACL',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WebACL':
        """
        Get an existing WebACL resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebACLArgs.__new__(WebACLArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["capacity"] = None
        __props__.__dict__["custom_response_bodies"] = None
        __props__.__dict__["default_action"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["label_namespace"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["rules"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["visibility_config"] = None
        return WebACL(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def capacity(self) -> pulumi.Output[int]:
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter(name="customResponseBodies")
    def custom_response_bodies(self) -> pulumi.Output[Optional['outputs.WebACLCustomResponseBodies']]:
        return pulumi.get(self, "custom_response_bodies")

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Output['outputs.WebACLDefaultAction']:
        return pulumi.get(self, "default_action")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="labelNamespace")
    def label_namespace(self) -> pulumi.Output[str]:
        return pulumi.get(self, "label_namespace")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence['outputs.WebACLRule']]]:
        """
        Collection of Rules.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output['WebACLScope']:
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.WebACLTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="visibilityConfig")
    def visibility_config(self) -> pulumi.Output['outputs.WebACLVisibilityConfig']:
        return pulumi.get(self, "visibility_config")

