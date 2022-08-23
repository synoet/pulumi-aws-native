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
    'AggregationAuthorizationTag',
    'ConfigRuleCustomPolicyDetails',
    'ConfigRuleScope',
    'ConfigRuleSource',
    'ConfigRuleSourceDetail',
    'ConfigurationAggregatorAccountAggregationSource',
    'ConfigurationAggregatorOrganizationAggregationSource',
    'ConfigurationAggregatorTag',
    'ConfigurationRecorderRecordingGroup',
    'ConformancePackInputParameter',
    'DeliveryChannelConfigSnapshotDeliveryProperties',
    'OrganizationConfigRuleOrganizationCustomRuleMetadata',
    'OrganizationConfigRuleOrganizationManagedRuleMetadata',
    'OrganizationConformancePackConformancePackInputParameter',
    'RemediationConfigurationExecutionControls',
    'RemediationConfigurationSsmControls',
    'StoredQueryTag',
    'TemplateSSMDocumentDetailsProperties',
]

@pulumi.output_type
class AggregationAuthorizationTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param str value: The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class ConfigRuleCustomPolicyDetails(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "enableDebugLogDelivery":
            suggest = "enable_debug_log_delivery"
        elif key == "policyRuntime":
            suggest = "policy_runtime"
        elif key == "policyText":
            suggest = "policy_text"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigRuleCustomPolicyDetails. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigRuleCustomPolicyDetails.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigRuleCustomPolicyDetails.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enable_debug_log_delivery: Optional[bool] = None,
                 policy_runtime: Optional[str] = None,
                 policy_text: Optional[str] = None):
        if enable_debug_log_delivery is not None:
            pulumi.set(__self__, "enable_debug_log_delivery", enable_debug_log_delivery)
        if policy_runtime is not None:
            pulumi.set(__self__, "policy_runtime", policy_runtime)
        if policy_text is not None:
            pulumi.set(__self__, "policy_text", policy_text)

    @property
    @pulumi.getter(name="enableDebugLogDelivery")
    def enable_debug_log_delivery(self) -> Optional[bool]:
        return pulumi.get(self, "enable_debug_log_delivery")

    @property
    @pulumi.getter(name="policyRuntime")
    def policy_runtime(self) -> Optional[str]:
        return pulumi.get(self, "policy_runtime")

    @property
    @pulumi.getter(name="policyText")
    def policy_text(self) -> Optional[str]:
        return pulumi.get(self, "policy_text")


@pulumi.output_type
class ConfigRuleScope(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "complianceResourceId":
            suggest = "compliance_resource_id"
        elif key == "complianceResourceTypes":
            suggest = "compliance_resource_types"
        elif key == "tagKey":
            suggest = "tag_key"
        elif key == "tagValue":
            suggest = "tag_value"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigRuleScope. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigRuleScope.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigRuleScope.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 compliance_resource_id: Optional[str] = None,
                 compliance_resource_types: Optional[Sequence[str]] = None,
                 tag_key: Optional[str] = None,
                 tag_value: Optional[str] = None):
        if compliance_resource_id is not None:
            pulumi.set(__self__, "compliance_resource_id", compliance_resource_id)
        if compliance_resource_types is not None:
            pulumi.set(__self__, "compliance_resource_types", compliance_resource_types)
        if tag_key is not None:
            pulumi.set(__self__, "tag_key", tag_key)
        if tag_value is not None:
            pulumi.set(__self__, "tag_value", tag_value)

    @property
    @pulumi.getter(name="complianceResourceId")
    def compliance_resource_id(self) -> Optional[str]:
        return pulumi.get(self, "compliance_resource_id")

    @property
    @pulumi.getter(name="complianceResourceTypes")
    def compliance_resource_types(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "compliance_resource_types")

    @property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> Optional[str]:
        return pulumi.get(self, "tag_key")

    @property
    @pulumi.getter(name="tagValue")
    def tag_value(self) -> Optional[str]:
        return pulumi.get(self, "tag_value")


