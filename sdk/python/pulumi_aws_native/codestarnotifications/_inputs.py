# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'NotificationRuleTargetArgs',
]

@pulumi.input_type
class NotificationRuleTargetArgs:
    def __init__(__self__, *,
                 target_address: pulumi.Input[str],
                 target_type: pulumi.Input[str]):
        pulumi.set(__self__, "target_address", target_address)
        pulumi.set(__self__, "target_type", target_type)

    @property
    @pulumi.getter(name="targetAddress")
    def target_address(self) -> pulumi.Input[str]:
        return pulumi.get(self, "target_address")

    @target_address.setter
    def target_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_address", value)

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "target_type")

    @target_type.setter
    def target_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_type", value)


