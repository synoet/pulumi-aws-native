# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'NamespaceTagArgs',
    'WorkgroupConfigParameterArgs',
    'WorkgroupTagArgs',
]

@pulumi.input_type
class NamespaceTagArgs:
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
class WorkgroupConfigParameterArgs:
    def __init__(__self__, *,
                 parameter_key: Optional[pulumi.Input[str]] = None,
                 parameter_value: Optional[pulumi.Input[str]] = None):
        if parameter_key is not None:
            pulumi.set(__self__, "parameter_key", parameter_key)
        if parameter_value is not None:
            pulumi.set(__self__, "parameter_value", parameter_value)

    @property
    @pulumi.getter(name="parameterKey")
    def parameter_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "parameter_key")

    @parameter_key.setter
    def parameter_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameter_key", value)

    @property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "parameter_value")

    @parameter_value.setter
    def parameter_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameter_value", value)


@pulumi.input_type
class WorkgroupTagArgs:
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


