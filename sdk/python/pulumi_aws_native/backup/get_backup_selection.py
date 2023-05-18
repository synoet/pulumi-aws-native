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
    'GetBackupSelectionResult',
    'AwaitableGetBackupSelectionResult',
    'get_backup_selection',
    'get_backup_selection_output',
]

@pulumi.output_type
class GetBackupSelectionResult:
    def __init__(__self__, id=None, selection_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if selection_id and not isinstance(selection_id, str):
            raise TypeError("Expected argument 'selection_id' to be a str")
        pulumi.set(__self__, "selection_id", selection_id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="selectionId")
    def selection_id(self) -> Optional[str]:
        return pulumi.get(self, "selection_id")


class AwaitableGetBackupSelectionResult(GetBackupSelectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBackupSelectionResult(
            id=self.id,
            selection_id=self.selection_id)


def get_backup_selection(id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBackupSelectionResult:
    """
    Resource Type definition for AWS::Backup::BackupSelection
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:backup:getBackupSelection', __args__, opts=opts, typ=GetBackupSelectionResult).value

    return AwaitableGetBackupSelectionResult(
        id=__ret__.id,
        selection_id=__ret__.selection_id)


@_utilities.lift_output_func(get_backup_selection)
def get_backup_selection_output(id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBackupSelectionResult]:
    """
    Resource Type definition for AWS::Backup::BackupSelection
    """
    ...
