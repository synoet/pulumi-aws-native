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

__all__ = ['RestApiArgs', 'RestApi']

@pulumi.input_type
class RestApiArgs:
    def __init__(__self__, *,
                 api_key_source_type: Optional[pulumi.Input[str]] = None,
                 binary_media_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 body: Optional[Any] = None,
                 body_s3_location: Optional[pulumi.Input['RestApiS3LocationArgs']] = None,
                 clone_from: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disable_execute_api_endpoint: Optional[pulumi.Input[bool]] = None,
                 endpoint_configuration: Optional[pulumi.Input['RestApiEndpointConfigurationArgs']] = None,
                 fail_on_warnings: Optional[pulumi.Input[bool]] = None,
                 minimum_compression_size: Optional[pulumi.Input[int]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 policy: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['RestApiTagArgs']]]] = None):
        """
        The set of arguments for constructing a RestApi resource.
        """
        if api_key_source_type is not None:
            pulumi.set(__self__, "api_key_source_type", api_key_source_type)
        if binary_media_types is not None:
            pulumi.set(__self__, "binary_media_types", binary_media_types)
        if body is not None:
            pulumi.set(__self__, "body", body)
        if body_s3_location is not None:
            pulumi.set(__self__, "body_s3_location", body_s3_location)
        if clone_from is not None:
            pulumi.set(__self__, "clone_from", clone_from)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if disable_execute_api_endpoint is not None:
            pulumi.set(__self__, "disable_execute_api_endpoint", disable_execute_api_endpoint)
        if endpoint_configuration is not None:
            pulumi.set(__self__, "endpoint_configuration", endpoint_configuration)
        if fail_on_warnings is not None:
            pulumi.set(__self__, "fail_on_warnings", fail_on_warnings)
        if minimum_compression_size is not None:
            pulumi.set(__self__, "minimum_compression_size", minimum_compression_size)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="apiKeySourceType")
    def api_key_source_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "api_key_source_type")

    @api_key_source_type.setter
    def api_key_source_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key_source_type", value)

    @property
    @pulumi.getter(name="binaryMediaTypes")
    def binary_media_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "binary_media_types")

    @binary_media_types.setter
    def binary_media_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "binary_media_types", value)

    @property
    @pulumi.getter
    def body(self) -> Optional[Any]:
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: Optional[Any]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter(name="bodyS3Location")
    def body_s3_location(self) -> Optional[pulumi.Input['RestApiS3LocationArgs']]:
        return pulumi.get(self, "body_s3_location")

    @body_s3_location.setter
    def body_s3_location(self, value: Optional[pulumi.Input['RestApiS3LocationArgs']]):
        pulumi.set(self, "body_s3_location", value)

    @property
    @pulumi.getter(name="cloneFrom")
    def clone_from(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "clone_from")

    @clone_from.setter
    def clone_from(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "clone_from", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="disableExecuteApiEndpoint")
    def disable_execute_api_endpoint(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "disable_execute_api_endpoint")

    @disable_execute_api_endpoint.setter
    def disable_execute_api_endpoint(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_execute_api_endpoint", value)

    @property
    @pulumi.getter(name="endpointConfiguration")
    def endpoint_configuration(self) -> Optional[pulumi.Input['RestApiEndpointConfigurationArgs']]:
        return pulumi.get(self, "endpoint_configuration")

    @endpoint_configuration.setter
    def endpoint_configuration(self, value: Optional[pulumi.Input['RestApiEndpointConfigurationArgs']]):
        pulumi.set(self, "endpoint_configuration", value)

    @property
    @pulumi.getter(name="failOnWarnings")
    def fail_on_warnings(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "fail_on_warnings")

    @fail_on_warnings.setter
    def fail_on_warnings(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "fail_on_warnings", value)

    @property
    @pulumi.getter(name="minimumCompressionSize")
    def minimum_compression_size(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "minimum_compression_size")

    @minimum_compression_size.setter
    def minimum_compression_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "minimum_compression_size", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Any]:
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[Any]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[Any]:
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[Any]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RestApiTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RestApiTagArgs']]]]):
        pulumi.set(self, "tags", value)


