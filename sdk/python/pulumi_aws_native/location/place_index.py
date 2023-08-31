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

__all__ = ['PlaceIndexArgs', 'PlaceIndex']

@pulumi.input_type
class PlaceIndexArgs:
    def __init__(__self__, *,
                 data_source: pulumi.Input[str],
                 index_name: pulumi.Input[str],
                 data_source_configuration: Optional[pulumi.Input['PlaceIndexDataSourceConfigurationArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 pricing_plan: Optional[pulumi.Input['PlaceIndexPricingPlan']] = None):
        """
        The set of arguments for constructing a PlaceIndex resource.
        """
        pulumi.set(__self__, "data_source", data_source)
        pulumi.set(__self__, "index_name", index_name)
        if data_source_configuration is not None:
            pulumi.set(__self__, "data_source_configuration", data_source_configuration)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if pricing_plan is not None:
            pulumi.set(__self__, "pricing_plan", pricing_plan)

    @property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Input[str]:
        return pulumi.get(self, "data_source")

    @data_source.setter
    def data_source(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_source", value)

    @property
    @pulumi.getter(name="indexName")
    def index_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "index_name")

    @index_name.setter
    def index_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "index_name", value)

    @property
    @pulumi.getter(name="dataSourceConfiguration")
    def data_source_configuration(self) -> Optional[pulumi.Input['PlaceIndexDataSourceConfigurationArgs']]:
        return pulumi.get(self, "data_source_configuration")

    @data_source_configuration.setter
    def data_source_configuration(self, value: Optional[pulumi.Input['PlaceIndexDataSourceConfigurationArgs']]):
        pulumi.set(self, "data_source_configuration", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="pricingPlan")
    def pricing_plan(self) -> Optional[pulumi.Input['PlaceIndexPricingPlan']]:
        return pulumi.get(self, "pricing_plan")

    @pricing_plan.setter
    def pricing_plan(self, value: Optional[pulumi.Input['PlaceIndexPricingPlan']]):
        pulumi.set(self, "pricing_plan", value)


class PlaceIndex(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_source: Optional[pulumi.Input[str]] = None,
                 data_source_configuration: Optional[pulumi.Input[pulumi.InputType['PlaceIndexDataSourceConfigurationArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 index_name: Optional[pulumi.Input[str]] = None,
                 pricing_plan: Optional[pulumi.Input['PlaceIndexPricingPlan']] = None,
                 __props__=None):
        """
        Definition of AWS::Location::PlaceIndex Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PlaceIndexArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::Location::PlaceIndex Resource Type

        :param str resource_name: The name of the resource.
        :param PlaceIndexArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PlaceIndexArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_source: Optional[pulumi.Input[str]] = None,
                 data_source_configuration: Optional[pulumi.Input[pulumi.InputType['PlaceIndexDataSourceConfigurationArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 index_name: Optional[pulumi.Input[str]] = None,
                 pricing_plan: Optional[pulumi.Input['PlaceIndexPricingPlan']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PlaceIndexArgs.__new__(PlaceIndexArgs)

            if data_source is None and not opts.urn:
                raise TypeError("Missing required property 'data_source'")
            __props__.__dict__["data_source"] = data_source
            __props__.__dict__["data_source_configuration"] = data_source_configuration
            __props__.__dict__["description"] = description
            if index_name is None and not opts.urn:
                raise TypeError("Missing required property 'index_name'")
            __props__.__dict__["index_name"] = index_name
            __props__.__dict__["pricing_plan"] = pricing_plan
            __props__.__dict__["arn"] = None
            __props__.__dict__["create_time"] = None
            __props__.__dict__["index_arn"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["data_source", "data_source_configuration", "description", "index_name", "pricing_plan"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(PlaceIndex, __self__).__init__(
            'aws-native:location:PlaceIndex',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PlaceIndex':
        """
        Get an existing PlaceIndex resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PlaceIndexArgs.__new__(PlaceIndexArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["data_source"] = None
        __props__.__dict__["data_source_configuration"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["index_arn"] = None
        __props__.__dict__["index_name"] = None
        __props__.__dict__["pricing_plan"] = None
        __props__.__dict__["update_time"] = None
        return PlaceIndex(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Output[str]:
        return pulumi.get(self, "data_source")

    @property
    @pulumi.getter(name="dataSourceConfiguration")
    def data_source_configuration(self) -> pulumi.Output[Optional['outputs.PlaceIndexDataSourceConfiguration']]:
        return pulumi.get(self, "data_source_configuration")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="indexArn")
    def index_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "index_arn")

    @property
    @pulumi.getter(name="indexName")
    def index_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "index_name")

    @property
    @pulumi.getter(name="pricingPlan")
    def pricing_plan(self) -> pulumi.Output[Optional['PlaceIndexPricingPlan']]:
        return pulumi.get(self, "pricing_plan")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "update_time")

