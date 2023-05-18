# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetSceneResult',
    'AwaitableGetSceneResult',
    'get_scene',
    'get_scene_output',
]

@pulumi.output_type
class GetSceneResult:
    def __init__(__self__, arn=None, capabilities=None, content_location=None, creation_date_time=None, description=None, generated_scene_metadata=None, scene_metadata=None, tags=None, update_date_time=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if capabilities and not isinstance(capabilities, list):
            raise TypeError("Expected argument 'capabilities' to be a list")
        pulumi.set(__self__, "capabilities", capabilities)
        if content_location and not isinstance(content_location, str):
            raise TypeError("Expected argument 'content_location' to be a str")
        pulumi.set(__self__, "content_location", content_location)
        if creation_date_time and not isinstance(creation_date_time, str):
            raise TypeError("Expected argument 'creation_date_time' to be a str")
        pulumi.set(__self__, "creation_date_time", creation_date_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if generated_scene_metadata and not isinstance(generated_scene_metadata, dict):
            raise TypeError("Expected argument 'generated_scene_metadata' to be a dict")
        pulumi.set(__self__, "generated_scene_metadata", generated_scene_metadata)
        if scene_metadata and not isinstance(scene_metadata, dict):
            raise TypeError("Expected argument 'scene_metadata' to be a dict")
        pulumi.set(__self__, "scene_metadata", scene_metadata)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if update_date_time and not isinstance(update_date_time, str):
            raise TypeError("Expected argument 'update_date_time' to be a str")
        pulumi.set(__self__, "update_date_time", update_date_time)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The ARN of the scene.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def capabilities(self) -> Optional[Sequence[str]]:
        """
        A list of capabilities that the scene uses to render.
        """
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter(name="contentLocation")
    def content_location(self) -> Optional[str]:
        """
        The relative path that specifies the location of the content definition file.
        """
        return pulumi.get(self, "content_location")

    @property
    @pulumi.getter(name="creationDateTime")
    def creation_date_time(self) -> Optional[str]:
        """
        The date and time when the scene was created.
        """
        return pulumi.get(self, "creation_date_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the scene.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="generatedSceneMetadata")
    def generated_scene_metadata(self) -> Optional[Any]:
        """
        A key-value pair of generated scene metadata for the scene.
        """
        return pulumi.get(self, "generated_scene_metadata")

    @property
    @pulumi.getter(name="sceneMetadata")
    def scene_metadata(self) -> Optional[Any]:
        """
        A key-value pair of scene metadata for the scene.
        """
        return pulumi.get(self, "scene_metadata")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        A key-value pair to associate with a resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updateDateTime")
    def update_date_time(self) -> Optional[str]:
        """
        The date and time of the current update.
        """
        return pulumi.get(self, "update_date_time")


class AwaitableGetSceneResult(GetSceneResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSceneResult(
            arn=self.arn,
            capabilities=self.capabilities,
            content_location=self.content_location,
            creation_date_time=self.creation_date_time,
            description=self.description,
            generated_scene_metadata=self.generated_scene_metadata,
            scene_metadata=self.scene_metadata,
            tags=self.tags,
            update_date_time=self.update_date_time)


def get_scene(scene_id: Optional[str] = None,
              workspace_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSceneResult:
    """
    Resource schema for AWS::IoTTwinMaker::Scene


    :param str scene_id: The ID of the scene.
    :param str workspace_id: The ID of the scene.
    """
    __args__ = dict()
    __args__['sceneId'] = scene_id
    __args__['workspaceId'] = workspace_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iottwinmaker:getScene', __args__, opts=opts, typ=GetSceneResult).value

    return AwaitableGetSceneResult(
        arn=__ret__.arn,
        capabilities=__ret__.capabilities,
        content_location=__ret__.content_location,
        creation_date_time=__ret__.creation_date_time,
        description=__ret__.description,
        generated_scene_metadata=__ret__.generated_scene_metadata,
        scene_metadata=__ret__.scene_metadata,
        tags=__ret__.tags,
        update_date_time=__ret__.update_date_time)


@_utilities.lift_output_func(get_scene)
def get_scene_output(scene_id: Optional[pulumi.Input[str]] = None,
                     workspace_id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSceneResult]:
    """
    Resource schema for AWS::IoTTwinMaker::Scene


    :param str scene_id: The ID of the scene.
    :param str workspace_id: The ID of the scene.
    """
    ...
