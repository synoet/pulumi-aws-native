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

__all__ = ['InputSecurityGroupArgs', 'InputSecurityGroup']

@pulumi.input_type
class InputSecurityGroupArgs:
    def __init__(__self__, *,
                 tags: Optional[Any] = None,
                 whitelist_rules: Optional[pulumi.Input[Sequence[pulumi.Input['InputSecurityGroupInputWhitelistRuleCidrArgs']]]] = None):
        """
        The set of arguments for constructing a InputSecurityGroup resource.
        """
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if whitelist_rules is not None:
            pulumi.set(__self__, "whitelist_rules", whitelist_rules)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="whitelistRules")
    def whitelist_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InputSecurityGroupInputWhitelistRuleCidrArgs']]]]:
        return pulumi.get(self, "whitelist_rules")

    @whitelist_rules.setter
    def whitelist_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InputSecurityGroupInputWhitelistRuleCidrArgs']]]]):
        pulumi.set(self, "whitelist_rules", value)


warnings.warn("""InputSecurityGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class InputSecurityGroup(pulumi.CustomResource):
    warnings.warn("""InputSecurityGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 tags: Optional[Any] = None,
                 whitelist_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputSecurityGroupInputWhitelistRuleCidrArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::MediaLive::InputSecurityGroup

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[InputSecurityGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::MediaLive::InputSecurityGroup

        :param str resource_name: The name of the resource.
        :param InputSecurityGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InputSecurityGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 tags: Optional[Any] = None,
                 whitelist_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputSecurityGroupInputWhitelistRuleCidrArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""InputSecurityGroup is deprecated: InputSecurityGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InputSecurityGroupArgs.__new__(InputSecurityGroupArgs)

            __props__.__dict__["tags"] = tags
            __props__.__dict__["whitelist_rules"] = whitelist_rules
            __props__.__dict__["arn"] = None
        super(InputSecurityGroup, __self__).__init__(
            'aws-native:medialive:InputSecurityGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InputSecurityGroup':
        """
        Get an existing InputSecurityGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InputSecurityGroupArgs.__new__(InputSecurityGroupArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["whitelist_rules"] = None
        return InputSecurityGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="whitelistRules")
    def whitelist_rules(self) -> pulumi.Output[Optional[Sequence['outputs.InputSecurityGroupInputWhitelistRuleCidr']]]:
        return pulumi.get(self, "whitelist_rules")

