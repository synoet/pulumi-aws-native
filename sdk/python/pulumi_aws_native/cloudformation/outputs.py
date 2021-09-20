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
    'ResourceVersionLoggingConfig',
    'StackSetAutoDeployment',
    'StackSetDeploymentTargets',
    'StackSetOperationPreferences',
    'StackSetParameter',
    'StackSetStackInstances',
    'StackSetTag',
    'TypeActivationLoggingConfig',
]

@pulumi.output_type
class ResourceVersionLoggingConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "logGroupName":
            suggest = "log_group_name"
        elif key == "logRoleArn":
            suggest = "log_role_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResourceVersionLoggingConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResourceVersionLoggingConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResourceVersionLoggingConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 log_group_name: Optional[str] = None,
                 log_role_arn: Optional[str] = None):
        """
        :param str log_group_name: The Amazon CloudWatch log group to which CloudFormation sends error logging information when invoking the type's handlers.
        :param str log_role_arn: The ARN of the role that CloudFormation should assume when sending log entries to CloudWatch logs.
        """
        if log_group_name is not None:
            pulumi.set(__self__, "log_group_name", log_group_name)
        if log_role_arn is not None:
            pulumi.set(__self__, "log_role_arn", log_role_arn)

    @property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[str]:
        """
        The Amazon CloudWatch log group to which CloudFormation sends error logging information when invoking the type's handlers.
        """
        return pulumi.get(self, "log_group_name")

    @property
    @pulumi.getter(name="logRoleArn")
    def log_role_arn(self) -> Optional[str]:
        """
        The ARN of the role that CloudFormation should assume when sending log entries to CloudWatch logs.
        """
        return pulumi.get(self, "log_role_arn")


@pulumi.output_type
class StackSetAutoDeployment(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "retainStacksOnAccountRemoval":
            suggest = "retain_stacks_on_account_removal"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in StackSetAutoDeployment. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        StackSetAutoDeployment.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        StackSetAutoDeployment.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: Optional[bool] = None,
                 retain_stacks_on_account_removal: Optional[bool] = None):
        """
        :param bool enabled: If set to true, StackSets automatically deploys additional stack instances to AWS Organizations accounts that are added to a target organization or organizational unit (OU) in the specified Regions. If an account is removed from a target organization or OU, StackSets deletes stack instances from the account in the specified Regions.
        :param bool retain_stacks_on_account_removal: If set to true, stack resources are retained when an account is removed from a target organization or OU. If set to false, stack resources are deleted. Specify only if Enabled is set to True.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if retain_stacks_on_account_removal is not None:
            pulumi.set(__self__, "retain_stacks_on_account_removal", retain_stacks_on_account_removal)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        If set to true, StackSets automatically deploys additional stack instances to AWS Organizations accounts that are added to a target organization or organizational unit (OU) in the specified Regions. If an account is removed from a target organization or OU, StackSets deletes stack instances from the account in the specified Regions.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="retainStacksOnAccountRemoval")
    def retain_stacks_on_account_removal(self) -> Optional[bool]:
        """
        If set to true, stack resources are retained when an account is removed from a target organization or OU. If set to false, stack resources are deleted. Specify only if Enabled is set to True.
        """
        return pulumi.get(self, "retain_stacks_on_account_removal")


@pulumi.output_type
class StackSetDeploymentTargets(dict):
    """
     The AWS OrganizationalUnitIds or Accounts for which to create stack instances in the specified Regions.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "organizationalUnitIds":
            suggest = "organizational_unit_ids"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in StackSetDeploymentTargets. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        StackSetDeploymentTargets.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        StackSetDeploymentTargets.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 accounts: Optional[Sequence[str]] = None,
                 organizational_unit_ids: Optional[Sequence[str]] = None):
        """
         The AWS OrganizationalUnitIds or Accounts for which to create stack instances in the specified Regions.
        :param Sequence[str] accounts: AWS accounts that you want to create stack instances in the specified Region(s) for.
        :param Sequence[str] organizational_unit_ids: The organization root ID or organizational unit (OU) IDs to which StackSets deploys.
        """
        if accounts is not None:
            pulumi.set(__self__, "accounts", accounts)
        if organizational_unit_ids is not None:
            pulumi.set(__self__, "organizational_unit_ids", organizational_unit_ids)

    @property
    @pulumi.getter
    def accounts(self) -> Optional[Sequence[str]]:
        """
        AWS accounts that you want to create stack instances in the specified Region(s) for.
        """
        return pulumi.get(self, "accounts")

    @property
    @pulumi.getter(name="organizationalUnitIds")
    def organizational_unit_ids(self) -> Optional[Sequence[str]]:
        """
        The organization root ID or organizational unit (OU) IDs to which StackSets deploys.
        """
        return pulumi.get(self, "organizational_unit_ids")


