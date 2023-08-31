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

__all__ = ['RegexPatternSetArgs', 'RegexPatternSet']

@pulumi.input_type
class RegexPatternSetArgs:
    def __init__(__self__, *,
                 regular_expression_list: pulumi.Input[Sequence[pulumi.Input[str]]],
                 scope: pulumi.Input['RegexPatternSetScope'],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['RegexPatternSetTagArgs']]]] = None):
        """
        The set of arguments for constructing a RegexPatternSet resource.
        :param pulumi.Input['RegexPatternSetScope'] scope: Use CLOUDFRONT for CloudFront RegexPatternSet, use REGIONAL for Application Load Balancer and API Gateway.
        :param pulumi.Input[str] description: Description of the entity.
        :param pulumi.Input[str] name: Name of the RegexPatternSet.
        """
        pulumi.set(__self__, "regular_expression_list", regular_expression_list)
        pulumi.set(__self__, "scope", scope)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="regularExpressionList")
    def regular_expression_list(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "regular_expression_list")

    @regular_expression_list.setter
    def regular_expression_list(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "regular_expression_list", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input['RegexPatternSetScope']:
        """
        Use CLOUDFRONT for CloudFront RegexPatternSet, use REGIONAL for Application Load Balancer and API Gateway.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input['RegexPatternSetScope']):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the entity.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the RegexPatternSet.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RegexPatternSetTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RegexPatternSetTagArgs']]]]):
        pulumi.set(self, "tags", value)


class RegexPatternSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regular_expression_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 scope: Optional[pulumi.Input['RegexPatternSetScope']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegexPatternSetTagArgs']]]]] = None,
                 __props__=None):
        """
        Contains a list of Regular expressions based on the provided inputs. RegexPatternSet can be used with other WAF entities with RegexPatternSetReferenceStatement to perform other actions .

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the entity.
        :param pulumi.Input[str] name: Name of the RegexPatternSet.
        :param pulumi.Input['RegexPatternSetScope'] scope: Use CLOUDFRONT for CloudFront RegexPatternSet, use REGIONAL for Application Load Balancer and API Gateway.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RegexPatternSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Contains a list of Regular expressions based on the provided inputs. RegexPatternSet can be used with other WAF entities with RegexPatternSetReferenceStatement to perform other actions .

        :param str resource_name: The name of the resource.
        :param RegexPatternSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegexPatternSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regular_expression_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 scope: Optional[pulumi.Input['RegexPatternSetScope']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegexPatternSetTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RegexPatternSetArgs.__new__(RegexPatternSetArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if regular_expression_list is None and not opts.urn:
                raise TypeError("Missing required property 'regular_expression_list'")
            __props__.__dict__["regular_expression_list"] = regular_expression_list
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name", "scope"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(RegexPatternSet, __self__).__init__(
            'aws-native:wafv2:RegexPatternSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RegexPatternSet':
        """
        Get an existing RegexPatternSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RegexPatternSetArgs.__new__(RegexPatternSetArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["regular_expression_list"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["tags"] = None
        return RegexPatternSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the WAF entity.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the entity.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the RegexPatternSet.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="regularExpressionList")
    def regular_expression_list(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "regular_expression_list")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output['RegexPatternSetScope']:
        """
        Use CLOUDFRONT for CloudFront RegexPatternSet, use REGIONAL for Application Load Balancer and API Gateway.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.RegexPatternSetTag']]]:
        return pulumi.get(self, "tags")

