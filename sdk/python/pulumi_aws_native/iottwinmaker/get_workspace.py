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
    'GetWorkspaceResult',
    'AwaitableGetWorkspaceResult',
    'get_workspace',
    'get_workspace_output',
]

@pulumi.output_type
class GetWorkspaceResult:
    def __init__(__self__, arn=None, creation_date_time=None, description=None, role=None, s3_location=None, tags=None, update_date_time=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if creation_date_time and not isinstance(creation_date_time, str):
            raise TypeError("Expected argument 'creation_date_time' to be a str")
        pulumi.set(__self__, "creation_date_time", creation_date_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if role and not isinstance(role, str):
            raise TypeError("Expected argument 'role' to be a str")
        pulumi.set(__self__, "role", role)
        if s3_location and not isinstance(s3_location, str):
            raise TypeError("Expected argument 's3_location' to be a str")
        pulumi.set(__self__, "s3_location", s3_location)
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
        The ARN of the workspace.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="creationDateTime")
    def creation_date_time(self) -> Optional[str]:
        """
        The date and time when the workspace was created.
        """
        return pulumi.get(self, "creation_date_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the workspace.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def role(self) -> Optional[str]:
        """
        The ARN of the execution role associated with the workspace.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="s3Location")
    def s3_location(self) -> Optional[str]:
        """
        The ARN of the S3 bucket where resources associated with the workspace are stored.
        """
        return pulumi.get(self, "s3_location")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        A map of key-value pairs to associate with a resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updateDateTime")
    def update_date_time(self) -> Optional[str]:
        """
        The date and time of the current update.
        """
        return pulumi.get(self, "update_date_time")


class AwaitableGetWorkspaceResult(GetWorkspaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceResult(
            arn=self.arn,
            creation_date_time=self.creation_date_time,
            description=self.description,
            role=self.role,
            s3_location=self.s3_location,
            tags=self.tags,
            update_date_time=self.update_date_time)


def get_workspace(workspace_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceResult:
    """
    Resource schema for AWS::IoTTwinMaker::Workspace


    :param str workspace_id: The ID of the workspace.
    """
    __args__ = dict()
    __args__['workspaceId'] = workspace_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iottwinmaker:getWorkspace', __args__, opts=opts, typ=GetWorkspaceResult).value

    return AwaitableGetWorkspaceResult(
        arn=__ret__.arn,
        creation_date_time=__ret__.creation_date_time,
        description=__ret__.description,
        role=__ret__.role,
        s3_location=__ret__.s3_location,
        tags=__ret__.tags,
        update_date_time=__ret__.update_date_time)


@_utilities.lift_output_func(get_workspace)
def get_workspace_output(workspace_id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceResult]:
    """
    Resource schema for AWS::IoTTwinMaker::Workspace


    :param str workspace_id: The ID of the workspace.
    """
    ...
