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

__all__ = ['ComponentArgs', 'Component']

@pulumi.input_type
class ComponentArgs:
    def __init__(__self__, *,
                 binding_properties: pulumi.Input['ComponentBindingPropertiesArgs'],
                 component_type: pulumi.Input[str],
                 overrides: pulumi.Input['ComponentOverridesArgs'],
                 properties: pulumi.Input['ComponentPropertiesArgs'],
                 variants: pulumi.Input[Sequence[pulumi.Input['ComponentVariantArgs']]],
                 app_id: Optional[pulumi.Input[str]] = None,
                 children: Optional[pulumi.Input[Sequence[pulumi.Input['ComponentChildArgs']]]] = None,
                 collection_properties: Optional[pulumi.Input['ComponentCollectionPropertiesArgs']] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 events: Optional[pulumi.Input['ComponentEventsArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schema_version: Optional[pulumi.Input[str]] = None,
                 source_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input['ComponentTagsArgs']] = None):
        """
        The set of arguments for constructing a Component resource.
        """
        pulumi.set(__self__, "binding_properties", binding_properties)
        pulumi.set(__self__, "component_type", component_type)
        pulumi.set(__self__, "overrides", overrides)
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "variants", variants)
        if app_id is not None:
            pulumi.set(__self__, "app_id", app_id)
        if children is not None:
            pulumi.set(__self__, "children", children)
        if collection_properties is not None:
            pulumi.set(__self__, "collection_properties", collection_properties)
        if environment_name is not None:
            pulumi.set(__self__, "environment_name", environment_name)
        if events is not None:
            pulumi.set(__self__, "events", events)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if schema_version is not None:
            pulumi.set(__self__, "schema_version", schema_version)
        if source_id is not None:
            pulumi.set(__self__, "source_id", source_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="bindingProperties")
    def binding_properties(self) -> pulumi.Input['ComponentBindingPropertiesArgs']:
        return pulumi.get(self, "binding_properties")

    @binding_properties.setter
    def binding_properties(self, value: pulumi.Input['ComponentBindingPropertiesArgs']):
        pulumi.set(self, "binding_properties", value)

    @property
    @pulumi.getter(name="componentType")
    def component_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "component_type")

    @component_type.setter
    def component_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "component_type", value)

    @property
    @pulumi.getter
    def overrides(self) -> pulumi.Input['ComponentOverridesArgs']:
        return pulumi.get(self, "overrides")

    @overrides.setter
    def overrides(self, value: pulumi.Input['ComponentOverridesArgs']):
        pulumi.set(self, "overrides", value)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input['ComponentPropertiesArgs']:
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input['ComponentPropertiesArgs']):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def variants(self) -> pulumi.Input[Sequence[pulumi.Input['ComponentVariantArgs']]]:
        return pulumi.get(self, "variants")

    @variants.setter
    def variants(self, value: pulumi.Input[Sequence[pulumi.Input['ComponentVariantArgs']]]):
        pulumi.set(self, "variants", value)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter
    def children(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ComponentChildArgs']]]]:
        return pulumi.get(self, "children")

    @children.setter
    def children(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ComponentChildArgs']]]]):
        pulumi.set(self, "children", value)

    @property
    @pulumi.getter(name="collectionProperties")
    def collection_properties(self) -> Optional[pulumi.Input['ComponentCollectionPropertiesArgs']]:
        return pulumi.get(self, "collection_properties")

    @collection_properties.setter
    def collection_properties(self, value: Optional[pulumi.Input['ComponentCollectionPropertiesArgs']]):
        pulumi.set(self, "collection_properties", value)

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_name", value)

    @property
    @pulumi.getter
    def events(self) -> Optional[pulumi.Input['ComponentEventsArgs']]:
        return pulumi.get(self, "events")

    @events.setter
    def events(self, value: Optional[pulumi.Input['ComponentEventsArgs']]):
        pulumi.set(self, "events", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "schema_version")

    @schema_version.setter
    def schema_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_version", value)

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_id")

    @source_id.setter
    def source_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input['ComponentTagsArgs']]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input['ComponentTagsArgs']]):
        pulumi.set(self, "tags", value)


