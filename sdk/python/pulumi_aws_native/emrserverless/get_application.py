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
    'GetApplicationResult',
    'AwaitableGetApplicationResult',
    'get_application',
    'get_application_output',
]

@pulumi.output_type
class GetApplicationResult:
    def __init__(__self__, application_id=None, arn=None, auto_start_configuration=None, auto_stop_configuration=None, initial_capacity=None, maximum_capacity=None, network_configuration=None, tags=None):
        if application_id and not isinstance(application_id, str):
            raise TypeError("Expected argument 'application_id' to be a str")
        pulumi.set(__self__, "application_id", application_id)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if auto_start_configuration and not isinstance(auto_start_configuration, dict):
            raise TypeError("Expected argument 'auto_start_configuration' to be a dict")
        pulumi.set(__self__, "auto_start_configuration", auto_start_configuration)
        if auto_stop_configuration and not isinstance(auto_stop_configuration, dict):
            raise TypeError("Expected argument 'auto_stop_configuration' to be a dict")
        pulumi.set(__self__, "auto_stop_configuration", auto_stop_configuration)
        if initial_capacity and not isinstance(initial_capacity, list):
            raise TypeError("Expected argument 'initial_capacity' to be a list")
        pulumi.set(__self__, "initial_capacity", initial_capacity)
        if maximum_capacity and not isinstance(maximum_capacity, dict):
            raise TypeError("Expected argument 'maximum_capacity' to be a dict")
        pulumi.set(__self__, "maximum_capacity", maximum_capacity)
        if network_configuration and not isinstance(network_configuration, dict):
            raise TypeError("Expected argument 'network_configuration' to be a dict")
        pulumi.set(__self__, "network_configuration", network_configuration)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[str]:
        """
        The ID of the EMR Serverless Application.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the EMR Serverless Application.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="autoStartConfiguration")
    def auto_start_configuration(self) -> Optional['outputs.ApplicationAutoStartConfiguration']:
        """
        Configuration for Auto Start of Application.
        """
        return pulumi.get(self, "auto_start_configuration")

    @property
    @pulumi.getter(name="autoStopConfiguration")
    def auto_stop_configuration(self) -> Optional['outputs.ApplicationAutoStopConfiguration']:
        """
        Configuration for Auto Stop of Application.
        """
        return pulumi.get(self, "auto_stop_configuration")

    @property
    @pulumi.getter(name="initialCapacity")
    def initial_capacity(self) -> Optional[Sequence['outputs.ApplicationInitialCapacityConfigKeyValuePair']]:
        """
        Initial capacity initialized when an Application is started.
        """
        return pulumi.get(self, "initial_capacity")

    @property
    @pulumi.getter(name="maximumCapacity")
    def maximum_capacity(self) -> Optional['outputs.ApplicationMaximumAllowedResources']:
        """
        Maximum allowed cumulative resources for an Application. No new resources will be created once the limit is hit.
        """
        return pulumi.get(self, "maximum_capacity")

    @property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional['outputs.ApplicationNetworkConfiguration']:
        """
        Network Configuration for customer VPC connectivity.
        """
        return pulumi.get(self, "network_configuration")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ApplicationTag']]:
        """
        Tag map with key and value
        """
        return pulumi.get(self, "tags")


class AwaitableGetApplicationResult(GetApplicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationResult(
            application_id=self.application_id,
            arn=self.arn,
            auto_start_configuration=self.auto_start_configuration,
            auto_stop_configuration=self.auto_stop_configuration,
            initial_capacity=self.initial_capacity,
            maximum_capacity=self.maximum_capacity,
            network_configuration=self.network_configuration,
            tags=self.tags)


def get_application(application_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationResult:
    """
    Resource schema for AWS::EMRServerless::Application Type


    :param str application_id: The ID of the EMR Serverless Application.
    """
    __args__ = dict()
    __args__['applicationId'] = application_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:emrserverless:getApplication', __args__, opts=opts, typ=GetApplicationResult).value

    return AwaitableGetApplicationResult(
        application_id=__ret__.application_id,
        arn=__ret__.arn,
        auto_start_configuration=__ret__.auto_start_configuration,
        auto_stop_configuration=__ret__.auto_stop_configuration,
        initial_capacity=__ret__.initial_capacity,
        maximum_capacity=__ret__.maximum_capacity,
        network_configuration=__ret__.network_configuration,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_application)
def get_application_output(application_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationResult]:
    """
    Resource schema for AWS::EMRServerless::Application Type


    :param str application_id: The ID of the EMR Serverless Application.
    """
    ...
