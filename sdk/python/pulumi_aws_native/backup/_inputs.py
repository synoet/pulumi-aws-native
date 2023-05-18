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
    'BackupPlanAdvancedBackupSettingResourceTypeArgs',
    'BackupPlanBackupRuleResourceTypeArgs',
    'BackupPlanCopyActionResourceTypeArgs',
    'BackupPlanLifecycleResourceTypeArgs',
    'BackupPlanResourceTypeArgs',
    'BackupSelectionConditionParameterArgs',
    'BackupSelectionConditionResourceTypeArgs',
    'BackupSelectionResourceTypeConditionsPropertiesArgs',
    'BackupSelectionResourceTypeArgs',
    'BackupVaultLockConfigurationTypeArgs',
    'BackupVaultNotificationObjectTypeArgs',
    'FrameworkControlControlScopePropertiesArgs',
    'FrameworkControlInputParameterArgs',
    'FrameworkControlArgs',
    'FrameworkTagArgs',
    'ReportDeliveryChannelPropertiesArgs',
    'ReportPlanTagArgs',
    'ReportSettingPropertiesArgs',
]

@pulumi.input_type
class BackupPlanAdvancedBackupSettingResourceTypeArgs:
    def __init__(__self__, *,
                 backup_options: Any,
                 resource_type: pulumi.Input[str]):
        pulumi.set(__self__, "backup_options", backup_options)
        pulumi.set(__self__, "resource_type", resource_type)

    @property
    @pulumi.getter(name="backupOptions")
    def backup_options(self) -> Any:
        return pulumi.get(self, "backup_options")

    @backup_options.setter
    def backup_options(self, value: Any):
        pulumi.set(self, "backup_options", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_type", value)


@pulumi.input_type
class BackupPlanBackupRuleResourceTypeArgs:
    def __init__(__self__, *,
                 rule_name: pulumi.Input[str],
                 target_backup_vault: pulumi.Input[str],
                 completion_window_minutes: Optional[pulumi.Input[float]] = None,
                 copy_actions: Optional[pulumi.Input[Sequence[pulumi.Input['BackupPlanCopyActionResourceTypeArgs']]]] = None,
                 enable_continuous_backup: Optional[pulumi.Input[bool]] = None,
                 lifecycle: Optional[pulumi.Input['BackupPlanLifecycleResourceTypeArgs']] = None,
                 recovery_point_tags: Optional[Any] = None,
                 schedule_expression: Optional[pulumi.Input[str]] = None,
                 start_window_minutes: Optional[pulumi.Input[float]] = None):
        pulumi.set(__self__, "rule_name", rule_name)
        pulumi.set(__self__, "target_backup_vault", target_backup_vault)
        if completion_window_minutes is not None:
            pulumi.set(__self__, "completion_window_minutes", completion_window_minutes)
        if copy_actions is not None:
            pulumi.set(__self__, "copy_actions", copy_actions)
        if enable_continuous_backup is not None:
            pulumi.set(__self__, "enable_continuous_backup", enable_continuous_backup)
        if lifecycle is not None:
            pulumi.set(__self__, "lifecycle", lifecycle)
        if recovery_point_tags is not None:
            pulumi.set(__self__, "recovery_point_tags", recovery_point_tags)
        if schedule_expression is not None:
            pulumi.set(__self__, "schedule_expression", schedule_expression)
        if start_window_minutes is not None:
            pulumi.set(__self__, "start_window_minutes", start_window_minutes)

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "rule_name")

    @rule_name.setter
    def rule_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "rule_name", value)

    @property
    @pulumi.getter(name="targetBackupVault")
    def target_backup_vault(self) -> pulumi.Input[str]:
        return pulumi.get(self, "target_backup_vault")

    @target_backup_vault.setter
    def target_backup_vault(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_backup_vault", value)

    @property
    @pulumi.getter(name="completionWindowMinutes")
    def completion_window_minutes(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "completion_window_minutes")

    @completion_window_minutes.setter
    def completion_window_minutes(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "completion_window_minutes", value)

    @property
    @pulumi.getter(name="copyActions")
    def copy_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BackupPlanCopyActionResourceTypeArgs']]]]:
        return pulumi.get(self, "copy_actions")

    @copy_actions.setter
    def copy_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BackupPlanCopyActionResourceTypeArgs']]]]):
        pulumi.set(self, "copy_actions", value)

    @property
    @pulumi.getter(name="enableContinuousBackup")
    def enable_continuous_backup(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_continuous_backup")

    @enable_continuous_backup.setter
    def enable_continuous_backup(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_continuous_backup", value)

    @property
    @pulumi.getter
    def lifecycle(self) -> Optional[pulumi.Input['BackupPlanLifecycleResourceTypeArgs']]:
        return pulumi.get(self, "lifecycle")

    @lifecycle.setter
    def lifecycle(self, value: Optional[pulumi.Input['BackupPlanLifecycleResourceTypeArgs']]):
        pulumi.set(self, "lifecycle", value)

    @property
    @pulumi.getter(name="recoveryPointTags")
    def recovery_point_tags(self) -> Optional[Any]:
        return pulumi.get(self, "recovery_point_tags")

    @recovery_point_tags.setter
    def recovery_point_tags(self, value: Optional[Any]):
        pulumi.set(self, "recovery_point_tags", value)

    @property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "schedule_expression")

    @schedule_expression.setter
    def schedule_expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schedule_expression", value)

    @property
    @pulumi.getter(name="startWindowMinutes")
    def start_window_minutes(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "start_window_minutes")

    @start_window_minutes.setter
    def start_window_minutes(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "start_window_minutes", value)


@pulumi.input_type
class BackupPlanCopyActionResourceTypeArgs:
    def __init__(__self__, *,
                 destination_backup_vault_arn: pulumi.Input[str],
                 lifecycle: Optional[pulumi.Input['BackupPlanLifecycleResourceTypeArgs']] = None):
        pulumi.set(__self__, "destination_backup_vault_arn", destination_backup_vault_arn)
        if lifecycle is not None:
            pulumi.set(__self__, "lifecycle", lifecycle)

    @property
    @pulumi.getter(name="destinationBackupVaultArn")
    def destination_backup_vault_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "destination_backup_vault_arn")

    @destination_backup_vault_arn.setter
    def destination_backup_vault_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination_backup_vault_arn", value)

    @property
    @pulumi.getter
    def lifecycle(self) -> Optional[pulumi.Input['BackupPlanLifecycleResourceTypeArgs']]:
        return pulumi.get(self, "lifecycle")

    @lifecycle.setter
    def lifecycle(self, value: Optional[pulumi.Input['BackupPlanLifecycleResourceTypeArgs']]):
        pulumi.set(self, "lifecycle", value)


@pulumi.input_type
class BackupPlanLifecycleResourceTypeArgs:
    def __init__(__self__, *,
                 delete_after_days: Optional[pulumi.Input[float]] = None,
                 move_to_cold_storage_after_days: Optional[pulumi.Input[float]] = None):
        if delete_after_days is not None:
            pulumi.set(__self__, "delete_after_days", delete_after_days)
        if move_to_cold_storage_after_days is not None:
            pulumi.set(__self__, "move_to_cold_storage_after_days", move_to_cold_storage_after_days)

    @property
    @pulumi.getter(name="deleteAfterDays")
    def delete_after_days(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "delete_after_days")

    @delete_after_days.setter
    def delete_after_days(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "delete_after_days", value)

    @property
    @pulumi.getter(name="moveToColdStorageAfterDays")
    def move_to_cold_storage_after_days(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "move_to_cold_storage_after_days")

    @move_to_cold_storage_after_days.setter
    def move_to_cold_storage_after_days(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "move_to_cold_storage_after_days", value)


@pulumi.input_type
class BackupPlanResourceTypeArgs:
    def __init__(__self__, *,
                 backup_plan_name: pulumi.Input[str],
                 backup_plan_rule: pulumi.Input[Sequence[pulumi.Input['BackupPlanBackupRuleResourceTypeArgs']]],
                 advanced_backup_settings: Optional[pulumi.Input[Sequence[pulumi.Input['BackupPlanAdvancedBackupSettingResourceTypeArgs']]]] = None):
        pulumi.set(__self__, "backup_plan_name", backup_plan_name)
        pulumi.set(__self__, "backup_plan_rule", backup_plan_rule)
        if advanced_backup_settings is not None:
            pulumi.set(__self__, "advanced_backup_settings", advanced_backup_settings)

    @property
    @pulumi.getter(name="backupPlanName")
    def backup_plan_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "backup_plan_name")

    @backup_plan_name.setter
    def backup_plan_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "backup_plan_name", value)

    @property
    @pulumi.getter(name="backupPlanRule")
    def backup_plan_rule(self) -> pulumi.Input[Sequence[pulumi.Input['BackupPlanBackupRuleResourceTypeArgs']]]:
        return pulumi.get(self, "backup_plan_rule")

    @backup_plan_rule.setter
    def backup_plan_rule(self, value: pulumi.Input[Sequence[pulumi.Input['BackupPlanBackupRuleResourceTypeArgs']]]):
        pulumi.set(self, "backup_plan_rule", value)

    @property
    @pulumi.getter(name="advancedBackupSettings")
    def advanced_backup_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BackupPlanAdvancedBackupSettingResourceTypeArgs']]]]:
        return pulumi.get(self, "advanced_backup_settings")

    @advanced_backup_settings.setter
    def advanced_backup_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BackupPlanAdvancedBackupSettingResourceTypeArgs']]]]):
        pulumi.set(self, "advanced_backup_settings", value)