class Component(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 binding_properties: Optional[pulumi.Input[pulumi.InputType['ComponentBindingPropertiesArgs']]] = None,
                 children: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ComponentChildArgs']]]]] = None,
                 collection_properties: Optional[pulumi.Input[pulumi.InputType['ComponentCollectionPropertiesArgs']]] = None,
                 component_type: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 events: Optional[pulumi.Input[pulumi.InputType['ComponentEventsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 overrides: Optional[pulumi.Input[pulumi.InputType['ComponentOverridesArgs']]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['ComponentPropertiesArgs']]] = None,
                 schema_version: Optional[pulumi.Input[str]] = None,
                 source_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['ComponentTagsArgs']]] = None,
                 variants: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ComponentVariantArgs']]]]] = None,
                 __props__=None):
        """
        Definition of AWS::AmplifyUIBuilder::Component Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComponentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::AmplifyUIBuilder::Component Resource Type

        :param str resource_name: The name of the resource.
        :param ComponentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComponentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 binding_properties: Optional[pulumi.Input[pulumi.InputType['ComponentBindingPropertiesArgs']]] = None,
                 children: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ComponentChildArgs']]]]] = None,
                 collection_properties: Optional[pulumi.Input[pulumi.InputType['ComponentCollectionPropertiesArgs']]] = None,
                 component_type: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 events: Optional[pulumi.Input[pulumi.InputType['ComponentEventsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 overrides: Optional[pulumi.Input[pulumi.InputType['ComponentOverridesArgs']]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['ComponentPropertiesArgs']]] = None,
                 schema_version: Optional[pulumi.Input[str]] = None,
                 source_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['ComponentTagsArgs']]] = None,
                 variants: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ComponentVariantArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ComponentArgs.__new__(ComponentArgs)

            __props__.__dict__["app_id"] = app_id
            if binding_properties is None and not opts.urn:
                raise TypeError("Missing required property 'binding_properties'")
            __props__.__dict__["binding_properties"] = binding_properties
            __props__.__dict__["children"] = children
            __props__.__dict__["collection_properties"] = collection_properties
            if component_type is None and not opts.urn:
                raise TypeError("Missing required property 'component_type'")
            __props__.__dict__["component_type"] = component_type
            __props__.__dict__["environment_name"] = environment_name
            __props__.__dict__["events"] = events
            __props__.__dict__["name"] = name
            if overrides is None and not opts.urn:
                raise TypeError("Missing required property 'overrides'")
            __props__.__dict__["overrides"] = overrides
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            __props__.__dict__["schema_version"] = schema_version
            __props__.__dict__["source_id"] = source_id
            __props__.__dict__["tags"] = tags
            if variants is None and not opts.urn:
                raise TypeError("Missing required property 'variants'")
            __props__.__dict__["variants"] = variants
        super(Component, __self__).__init__(
            'aws-native:amplifyuibuilder:Component',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Component':
        """
        Get an existing Component resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ComponentArgs.__new__(ComponentArgs)

        __props__.__dict__["app_id"] = None
        __props__.__dict__["binding_properties"] = None
        __props__.__dict__["children"] = None
        __props__.__dict__["collection_properties"] = None
        __props__.__dict__["component_type"] = None
        __props__.__dict__["environment_name"] = None
        __props__.__dict__["events"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["overrides"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["schema_version"] = None
        __props__.__dict__["source_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["variants"] = None
        return Component(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="bindingProperties")
    def binding_properties(self) -> pulumi.Output['outputs.ComponentBindingProperties']:
        return pulumi.get(self, "binding_properties")

    @property
    @pulumi.getter
    def children(self) -> pulumi.Output[Optional[Sequence['outputs.ComponentChild']]]:
        return pulumi.get(self, "children")

    @property
    @pulumi.getter(name="collectionProperties")
    def collection_properties(self) -> pulumi.Output[Optional['outputs.ComponentCollectionProperties']]:
        return pulumi.get(self, "collection_properties")

    @property
    @pulumi.getter(name="componentType")
    def component_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "component_type")

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "environment_name")

    @property
    @pulumi.getter
    def events(self) -> pulumi.Output[Optional['outputs.ComponentEvents']]:
        return pulumi.get(self, "events")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def overrides(self) -> pulumi.Output['outputs.ComponentOverrides']:
        return pulumi.get(self, "overrides")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.ComponentProperties']:
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "schema_version")

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "source_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional['outputs.ComponentTags']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def variants(self) -> pulumi.Output[Sequence['outputs.ComponentVariant']]:
        return pulumi.get(self, "variants")

