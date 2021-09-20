# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'BudgetsActionActionThreshold',
    'BudgetsActionDefinition',
    'BudgetsActionIamActionDefinition',
    'BudgetsActionScpActionDefinition',
    'BudgetsActionSsmActionDefinition',
    'BudgetsActionSubscriber',
]

@pulumi.output_type
class BudgetsActionActionThreshold(dict):
    def __init__(__self__, *,
                 type: 'BudgetsActionActionThresholdType',
                 value: float):
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> 'BudgetsActionActionThresholdType':
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> float:
        return pulumi.get(self, "value")


@pulumi.output_type
class BudgetsActionDefinition(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "iamActionDefinition":
            suggest = "iam_action_definition"
        elif key == "scpActionDefinition":
            suggest = "scp_action_definition"
        elif key == "ssmActionDefinition":
            suggest = "ssm_action_definition"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BudgetsActionDefinition. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BudgetsActionDefinition.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BudgetsActionDefinition.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 iam_action_definition: Optional['outputs.BudgetsActionIamActionDefinition'] = None,
                 scp_action_definition: Optional['outputs.BudgetsActionScpActionDefinition'] = None,
                 ssm_action_definition: Optional['outputs.BudgetsActionSsmActionDefinition'] = None):
        if iam_action_definition is not None:
            pulumi.set(__self__, "iam_action_definition", iam_action_definition)
        if scp_action_definition is not None:
            pulumi.set(__self__, "scp_action_definition", scp_action_definition)
        if ssm_action_definition is not None:
            pulumi.set(__self__, "ssm_action_definition", ssm_action_definition)

    @property
    @pulumi.getter(name="iamActionDefinition")
    def iam_action_definition(self) -> Optional['outputs.BudgetsActionIamActionDefinition']:
        return pulumi.get(self, "iam_action_definition")

    @property
    @pulumi.getter(name="scpActionDefinition")
    def scp_action_definition(self) -> Optional['outputs.BudgetsActionScpActionDefinition']:
        return pulumi.get(self, "scp_action_definition")

    @property
    @pulumi.getter(name="ssmActionDefinition")
    def ssm_action_definition(self) -> Optional['outputs.BudgetsActionSsmActionDefinition']:
        return pulumi.get(self, "ssm_action_definition")


@pulumi.output_type
class BudgetsActionIamActionDefinition(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "policyArn":
            suggest = "policy_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BudgetsActionIamActionDefinition. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BudgetsActionIamActionDefinition.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BudgetsActionIamActionDefinition.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 policy_arn: str,
                 groups: Optional[Sequence[str]] = None,
                 roles: Optional[Sequence[str]] = None,
                 users: Optional[Sequence[str]] = None):
        pulumi.set(__self__, "policy_arn", policy_arn)
        if groups is not None:
            pulumi.set(__self__, "groups", groups)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)
        if users is not None:
            pulumi.set(__self__, "users", users)

    @property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> str:
        return pulumi.get(self, "policy_arn")

    @property
    @pulumi.getter
    def groups(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def users(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "users")


@pulumi.output_type
class BudgetsActionScpActionDefinition(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "policyId":
            suggest = "policy_id"
        elif key == "targetIds":
            suggest = "target_ids"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BudgetsActionScpActionDefinition. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BudgetsActionScpActionDefinition.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BudgetsActionScpActionDefinition.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 policy_id: str,
                 target_ids: Sequence[str]):
        pulumi.set(__self__, "policy_id", policy_id)
        pulumi.set(__self__, "target_ids", target_ids)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> str:
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter(name="targetIds")
    def target_ids(self) -> Sequence[str]:
        return pulumi.get(self, "target_ids")


@pulumi.output_type
class BudgetsActionSsmActionDefinition(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "instanceIds":
            suggest = "instance_ids"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BudgetsActionSsmActionDefinition. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BudgetsActionSsmActionDefinition.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BudgetsActionSsmActionDefinition.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 instance_ids: Sequence[str],
                 region: str,
                 subtype: 'BudgetsActionSsmActionDefinitionSubtype'):
        pulumi.set(__self__, "instance_ids", instance_ids)
        pulumi.set(__self__, "region", region)
        pulumi.set(__self__, "subtype", subtype)

    @property
    @pulumi.getter(name="instanceIds")
    def instance_ids(self) -> Sequence[str]:
        return pulumi.get(self, "instance_ids")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def subtype(self) -> 'BudgetsActionSsmActionDefinitionSubtype':
        return pulumi.get(self, "subtype")


@pulumi.output_type
class BudgetsActionSubscriber(dict):
    def __init__(__self__, *,
                 address: str,
                 type: 'BudgetsActionSubscriberType'):
        pulumi.set(__self__, "address", address)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def address(self) -> str:
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def type(self) -> 'BudgetsActionSubscriberType':
        return pulumi.get(self, "type")