@pulumi.input_type
class BackupSelectionConditionParameterArgs:
    def __init__(__self__, *,
                 condition_key: Optional[pulumi.Input[str]] = None,
                 condition_value: Optional[pulumi.Input[str]] = None):
        if condition_key is not None:
            pulumi.set(__self__, "condition_key", condition_key)
        if condition_value is not None:
            pulumi.set(__self__, "condition_value", condition_value)

    @property
    @pulumi.getter(name="conditionKey")
    def condition_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "condition_key")

    @condition_key.setter
    def condition_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "condition_key", value)

    @property
    @pulumi.getter(name="conditionValue")
    def condition_value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "condition_value")

    @condition_value.setter
    def condition_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "condition_value", value)


@pulumi.input_type
class BackupSelectionConditionResourceTypeArgs:
    def __init__(__self__, *,
                 condition_key: pulumi.Input[str],
                 condition_type: pulumi.Input[str],
                 condition_value: pulumi.Input[str]):
        pulumi.set(__self__, "condition_key", condition_key)
        pulumi.set(__self__, "condition_type", condition_type)
        pulumi.set(__self__, "condition_value", condition_value)

    @property
    @pulumi.getter(name="conditionKey")
    def condition_key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "condition_key")

    @condition_key.setter
    def condition_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "condition_key", value)

    @property
    @pulumi.getter(name="conditionType")
    def condition_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "condition_type")

    @condition_type.setter
    def condition_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "condition_type", value)

    @property
    @pulumi.getter(name="conditionValue")
    def condition_value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "condition_value")

    @condition_value.setter
    def condition_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "condition_value", value)


