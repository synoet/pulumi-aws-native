# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['StackSetConstraintArgs', 'StackSetConstraint']

@pulumi.input_type
class StackSetConstraintArgs:
    def __init__(__self__, *,
                 account_list: pulumi.Input[Sequence[pulumi.Input[str]]],
                 admin_role: pulumi.Input[str],
                 description: pulumi.Input[str],
                 execution_role: pulumi.Input[str],
                 portfolio_id: pulumi.Input[str],
                 product_id: pulumi.Input[str],
                 region_list: pulumi.Input[Sequence[pulumi.Input[str]]],
                 stack_instance_control: pulumi.Input[str],
                 accept_language: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StackSetConstraint resource.
        """
        pulumi.set(__self__, "account_list", account_list)
        pulumi.set(__self__, "admin_role", admin_role)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "execution_role", execution_role)
        pulumi.set(__self__, "portfolio_id", portfolio_id)
        pulumi.set(__self__, "product_id", product_id)
        pulumi.set(__self__, "region_list", region_list)
        pulumi.set(__self__, "stack_instance_control", stack_instance_control)
        if accept_language is not None:
            pulumi.set(__self__, "accept_language", accept_language)

    @property
    @pulumi.getter(name="accountList")
    def account_list(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "account_list")

    @account_list.setter
    def account_list(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "account_list", value)

    @property
    @pulumi.getter(name="adminRole")
    def admin_role(self) -> pulumi.Input[str]:
        return pulumi.get(self, "admin_role")

    @admin_role.setter
    def admin_role(self, value: pulumi.Input[str]):
        pulumi.set(self, "admin_role", value)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> pulumi.Input[str]:
        return pulumi.get(self, "execution_role")

    @execution_role.setter
    def execution_role(self, value: pulumi.Input[str]):
        pulumi.set(self, "execution_role", value)

    @property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "portfolio_id")

    @portfolio_id.setter
    def portfolio_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "portfolio_id", value)

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "product_id")

    @product_id.setter
    def product_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "product_id", value)

    @property
    @pulumi.getter(name="regionList")
    def region_list(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "region_list")

    @region_list.setter
    def region_list(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "region_list", value)

    @property
    @pulumi.getter(name="stackInstanceControl")
    def stack_instance_control(self) -> pulumi.Input[str]:
        return pulumi.get(self, "stack_instance_control")

    @stack_instance_control.setter
    def stack_instance_control(self, value: pulumi.Input[str]):
        pulumi.set(self, "stack_instance_control", value)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "accept_language")

    @accept_language.setter
    def accept_language(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accept_language", value)


warnings.warn("""StackSetConstraint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class StackSetConstraint(pulumi.CustomResource):
    warnings.warn("""StackSetConstraint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accept_language: Optional[pulumi.Input[str]] = None,
                 account_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 admin_role: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 execution_role: Optional[pulumi.Input[str]] = None,
                 portfolio_id: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 region_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 stack_instance_control: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ServiceCatalog::StackSetConstraint

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StackSetConstraintArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ServiceCatalog::StackSetConstraint

        :param str resource_name: The name of the resource.
        :param StackSetConstraintArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StackSetConstraintArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accept_language: Optional[pulumi.Input[str]] = None,
                 account_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 admin_role: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 execution_role: Optional[pulumi.Input[str]] = None,
                 portfolio_id: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 region_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 stack_instance_control: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""StackSetConstraint is deprecated: StackSetConstraint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StackSetConstraintArgs.__new__(StackSetConstraintArgs)

            __props__.__dict__["accept_language"] = accept_language
            if account_list is None and not opts.urn:
                raise TypeError("Missing required property 'account_list'")
            __props__.__dict__["account_list"] = account_list
            if admin_role is None and not opts.urn:
                raise TypeError("Missing required property 'admin_role'")
            __props__.__dict__["admin_role"] = admin_role
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if execution_role is None and not opts.urn:
                raise TypeError("Missing required property 'execution_role'")
            __props__.__dict__["execution_role"] = execution_role
            if portfolio_id is None and not opts.urn:
                raise TypeError("Missing required property 'portfolio_id'")
            __props__.__dict__["portfolio_id"] = portfolio_id
            if product_id is None and not opts.urn:
                raise TypeError("Missing required property 'product_id'")
            __props__.__dict__["product_id"] = product_id
            if region_list is None and not opts.urn:
                raise TypeError("Missing required property 'region_list'")
            __props__.__dict__["region_list"] = region_list
            if stack_instance_control is None and not opts.urn:
                raise TypeError("Missing required property 'stack_instance_control'")
            __props__.__dict__["stack_instance_control"] = stack_instance_control
        super(StackSetConstraint, __self__).__init__(
            'aws-native:servicecatalog:StackSetConstraint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StackSetConstraint':
        """
        Get an existing StackSetConstraint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StackSetConstraintArgs.__new__(StackSetConstraintArgs)

        __props__.__dict__["accept_language"] = None
        __props__.__dict__["account_list"] = None
        __props__.__dict__["admin_role"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["execution_role"] = None
        __props__.__dict__["portfolio_id"] = None
        __props__.__dict__["product_id"] = None
        __props__.__dict__["region_list"] = None
        __props__.__dict__["stack_instance_control"] = None
        return StackSetConstraint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "accept_language")

    @property
    @pulumi.getter(name="accountList")
    def account_list(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "account_list")

    @property
    @pulumi.getter(name="adminRole")
    def admin_role(self) -> pulumi.Output[str]:
        return pulumi.get(self, "admin_role")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> pulumi.Output[str]:
        return pulumi.get(self, "execution_role")

    @property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "portfolio_id")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter(name="regionList")
    def region_list(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "region_list")

    @property
    @pulumi.getter(name="stackInstanceControl")
    def stack_instance_control(self) -> pulumi.Output[str]:
        return pulumi.get(self, "stack_instance_control")

