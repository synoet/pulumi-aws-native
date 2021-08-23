# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._inputs import *

__all__ = ['AssetArgs', 'Asset']

@pulumi.input_type
class AssetArgs:
    def __init__(__self__, *,
                 asset_model_id: pulumi.Input[str],
                 asset_name: pulumi.Input[str],
                 asset_hierarchies: Optional[pulumi.Input[Sequence[pulumi.Input['AssetAssetHierarchyArgs']]]] = None,
                 asset_properties: Optional[pulumi.Input[Sequence[pulumi.Input['AssetAssetPropertyArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Asset resource.
        :param pulumi.Input[str] asset_model_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetmodelid
        :param pulumi.Input[str] asset_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetname
        :param pulumi.Input[Sequence[pulumi.Input['AssetAssetHierarchyArgs']]] asset_hierarchies: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assethierarchies
        :param pulumi.Input[Sequence[pulumi.Input['AssetAssetPropertyArgs']]] asset_properties: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetproperties
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-tags
        """
        pulumi.set(__self__, "asset_model_id", asset_model_id)
        pulumi.set(__self__, "asset_name", asset_name)
        if asset_hierarchies is not None:
            pulumi.set(__self__, "asset_hierarchies", asset_hierarchies)
        if asset_properties is not None:
            pulumi.set(__self__, "asset_properties", asset_properties)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="assetModelId")
    def asset_model_id(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetmodelid
        """
        return pulumi.get(self, "asset_model_id")

    @asset_model_id.setter
    def asset_model_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "asset_model_id", value)

    @property
    @pulumi.getter(name="assetName")
    def asset_name(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetname
        """
        return pulumi.get(self, "asset_name")

    @asset_name.setter
    def asset_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "asset_name", value)

    @property
    @pulumi.getter(name="assetHierarchies")
    def asset_hierarchies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AssetAssetHierarchyArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assethierarchies
        """
        return pulumi.get(self, "asset_hierarchies")

    @asset_hierarchies.setter
    def asset_hierarchies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AssetAssetHierarchyArgs']]]]):
        pulumi.set(self, "asset_hierarchies", value)

    @property
    @pulumi.getter(name="assetProperties")
    def asset_properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AssetAssetPropertyArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetproperties
        """
        return pulumi.get(self, "asset_properties")

    @asset_properties.setter
    def asset_properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AssetAssetPropertyArgs']]]]):
        pulumi.set(self, "asset_properties", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Asset(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asset_hierarchies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetAssetHierarchyArgs']]]]] = None,
                 asset_model_id: Optional[pulumi.Input[str]] = None,
                 asset_name: Optional[pulumi.Input[str]] = None,
                 asset_properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetAssetPropertyArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetAssetHierarchyArgs']]]] asset_hierarchies: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assethierarchies
        :param pulumi.Input[str] asset_model_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetmodelid
        :param pulumi.Input[str] asset_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetname
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetAssetPropertyArgs']]]] asset_properties: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetproperties
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AssetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html

        :param str resource_name: The name of the resource.
        :param AssetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asset_hierarchies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetAssetHierarchyArgs']]]]] = None,
                 asset_model_id: Optional[pulumi.Input[str]] = None,
                 asset_name: Optional[pulumi.Input[str]] = None,
                 asset_properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetAssetPropertyArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
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
            __props__ = AssetArgs.__new__(AssetArgs)

            __props__.__dict__["asset_hierarchies"] = asset_hierarchies
            if asset_model_id is None and not opts.urn:
                raise TypeError("Missing required property 'asset_model_id'")
            __props__.__dict__["asset_model_id"] = asset_model_id
            if asset_name is None and not opts.urn:
                raise TypeError("Missing required property 'asset_name'")
            __props__.__dict__["asset_name"] = asset_name
            __props__.__dict__["asset_properties"] = asset_properties
            __props__.__dict__["tags"] = tags
            __props__.__dict__["asset_arn"] = None
            __props__.__dict__["asset_id"] = None
        super(Asset, __self__).__init__(
            'aws-native:iotsitewise:Asset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Asset':
        """
        Get an existing Asset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AssetArgs.__new__(AssetArgs)

        __props__.__dict__["asset_arn"] = None
        __props__.__dict__["asset_hierarchies"] = None
        __props__.__dict__["asset_id"] = None
        __props__.__dict__["asset_model_id"] = None
        __props__.__dict__["asset_name"] = None
        __props__.__dict__["asset_properties"] = None
        __props__.__dict__["tags"] = None
        return Asset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assetArn")
    def asset_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "asset_arn")

    @property
    @pulumi.getter(name="assetHierarchies")
    def asset_hierarchies(self) -> pulumi.Output[Optional[Sequence['outputs.AssetAssetHierarchy']]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assethierarchies
        """
        return pulumi.get(self, "asset_hierarchies")

    @property
    @pulumi.getter(name="assetId")
    def asset_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "asset_id")

    @property
    @pulumi.getter(name="assetModelId")
    def asset_model_id(self) -> pulumi.Output[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetmodelid
        """
        return pulumi.get(self, "asset_model_id")

    @property
    @pulumi.getter(name="assetName")
    def asset_name(self) -> pulumi.Output[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetname
        """
        return pulumi.get(self, "asset_name")

    @property
    @pulumi.getter(name="assetProperties")
    def asset_properties(self) -> pulumi.Output[Optional[Sequence['outputs.AssetAssetProperty']]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetproperties
        """
        return pulumi.get(self, "asset_properties")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-tags
        """
        return pulumi.get(self, "tags")