@pulumi.input_type
class BackupSelectionResourceTypeConditionsPropertiesArgs:
    def __init__(__self__, *,
                 string_equals: Optional[pulumi.Input[Sequence[pulumi.Input['BackupSelectionConditionParameterArgs']]]] = None,
                 string_like: Optional[pulumi.Input[Sequence[pulumi.Input['BackupSelectionConditionParameterArgs']]]] = None,
                 string_not_equals: Optional[pulumi.Input[Sequence[pulumi.Input['BackupSelectionConditionParameterArgs']]]] = None,
                 string_not_like: Optional[pulumi.Input[Sequence[pulumi.Input['BackupSelectionConditionParameterArgs']]]] = None):
        if string_equals is not None:
            pulumi.set(__self__, "string_equals", string_equals)
        if string_like is not None:
            pulumi.set(__self__, "string_like", string_like)
        if string_not_equals is not None:
            pulumi.set(__self__, "string_not_equals", string_not_equals)
        if string_not_like is not None:
            pulumi.set(__self__, "string_not_like", string_not_like)

    @property
    @pulumi.getter(name="stringEquals")
    def string_equals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BackupSelectionConditionParameterArgs']]]]:
        return pulumi.get(self, "string_equals")

    @string_equals.setter
    def string_equals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BackupSelectionConditionParameterArgs']]]]):
        pulumi.set(self, "string_equals", value)

    @property
    @pulumi.getter(name="stringLike")
    def string_like(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BackupSelectionConditionParameterArgs']]]]:
        return pulumi.get(self, "string_like")

    @string_like.setter
    def string_like(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BackupSelectionConditionParameterArgs']]]]):
        pulumi.set(self, "string_like", value)

    @property
    @pulumi.getter(name="stringNotEquals")
    def string_not_equals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BackupSelectionConditionParameterArgs']]]]:
        return pulumi.get(self, "string_not_equals")

    @string_not_equals.setter
    def string_not_equals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BackupSelectionConditionParameterArgs']]]]):
        pulumi.set(self, "string_not_equals", value)

    @property
    @pulumi.getter(name="stringNotLike")
    def string_not_like(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BackupSelectionConditionParameterArgs']]]]:
        return pulumi.get(self, "string_not_like")

    @string_not_like.setter
    def string_not_like(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BackupSelectionConditionParameterArgs']]]]):
        pulumi.set(self, "string_not_like", value)


@pulumi.input_type
class BackupSelectionResourceTypeArgs:
    def __init__(__self__, *,
                 iam_role_arn: pulumi.Input[str],
                 selection_name: pulumi.Input[str],
                 conditions: Optional[pulumi.Input['BackupSelectionResourceTypeConditionsPropertiesArgs']] = None,
                 list_of_tags: Optional[pulumi.Input[Sequence[pulumi.Input['BackupSelectionConditionResourceTypeArgs']]]] = None,
                 not_resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        pulumi.set(__self__, "iam_role_arn", iam_role_arn)
        pulumi.set(__self__, "selection_name", selection_name)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if list_of_tags is not None:
            pulumi.set(__self__, "list_of_tags", list_of_tags)
        if not_resources is not None:
            pulumi.set(__self__, "not_resources", not_resources)
        if resources is not None:
            pulumi.set(__self__, "resources", resources)

    @property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "iam_role_arn")

    @iam_role_arn.setter
    def iam_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "iam_role_arn", value)

    @property
    @pulumi.getter(name="selectionName")
    def selection_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "selection_name")

    @selection_name.setter
    def selection_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "selection_name", value)

    @property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input['BackupSelectionResourceTypeConditionsPropertiesArgs']]:
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input['BackupSelectionResourceTypeConditionsPropertiesArgs']]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter(name="listOfTags")
    def list_of_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BackupSelectionConditionResourceTypeArgs']]]]:
        return pulumi.get(self, "list_of_tags")

    @list_of_tags.setter
    def list_of_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BackupSelectionConditionResourceTypeArgs']]]]):
        pulumi.set(self, "list_of_tags", value)

    @property
    @pulumi.getter(name="notResources")
    def not_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "not_resources")

    @not_resources.setter
    def not_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "not_resources", value)

    @property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "resources", value)


