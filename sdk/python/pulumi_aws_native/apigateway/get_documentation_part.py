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
    'GetDocumentationPartResult',
    'AwaitableGetDocumentationPartResult',
    'get_documentation_part',
    'get_documentation_part_output',
]

@pulumi.output_type
class GetDocumentationPartResult:
    def __init__(__self__, documentation_part_id=None, properties=None):
        if documentation_part_id and not isinstance(documentation_part_id, str):
            raise TypeError("Expected argument 'documentation_part_id' to be a str")
        pulumi.set(__self__, "documentation_part_id", documentation_part_id)
        if properties and not isinstance(properties, str):
            raise TypeError("Expected argument 'properties' to be a str")
        pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter(name="documentationPartId")
    def documentation_part_id(self) -> Optional[str]:
        """
        The identifier of the documentation Part.
        """
        return pulumi.get(self, "documentation_part_id")

    @property
    @pulumi.getter
    def properties(self) -> Optional[str]:
        """
        The documentation content map of the targeted API entity.
        """
        return pulumi.get(self, "properties")


class AwaitableGetDocumentationPartResult(GetDocumentationPartResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDocumentationPartResult(
            documentation_part_id=self.documentation_part_id,
            properties=self.properties)


def get_documentation_part(documentation_part_id: Optional[str] = None,
                           rest_api_id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDocumentationPartResult:
    """
    Resource Type definition for AWS::ApiGateway::DocumentationPart


    :param str documentation_part_id: The identifier of the documentation Part.
    :param str rest_api_id: Identifier of the targeted API entity
    """
    __args__ = dict()
    __args__['documentationPartId'] = documentation_part_id
    __args__['restApiId'] = rest_api_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:apigateway:getDocumentationPart', __args__, opts=opts, typ=GetDocumentationPartResult).value

    return AwaitableGetDocumentationPartResult(
        documentation_part_id=__ret__.documentation_part_id,
        properties=__ret__.properties)


@_utilities.lift_output_func(get_documentation_part)
def get_documentation_part_output(documentation_part_id: Optional[pulumi.Input[str]] = None,
                                  rest_api_id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDocumentationPartResult]:
    """
    Resource Type definition for AWS::ApiGateway::DocumentationPart


    :param str documentation_part_id: The identifier of the documentation Part.
    :param str rest_api_id: Identifier of the targeted API entity
    """
    ...