@pulumi.output_type
class StackSetOperationPreferences(dict):
    """
    The user-specified preferences for how AWS CloudFormation performs a stack set operation.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "failureToleranceCount":
            suggest = "failure_tolerance_count"
        elif key == "failureTolerancePercentage":
            suggest = "failure_tolerance_percentage"
        elif key == "maxConcurrentCount":
            suggest = "max_concurrent_count"
        elif key == "maxConcurrentPercentage":
            suggest = "max_concurrent_percentage"
        elif key == "regionConcurrencyType":
            suggest = "region_concurrency_type"
        elif key == "regionOrder":
            suggest = "region_order"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in StackSetOperationPreferences. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        StackSetOperationPreferences.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        StackSetOperationPreferences.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 failure_tolerance_count: Optional[int] = None,
                 failure_tolerance_percentage: Optional[int] = None,
                 max_concurrent_count: Optional[int] = None,
                 max_concurrent_percentage: Optional[int] = None,
                 region_concurrency_type: Optional['StackSetRegionConcurrencyType'] = None,
                 region_order: Optional[Sequence[str]] = None):
        """
        The user-specified preferences for how AWS CloudFormation performs a stack set operation.
        """
        if failure_tolerance_count is not None:
            pulumi.set(__self__, "failure_tolerance_count", failure_tolerance_count)
        if failure_tolerance_percentage is not None:
            pulumi.set(__self__, "failure_tolerance_percentage", failure_tolerance_percentage)
        if max_concurrent_count is not None:
            pulumi.set(__self__, "max_concurrent_count", max_concurrent_count)
        if max_concurrent_percentage is not None:
            pulumi.set(__self__, "max_concurrent_percentage", max_concurrent_percentage)
        if region_concurrency_type is not None:
            pulumi.set(__self__, "region_concurrency_type", region_concurrency_type)
        if region_order is not None:
            pulumi.set(__self__, "region_order", region_order)

    @property
    @pulumi.getter(name="failureToleranceCount")
    def failure_tolerance_count(self) -> Optional[int]:
        return pulumi.get(self, "failure_tolerance_count")

    @property
    @pulumi.getter(name="failureTolerancePercentage")
    def failure_tolerance_percentage(self) -> Optional[int]:
        return pulumi.get(self, "failure_tolerance_percentage")

    @property
    @pulumi.getter(name="maxConcurrentCount")
    def max_concurrent_count(self) -> Optional[int]:
        return pulumi.get(self, "max_concurrent_count")

    @property
    @pulumi.getter(name="maxConcurrentPercentage")
    def max_concurrent_percentage(self) -> Optional[int]:
        return pulumi.get(self, "max_concurrent_percentage")

    @property
    @pulumi.getter(name="regionConcurrencyType")
    def region_concurrency_type(self) -> Optional['StackSetRegionConcurrencyType']:
        return pulumi.get(self, "region_concurrency_type")

    @property
    @pulumi.getter(name="regionOrder")
    def region_order(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "region_order")


@pulumi.output_type
class StackSetParameter(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "parameterKey":
            suggest = "parameter_key"
        elif key == "parameterValue":
            suggest = "parameter_value"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in StackSetParameter. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        StackSetParameter.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        StackSetParameter.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 parameter_key: str,
                 parameter_value: str):
        """
        :param str parameter_key: The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
        :param str parameter_value: The input value associated with the parameter.
        """
        pulumi.set(__self__, "parameter_key", parameter_key)
        pulumi.set(__self__, "parameter_value", parameter_value)

    @property
    @pulumi.getter(name="parameterKey")
    def parameter_key(self) -> str:
        """
        The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
        """
        return pulumi.get(self, "parameter_key")

    @property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> str:
        """
        The input value associated with the parameter.
        """
        return pulumi.get(self, "parameter_value")


@pulumi.output_type
class StackSetStackInstances(dict):
    """
    Stack instances in some specific accounts and Regions.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "deploymentTargets":
            suggest = "deployment_targets"
        elif key == "parameterOverrides":
            suggest = "parameter_overrides"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in StackSetStackInstances. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        StackSetStackInstances.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        StackSetStackInstances.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 deployment_targets: 'outputs.StackSetDeploymentTargets',
                 regions: Sequence[str],
                 parameter_overrides: Optional[Sequence['outputs.StackSetParameter']] = None):
        """
        Stack instances in some specific accounts and Regions.
        :param Sequence[str] regions: The names of one or more Regions where you want to create stack instances using the specified AWS account(s).
        :param Sequence['StackSetParameter'] parameter_overrides: A list of stack set parameters whose values you want to override in the selected stack instances.
        """
        pulumi.set(__self__, "deployment_targets", deployment_targets)
        pulumi.set(__self__, "regions", regions)
        if parameter_overrides is not None:
            pulumi.set(__self__, "parameter_overrides", parameter_overrides)

    @property
    @pulumi.getter(name="deploymentTargets")
    def deployment_targets(self) -> 'outputs.StackSetDeploymentTargets':
        return pulumi.get(self, "deployment_targets")

    @property
    @pulumi.getter
    def regions(self) -> Sequence[str]:
        """
        The names of one or more Regions where you want to create stack instances using the specified AWS account(s).
        """
        return pulumi.get(self, "regions")

    @property
    @pulumi.getter(name="parameterOverrides")
    def parameter_overrides(self) -> Optional[Sequence['outputs.StackSetParameter']]:
        """
        A list of stack set parameters whose values you want to override in the selected stack instances.
        """
        return pulumi.get(self, "parameter_overrides")


