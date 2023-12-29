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

__all__ = ['DomainNameArgs', 'DomainName']

@pulumi.input_type
class DomainNameArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 domain_name_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['DomainNameConfigurationArgs']]]] = None,
                 mutual_tls_authentication: Optional[pulumi.Input['DomainNameMutualTlsAuthenticationArgs']] = None,
                 tags: Optional[Any] = None):
        """
        The set of arguments for constructing a DomainName resource.
        :param pulumi.Input[str] domain_name: The custom domain name for your API in Amazon API Gateway. Uppercase letters are not supported.
        :param pulumi.Input[Sequence[pulumi.Input['DomainNameConfigurationArgs']]] domain_name_configurations: The domain name configurations.
        :param pulumi.Input['DomainNameMutualTlsAuthenticationArgs'] mutual_tls_authentication: The mutual TLS authentication configuration for a custom domain name.
        :param Any tags: The collection of tags associated with a domain name.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        if domain_name_configurations is not None:
            pulumi.set(__self__, "domain_name_configurations", domain_name_configurations)
        if mutual_tls_authentication is not None:
            pulumi.set(__self__, "mutual_tls_authentication", mutual_tls_authentication)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The custom domain name for your API in Amazon API Gateway. Uppercase letters are not supported.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="domainNameConfigurations")
    def domain_name_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainNameConfigurationArgs']]]]:
        """
        The domain name configurations.
        """
        return pulumi.get(self, "domain_name_configurations")

    @domain_name_configurations.setter
    def domain_name_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainNameConfigurationArgs']]]]):
        pulumi.set(self, "domain_name_configurations", value)

    @property
    @pulumi.getter(name="mutualTlsAuthentication")
    def mutual_tls_authentication(self) -> Optional[pulumi.Input['DomainNameMutualTlsAuthenticationArgs']]:
        """
        The mutual TLS authentication configuration for a custom domain name.
        """
        return pulumi.get(self, "mutual_tls_authentication")

    @mutual_tls_authentication.setter
    def mutual_tls_authentication(self, value: Optional[pulumi.Input['DomainNameMutualTlsAuthenticationArgs']]):
        pulumi.set(self, "mutual_tls_authentication", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        The collection of tags associated with a domain name.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)


class DomainName(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_name_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainNameConfigurationArgs']]]]] = None,
                 mutual_tls_authentication: Optional[pulumi.Input[pulumi.InputType['DomainNameMutualTlsAuthenticationArgs']]] = None,
                 tags: Optional[Any] = None,
                 __props__=None):
        """
        The ``AWS::ApiGatewayV2::DomainName`` resource specifies a custom domain name for your API in Amazon API Gateway (API Gateway).
         You can use a custom domain name to provide a URL that's more intuitive and easier to recall. For more information about using custom domain names, see [Set up Custom Domain Name for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html) in the *API Gateway Developer Guide*.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: The custom domain name for your API in Amazon API Gateway. Uppercase letters are not supported.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainNameConfigurationArgs']]]] domain_name_configurations: The domain name configurations.
        :param pulumi.Input[pulumi.InputType['DomainNameMutualTlsAuthenticationArgs']] mutual_tls_authentication: The mutual TLS authentication configuration for a custom domain name.
        :param Any tags: The collection of tags associated with a domain name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainNameArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The ``AWS::ApiGatewayV2::DomainName`` resource specifies a custom domain name for your API in Amazon API Gateway (API Gateway).
         You can use a custom domain name to provide a URL that's more intuitive and easier to recall. For more information about using custom domain names, see [Set up Custom Domain Name for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html) in the *API Gateway Developer Guide*.

        :param str resource_name: The name of the resource.
        :param DomainNameArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainNameArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_name_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainNameConfigurationArgs']]]]] = None,
                 mutual_tls_authentication: Optional[pulumi.Input[pulumi.InputType['DomainNameMutualTlsAuthenticationArgs']]] = None,
                 tags: Optional[Any] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainNameArgs.__new__(DomainNameArgs)

            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["domain_name_configurations"] = domain_name_configurations
            __props__.__dict__["mutual_tls_authentication"] = mutual_tls_authentication
            __props__.__dict__["tags"] = tags
            __props__.__dict__["regional_domain_name"] = None
            __props__.__dict__["regional_hosted_zone_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["domain_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DomainName, __self__).__init__(
            'aws-native:apigatewayv2:DomainName',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DomainName':
        """
        Get an existing DomainName resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DomainNameArgs.__new__(DomainNameArgs)

        __props__.__dict__["domain_name"] = None
        __props__.__dict__["domain_name_configurations"] = None
        __props__.__dict__["mutual_tls_authentication"] = None
        __props__.__dict__["regional_domain_name"] = None
        __props__.__dict__["regional_hosted_zone_id"] = None
        __props__.__dict__["tags"] = None
        return DomainName(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The custom domain name for your API in Amazon API Gateway. Uppercase letters are not supported.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="domainNameConfigurations")
    def domain_name_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.DomainNameConfiguration']]]:
        """
        The domain name configurations.
        """
        return pulumi.get(self, "domain_name_configurations")

    @property
    @pulumi.getter(name="mutualTlsAuthentication")
    def mutual_tls_authentication(self) -> pulumi.Output[Optional['outputs.DomainNameMutualTlsAuthentication']]:
        """
        The mutual TLS authentication configuration for a custom domain name.
        """
        return pulumi.get(self, "mutual_tls_authentication")

    @property
    @pulumi.getter(name="regionalDomainName")
    def regional_domain_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "regional_domain_name")

    @property
    @pulumi.getter(name="regionalHostedZoneId")
    def regional_hosted_zone_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "regional_hosted_zone_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        """
        The collection of tags associated with a domain name.
        """
        return pulumi.get(self, "tags")