class RestApi(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key_source_type: Optional[pulumi.Input[str]] = None,
                 binary_media_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 body: Optional[Any] = None,
                 body_s3_location: Optional[pulumi.Input[pulumi.InputType['RestApiS3LocationArgs']]] = None,
                 clone_from: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disable_execute_api_endpoint: Optional[pulumi.Input[bool]] = None,
                 endpoint_configuration: Optional[pulumi.Input[pulumi.InputType['RestApiEndpointConfigurationArgs']]] = None,
                 fail_on_warnings: Optional[pulumi.Input[bool]] = None,
                 minimum_compression_size: Optional[pulumi.Input[int]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 policy: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RestApiTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ApiGateway::RestApi

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[RestApiArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ApiGateway::RestApi

        :param str resource_name: The name of the resource.
        :param RestApiArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RestApiArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key_source_type: Optional[pulumi.Input[str]] = None,
                 binary_media_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 body: Optional[Any] = None,
                 body_s3_location: Optional[pulumi.Input[pulumi.InputType['RestApiS3LocationArgs']]] = None,
                 clone_from: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disable_execute_api_endpoint: Optional[pulumi.Input[bool]] = None,
                 endpoint_configuration: Optional[pulumi.Input[pulumi.InputType['RestApiEndpointConfigurationArgs']]] = None,
                 fail_on_warnings: Optional[pulumi.Input[bool]] = None,
                 minimum_compression_size: Optional[pulumi.Input[int]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 policy: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RestApiTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RestApiArgs.__new__(RestApiArgs)

            __props__.__dict__["api_key_source_type"] = api_key_source_type
            __props__.__dict__["binary_media_types"] = binary_media_types
            __props__.__dict__["body"] = body
            __props__.__dict__["body_s3_location"] = body_s3_location
            __props__.__dict__["clone_from"] = clone_from
            __props__.__dict__["description"] = description
            __props__.__dict__["disable_execute_api_endpoint"] = disable_execute_api_endpoint
            __props__.__dict__["endpoint_configuration"] = endpoint_configuration
            __props__.__dict__["fail_on_warnings"] = fail_on_warnings
            __props__.__dict__["minimum_compression_size"] = minimum_compression_size
            __props__.__dict__["mode"] = mode
            __props__.__dict__["name"] = name
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["policy"] = policy
            __props__.__dict__["tags"] = tags
            __props__.__dict__["rest_api_id"] = None
            __props__.__dict__["root_resource_id"] = None
        super(RestApi, __self__).__init__(
            'aws-native:apigateway:RestApi',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RestApi':
        """
        Get an existing RestApi resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RestApiArgs.__new__(RestApiArgs)

        __props__.__dict__["api_key_source_type"] = None
        __props__.__dict__["binary_media_types"] = None
        __props__.__dict__["body"] = None
        __props__.__dict__["body_s3_location"] = None
        __props__.__dict__["clone_from"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["disable_execute_api_endpoint"] = None
        __props__.__dict__["endpoint_configuration"] = None
        __props__.__dict__["fail_on_warnings"] = None
        __props__.__dict__["minimum_compression_size"] = None
        __props__.__dict__["mode"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["policy"] = None
        __props__.__dict__["rest_api_id"] = None
        __props__.__dict__["root_resource_id"] = None
        __props__.__dict__["tags"] = None
        return RestApi(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiKeySourceType")
    def api_key_source_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "api_key_source_type")

    @property
    @pulumi.getter(name="binaryMediaTypes")
    def binary_media_types(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "binary_media_types")

    @property
    @pulumi.getter
    def body(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "body")

    @property
    @pulumi.getter(name="bodyS3Location")
    def body_s3_location(self) -> pulumi.Output[Optional['outputs.RestApiS3Location']]:
        return pulumi.get(self, "body_s3_location")

    @property
    @pulumi.getter(name="cloneFrom")
    def clone_from(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "clone_from")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="disableExecuteApiEndpoint")
    def disable_execute_api_endpoint(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "disable_execute_api_endpoint")

    @property
    @pulumi.getter(name="endpointConfiguration")
    def endpoint_configuration(self) -> pulumi.Output[Optional['outputs.RestApiEndpointConfiguration']]:
        return pulumi.get(self, "endpoint_configuration")

    @property
    @pulumi.getter(name="failOnWarnings")
    def fail_on_warnings(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "fail_on_warnings")

    @property
    @pulumi.getter(name="minimumCompressionSize")
    def minimum_compression_size(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "minimum_compression_size")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "rest_api_id")

    @property
    @pulumi.getter(name="rootResourceId")
    def root_resource_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "root_resource_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.RestApiTag']]]:
        return pulumi.get(self, "tags")