@pulumi.input_type
class BackupVaultLockConfigurationTypeArgs:
    def __init__(__self__, *,
                 min_retention_days: pulumi.Input[int],
                 changeable_for_days: Optional[pulumi.Input[int]] = None,
                 max_retention_days: Optional[pulumi.Input[int]] = None):
        pulumi.set(__self__, "min_retention_days", min_retention_days)
        if changeable_for_days is not None:
            pulumi.set(__self__, "changeable_for_days", changeable_for_days)
        if max_retention_days is not None:
            pulumi.set(__self__, "max_retention_days", max_retention_days)

    @property
    @pulumi.getter(name="minRetentionDays")
    def min_retention_days(self) -> pulumi.Input[int]:
        return pulumi.get(self, "min_retention_days")

    @min_retention_days.setter
    def min_retention_days(self, value: pulumi.Input[int]):
        pulumi.set(self, "min_retention_days", value)

    @property
    @pulumi.getter(name="changeableForDays")
    def changeable_for_days(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "changeable_for_days")

    @changeable_for_days.setter
    def changeable_for_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "changeable_for_days", value)

    @property
    @pulumi.getter(name="maxRetentionDays")
    def max_retention_days(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_retention_days")

    @max_retention_days.setter
    def max_retention_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_retention_days", value)


@pulumi.input_type
class BackupVaultNotificationObjectTypeArgs:
    def __init__(__self__, *,
                 backup_vault_events: pulumi.Input[Sequence[pulumi.Input[str]]],
                 s_ns_topic_arn: pulumi.Input[str]):
        pulumi.set(__self__, "backup_vault_events", backup_vault_events)
        pulumi.set(__self__, "s_ns_topic_arn", s_ns_topic_arn)

    @property
    @pulumi.getter(name="backupVaultEvents")
    def backup_vault_events(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "backup_vault_events")

    @backup_vault_events.setter
    def backup_vault_events(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "backup_vault_events", value)

    @property
    @pulumi.getter(name="sNSTopicArn")
    def s_ns_topic_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "s_ns_topic_arn")

    @s_ns_topic_arn.setter
    def s_ns_topic_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "s_ns_topic_arn", value)