@pulumi.output_type
class ConfigRuleSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "customPolicyDetails":
            suggest = "custom_policy_details"
        elif key == "sourceDetails":
            suggest = "source_details"
        elif key == "sourceIdentifier":
            suggest = "source_identifier"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigRuleSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigRuleSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigRuleSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 owner: str,
                 custom_policy_details: Optional['outputs.ConfigRuleCustomPolicyDetails'] = None,
                 source_details: Optional[Sequence['outputs.ConfigRuleSourceDetail']] = None,
                 source_identifier: Optional[str] = None):
        pulumi.set(__self__, "owner", owner)
        if custom_policy_details is not None:
            pulumi.set(__self__, "custom_policy_details", custom_policy_details)
        if source_details is not None:
            pulumi.set(__self__, "source_details", source_details)
        if source_identifier is not None:
            pulumi.set(__self__, "source_identifier", source_identifier)

    @property
    @pulumi.getter
    def owner(self) -> str:
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="customPolicyDetails")
    def custom_policy_details(self) -> Optional['outputs.ConfigRuleCustomPolicyDetails']:
        return pulumi.get(self, "custom_policy_details")

    @property
    @pulumi.getter(name="sourceDetails")
    def source_details(self) -> Optional[Sequence['outputs.ConfigRuleSourceDetail']]:
        return pulumi.get(self, "source_details")

    @property
    @pulumi.getter(name="sourceIdentifier")
    def source_identifier(self) -> Optional[str]:
        return pulumi.get(self, "source_identifier")


@pulumi.output_type
class ConfigRuleSourceDetail(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "eventSource":
            suggest = "event_source"
        elif key == "messageType":
            suggest = "message_type"
        elif key == "maximumExecutionFrequency":
            suggest = "maximum_execution_frequency"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigRuleSourceDetail. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigRuleSourceDetail.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigRuleSourceDetail.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 event_source: str,
                 message_type: str,
                 maximum_execution_frequency: Optional[str] = None):
        pulumi.set(__self__, "event_source", event_source)
        pulumi.set(__self__, "message_type", message_type)
        if maximum_execution_frequency is not None:
            pulumi.set(__self__, "maximum_execution_frequency", maximum_execution_frequency)

    @property
    @pulumi.getter(name="eventSource")
    def event_source(self) -> str:
        return pulumi.get(self, "event_source")

    @property
    @pulumi.getter(name="messageType")
    def message_type(self) -> str:
        return pulumi.get(self, "message_type")

    @property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> Optional[str]:
        return pulumi.get(self, "maximum_execution_frequency")


@pulumi.output_type
class ConfigurationAggregatorAccountAggregationSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "accountIds":
            suggest = "account_ids"
        elif key == "allAwsRegions":
            suggest = "all_aws_regions"
        elif key == "awsRegions":
            suggest = "aws_regions"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationAggregatorAccountAggregationSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationAggregatorAccountAggregationSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationAggregatorAccountAggregationSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 account_ids: Sequence[str],
                 all_aws_regions: Optional[bool] = None,
                 aws_regions: Optional[Sequence[str]] = None):
        pulumi.set(__self__, "account_ids", account_ids)
        if all_aws_regions is not None:
            pulumi.set(__self__, "all_aws_regions", all_aws_regions)
        if aws_regions is not None:
            pulumi.set(__self__, "aws_regions", aws_regions)

    @property
    @pulumi.getter(name="accountIds")
    def account_ids(self) -> Sequence[str]:
        return pulumi.get(self, "account_ids")

    @property
    @pulumi.getter(name="allAwsRegions")
    def all_aws_regions(self) -> Optional[bool]:
        return pulumi.get(self, "all_aws_regions")

    @property
    @pulumi.getter(name="awsRegions")
    def aws_regions(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "aws_regions")


@pulumi.output_type
class ConfigurationAggregatorOrganizationAggregationSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "roleArn":
            suggest = "role_arn"
        elif key == "allAwsRegions":
            suggest = "all_aws_regions"
        elif key == "awsRegions":
            suggest = "aws_regions"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationAggregatorOrganizationAggregationSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationAggregatorOrganizationAggregationSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationAggregatorOrganizationAggregationSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 role_arn: str,
                 all_aws_regions: Optional[bool] = None,
                 aws_regions: Optional[Sequence[str]] = None):
        pulumi.set(__self__, "role_arn", role_arn)
        if all_aws_regions is not None:
            pulumi.set(__self__, "all_aws_regions", all_aws_regions)
        if aws_regions is not None:
            pulumi.set(__self__, "aws_regions", aws_regions)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> str:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="allAwsRegions")
    def all_aws_regions(self) -> Optional[bool]:
        return pulumi.get(self, "all_aws_regions")

    @property
    @pulumi.getter(name="awsRegions")
    def aws_regions(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "aws_regions")


