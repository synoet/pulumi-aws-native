# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._inputs import *

__all__ = ['Registry']


class Registry(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deletion_policy: Optional[pulumi.Input[str]] = None,
                 logical_id: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Union[Any, str]]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['RegistryPropertiesArgs']]] = None,
                 update_replace_policy: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-registry.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deletion_policy: With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
        :param pulumi.Input[str] logical_id: An explicit logical ID for the resource
        :param pulumi.Input[Union[Any, str]] metadata: Arbitrary structured data associated with the resource
        :param pulumi.Input[pulumi.InputType['RegistryPropertiesArgs']] properties: The input properties associated with the resource
        :param pulumi.Input[str] update_replace_policy: Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['deletion_policy'] = deletion_policy
            __props__['logical_id'] = logical_id
            __props__['metadata'] = metadata
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__['properties'] = properties
            __props__['update_replace_policy'] = update_replace_policy
            __props__['attributes'] = None
        super(Registry, __self__).__init__(
            'cloudformation:Glue:Registry',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Registry':
        """
        Get an existing Registry resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return Registry(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Output['outputs.RegistryAttributes']:
        """
        The attributes associated with the resource
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="logicalId")
    def logical_id(self) -> pulumi.Output[Optional[str]]:
        """
        An explicit logical ID for the resource
        """
        return pulumi.get(self, "logical_id")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[str]]:
        """
        Arbitrary structured data associated with the resource
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.RegistryProperties']:
        """
        The input properties associated with the resource
        """
        return pulumi.get(self, "properties")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

