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
    'GetEventInvokeConfigResult',
    'AwaitableGetEventInvokeConfigResult',
    'get_event_invoke_config',
    'get_event_invoke_config_output',
]

@pulumi.output_type
class GetEventInvokeConfigResult:
    def __init__(__self__, destination_config=None, id=None, maximum_event_age_in_seconds=None, maximum_retry_attempts=None):
        if destination_config and not isinstance(destination_config, dict):
            raise TypeError("Expected argument 'destination_config' to be a dict")
        pulumi.set(__self__, "destination_config", destination_config)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if maximum_event_age_in_seconds and not isinstance(maximum_event_age_in_seconds, int):
            raise TypeError("Expected argument 'maximum_event_age_in_seconds' to be a int")
        pulumi.set(__self__, "maximum_event_age_in_seconds", maximum_event_age_in_seconds)
        if maximum_retry_attempts and not isinstance(maximum_retry_attempts, int):
            raise TypeError("Expected argument 'maximum_retry_attempts' to be a int")
        pulumi.set(__self__, "maximum_retry_attempts", maximum_retry_attempts)

    @property
    @pulumi.getter(name="destinationConfig")
    def destination_config(self) -> Optional['outputs.EventInvokeConfigDestinationConfig']:
        return pulumi.get(self, "destination_config")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> Optional[int]:
        return pulumi.get(self, "maximum_event_age_in_seconds")

    @property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> Optional[int]:
        return pulumi.get(self, "maximum_retry_attempts")


class AwaitableGetEventInvokeConfigResult(GetEventInvokeConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEventInvokeConfigResult(
            destination_config=self.destination_config,
            id=self.id,
            maximum_event_age_in_seconds=self.maximum_event_age_in_seconds,
            maximum_retry_attempts=self.maximum_retry_attempts)


def get_event_invoke_config(id: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEventInvokeConfigResult:
    """
    Resource Type definition for AWS::Lambda::EventInvokeConfig
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:lambda:getEventInvokeConfig', __args__, opts=opts, typ=GetEventInvokeConfigResult).value

    return AwaitableGetEventInvokeConfigResult(
        destination_config=__ret__.destination_config,
        id=__ret__.id,
        maximum_event_age_in_seconds=__ret__.maximum_event_age_in_seconds,
        maximum_retry_attempts=__ret__.maximum_retry_attempts)


@_utilities.lift_output_func(get_event_invoke_config)
def get_event_invoke_config_output(id: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEventInvokeConfigResult]:
    """
    Resource Type definition for AWS::Lambda::EventInvokeConfig
    """
    ...
