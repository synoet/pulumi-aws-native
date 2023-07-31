# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ResolverRuleAssociationArgs', 'ResolverRuleAssociation']

@pulumi.input_type
class ResolverRuleAssociationArgs:
    def __init__(__self__, *,
                 resolver_rule_id: pulumi.Input[str],
                 vpc_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ResolverRuleAssociation resource.
        :param pulumi.Input[str] resolver_rule_id: The ID of the Resolver rule that you associated with the VPC that is specified by VPCId.
        :param pulumi.Input[str] vpc_id: The ID of the VPC that you associated the Resolver rule with.
        :param pulumi.Input[str] name: The name of an association between a Resolver rule and a VPC.
        """
        pulumi.set(__self__, "resolver_rule_id", resolver_rule_id)
        pulumi.set(__self__, "vpc_id", vpc_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="resolverRuleId")
    def resolver_rule_id(self) -> pulumi.Input[str]:
        """
        The ID of the Resolver rule that you associated with the VPC that is specified by VPCId.
        """
        return pulumi.get(self, "resolver_rule_id")

    @resolver_rule_id.setter
    def resolver_rule_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resolver_rule_id", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        """
        The ID of the VPC that you associated the Resolver rule with.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of an association between a Resolver rule and a VPC.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class ResolverRuleAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resolver_rule_id: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Route53Resolver::ResolverRuleAssociation

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of an association between a Resolver rule and a VPC.
        :param pulumi.Input[str] resolver_rule_id: The ID of the Resolver rule that you associated with the VPC that is specified by VPCId.
        :param pulumi.Input[str] vpc_id: The ID of the VPC that you associated the Resolver rule with.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResolverRuleAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Route53Resolver::ResolverRuleAssociation

        :param str resource_name: The name of the resource.
        :param ResolverRuleAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResolverRuleAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resolver_rule_id: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResolverRuleAssociationArgs.__new__(ResolverRuleAssociationArgs)

            __props__.__dict__["name"] = name
            if resolver_rule_id is None and not opts.urn:
                raise TypeError("Missing required property 'resolver_rule_id'")
            __props__.__dict__["resolver_rule_id"] = resolver_rule_id
            if vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_id'")
            __props__.__dict__["vpc_id"] = vpc_id
            __props__.__dict__["resolver_rule_association_id"] = None
        super(ResolverRuleAssociation, __self__).__init__(
            'aws-native:route53resolver:ResolverRuleAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ResolverRuleAssociation':
        """
        Get an existing ResolverRuleAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ResolverRuleAssociationArgs.__new__(ResolverRuleAssociationArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["resolver_rule_association_id"] = None
        __props__.__dict__["resolver_rule_id"] = None
        __props__.__dict__["vpc_id"] = None
        return ResolverRuleAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of an association between a Resolver rule and a VPC.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resolverRuleAssociationId")
    def resolver_rule_association_id(self) -> pulumi.Output[str]:
        """
        Primary Identifier for Resolver Rule Association
        """
        return pulumi.get(self, "resolver_rule_association_id")

    @property
    @pulumi.getter(name="resolverRuleId")
    def resolver_rule_id(self) -> pulumi.Output[str]:
        """
        The ID of the Resolver rule that you associated with the VPC that is specified by VPCId.
        """
        return pulumi.get(self, "resolver_rule_id")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        The ID of the VPC that you associated the Resolver rule with.
        """
        return pulumi.get(self, "vpc_id")

