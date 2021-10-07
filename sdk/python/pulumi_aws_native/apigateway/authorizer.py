# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AuthorizerArgs', 'Authorizer']

@pulumi.input_type
class AuthorizerArgs:
    def __init__(__self__, *,
                 rest_api_id: pulumi.Input[str],
                 type: pulumi.Input[str],
                 auth_type: Optional[pulumi.Input[str]] = None,
                 authorizer_credentials: Optional[pulumi.Input[str]] = None,
                 authorizer_result_ttl_in_seconds: Optional[pulumi.Input[int]] = None,
                 authorizer_uri: Optional[pulumi.Input[str]] = None,
                 identity_source: Optional[pulumi.Input[str]] = None,
                 identity_validation_expression: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provider_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Authorizer resource.
        """
        pulumi.set(__self__, "rest_api_id", rest_api_id)
        pulumi.set(__self__, "type", type)
        if auth_type is not None:
            pulumi.set(__self__, "auth_type", auth_type)
        if authorizer_credentials is not None:
            pulumi.set(__self__, "authorizer_credentials", authorizer_credentials)
        if authorizer_result_ttl_in_seconds is not None:
            pulumi.set(__self__, "authorizer_result_ttl_in_seconds", authorizer_result_ttl_in_seconds)
        if authorizer_uri is not None:
            pulumi.set(__self__, "authorizer_uri", authorizer_uri)
        if identity_source is not None:
            pulumi.set(__self__, "identity_source", identity_source)
        if identity_validation_expression is not None:
            pulumi.set(__self__, "identity_validation_expression", identity_validation_expression)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if provider_arns is not None:
            pulumi.set(__self__, "provider_arns", provider_arns)

    @property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "rest_api_id")

    @rest_api_id.setter
    def rest_api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "rest_api_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "auth_type")

    @auth_type.setter
    def auth_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_type", value)

    @property
    @pulumi.getter(name="authorizerCredentials")
    def authorizer_credentials(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "authorizer_credentials")

    @authorizer_credentials.setter
    def authorizer_credentials(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorizer_credentials", value)

    @property
    @pulumi.getter(name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "authorizer_result_ttl_in_seconds")

    @authorizer_result_ttl_in_seconds.setter
    def authorizer_result_ttl_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "authorizer_result_ttl_in_seconds", value)

    @property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "authorizer_uri")

    @authorizer_uri.setter
    def authorizer_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorizer_uri", value)

    @property
    @pulumi.getter(name="identitySource")
    def identity_source(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "identity_source")

    @identity_source.setter
    def identity_source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_source", value)

    @property
    @pulumi.getter(name="identityValidationExpression")
    def identity_validation_expression(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "identity_validation_expression")

    @identity_validation_expression.setter
    def identity_validation_expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_validation_expression", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="providerARNs")
    def provider_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "provider_arns")

    @provider_arns.setter
    def provider_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "provider_arns", value)


class Authorizer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 authorizer_credentials: Optional[pulumi.Input[str]] = None,
                 authorizer_result_ttl_in_seconds: Optional[pulumi.Input[int]] = None,
                 authorizer_uri: Optional[pulumi.Input[str]] = None,
                 identity_source: Optional[pulumi.Input[str]] = None,
                 identity_validation_expression: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provider_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 rest_api_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ApiGateway::Authorizer

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AuthorizerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ApiGateway::Authorizer

        :param str resource_name: The name of the resource.
        :param AuthorizerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AuthorizerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 authorizer_credentials: Optional[pulumi.Input[str]] = None,
                 authorizer_result_ttl_in_seconds: Optional[pulumi.Input[int]] = None,
                 authorizer_uri: Optional[pulumi.Input[str]] = None,
                 identity_source: Optional[pulumi.Input[str]] = None,
                 identity_validation_expression: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provider_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 rest_api_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
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
            __props__ = AuthorizerArgs.__new__(AuthorizerArgs)

            __props__.__dict__["auth_type"] = auth_type
            __props__.__dict__["authorizer_credentials"] = authorizer_credentials
            __props__.__dict__["authorizer_result_ttl_in_seconds"] = authorizer_result_ttl_in_seconds
            __props__.__dict__["authorizer_uri"] = authorizer_uri
            __props__.__dict__["identity_source"] = identity_source
            __props__.__dict__["identity_validation_expression"] = identity_validation_expression
            __props__.__dict__["name"] = name
            __props__.__dict__["provider_arns"] = provider_arns
            if rest_api_id is None and not opts.urn:
                raise TypeError("Missing required property 'rest_api_id'")
            __props__.__dict__["rest_api_id"] = rest_api_id
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(Authorizer, __self__).__init__(
            'aws-native:apigateway:Authorizer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Authorizer':
        """
        Get an existing Authorizer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AuthorizerArgs.__new__(AuthorizerArgs)

        __props__.__dict__["auth_type"] = None
        __props__.__dict__["authorizer_credentials"] = None
        __props__.__dict__["authorizer_result_ttl_in_seconds"] = None
        __props__.__dict__["authorizer_uri"] = None
        __props__.__dict__["identity_source"] = None
        __props__.__dict__["identity_validation_expression"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provider_arns"] = None
        __props__.__dict__["rest_api_id"] = None
        __props__.__dict__["type"] = None
        return Authorizer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "auth_type")

    @property
    @pulumi.getter(name="authorizerCredentials")
    def authorizer_credentials(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "authorizer_credentials")

    @property
    @pulumi.getter(name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "authorizer_result_ttl_in_seconds")

    @property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "authorizer_uri")

    @property
    @pulumi.getter(name="identitySource")
    def identity_source(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "identity_source")

    @property
    @pulumi.getter(name="identityValidationExpression")
    def identity_validation_expression(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "identity_validation_expression")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="providerARNs")
    def provider_arns(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "provider_arns")

    @property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "rest_api_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "type")

