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

__all__ = ['IdentityProviderConfigArgs', 'IdentityProviderConfig']

@pulumi.input_type
class IdentityProviderConfigArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 type: pulumi.Input['IdentityProviderConfigType'],
                 identity_provider_config_name: Optional[pulumi.Input[str]] = None,
                 oidc: Optional[pulumi.Input['IdentityProviderConfigOidcIdentityProviderConfigArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['IdentityProviderConfigTagArgs']]]] = None):
        """
        The set of arguments for constructing a IdentityProviderConfig resource.
        :param pulumi.Input[str] cluster_name: The name of the identity provider configuration.
        :param pulumi.Input['IdentityProviderConfigType'] type: The type of the identity provider configuration.
        :param pulumi.Input[str] identity_provider_config_name: The name of the OIDC provider configuration.
        :param pulumi.Input[Sequence[pulumi.Input['IdentityProviderConfigTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "type", type)
        if identity_provider_config_name is not None:
            pulumi.set(__self__, "identity_provider_config_name", identity_provider_config_name)
        if oidc is not None:
            pulumi.set(__self__, "oidc", oidc)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the identity provider configuration.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['IdentityProviderConfigType']:
        """
        The type of the identity provider configuration.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['IdentityProviderConfigType']):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="identityProviderConfigName")
    def identity_provider_config_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the OIDC provider configuration.
        """
        return pulumi.get(self, "identity_provider_config_name")

    @identity_provider_config_name.setter
    def identity_provider_config_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_provider_config_name", value)

    @property
    @pulumi.getter
    def oidc(self) -> Optional[pulumi.Input['IdentityProviderConfigOidcIdentityProviderConfigArgs']]:
        return pulumi.get(self, "oidc")

    @oidc.setter
    def oidc(self, value: Optional[pulumi.Input['IdentityProviderConfigOidcIdentityProviderConfigArgs']]):
        pulumi.set(self, "oidc", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IdentityProviderConfigTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IdentityProviderConfigTagArgs']]]]):
        pulumi.set(self, "tags", value)


class IdentityProviderConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 identity_provider_config_name: Optional[pulumi.Input[str]] = None,
                 oidc: Optional[pulumi.Input[pulumi.InputType['IdentityProviderConfigOidcIdentityProviderConfigArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IdentityProviderConfigTagArgs']]]]] = None,
                 type: Optional[pulumi.Input['IdentityProviderConfigType']] = None,
                 __props__=None):
        """
        An object representing an Amazon EKS IdentityProviderConfig.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The name of the identity provider configuration.
        :param pulumi.Input[str] identity_provider_config_name: The name of the OIDC provider configuration.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IdentityProviderConfigTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input['IdentityProviderConfigType'] type: The type of the identity provider configuration.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IdentityProviderConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An object representing an Amazon EKS IdentityProviderConfig.

        :param str resource_name: The name of the resource.
        :param IdentityProviderConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IdentityProviderConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 identity_provider_config_name: Optional[pulumi.Input[str]] = None,
                 oidc: Optional[pulumi.Input[pulumi.InputType['IdentityProviderConfigOidcIdentityProviderConfigArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IdentityProviderConfigTagArgs']]]]] = None,
                 type: Optional[pulumi.Input['IdentityProviderConfigType']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IdentityProviderConfigArgs.__new__(IdentityProviderConfigArgs)

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["identity_provider_config_name"] = identity_provider_config_name
            __props__.__dict__["oidc"] = oidc
            __props__.__dict__["tags"] = tags
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["identity_provider_config_arn"] = None
        super(IdentityProviderConfig, __self__).__init__(
            'aws-native:eks:IdentityProviderConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IdentityProviderConfig':
        """
        Get an existing IdentityProviderConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IdentityProviderConfigArgs.__new__(IdentityProviderConfigArgs)

        __props__.__dict__["cluster_name"] = None
        __props__.__dict__["identity_provider_config_arn"] = None
        __props__.__dict__["identity_provider_config_name"] = None
        __props__.__dict__["oidc"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return IdentityProviderConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        """
        The name of the identity provider configuration.
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="identityProviderConfigArn")
    def identity_provider_config_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the configuration.
        """
        return pulumi.get(self, "identity_provider_config_arn")

    @property
    @pulumi.getter(name="identityProviderConfigName")
    def identity_provider_config_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the OIDC provider configuration.
        """
        return pulumi.get(self, "identity_provider_config_name")

    @property
    @pulumi.getter
    def oidc(self) -> pulumi.Output[Optional['outputs.IdentityProviderConfigOidcIdentityProviderConfig']]:
        return pulumi.get(self, "oidc")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.IdentityProviderConfigTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output['IdentityProviderConfigType']:
        """
        The type of the identity provider configuration.
        """
        return pulumi.get(self, "type")

