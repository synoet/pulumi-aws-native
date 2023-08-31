# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PortfolioShareArgs', 'PortfolioShare']

@pulumi.input_type
class PortfolioShareArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 portfolio_id: pulumi.Input[str],
                 accept_language: Optional[pulumi.Input[str]] = None,
                 share_tag_options: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a PortfolioShare resource.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "portfolio_id", portfolio_id)
        if accept_language is not None:
            pulumi.set(__self__, "accept_language", accept_language)
        if share_tag_options is not None:
            pulumi.set(__self__, "share_tag_options", share_tag_options)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "portfolio_id")

    @portfolio_id.setter
    def portfolio_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "portfolio_id", value)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "accept_language")

    @accept_language.setter
    def accept_language(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accept_language", value)

    @property
    @pulumi.getter(name="shareTagOptions")
    def share_tag_options(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "share_tag_options")

    @share_tag_options.setter
    def share_tag_options(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "share_tag_options", value)


warnings.warn("""PortfolioShare is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class PortfolioShare(pulumi.CustomResource):
    warnings.warn("""PortfolioShare is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accept_language: Optional[pulumi.Input[str]] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 portfolio_id: Optional[pulumi.Input[str]] = None,
                 share_tag_options: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ServiceCatalog::PortfolioShare

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PortfolioShareArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ServiceCatalog::PortfolioShare

        :param str resource_name: The name of the resource.
        :param PortfolioShareArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PortfolioShareArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accept_language: Optional[pulumi.Input[str]] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 portfolio_id: Optional[pulumi.Input[str]] = None,
                 share_tag_options: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        pulumi.log.warn("""PortfolioShare is deprecated: PortfolioShare is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PortfolioShareArgs.__new__(PortfolioShareArgs)

            __props__.__dict__["accept_language"] = accept_language
            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            if portfolio_id is None and not opts.urn:
                raise TypeError("Missing required property 'portfolio_id'")
            __props__.__dict__["portfolio_id"] = portfolio_id
            __props__.__dict__["share_tag_options"] = share_tag_options
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["accept_language", "account_id", "portfolio_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(PortfolioShare, __self__).__init__(
            'aws-native:servicecatalog:PortfolioShare',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PortfolioShare':
        """
        Get an existing PortfolioShare resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PortfolioShareArgs.__new__(PortfolioShareArgs)

        __props__.__dict__["accept_language"] = None
        __props__.__dict__["account_id"] = None
        __props__.__dict__["portfolio_id"] = None
        __props__.__dict__["share_tag_options"] = None
        return PortfolioShare(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "accept_language")

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "portfolio_id")

    @property
    @pulumi.getter(name="shareTagOptions")
    def share_tag_options(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "share_tag_options")

