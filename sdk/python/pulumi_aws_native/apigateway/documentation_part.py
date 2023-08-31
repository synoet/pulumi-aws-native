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

__all__ = ['DocumentationPartArgs', 'DocumentationPart']

@pulumi.input_type
class DocumentationPartArgs:
    def __init__(__self__, *,
                 location: pulumi.Input['DocumentationPartLocationArgs'],
                 properties: pulumi.Input[str],
                 rest_api_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a DocumentationPart resource.
        :param pulumi.Input['DocumentationPartLocationArgs'] location: The location of the API entity that the documentation applies to.
        :param pulumi.Input[str] properties: The documentation content map of the targeted API entity.
        :param pulumi.Input[str] rest_api_id: Identifier of the targeted API entity
        """
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "rest_api_id", rest_api_id)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input['DocumentationPartLocationArgs']:
        """
        The location of the API entity that the documentation applies to.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input['DocumentationPartLocationArgs']):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input[str]:
        """
        The documentation content map of the targeted API entity.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input[str]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> pulumi.Input[str]:
        """
        Identifier of the targeted API entity
        """
        return pulumi.get(self, "rest_api_id")

    @rest_api_id.setter
    def rest_api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "rest_api_id", value)


class DocumentationPart(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[pulumi.InputType['DocumentationPartLocationArgs']]] = None,
                 properties: Optional[pulumi.Input[str]] = None,
                 rest_api_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ApiGateway::DocumentationPart

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DocumentationPartLocationArgs']] location: The location of the API entity that the documentation applies to.
        :param pulumi.Input[str] properties: The documentation content map of the targeted API entity.
        :param pulumi.Input[str] rest_api_id: Identifier of the targeted API entity
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DocumentationPartArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ApiGateway::DocumentationPart

        :param str resource_name: The name of the resource.
        :param DocumentationPartArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DocumentationPartArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[pulumi.InputType['DocumentationPartLocationArgs']]] = None,
                 properties: Optional[pulumi.Input[str]] = None,
                 rest_api_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DocumentationPartArgs.__new__(DocumentationPartArgs)

            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            if rest_api_id is None and not opts.urn:
                raise TypeError("Missing required property 'rest_api_id'")
            __props__.__dict__["rest_api_id"] = rest_api_id
            __props__.__dict__["documentation_part_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["location", "rest_api_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DocumentationPart, __self__).__init__(
            'aws-native:apigateway:DocumentationPart',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DocumentationPart':
        """
        Get an existing DocumentationPart resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DocumentationPartArgs.__new__(DocumentationPartArgs)

        __props__.__dict__["documentation_part_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["rest_api_id"] = None
        return DocumentationPart(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="documentationPartId")
    def documentation_part_id(self) -> pulumi.Output[str]:
        """
        The identifier of the documentation Part.
        """
        return pulumi.get(self, "documentation_part_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output['outputs.DocumentationPartLocation']:
        """
        The location of the API entity that the documentation applies to.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[str]:
        """
        The documentation content map of the targeted API entity.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> pulumi.Output[str]:
        """
        Identifier of the targeted API entity
        """
        return pulumi.get(self, "rest_api_id")

