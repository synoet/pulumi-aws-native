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
    'GetSchemaResult',
    'AwaitableGetSchemaResult',
    'get_schema',
    'get_schema_output',
]

@pulumi.output_type
class GetSchemaResult:
    def __init__(__self__, schema_arn=None):
        if schema_arn and not isinstance(schema_arn, str):
            raise TypeError("Expected argument 'schema_arn' to be a str")
        pulumi.set(__self__, "schema_arn", schema_arn)

    @property
    @pulumi.getter(name="schemaArn")
    def schema_arn(self) -> Optional[str]:
        """
        Arn for the schema.
        """
        return pulumi.get(self, "schema_arn")


class AwaitableGetSchemaResult(GetSchemaResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSchemaResult(
            schema_arn=self.schema_arn)


def get_schema(schema_arn: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSchemaResult:
    """
    Resource schema for AWS::Personalize::Schema.


    :param str schema_arn: Arn for the schema.
    """
    __args__ = dict()
    __args__['schemaArn'] = schema_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:personalize:getSchema', __args__, opts=opts, typ=GetSchemaResult).value

    return AwaitableGetSchemaResult(
        schema_arn=__ret__.schema_arn)


@_utilities.lift_output_func(get_schema)
def get_schema_output(schema_arn: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSchemaResult]:
    """
    Resource schema for AWS::Personalize::Schema.


    :param str schema_arn: Arn for the schema.
    """
    ...
