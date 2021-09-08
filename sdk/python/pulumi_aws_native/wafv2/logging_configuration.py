# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['LoggingConfigurationArgs', 'LoggingConfiguration']

@pulumi.input_type
class LoggingConfigurationArgs:
    def __init__(__self__, *,
                 log_destination_configs: pulumi.Input[Sequence[pulumi.Input[str]]],
                 resource_arn: pulumi.Input[str],
                 logging_filter: Optional[pulumi.Input[Union[Any, str]]] = None,
                 redacted_fields: Optional[pulumi.Input[Sequence[pulumi.Input['LoggingConfigurationFieldToMatchArgs']]]] = None):
        """
        The set of arguments for constructing a LoggingConfiguration resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] log_destination_configs: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-logdestinationconfigs
        :param pulumi.Input[str] resource_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-resourcearn
        :param pulumi.Input[Union[Any, str]] logging_filter: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-loggingfilter
        :param pulumi.Input[Sequence[pulumi.Input['LoggingConfigurationFieldToMatchArgs']]] redacted_fields: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-redactedfields
        """
        pulumi.set(__self__, "log_destination_configs", log_destination_configs)
        pulumi.set(__self__, "resource_arn", resource_arn)
        if logging_filter is not None:
            pulumi.set(__self__, "logging_filter", logging_filter)
        if redacted_fields is not None:
            pulumi.set(__self__, "redacted_fields", redacted_fields)

    @property
    @pulumi.getter(name="logDestinationConfigs")
    def log_destination_configs(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-logdestinationconfigs
        """
        return pulumi.get(self, "log_destination_configs")

    @log_destination_configs.setter
    def log_destination_configs(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "log_destination_configs", value)

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-resourcearn
        """
        return pulumi.get(self, "resource_arn")

    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_arn", value)

    @property
    @pulumi.getter(name="loggingFilter")
    def logging_filter(self) -> Optional[pulumi.Input[Union[Any, str]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-loggingfilter
        """
        return pulumi.get(self, "logging_filter")

    @logging_filter.setter
    def logging_filter(self, value: Optional[pulumi.Input[Union[Any, str]]]):
        pulumi.set(self, "logging_filter", value)

    @property
    @pulumi.getter(name="redactedFields")
    def redacted_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LoggingConfigurationFieldToMatchArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-redactedfields
        """
        return pulumi.get(self, "redacted_fields")

    @redacted_fields.setter
    def redacted_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LoggingConfigurationFieldToMatchArgs']]]]):
        pulumi.set(self, "redacted_fields", value)


class LoggingConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 log_destination_configs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 logging_filter: Optional[pulumi.Input[Union[Any, str]]] = None,
                 redacted_fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoggingConfigurationFieldToMatchArgs']]]]] = None,
                 resource_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] log_destination_configs: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-logdestinationconfigs
        :param pulumi.Input[Union[Any, str]] logging_filter: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-loggingfilter
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoggingConfigurationFieldToMatchArgs']]]] redacted_fields: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-redactedfields
        :param pulumi.Input[str] resource_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-resourcearn
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LoggingConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html

        :param str resource_name: The name of the resource.
        :param LoggingConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LoggingConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 log_destination_configs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 logging_filter: Optional[pulumi.Input[Union[Any, str]]] = None,
                 redacted_fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoggingConfigurationFieldToMatchArgs']]]]] = None,
                 resource_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LoggingConfigurationArgs.__new__(LoggingConfigurationArgs)

            if log_destination_configs is None and not opts.urn:
                raise TypeError("Missing required property 'log_destination_configs'")
            __props__.__dict__["log_destination_configs"] = log_destination_configs
            __props__.__dict__["logging_filter"] = logging_filter
            __props__.__dict__["redacted_fields"] = redacted_fields
            if resource_arn is None and not opts.urn:
                raise TypeError("Missing required property 'resource_arn'")
            __props__.__dict__["resource_arn"] = resource_arn
            __props__.__dict__["managed_by_firewall_manager"] = None
        super(LoggingConfiguration, __self__).__init__(
            'aws-native:wafv2:LoggingConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LoggingConfiguration':
        """
        Get an existing LoggingConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LoggingConfigurationArgs.__new__(LoggingConfigurationArgs)

        __props__.__dict__["log_destination_configs"] = None
        __props__.__dict__["logging_filter"] = None
        __props__.__dict__["managed_by_firewall_manager"] = None
        __props__.__dict__["redacted_fields"] = None
        __props__.__dict__["resource_arn"] = None
        return LoggingConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="logDestinationConfigs")
    def log_destination_configs(self) -> pulumi.Output[Sequence[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-logdestinationconfigs
        """
        return pulumi.get(self, "log_destination_configs")

    @property
    @pulumi.getter(name="loggingFilter")
    def logging_filter(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-loggingfilter
        """
        return pulumi.get(self, "logging_filter")

    @property
    @pulumi.getter(name="managedByFirewallManager")
    def managed_by_firewall_manager(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "managed_by_firewall_manager")

    @property
    @pulumi.getter(name="redactedFields")
    def redacted_fields(self) -> pulumi.Output[Optional[Sequence['outputs.LoggingConfigurationFieldToMatch']]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-redactedfields
        """
        return pulumi.get(self, "redacted_fields")

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-resourcearn
        """
        return pulumi.get(self, "resource_arn")