@pulumi.output_type
class ConfigurationAggregatorTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param str value: The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class ConfigurationRecorderRecordingGroup(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allSupported":
            suggest = "all_supported"
        elif key == "includeGlobalResourceTypes":
            suggest = "include_global_resource_types"
        elif key == "resourceTypes":
            suggest = "resource_types"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationRecorderRecordingGroup. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationRecorderRecordingGroup.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationRecorderRecordingGroup.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 all_supported: Optional[bool] = None,
                 include_global_resource_types: Optional[bool] = None,
                 resource_types: Optional[Sequence[str]] = None):
        if all_supported is not None:
            pulumi.set(__self__, "all_supported", all_supported)
        if include_global_resource_types is not None:
            pulumi.set(__self__, "include_global_resource_types", include_global_resource_types)
        if resource_types is not None:
            pulumi.set(__self__, "resource_types", resource_types)

    @property
    @pulumi.getter(name="allSupported")
    def all_supported(self) -> Optional[bool]:
        return pulumi.get(self, "all_supported")

    @property
    @pulumi.getter(name="includeGlobalResourceTypes")
    def include_global_resource_types(self) -> Optional[bool]:
        return pulumi.get(self, "include_global_resource_types")

    @property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "resource_types")


@pulumi.output_type
class ConformancePackInputParameter(dict):
    """
    Input parameters in the form of key-value pairs for the conformance pack.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "parameterName":
            suggest = "parameter_name"
        elif key == "parameterValue":
            suggest = "parameter_value"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConformancePackInputParameter. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConformancePackInputParameter.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConformancePackInputParameter.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 parameter_name: str,
                 parameter_value: str):
        """
        Input parameters in the form of key-value pairs for the conformance pack.
        """
        pulumi.set(__self__, "parameter_name", parameter_name)
        pulumi.set(__self__, "parameter_value", parameter_value)

    @property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> str:
        return pulumi.get(self, "parameter_name")

    @property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> str:
        return pulumi.get(self, "parameter_value")


@pulumi.output_type
class DeliveryChannelConfigSnapshotDeliveryProperties(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "deliveryFrequency":
            suggest = "delivery_frequency"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DeliveryChannelConfigSnapshotDeliveryProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DeliveryChannelConfigSnapshotDeliveryProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DeliveryChannelConfigSnapshotDeliveryProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 delivery_frequency: Optional[str] = None):
        if delivery_frequency is not None:
            pulumi.set(__self__, "delivery_frequency", delivery_frequency)

    @property
    @pulumi.getter(name="deliveryFrequency")
    def delivery_frequency(self) -> Optional[str]:
        return pulumi.get(self, "delivery_frequency")


@pulumi.output_type
class OrganizationConfigRuleOrganizationCustomRuleMetadata(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "lambdaFunctionArn":
            suggest = "lambda_function_arn"
        elif key == "organizationConfigRuleTriggerTypes":
            suggest = "organization_config_rule_trigger_types"
        elif key == "inputParameters":
            suggest = "input_parameters"
        elif key == "maximumExecutionFrequency":
            suggest = "maximum_execution_frequency"
        elif key == "resourceIdScope":
            suggest = "resource_id_scope"
        elif key == "resourceTypesScope":
            suggest = "resource_types_scope"
        elif key == "tagKeyScope":
            suggest = "tag_key_scope"
        elif key == "tagValueScope":
            suggest = "tag_value_scope"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OrganizationConfigRuleOrganizationCustomRuleMetadata. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OrganizationConfigRuleOrganizationCustomRuleMetadata.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OrganizationConfigRuleOrganizationCustomRuleMetadata.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 lambda_function_arn: str,
                 organization_config_rule_trigger_types: Sequence[str],
                 description: Optional[str] = None,
                 input_parameters: Optional[str] = None,
                 maximum_execution_frequency: Optional[str] = None,
                 resource_id_scope: Optional[str] = None,
                 resource_types_scope: Optional[Sequence[str]] = None,
                 tag_key_scope: Optional[str] = None,
                 tag_value_scope: Optional[str] = None):
        pulumi.set(__self__, "lambda_function_arn", lambda_function_arn)
        pulumi.set(__self__, "organization_config_rule_trigger_types", organization_config_rule_trigger_types)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if input_parameters is not None:
            pulumi.set(__self__, "input_parameters", input_parameters)
        if maximum_execution_frequency is not None:
            pulumi.set(__self__, "maximum_execution_frequency", maximum_execution_frequency)
        if resource_id_scope is not None:
            pulumi.set(__self__, "resource_id_scope", resource_id_scope)
        if resource_types_scope is not None:
            pulumi.set(__self__, "resource_types_scope", resource_types_scope)
        if tag_key_scope is not None:
            pulumi.set(__self__, "tag_key_scope", tag_key_scope)
        if tag_value_scope is not None:
            pulumi.set(__self__, "tag_value_scope", tag_value_scope)

    @property
    @pulumi.getter(name="lambdaFunctionArn")
    def lambda_function_arn(self) -> str:
        return pulumi.get(self, "lambda_function_arn")

    @property
    @pulumi.getter(name="organizationConfigRuleTriggerTypes")
    def organization_config_rule_trigger_types(self) -> Sequence[str]:
        return pulumi.get(self, "organization_config_rule_trigger_types")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> Optional[str]:
        return pulumi.get(self, "input_parameters")

    @property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> Optional[str]:
        return pulumi.get(self, "maximum_execution_frequency")

    @property
    @pulumi.getter(name="resourceIdScope")
    def resource_id_scope(self) -> Optional[str]:
        return pulumi.get(self, "resource_id_scope")

    @property
    @pulumi.getter(name="resourceTypesScope")
    def resource_types_scope(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "resource_types_scope")

    @property
    @pulumi.getter(name="tagKeyScope")
    def tag_key_scope(self) -> Optional[str]:
        return pulumi.get(self, "tag_key_scope")

    @property
    @pulumi.getter(name="tagValueScope")
    def tag_value_scope(self) -> Optional[str]:
        return pulumi.get(self, "tag_value_scope")


@pulumi.output_type
class OrganizationConfigRuleOrganizationManagedRuleMetadata(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ruleIdentifier":
            suggest = "rule_identifier"
        elif key == "inputParameters":
            suggest = "input_parameters"
        elif key == "maximumExecutionFrequency":
            suggest = "maximum_execution_frequency"
        elif key == "resourceIdScope":
            suggest = "resource_id_scope"
        elif key == "resourceTypesScope":
            suggest = "resource_types_scope"
        elif key == "tagKeyScope":
            suggest = "tag_key_scope"
        elif key == "tagValueScope":
            suggest = "tag_value_scope"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OrganizationConfigRuleOrganizationManagedRuleMetadata. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OrganizationConfigRuleOrganizationManagedRuleMetadata.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OrganizationConfigRuleOrganizationManagedRuleMetadata.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 rule_identifier: str,
                 description: Optional[str] = None,
                 input_parameters: Optional[str] = None,
                 maximum_execution_frequency: Optional[str] = None,
                 resource_id_scope: Optional[str] = None,
                 resource_types_scope: Optional[Sequence[str]] = None,
                 tag_key_scope: Optional[str] = None,
                 tag_value_scope: Optional[str] = None):
        pulumi.set(__self__, "rule_identifier", rule_identifier)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if input_parameters is not None:
            pulumi.set(__self__, "input_parameters", input_parameters)
        if maximum_execution_frequency is not None:
            pulumi.set(__self__, "maximum_execution_frequency", maximum_execution_frequency)
        if resource_id_scope is not None:
            pulumi.set(__self__, "resource_id_scope", resource_id_scope)
        if resource_types_scope is not None:
            pulumi.set(__self__, "resource_types_scope", resource_types_scope)
        if tag_key_scope is not None:
            pulumi.set(__self__, "tag_key_scope", tag_key_scope)
        if tag_value_scope is not None:
            pulumi.set(__self__, "tag_value_scope", tag_value_scope)

    @property
    @pulumi.getter(name="ruleIdentifier")
    def rule_identifier(self) -> str:
        return pulumi.get(self, "rule_identifier")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> Optional[str]:
        return pulumi.get(self, "input_parameters")

    @property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> Optional[str]:
        return pulumi.get(self, "maximum_execution_frequency")

    @property
    @pulumi.getter(name="resourceIdScope")
    def resource_id_scope(self) -> Optional[str]:
        return pulumi.get(self, "resource_id_scope")

    @property
    @pulumi.getter(name="resourceTypesScope")
    def resource_types_scope(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "resource_types_scope")

    @property
    @pulumi.getter(name="tagKeyScope")
    def tag_key_scope(self) -> Optional[str]:
        return pulumi.get(self, "tag_key_scope")

    @property
    @pulumi.getter(name="tagValueScope")
    def tag_value_scope(self) -> Optional[str]:
        return pulumi.get(self, "tag_value_scope")


@pulumi.output_type
class OrganizationConformancePackConformancePackInputParameter(dict):
    """
    Input parameters in the form of key-value pairs for the conformance pack.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "parameterName":
            suggest = "parameter_name"
        elif key == "parameterValue":
            suggest = "parameter_value"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OrganizationConformancePackConformancePackInputParameter. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OrganizationConformancePackConformancePackInputParameter.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OrganizationConformancePackConformancePackInputParameter.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 parameter_name: str,
                 parameter_value: str):
        """
        Input parameters in the form of key-value pairs for the conformance pack.
        """
        pulumi.set(__self__, "parameter_name", parameter_name)
        pulumi.set(__self__, "parameter_value", parameter_value)

    @property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> str:
        return pulumi.get(self, "parameter_name")

    @property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> str:
        return pulumi.get(self, "parameter_value")


