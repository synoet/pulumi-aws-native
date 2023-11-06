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
    'GetResourceResult',
    'AwaitableGetResourceResult',
    'get_resource',
    'get_resource_output',
]

@pulumi.output_type
class GetResourceResult:
    def __init__(__self__, resource_id=None):
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        return pulumi.get(self, "resource_id")


class AwaitableGetResourceResult(GetResourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourceResult(
            resource_id=self.resource_id)


def get_resource(resource_id: Optional[str] = None,
                 rest_api_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourceResult:
    """
    The ``AWS::ApiGateway::Resource`` resource creates a resource in an API.


    :param str rest_api_id: The string identifier of the associated RestApi.
    """
    __args__ = dict()
    __args__['resourceId'] = resource_id
    __args__['restApiId'] = rest_api_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:apigateway:getResource', __args__, opts=opts, typ=GetResourceResult).value

    return AwaitableGetResourceResult(
        resource_id=pulumi.get(__ret__, 'resource_id'))


@_utilities.lift_output_func(get_resource)
def get_resource_output(resource_id: Optional[pulumi.Input[str]] = None,
                        rest_api_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourceResult]:
    """
    The ``AWS::ApiGateway::Resource`` resource creates a resource in an API.


    :param str rest_api_id: The string identifier of the associated RestApi.
    """
    ...