@pulumi.input_type
class FrameworkControlControlScopePropertiesArgs:
    def __init__(__self__, *,
                 compliance_resource_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 compliance_resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['FrameworkTagArgs']]]] = None):
        """
        The scope of a control. The control scope defines what the control will evaluate. Three examples of control scopes are: a specific backup plan, all backup plans with a specific tag, or all backup plans.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] compliance_resource_ids: The ID of the only AWS resource that you want your control scope to contain.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] compliance_resource_types: Describes whether the control scope includes one or more types of resources, such as `EFS` or `RDS`.
        :param pulumi.Input[Sequence[pulumi.Input['FrameworkTagArgs']]] tags: Describes whether the control scope includes resources with one or more tags. Each tag is a key-value pair.
        """
        if compliance_resource_ids is not None:
            pulumi.set(__self__, "compliance_resource_ids", compliance_resource_ids)
        if compliance_resource_types is not None:
            pulumi.set(__self__, "compliance_resource_types", compliance_resource_types)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="complianceResourceIds")
    def compliance_resource_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The ID of the only AWS resource that you want your control scope to contain.
        """
        return pulumi.get(self, "compliance_resource_ids")

    @compliance_resource_ids.setter
    def compliance_resource_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "compliance_resource_ids", value)

    @property
    @pulumi.getter(name="complianceResourceTypes")
    def compliance_resource_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Describes whether the control scope includes one or more types of resources, such as `EFS` or `RDS`.
        """
        return pulumi.get(self, "compliance_resource_types")

    @compliance_resource_types.setter
    def compliance_resource_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "compliance_resource_types", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FrameworkTagArgs']]]]:
        """
        Describes whether the control scope includes resources with one or more tags. Each tag is a key-value pair.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FrameworkTagArgs']]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class FrameworkControlInputParameterArgs:
    def __init__(__self__, *,
                 parameter_name: pulumi.Input[str],
                 parameter_value: pulumi.Input[str]):
        pulumi.set(__self__, "parameter_name", parameter_name)
        pulumi.set(__self__, "parameter_value", parameter_value)

    @property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "parameter_name")

    @parameter_name.setter
    def parameter_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "parameter_name", value)

    @property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "parameter_value")

    @parameter_value.setter
    def parameter_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "parameter_value", value)


@pulumi.input_type
class FrameworkControlArgs:
    def __init__(__self__, *,
                 control_name: pulumi.Input[str],
                 control_input_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['FrameworkControlInputParameterArgs']]]] = None,
                 control_scope: Optional[pulumi.Input['FrameworkControlControlScopePropertiesArgs']] = None):
        """
        :param pulumi.Input[str] control_name: The name of a control. This name is between 1 and 256 characters.
        :param pulumi.Input[Sequence[pulumi.Input['FrameworkControlInputParameterArgs']]] control_input_parameters: A list of ParameterName and ParameterValue pairs.
        :param pulumi.Input['FrameworkControlControlScopePropertiesArgs'] control_scope: The scope of a control. The control scope defines what the control will evaluate. Three examples of control scopes are: a specific backup plan, all backup plans with a specific tag, or all backup plans.
        """
        pulumi.set(__self__, "control_name", control_name)
        if control_input_parameters is not None:
            pulumi.set(__self__, "control_input_parameters", control_input_parameters)
        if control_scope is not None:
            pulumi.set(__self__, "control_scope", control_scope)

    @property
    @pulumi.getter(name="controlName")
    def control_name(self) -> pulumi.Input[str]:
        """
        The name of a control. This name is between 1 and 256 characters.
        """
        return pulumi.get(self, "control_name")

    @control_name.setter
    def control_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "control_name", value)

    @property
    @pulumi.getter(name="controlInputParameters")
    def control_input_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FrameworkControlInputParameterArgs']]]]:
        """
        A list of ParameterName and ParameterValue pairs.
        """
        return pulumi.get(self, "control_input_parameters")

    @control_input_parameters.setter
    def control_input_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FrameworkControlInputParameterArgs']]]]):
        pulumi.set(self, "control_input_parameters", value)

    @property
    @pulumi.getter(name="controlScope")
    def control_scope(self) -> Optional[pulumi.Input['FrameworkControlControlScopePropertiesArgs']]:
        """
        The scope of a control. The control scope defines what the control will evaluate. Three examples of control scopes are: a specific backup plan, all backup plans with a specific tag, or all backup plans.
        """
        return pulumi.get(self, "control_scope")

    @control_scope.setter
    def control_scope(self, value: Optional[pulumi.Input['FrameworkControlControlScopePropertiesArgs']]):
        pulumi.set(self, "control_scope", value)


@pulumi.input_type
class FrameworkTagArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ReportDeliveryChannelPropertiesArgs:
    def __init__(__self__, *,
                 s3_bucket_name: pulumi.Input[str],
                 formats: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 s3_key_prefix: Optional[pulumi.Input[str]] = None):
        """
        A structure that contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.
        :param pulumi.Input[str] s3_bucket_name: The unique name of the S3 bucket that receives your reports.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] formats: A list of the format of your reports: CSV, JSON, or both. If not specified, the default format is CSV.
        :param pulumi.Input[str] s3_key_prefix: The prefix for where AWS Backup Audit Manager delivers your reports to Amazon S3. The prefix is this part of the following path: s3://your-bucket-name/prefix/Backup/us-west-2/year/month/day/report-name. If not specified, there is no prefix.
        """
        pulumi.set(__self__, "s3_bucket_name", s3_bucket_name)
        if formats is not None:
            pulumi.set(__self__, "formats", formats)
        if s3_key_prefix is not None:
            pulumi.set(__self__, "s3_key_prefix", s3_key_prefix)

    @property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> pulumi.Input[str]:
        """
        The unique name of the S3 bucket that receives your reports.
        """
        return pulumi.get(self, "s3_bucket_name")

    @s3_bucket_name.setter
    def s3_bucket_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "s3_bucket_name", value)

    @property
    @pulumi.getter
    def formats(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of the format of your reports: CSV, JSON, or both. If not specified, the default format is CSV.
        """
        return pulumi.get(self, "formats")

    @formats.setter
    def formats(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "formats", value)

    @property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The prefix for where AWS Backup Audit Manager delivers your reports to Amazon S3. The prefix is this part of the following path: s3://your-bucket-name/prefix/Backup/us-west-2/year/month/day/report-name. If not specified, there is no prefix.
        """
        return pulumi.get(self, "s3_key_prefix")

    @s3_key_prefix.setter
    def s3_key_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "s3_key_prefix", value)


@pulumi.input_type
class ReportPlanTagArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ReportSettingPropertiesArgs:
    def __init__(__self__, *,
                 report_template: pulumi.Input[str],
                 accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 framework_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 organization_units: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Identifies the report template for the report. Reports are built using a report template.
        :param pulumi.Input[str] report_template: Identifies the report template for the report. Reports are built using a report template. The report templates are: `BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT`
        :param pulumi.Input[Sequence[pulumi.Input[str]]] accounts: The list of AWS accounts that a report covers.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] framework_arns: The Amazon Resource Names (ARNs) of the frameworks a report covers.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] organization_units: The list of AWS organization units that a report covers.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regions: The list of AWS regions that a report covers.
        """
        pulumi.set(__self__, "report_template", report_template)
        if accounts is not None:
            pulumi.set(__self__, "accounts", accounts)
        if framework_arns is not None:
            pulumi.set(__self__, "framework_arns", framework_arns)
        if organization_units is not None:
            pulumi.set(__self__, "organization_units", organization_units)
        if regions is not None:
            pulumi.set(__self__, "regions", regions)

    @property
    @pulumi.getter(name="reportTemplate")
    def report_template(self) -> pulumi.Input[str]:
        """
        Identifies the report template for the report. Reports are built using a report template. The report templates are: `BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT`
        """
        return pulumi.get(self, "report_template")

    @report_template.setter
    def report_template(self, value: pulumi.Input[str]):
        pulumi.set(self, "report_template", value)

    @property
    @pulumi.getter
    def accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of AWS accounts that a report covers.
        """
        return pulumi.get(self, "accounts")

    @accounts.setter
    def accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "accounts", value)

    @property
    @pulumi.getter(name="frameworkArns")
    def framework_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The Amazon Resource Names (ARNs) of the frameworks a report covers.
        """
        return pulumi.get(self, "framework_arns")

    @framework_arns.setter
    def framework_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "framework_arns", value)

    @property
    @pulumi.getter(name="organizationUnits")
    def organization_units(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of AWS organization units that a report covers.
        """
        return pulumi.get(self, "organization_units")

    @organization_units.setter
    def organization_units(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "organization_units", value)

    @property
    @pulumi.getter
    def regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of AWS regions that a report covers.
        """
        return pulumi.get(self, "regions")

    @regions.setter
    def regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "regions", value)