@pulumi.output_type
class RemediationConfigurationExecutionControls(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ssmControls":
            suggest = "ssm_controls"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RemediationConfigurationExecutionControls. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RemediationConfigurationExecutionControls.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RemediationConfigurationExecutionControls.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 ssm_controls: Optional['outputs.RemediationConfigurationSsmControls'] = None):
        if ssm_controls is not None:
            pulumi.set(__self__, "ssm_controls", ssm_controls)

    @property
    @pulumi.getter(name="ssmControls")
    def ssm_controls(self) -> Optional['outputs.RemediationConfigurationSsmControls']:
        return pulumi.get(self, "ssm_controls")


@pulumi.output_type
class RemediationConfigurationSsmControls(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "concurrentExecutionRatePercentage":
            suggest = "concurrent_execution_rate_percentage"
        elif key == "errorPercentage":
            suggest = "error_percentage"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RemediationConfigurationSsmControls. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RemediationConfigurationSsmControls.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RemediationConfigurationSsmControls.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 concurrent_execution_rate_percentage: Optional[int] = None,
                 error_percentage: Optional[int] = None):
        if concurrent_execution_rate_percentage is not None:
            pulumi.set(__self__, "concurrent_execution_rate_percentage", concurrent_execution_rate_percentage)
        if error_percentage is not None:
            pulumi.set(__self__, "error_percentage", error_percentage)

    @property
    @pulumi.getter(name="concurrentExecutionRatePercentage")
    def concurrent_execution_rate_percentage(self) -> Optional[int]:
        return pulumi.get(self, "concurrent_execution_rate_percentage")

    @property
    @pulumi.getter(name="errorPercentage")
    def error_percentage(self) -> Optional[int]:
        return pulumi.get(self, "error_percentage")


@pulumi.output_type
class StoredQueryTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param str value: The value for the tag. You can specify a value that is 0 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is 0 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class TemplateSSMDocumentDetailsProperties(dict):
    """
    The TemplateSSMDocumentDetails object contains the name of the SSM document and the version of the SSM document.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "documentName":
            suggest = "document_name"
        elif key == "documentVersion":
            suggest = "document_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TemplateSSMDocumentDetailsProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TemplateSSMDocumentDetailsProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TemplateSSMDocumentDetailsProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 document_name: Optional[str] = None,
                 document_version: Optional[str] = None):
        """
        The TemplateSSMDocumentDetails object contains the name of the SSM document and the version of the SSM document.
        """
        if document_name is not None:
            pulumi.set(__self__, "document_name", document_name)
        if document_version is not None:
            pulumi.set(__self__, "document_version", document_version)

    @property
    @pulumi.getter(name="documentName")
    def document_name(self) -> Optional[str]:
        return pulumi.get(self, "document_name")

    @property
    @pulumi.getter(name="documentVersion")
    def document_version(self) -> Optional[str]:
        return pulumi.get(self, "document_version")


