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
    'GetBudgetsActionResult',
    'AwaitableGetBudgetsActionResult',
    'get_budgets_action',
    'get_budgets_action_output',
]

@pulumi.output_type
class GetBudgetsActionResult:
    def __init__(__self__, action_id=None, action_threshold=None, approval_model=None, definition=None, execution_role_arn=None, notification_type=None, subscribers=None):
        if action_id and not isinstance(action_id, str):
            raise TypeError("Expected argument 'action_id' to be a str")
        pulumi.set(__self__, "action_id", action_id)
        if action_threshold and not isinstance(action_threshold, dict):
            raise TypeError("Expected argument 'action_threshold' to be a dict")
        pulumi.set(__self__, "action_threshold", action_threshold)
        if approval_model and not isinstance(approval_model, str):
            raise TypeError("Expected argument 'approval_model' to be a str")
        pulumi.set(__self__, "approval_model", approval_model)
        if definition and not isinstance(definition, dict):
            raise TypeError("Expected argument 'definition' to be a dict")
        pulumi.set(__self__, "definition", definition)
        if execution_role_arn and not isinstance(execution_role_arn, str):
            raise TypeError("Expected argument 'execution_role_arn' to be a str")
        pulumi.set(__self__, "execution_role_arn", execution_role_arn)
        if notification_type and not isinstance(notification_type, str):
            raise TypeError("Expected argument 'notification_type' to be a str")
        pulumi.set(__self__, "notification_type", notification_type)
        if subscribers and not isinstance(subscribers, list):
            raise TypeError("Expected argument 'subscribers' to be a list")
        pulumi.set(__self__, "subscribers", subscribers)

    @property
    @pulumi.getter(name="actionId")
    def action_id(self) -> Optional[str]:
        return pulumi.get(self, "action_id")

    @property
    @pulumi.getter(name="actionThreshold")
    def action_threshold(self) -> Optional['outputs.BudgetsActionActionThreshold']:
        return pulumi.get(self, "action_threshold")

    @property
    @pulumi.getter(name="approvalModel")
    def approval_model(self) -> Optional['BudgetsActionApprovalModel']:
        return pulumi.get(self, "approval_model")

    @property
    @pulumi.getter
    def definition(self) -> Optional['outputs.BudgetsActionDefinition']:
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[str]:
        return pulumi.get(self, "execution_role_arn")

    @property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> Optional['BudgetsActionNotificationType']:
        return pulumi.get(self, "notification_type")

    @property
    @pulumi.getter
    def subscribers(self) -> Optional[Sequence['outputs.BudgetsActionSubscriber']]:
        return pulumi.get(self, "subscribers")


class AwaitableGetBudgetsActionResult(GetBudgetsActionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBudgetsActionResult(
            action_id=self.action_id,
            action_threshold=self.action_threshold,
            approval_model=self.approval_model,
            definition=self.definition,
            execution_role_arn=self.execution_role_arn,
            notification_type=self.notification_type,
            subscribers=self.subscribers)


def get_budgets_action(action_id: Optional[str] = None,
                       budget_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBudgetsActionResult:
    """
    An example resource schema demonstrating some basic constructs and validation rules.
    """
    __args__ = dict()
    __args__['actionId'] = action_id
    __args__['budgetName'] = budget_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:budgets:getBudgetsAction', __args__, opts=opts, typ=GetBudgetsActionResult).value

    return AwaitableGetBudgetsActionResult(
        action_id=__ret__.action_id,
        action_threshold=__ret__.action_threshold,
        approval_model=__ret__.approval_model,
        definition=__ret__.definition,
        execution_role_arn=__ret__.execution_role_arn,
        notification_type=__ret__.notification_type,
        subscribers=__ret__.subscribers)


@_utilities.lift_output_func(get_budgets_action)
def get_budgets_action_output(action_id: Optional[pulumi.Input[str]] = None,
                              budget_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBudgetsActionResult]:
    """
    An example resource schema demonstrating some basic constructs and validation rules.
    """
    ...
