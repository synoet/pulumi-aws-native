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

__all__ = [
    'GetFileSystemResult',
    'AwaitableGetFileSystemResult',
    'get_file_system',
    'get_file_system_output',
]

@pulumi.output_type
class GetFileSystemResult:
    def __init__(__self__, d_ns_name=None, id=None, lustre_configuration=None, lustre_mount_name=None, ontap_configuration=None, open_zfs_configuration=None, root_volume_id=None, storage_capacity=None, tags=None, windows_configuration=None):
        if d_ns_name and not isinstance(d_ns_name, str):
            raise TypeError("Expected argument 'd_ns_name' to be a str")
        pulumi.set(__self__, "d_ns_name", d_ns_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lustre_configuration and not isinstance(lustre_configuration, dict):
            raise TypeError("Expected argument 'lustre_configuration' to be a dict")
        pulumi.set(__self__, "lustre_configuration", lustre_configuration)
        if lustre_mount_name and not isinstance(lustre_mount_name, str):
            raise TypeError("Expected argument 'lustre_mount_name' to be a str")
        pulumi.set(__self__, "lustre_mount_name", lustre_mount_name)
        if ontap_configuration and not isinstance(ontap_configuration, dict):
            raise TypeError("Expected argument 'ontap_configuration' to be a dict")
        pulumi.set(__self__, "ontap_configuration", ontap_configuration)
        if open_zfs_configuration and not isinstance(open_zfs_configuration, dict):
            raise TypeError("Expected argument 'open_zfs_configuration' to be a dict")
        pulumi.set(__self__, "open_zfs_configuration", open_zfs_configuration)
        if root_volume_id and not isinstance(root_volume_id, str):
            raise TypeError("Expected argument 'root_volume_id' to be a str")
        pulumi.set(__self__, "root_volume_id", root_volume_id)
        if storage_capacity and not isinstance(storage_capacity, int):
            raise TypeError("Expected argument 'storage_capacity' to be a int")
        pulumi.set(__self__, "storage_capacity", storage_capacity)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if windows_configuration and not isinstance(windows_configuration, dict):
            raise TypeError("Expected argument 'windows_configuration' to be a dict")
        pulumi.set(__self__, "windows_configuration", windows_configuration)

    @property
    @pulumi.getter(name="dNSName")
    def d_ns_name(self) -> Optional[str]:
        return pulumi.get(self, "d_ns_name")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lustreConfiguration")
    def lustre_configuration(self) -> Optional['outputs.FileSystemLustreConfiguration']:
        return pulumi.get(self, "lustre_configuration")

    @property
    @pulumi.getter(name="lustreMountName")
    def lustre_mount_name(self) -> Optional[str]:
        return pulumi.get(self, "lustre_mount_name")

    @property
    @pulumi.getter(name="ontapConfiguration")
    def ontap_configuration(self) -> Optional['outputs.FileSystemOntapConfiguration']:
        return pulumi.get(self, "ontap_configuration")

    @property
    @pulumi.getter(name="openZFSConfiguration")
    def open_zfs_configuration(self) -> Optional['outputs.FileSystemOpenZFSConfiguration']:
        return pulumi.get(self, "open_zfs_configuration")

    @property
    @pulumi.getter(name="rootVolumeId")
    def root_volume_id(self) -> Optional[str]:
        return pulumi.get(self, "root_volume_id")

    @property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> Optional[int]:
        return pulumi.get(self, "storage_capacity")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.FileSystemTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="windowsConfiguration")
    def windows_configuration(self) -> Optional['outputs.FileSystemWindowsConfiguration']:
        return pulumi.get(self, "windows_configuration")


class AwaitableGetFileSystemResult(GetFileSystemResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFileSystemResult(
            d_ns_name=self.d_ns_name,
            id=self.id,
            lustre_configuration=self.lustre_configuration,
            lustre_mount_name=self.lustre_mount_name,
            ontap_configuration=self.ontap_configuration,
            open_zfs_configuration=self.open_zfs_configuration,
            root_volume_id=self.root_volume_id,
            storage_capacity=self.storage_capacity,
            tags=self.tags,
            windows_configuration=self.windows_configuration)


def get_file_system(id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFileSystemResult:
    """
    Resource Type definition for AWS::FSx::FileSystem
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:fsx:getFileSystem', __args__, opts=opts, typ=GetFileSystemResult).value

    return AwaitableGetFileSystemResult(
        d_ns_name=__ret__.d_ns_name,
        id=__ret__.id,
        lustre_configuration=__ret__.lustre_configuration,
        lustre_mount_name=__ret__.lustre_mount_name,
        ontap_configuration=__ret__.ontap_configuration,
        open_zfs_configuration=__ret__.open_zfs_configuration,
        root_volume_id=__ret__.root_volume_id,
        storage_capacity=__ret__.storage_capacity,
        tags=__ret__.tags,
        windows_configuration=__ret__.windows_configuration)


@_utilities.lift_output_func(get_file_system)
def get_file_system_output(id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFileSystemResult]:
    """
    Resource Type definition for AWS::FSx::FileSystem
    """
    ...
