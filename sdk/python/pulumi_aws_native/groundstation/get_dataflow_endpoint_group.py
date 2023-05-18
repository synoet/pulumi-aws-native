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
from ._enums import *

__all__ = [
    'GetDataflowEndpointGroupResult',
    'AwaitableGetDataflowEndpointGroupResult',
    'get_dataflow_endpoint_group',
    'get_dataflow_endpoint_group_output',
]

@pulumi.output_type
class GetDataflowEndpointGroupResult:
    def __init__(__self__, arn=None, contact_post_pass_duration_seconds=None, contact_pre_pass_duration_seconds=None, endpoint_details=None, id=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if contact_post_pass_duration_seconds and not isinstance(contact_post_pass_duration_seconds, int):
            raise TypeError("Expected argument 'contact_post_pass_duration_seconds' to be a int")
        pulumi.set(__self__, "contact_post_pass_duration_seconds", contact_post_pass_duration_seconds)
        if contact_pre_pass_duration_seconds and not isinstance(contact_pre_pass_duration_seconds, int):
            raise TypeError("Expected argument 'contact_pre_pass_duration_seconds' to be a int")
        pulumi.set(__self__, "contact_pre_pass_duration_seconds", contact_pre_pass_duration_seconds)
        if endpoint_details and not isinstance(endpoint_details, list):
            raise TypeError("Expected argument 'endpoint_details' to be a list")
        pulumi.set(__self__, "endpoint_details", endpoint_details)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="contactPostPassDurationSeconds")
    def contact_post_pass_duration_seconds(self) -> Optional[int]:
        """
        Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a POSTPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the POSTPASS state.
        """
        return pulumi.get(self, "contact_post_pass_duration_seconds")

    @property
    @pulumi.getter(name="contactPrePassDurationSeconds")
    def contact_pre_pass_duration_seconds(self) -> Optional[int]:
        """
        Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a PREPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the PREPASS state.
        """
        return pulumi.get(self, "contact_pre_pass_duration_seconds")

    @property
    @pulumi.getter(name="endpointDetails")
    def endpoint_details(self) -> Optional[Sequence['outputs.DataflowEndpointGroupEndpointDetails']]:
        return pulumi.get(self, "endpoint_details")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DataflowEndpointGroupTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetDataflowEndpointGroupResult(GetDataflowEndpointGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataflowEndpointGroupResult(
            arn=self.arn,
            contact_post_pass_duration_seconds=self.contact_post_pass_duration_seconds,
            contact_pre_pass_duration_seconds=self.contact_pre_pass_duration_seconds,
            endpoint_details=self.endpoint_details,
            id=self.id,
            tags=self.tags)


def get_dataflow_endpoint_group(id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataflowEndpointGroupResult:
    """
    AWS Ground Station DataflowEndpointGroup schema for CloudFormation
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:groundstation:getDataflowEndpointGroup', __args__, opts=opts, typ=GetDataflowEndpointGroupResult).value

    return AwaitableGetDataflowEndpointGroupResult(
        arn=__ret__.arn,
        contact_post_pass_duration_seconds=__ret__.contact_post_pass_duration_seconds,
        contact_pre_pass_duration_seconds=__ret__.contact_pre_pass_duration_seconds,
        endpoint_details=__ret__.endpoint_details,
        id=__ret__.id,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_dataflow_endpoint_group)
def get_dataflow_endpoint_group_output(id: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDataflowEndpointGroupResult]:
    """
    AWS Ground Station DataflowEndpointGroup schema for CloudFormation
    """
    ...