@pulumi.output_type
class StackSetTag(dict):
    """
    Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation StackSet.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation StackSet.
        :param str key: A string used to identify this tag. You can specify a maximum of 127 characters for a tag key.
        :param str value: A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        A string used to identify this tag. You can specify a maximum of 127 characters for a tag key.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class TypeActivationLoggingConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "logGroupName":
            suggest = "log_group_name"
        elif key == "logRoleArn":
            suggest = "log_role_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TypeActivationLoggingConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TypeActivationLoggingConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TypeActivationLoggingConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 log_group_name: Optional[str] = None,
                 log_role_arn: Optional[str] = None):
        """
        :param str log_group_name: The Amazon CloudWatch log group to which CloudFormation sends error logging information when invoking the type's handlers.
        :param str log_role_arn: The ARN of the role that CloudFormation should assume when sending log entries to CloudWatch logs.
        """
        if log_group_name is not None:
            pulumi.set(__self__, "log_group_name", log_group_name)
        if log_role_arn is not None:
            pulumi.set(__self__, "log_role_arn", log_role_arn)

    @property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[str]:
        """
        The Amazon CloudWatch log group to which CloudFormation sends error logging information when invoking the type's handlers.
        """
        return pulumi.get(self, "log_group_name")

    @property
    @pulumi.getter(name="logRoleArn")
    def log_role_arn(self) -> Optional[str]:
        """
        The ARN of the role that CloudFormation should assume when sending log entries to CloudWatch logs.
        """
        return pulumi.get(self, "log_role_arn")


