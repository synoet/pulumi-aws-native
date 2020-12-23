# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'ActivityPropertiesArgs',
    'ActivityTagsEntryArgs',
    'StateMachineCloudWatchLogsLogGroupArgs',
    'StateMachineDefinitionSubstitutionsArgs',
    'StateMachineLogDestinationArgs',
    'StateMachineLoggingConfigurationArgs',
    'StateMachinePropertiesArgs',
    'StateMachineS3LocationArgs',
    'StateMachineTagsEntryArgs',
    'StateMachineTracingConfigurationArgs',
]

@pulumi.input_type
class ActivityPropertiesArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ActivityTagsEntryArgs']]]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html
        :param pulumi.Input[str] name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#cfn-stepfunctions-activity-name
        :param pulumi.Input[Sequence[pulumi.Input['ActivityTagsEntryArgs']]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#cfn-stepfunctions-activity-tags
        """
        pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="Name")
    def name(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#cfn-stepfunctions-activity-name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="Tags")
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ActivityTagsEntryArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#cfn-stepfunctions-activity-tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ActivityTagsEntryArgs']]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class ActivityTagsEntryArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html
        :param pulumi.Input[str] key: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html#cfn-stepfunctions-activity-tagsentry-key
        :param pulumi.Input[str] value: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html#cfn-stepfunctions-activity-tagsentry-value
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="Key")
    def key(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html#cfn-stepfunctions-activity-tagsentry-key
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="Value")
    def value(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html#cfn-stepfunctions-activity-tagsentry-value
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class StateMachineCloudWatchLogsLogGroupArgs:
    def __init__(__self__, *,
                 log_group_arn: Optional[pulumi.Input[str]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html
        :param pulumi.Input[str] log_group_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html#cfn-stepfunctions-statemachine-cloudwatchlogsloggroup-loggrouparn
        """
        if log_group_arn is not None:
            pulumi.set(__self__, "log_group_arn", log_group_arn)

    @property
    @pulumi.getter(name="LogGroupArn")
    def log_group_arn(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html#cfn-stepfunctions-statemachine-cloudwatchlogsloggroup-loggrouparn
        """
        return pulumi.get(self, "log_group_arn")

    @log_group_arn.setter
    def log_group_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_group_arn", value)


@pulumi.input_type
class StateMachineDefinitionSubstitutionsArgs:
    def __init__(__self__):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-definitionsubstitutions.html
        """
        pass


@pulumi.input_type
class StateMachineLogDestinationArgs:
    def __init__(__self__, *,
                 cloud_watch_logs_log_group: Optional[pulumi.Input['StateMachineCloudWatchLogsLogGroupArgs']] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html
        :param pulumi.Input['StateMachineCloudWatchLogsLogGroupArgs'] cloud_watch_logs_log_group: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html#cfn-stepfunctions-statemachine-logdestination-cloudwatchlogsloggroup
        """
        if cloud_watch_logs_log_group is not None:
            pulumi.set(__self__, "cloud_watch_logs_log_group", cloud_watch_logs_log_group)

    @property
    @pulumi.getter(name="CloudWatchLogsLogGroup")
    def cloud_watch_logs_log_group(self) -> Optional[pulumi.Input['StateMachineCloudWatchLogsLogGroupArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html#cfn-stepfunctions-statemachine-logdestination-cloudwatchlogsloggroup
        """
        return pulumi.get(self, "cloud_watch_logs_log_group")

    @cloud_watch_logs_log_group.setter
    def cloud_watch_logs_log_group(self, value: Optional[pulumi.Input['StateMachineCloudWatchLogsLogGroupArgs']]):
        pulumi.set(self, "cloud_watch_logs_log_group", value)


@pulumi.input_type
class StateMachineLoggingConfigurationArgs:
    def __init__(__self__, *,
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input['StateMachineLogDestinationArgs']]]] = None,
                 include_execution_data: Optional[pulumi.Input[bool]] = None,
                 level: Optional[pulumi.Input[str]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html
        :param pulumi.Input[Sequence[pulumi.Input['StateMachineLogDestinationArgs']]] destinations: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-destinations
        :param pulumi.Input[bool] include_execution_data: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-includeexecutiondata
        :param pulumi.Input[str] level: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-level
        """
        if destinations is not None:
            pulumi.set(__self__, "destinations", destinations)
        if include_execution_data is not None:
            pulumi.set(__self__, "include_execution_data", include_execution_data)
        if level is not None:
            pulumi.set(__self__, "level", level)

    @property
    @pulumi.getter(name="Destinations")
    def destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StateMachineLogDestinationArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-destinations
        """
        return pulumi.get(self, "destinations")

    @destinations.setter
    def destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StateMachineLogDestinationArgs']]]]):
        pulumi.set(self, "destinations", value)

    @property
    @pulumi.getter(name="IncludeExecutionData")
    def include_execution_data(self) -> Optional[pulumi.Input[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-includeexecutiondata
        """
        return pulumi.get(self, "include_execution_data")

    @include_execution_data.setter
    def include_execution_data(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_execution_data", value)

    @property
    @pulumi.getter(name="Level")
    def level(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-level
        """
        return pulumi.get(self, "level")

    @level.setter
    def level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "level", value)


@pulumi.input_type
class StateMachinePropertiesArgs:
    def __init__(__self__, *,
                 role_arn: pulumi.Input[str],
                 definition_s3_location: Optional[pulumi.Input['StateMachineS3LocationArgs']] = None,
                 definition_string: Optional[pulumi.Input[str]] = None,
                 definition_substitutions: Optional[pulumi.Input['StateMachineDefinitionSubstitutionsArgs']] = None,
                 logging_configuration: Optional[pulumi.Input['StateMachineLoggingConfigurationArgs']] = None,
                 state_machine_name: Optional[pulumi.Input[str]] = None,
                 state_machine_type: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['StateMachineTagsEntryArgs']]]] = None,
                 tracing_configuration: Optional[pulumi.Input['StateMachineTracingConfigurationArgs']] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html
        :param pulumi.Input[str] role_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-rolearn
        :param pulumi.Input['StateMachineS3LocationArgs'] definition_s3_location: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitions3location
        :param pulumi.Input[str] definition_string: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionstring
        :param pulumi.Input['StateMachineDefinitionSubstitutionsArgs'] definition_substitutions: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionsubstitutions
        :param pulumi.Input['StateMachineLoggingConfigurationArgs'] logging_configuration: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-loggingconfiguration
        :param pulumi.Input[str] state_machine_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinename
        :param pulumi.Input[str] state_machine_type: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinetype
        :param pulumi.Input[Sequence[pulumi.Input['StateMachineTagsEntryArgs']]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tags
        :param pulumi.Input['StateMachineTracingConfigurationArgs'] tracing_configuration: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tracingconfiguration
        """
        pulumi.set(__self__, "role_arn", role_arn)
        if definition_s3_location is not None:
            pulumi.set(__self__, "definition_s3_location", definition_s3_location)
        if definition_string is not None:
            pulumi.set(__self__, "definition_string", definition_string)
        if definition_substitutions is not None:
            pulumi.set(__self__, "definition_substitutions", definition_substitutions)
        if logging_configuration is not None:
            pulumi.set(__self__, "logging_configuration", logging_configuration)
        if state_machine_name is not None:
            pulumi.set(__self__, "state_machine_name", state_machine_name)
        if state_machine_type is not None:
            pulumi.set(__self__, "state_machine_type", state_machine_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tracing_configuration is not None:
            pulumi.set(__self__, "tracing_configuration", tracing_configuration)

    @property
    @pulumi.getter(name="RoleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-rolearn
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="DefinitionS3Location")
    def definition_s3_location(self) -> Optional[pulumi.Input['StateMachineS3LocationArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitions3location
        """
        return pulumi.get(self, "definition_s3_location")

    @definition_s3_location.setter
    def definition_s3_location(self, value: Optional[pulumi.Input['StateMachineS3LocationArgs']]):
        pulumi.set(self, "definition_s3_location", value)

    @property
    @pulumi.getter(name="DefinitionString")
    def definition_string(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionstring
        """
        return pulumi.get(self, "definition_string")

    @definition_string.setter
    def definition_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "definition_string", value)

    @property
    @pulumi.getter(name="DefinitionSubstitutions")
    def definition_substitutions(self) -> Optional[pulumi.Input['StateMachineDefinitionSubstitutionsArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionsubstitutions
        """
        return pulumi.get(self, "definition_substitutions")

    @definition_substitutions.setter
    def definition_substitutions(self, value: Optional[pulumi.Input['StateMachineDefinitionSubstitutionsArgs']]):
        pulumi.set(self, "definition_substitutions", value)

    @property
    @pulumi.getter(name="LoggingConfiguration")
    def logging_configuration(self) -> Optional[pulumi.Input['StateMachineLoggingConfigurationArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-loggingconfiguration
        """
        return pulumi.get(self, "logging_configuration")

    @logging_configuration.setter
    def logging_configuration(self, value: Optional[pulumi.Input['StateMachineLoggingConfigurationArgs']]):
        pulumi.set(self, "logging_configuration", value)

    @property
    @pulumi.getter(name="StateMachineName")
    def state_machine_name(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinename
        """
        return pulumi.get(self, "state_machine_name")

    @state_machine_name.setter
    def state_machine_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state_machine_name", value)

    @property
    @pulumi.getter(name="StateMachineType")
    def state_machine_type(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinetype
        """
        return pulumi.get(self, "state_machine_type")

    @state_machine_type.setter
    def state_machine_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state_machine_type", value)

    @property
    @pulumi.getter(name="Tags")
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StateMachineTagsEntryArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StateMachineTagsEntryArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="TracingConfiguration")
    def tracing_configuration(self) -> Optional[pulumi.Input['StateMachineTracingConfigurationArgs']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tracingconfiguration
        """
        return pulumi.get(self, "tracing_configuration")

    @tracing_configuration.setter
    def tracing_configuration(self, value: Optional[pulumi.Input['StateMachineTracingConfigurationArgs']]):
        pulumi.set(self, "tracing_configuration", value)


@pulumi.input_type
class StateMachineS3LocationArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 key: pulumi.Input[str],
                 version: Optional[pulumi.Input[str]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html
        :param pulumi.Input[str] bucket: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-bucket
        :param pulumi.Input[str] key: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-key
        :param pulumi.Input[str] version: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-version
        """
        pulumi.set(__self__, "bucket", bucket)
        pulumi.set(__self__, "key", key)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="Bucket")
    def bucket(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-bucket
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="Key")
    def key(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-key
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="Version")
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-version
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class StateMachineTagsEntryArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html
        :param pulumi.Input[str] key: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html#cfn-stepfunctions-statemachine-tagsentry-key
        :param pulumi.Input[str] value: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html#cfn-stepfunctions-statemachine-tagsentry-value
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="Key")
    def key(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html#cfn-stepfunctions-statemachine-tagsentry-key
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="Value")
    def value(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html#cfn-stepfunctions-statemachine-tagsentry-value
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class StateMachineTracingConfigurationArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html
        :param pulumi.Input[bool] enabled: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html#cfn-stepfunctions-statemachine-tracingconfiguration-enabled
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter(name="Enabled")
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html#cfn-stepfunctions-statemachine-tracingconfiguration-enabled
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)


