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
from ._inputs import *

__all__ = ['NetworkInsightsAccessScopeAnalysisArgs', 'NetworkInsightsAccessScopeAnalysis']

@pulumi.input_type
class NetworkInsightsAccessScopeAnalysisArgs:
    def __init__(__self__, *,
                 network_insights_access_scope_id: pulumi.Input[str],
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsAccessScopeAnalysisTagArgs']]]] = None):
        """
        The set of arguments for constructing a NetworkInsightsAccessScopeAnalysis resource.
        """
        pulumi.set(__self__, "network_insights_access_scope_id", network_insights_access_scope_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="networkInsightsAccessScopeId")
    def network_insights_access_scope_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "network_insights_access_scope_id")

    @network_insights_access_scope_id.setter
    def network_insights_access_scope_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_insights_access_scope_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsAccessScopeAnalysisTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsAccessScopeAnalysisTagArgs']]]]):
        pulumi.set(self, "tags", value)


class NetworkInsightsAccessScopeAnalysis(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network_insights_access_scope_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInsightsAccessScopeAnalysisTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::EC2::NetworkInsightsAccessScopeAnalysis

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkInsightsAccessScopeAnalysisArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::EC2::NetworkInsightsAccessScopeAnalysis

        :param str resource_name: The name of the resource.
        :param NetworkInsightsAccessScopeAnalysisArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkInsightsAccessScopeAnalysisArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network_insights_access_scope_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInsightsAccessScopeAnalysisTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkInsightsAccessScopeAnalysisArgs.__new__(NetworkInsightsAccessScopeAnalysisArgs)

            if network_insights_access_scope_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_insights_access_scope_id'")
            __props__.__dict__["network_insights_access_scope_id"] = network_insights_access_scope_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["analyzed_eni_count"] = None
            __props__.__dict__["end_date"] = None
            __props__.__dict__["findings_found"] = None
            __props__.__dict__["network_insights_access_scope_analysis_arn"] = None
            __props__.__dict__["network_insights_access_scope_analysis_id"] = None
            __props__.__dict__["start_date"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["status_message"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["network_insights_access_scope_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(NetworkInsightsAccessScopeAnalysis, __self__).__init__(
            'aws-native:ec2:NetworkInsightsAccessScopeAnalysis',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkInsightsAccessScopeAnalysis':
        """
        Get an existing NetworkInsightsAccessScopeAnalysis resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkInsightsAccessScopeAnalysisArgs.__new__(NetworkInsightsAccessScopeAnalysisArgs)

        __props__.__dict__["analyzed_eni_count"] = None
        __props__.__dict__["end_date"] = None
        __props__.__dict__["findings_found"] = None
        __props__.__dict__["network_insights_access_scope_analysis_arn"] = None
        __props__.__dict__["network_insights_access_scope_analysis_id"] = None
        __props__.__dict__["network_insights_access_scope_id"] = None
        __props__.__dict__["start_date"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["status_message"] = None
        __props__.__dict__["tags"] = None
        return NetworkInsightsAccessScopeAnalysis(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="analyzedEniCount")
    def analyzed_eni_count(self) -> pulumi.Output[int]:
        return pulumi.get(self, "analyzed_eni_count")

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Output[str]:
        return pulumi.get(self, "end_date")

    @property
    @pulumi.getter(name="findingsFound")
    def findings_found(self) -> pulumi.Output['NetworkInsightsAccessScopeAnalysisFindingsFound']:
        return pulumi.get(self, "findings_found")

    @property
    @pulumi.getter(name="networkInsightsAccessScopeAnalysisArn")
    def network_insights_access_scope_analysis_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "network_insights_access_scope_analysis_arn")

    @property
    @pulumi.getter(name="networkInsightsAccessScopeAnalysisId")
    def network_insights_access_scope_analysis_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "network_insights_access_scope_analysis_id")

    @property
    @pulumi.getter(name="networkInsightsAccessScopeId")
    def network_insights_access_scope_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "network_insights_access_scope_id")

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Output[str]:
        return pulumi.get(self, "start_date")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['NetworkInsightsAccessScopeAnalysisStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[str]:
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.NetworkInsightsAccessScopeAnalysisTag']]]:
        return pulumi.get(self, "tags")

