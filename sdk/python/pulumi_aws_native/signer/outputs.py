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
    'SigningProfileSignatureValidityPeriod',
    'SigningProfileTag',
]

@pulumi.output_type
class SigningProfileSignatureValidityPeriod(dict):
    def __init__(__self__, *,
                 type: Optional['SigningProfileSignatureValidityPeriodType'] = None,
                 value: Optional[int] = None):
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> Optional['SigningProfileSignatureValidityPeriodType']:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> Optional[int]:
        return pulumi.get(self, "value")


@pulumi.output_type
class SigningProfileTag(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 value: Optional[str] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


