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
    'AccessPointCreationInfoArgs',
    'AccessPointPosixUserArgs',
    'AccessPointRootDirectoryArgs',
    'AccessPointTagArgs',
    'FileSystemBackupPolicyArgs',
    'FileSystemElasticFileSystemTagArgs',
    'FileSystemLifecyclePolicyArgs',
]

@pulumi.input_type
class AccessPointCreationInfoArgs:
    def __init__(__self__, *,
                 owner_gid: pulumi.Input[str],
                 owner_uid: pulumi.Input[str],
                 permissions: pulumi.Input[str]):
        """
        :param pulumi.Input[str] owner_gid: Specifies the POSIX group ID to apply to the RootDirectory. Accepts values from 0 to 2^32 (4294967295).
        :param pulumi.Input[str] owner_uid: Specifies the POSIX user ID to apply to the RootDirectory. Accepts values from 0 to 2^32 (4294967295).
        :param pulumi.Input[str] permissions: Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.
        """
        pulumi.set(__self__, "owner_gid", owner_gid)
        pulumi.set(__self__, "owner_uid", owner_uid)
        pulumi.set(__self__, "permissions", permissions)

    @property
    @pulumi.getter(name="ownerGid")
    def owner_gid(self) -> pulumi.Input[str]:
        """
        Specifies the POSIX group ID to apply to the RootDirectory. Accepts values from 0 to 2^32 (4294967295).
        """
        return pulumi.get(self, "owner_gid")

    @owner_gid.setter
    def owner_gid(self, value: pulumi.Input[str]):
        pulumi.set(self, "owner_gid", value)

    @property
    @pulumi.getter(name="ownerUid")
    def owner_uid(self) -> pulumi.Input[str]:
        """
        Specifies the POSIX user ID to apply to the RootDirectory. Accepts values from 0 to 2^32 (4294967295).
        """
        return pulumi.get(self, "owner_uid")

    @owner_uid.setter
    def owner_uid(self, value: pulumi.Input[str]):
        pulumi.set(self, "owner_uid", value)

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Input[str]:
        """
        Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: pulumi.Input[str]):
        pulumi.set(self, "permissions", value)


@pulumi.input_type
class AccessPointPosixUserArgs:
    def __init__(__self__, *,
                 gid: pulumi.Input[str],
                 uid: pulumi.Input[str],
                 secondary_gids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] gid: The POSIX group ID used for all file system operations using this access point.
        :param pulumi.Input[str] uid: The POSIX user ID used for all file system operations using this access point.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] secondary_gids: Secondary POSIX group IDs used for all file system operations using this access point.
        """
        pulumi.set(__self__, "gid", gid)
        pulumi.set(__self__, "uid", uid)
        if secondary_gids is not None:
            pulumi.set(__self__, "secondary_gids", secondary_gids)

    @property
    @pulumi.getter
    def gid(self) -> pulumi.Input[str]:
        """
        The POSIX group ID used for all file system operations using this access point.
        """
        return pulumi.get(self, "gid")

    @gid.setter
    def gid(self, value: pulumi.Input[str]):
        pulumi.set(self, "gid", value)

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Input[str]:
        """
        The POSIX user ID used for all file system operations using this access point.
        """
        return pulumi.get(self, "uid")

    @uid.setter
    def uid(self, value: pulumi.Input[str]):
        pulumi.set(self, "uid", value)

    @property
    @pulumi.getter(name="secondaryGids")
    def secondary_gids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Secondary POSIX group IDs used for all file system operations using this access point.
        """
        return pulumi.get(self, "secondary_gids")

    @secondary_gids.setter
    def secondary_gids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "secondary_gids", value)


@pulumi.input_type
class AccessPointRootDirectoryArgs:
    def __init__(__self__, *,
                 creation_info: Optional[pulumi.Input['AccessPointCreationInfoArgs']] = None,
                 path: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input['AccessPointCreationInfoArgs'] creation_info: (Optional) Specifies the POSIX IDs and permissions to apply to the access point's RootDirectory. If the RootDirectory>Path specified does not exist, EFS creates the root directory using the CreationInfo settings when a client connects to an access point. When specifying the CreationInfo, you must provide values for all properties.   If you do not provide CreationInfo and the specified RootDirectory>Path does not exist, attempts to mount the file system using the access point will fail. 
        :param pulumi.Input[str] path: Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide the CreationInfo.
        """
        if creation_info is not None:
            pulumi.set(__self__, "creation_info", creation_info)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter(name="creationInfo")
    def creation_info(self) -> Optional[pulumi.Input['AccessPointCreationInfoArgs']]:
        """
        (Optional) Specifies the POSIX IDs and permissions to apply to the access point's RootDirectory. If the RootDirectory>Path specified does not exist, EFS creates the root directory using the CreationInfo settings when a client connects to an access point. When specifying the CreationInfo, you must provide values for all properties.   If you do not provide CreationInfo and the specified RootDirectory>Path does not exist, attempts to mount the file system using the access point will fail. 
        """
        return pulumi.get(self, "creation_info")

    @creation_info.setter
    def creation_info(self, value: Optional[pulumi.Input['AccessPointCreationInfoArgs']]):
        pulumi.set(self, "creation_info", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide the CreationInfo.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)


@pulumi.input_type
class AccessPointTagArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class FileSystemBackupPolicyArgs:
    def __init__(__self__, *,
                 status: pulumi.Input[str]):
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input[str]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input[str]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class FileSystemElasticFileSystemTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class FileSystemLifecyclePolicyArgs:
    def __init__(__self__, *,
                 transition_to_ia: Optional[pulumi.Input[str]] = None,
                 transition_to_primary_storage_class: Optional[pulumi.Input[str]] = None):
        if transition_to_ia is not None:
            pulumi.set(__self__, "transition_to_ia", transition_to_ia)
        if transition_to_primary_storage_class is not None:
            pulumi.set(__self__, "transition_to_primary_storage_class", transition_to_primary_storage_class)

    @property
    @pulumi.getter(name="transitionToIa")
    def transition_to_ia(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "transition_to_ia")

    @transition_to_ia.setter
    def transition_to_ia(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transition_to_ia", value)

    @property
    @pulumi.getter(name="transitionToPrimaryStorageClass")
    def transition_to_primary_storage_class(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "transition_to_primary_storage_class")

    @transition_to_primary_storage_class.setter
    def transition_to_primary_storage_class(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transition_to_primary_storage_class", value)


