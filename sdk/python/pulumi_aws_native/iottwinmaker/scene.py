# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SceneArgs', 'Scene']

@pulumi.input_type
class SceneArgs:
    def __init__(__self__, *,
                 content_location: pulumi.Input[str],
                 scene_id: pulumi.Input[str],
                 workspace_id: pulumi.Input[str],
                 capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 scene_metadata: Optional[Any] = None,
                 tags: Optional[Any] = None):
        """
        The set of arguments for constructing a Scene resource.
        :param pulumi.Input[str] content_location: The relative path that specifies the location of the content definition file.
        :param pulumi.Input[str] scene_id: The ID of the scene.
        :param pulumi.Input[str] workspace_id: The ID of the scene.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] capabilities: A list of capabilities that the scene uses to render.
        :param pulumi.Input[str] description: The description of the scene.
        :param Any scene_metadata: A key-value pair of scene metadata for the scene.
        :param Any tags: A key-value pair to associate with a resource.
        """
        pulumi.set(__self__, "content_location", content_location)
        pulumi.set(__self__, "scene_id", scene_id)
        pulumi.set(__self__, "workspace_id", workspace_id)
        if capabilities is not None:
            pulumi.set(__self__, "capabilities", capabilities)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if scene_metadata is not None:
            pulumi.set(__self__, "scene_metadata", scene_metadata)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="contentLocation")
    def content_location(self) -> pulumi.Input[str]:
        """
        The relative path that specifies the location of the content definition file.
        """
        return pulumi.get(self, "content_location")

    @content_location.setter
    def content_location(self, value: pulumi.Input[str]):
        pulumi.set(self, "content_location", value)

    @property
    @pulumi.getter(name="sceneId")
    def scene_id(self) -> pulumi.Input[str]:
        """
        The ID of the scene.
        """
        return pulumi.get(self, "scene_id")

    @scene_id.setter
    def scene_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "scene_id", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[str]:
        """
        The ID of the scene.
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_id", value)

    @property
    @pulumi.getter
    def capabilities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of capabilities that the scene uses to render.
        """
        return pulumi.get(self, "capabilities")

    @capabilities.setter
    def capabilities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "capabilities", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the scene.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="sceneMetadata")
    def scene_metadata(self) -> Optional[Any]:
        """
        A key-value pair of scene metadata for the scene.
        """
        return pulumi.get(self, "scene_metadata")

    @scene_metadata.setter
    def scene_metadata(self, value: Optional[Any]):
        pulumi.set(self, "scene_metadata", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        A key-value pair to associate with a resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)


class Scene(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 content_location: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 scene_id: Optional[pulumi.Input[str]] = None,
                 scene_metadata: Optional[Any] = None,
                 tags: Optional[Any] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource schema for AWS::IoTTwinMaker::Scene

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] capabilities: A list of capabilities that the scene uses to render.
        :param pulumi.Input[str] content_location: The relative path that specifies the location of the content definition file.
        :param pulumi.Input[str] description: The description of the scene.
        :param pulumi.Input[str] scene_id: The ID of the scene.
        :param Any scene_metadata: A key-value pair of scene metadata for the scene.
        :param Any tags: A key-value pair to associate with a resource.
        :param pulumi.Input[str] workspace_id: The ID of the scene.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SceneArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::IoTTwinMaker::Scene

        :param str resource_name: The name of the resource.
        :param SceneArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SceneArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 content_location: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 scene_id: Optional[pulumi.Input[str]] = None,
                 scene_metadata: Optional[Any] = None,
                 tags: Optional[Any] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SceneArgs.__new__(SceneArgs)

            __props__.__dict__["capabilities"] = capabilities
            if content_location is None and not opts.urn:
                raise TypeError("Missing required property 'content_location'")
            __props__.__dict__["content_location"] = content_location
            __props__.__dict__["description"] = description
            if scene_id is None and not opts.urn:
                raise TypeError("Missing required property 'scene_id'")
            __props__.__dict__["scene_id"] = scene_id
            __props__.__dict__["scene_metadata"] = scene_metadata
            __props__.__dict__["tags"] = tags
            if workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_id'")
            __props__.__dict__["workspace_id"] = workspace_id
            __props__.__dict__["arn"] = None
            __props__.__dict__["creation_date_time"] = None
            __props__.__dict__["generated_scene_metadata"] = None
            __props__.__dict__["update_date_time"] = None
        super(Scene, __self__).__init__(
            'aws-native:iottwinmaker:Scene',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Scene':
        """
        Get an existing Scene resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SceneArgs.__new__(SceneArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["capabilities"] = None
        __props__.__dict__["content_location"] = None
        __props__.__dict__["creation_date_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["generated_scene_metadata"] = None
        __props__.__dict__["scene_id"] = None
        __props__.__dict__["scene_metadata"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["update_date_time"] = None
        __props__.__dict__["workspace_id"] = None
        return Scene(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the scene.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def capabilities(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of capabilities that the scene uses to render.
        """
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter(name="contentLocation")
    def content_location(self) -> pulumi.Output[str]:
        """
        The relative path that specifies the location of the content definition file.
        """
        return pulumi.get(self, "content_location")

    @property
    @pulumi.getter(name="creationDateTime")
    def creation_date_time(self) -> pulumi.Output[str]:
        """
        The date and time when the scene was created.
        """
        return pulumi.get(self, "creation_date_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the scene.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="generatedSceneMetadata")
    def generated_scene_metadata(self) -> pulumi.Output[Any]:
        """
        A key-value pair of generated scene metadata for the scene.
        """
        return pulumi.get(self, "generated_scene_metadata")

    @property
    @pulumi.getter(name="sceneId")
    def scene_id(self) -> pulumi.Output[str]:
        """
        The ID of the scene.
        """
        return pulumi.get(self, "scene_id")

    @property
    @pulumi.getter(name="sceneMetadata")
    def scene_metadata(self) -> pulumi.Output[Optional[Any]]:
        """
        A key-value pair of scene metadata for the scene.
        """
        return pulumi.get(self, "scene_metadata")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        """
        A key-value pair to associate with a resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updateDateTime")
    def update_date_time(self) -> pulumi.Output[str]:
        """
        The date and time of the current update.
        """
        return pulumi.get(self, "update_date_time")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[str]:
        """
        The ID of the scene.
        """
        return pulumi.get(self, "workspace_id")

