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
    'GetGroupResult',
    'AwaitableGetGroupResult',
    'get_group',
    'get_group_output',
]

@pulumi.output_type
class GetGroupResult:
    def __init__(__self__, filter_expression=None, group_arn=None, group_name=None, insights_configuration=None, tags=None):
        if filter_expression and not isinstance(filter_expression, str):
            raise TypeError("Expected argument 'filter_expression' to be a str")
        pulumi.set(__self__, "filter_expression", filter_expression)
        if group_arn and not isinstance(group_arn, str):
            raise TypeError("Expected argument 'group_arn' to be a str")
        pulumi.set(__self__, "group_arn", group_arn)
        if group_name and not isinstance(group_name, str):
            raise TypeError("Expected argument 'group_name' to be a str")
        pulumi.set(__self__, "group_name", group_name)
        if insights_configuration and not isinstance(insights_configuration, dict):
            raise TypeError("Expected argument 'insights_configuration' to be a dict")
        pulumi.set(__self__, "insights_configuration", insights_configuration)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="filterExpression")
    def filter_expression(self) -> Optional[str]:
        """
        The filter expression defining criteria by which to group traces.
        """
        return pulumi.get(self, "filter_expression")

    @property
    @pulumi.getter(name="groupARN")
    def group_arn(self) -> Optional[str]:
        """
        The ARN of the group that was generated on creation.
        """
        return pulumi.get(self, "group_arn")

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[str]:
        """
        The case-sensitive name of the new group. Names must be unique.
        """
        return pulumi.get(self, "group_name")

    @property
    @pulumi.getter(name="insightsConfiguration")
    def insights_configuration(self) -> Optional['outputs.GroupInsightsConfiguration']:
        return pulumi.get(self, "insights_configuration")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.TagsItemProperties']]:
        return pulumi.get(self, "tags")


class AwaitableGetGroupResult(GetGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupResult(
            filter_expression=self.filter_expression,
            group_arn=self.group_arn,
            group_name=self.group_name,
            insights_configuration=self.insights_configuration,
            tags=self.tags)


def get_group(group_arn: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGroupResult:
    """
    This schema provides construct and validation rules for AWS-XRay Group resource parameters.


    :param str group_arn: The ARN of the group that was generated on creation.
    """
    __args__ = dict()
    __args__['groupARN'] = group_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:xray:getGroup', __args__, opts=opts, typ=GetGroupResult).value

    return AwaitableGetGroupResult(
        filter_expression=__ret__.filter_expression,
        group_arn=__ret__.group_arn,
        group_name=__ret__.group_name,
        insights_configuration=__ret__.insights_configuration,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_group)
def get_group_output(group_arn: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGroupResult]:
    """
    This schema provides construct and validation rules for AWS-XRay Group resource parameters.


    :param str group_arn: The ARN of the group that was generated on creation.
    """
    ...
