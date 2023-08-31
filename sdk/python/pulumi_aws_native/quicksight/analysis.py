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

__all__ = ['AnalysisArgs', 'Analysis']

@pulumi.input_type
class AnalysisArgs:
    def __init__(__self__, *,
                 analysis_id: pulumi.Input[str],
                 aws_account_id: pulumi.Input[str],
                 definition: Optional[pulumi.Input['AnalysisDefinitionArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input['AnalysisParametersArgs']] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input['AnalysisResourcePermissionArgs']]]] = None,
                 source_entity: Optional[pulumi.Input['AnalysisSourceEntityArgs']] = None,
                 status: Optional[pulumi.Input['AnalysisResourceStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['AnalysisTagArgs']]]] = None,
                 theme_arn: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Analysis resource.
        """
        pulumi.set(__self__, "analysis_id", analysis_id)
        pulumi.set(__self__, "aws_account_id", aws_account_id)
        if definition is not None:
            pulumi.set(__self__, "definition", definition)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if source_entity is not None:
            pulumi.set(__self__, "source_entity", source_entity)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if theme_arn is not None:
            pulumi.set(__self__, "theme_arn", theme_arn)

    @property
    @pulumi.getter(name="analysisId")
    def analysis_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "analysis_id")

    @analysis_id.setter
    def analysis_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "analysis_id", value)

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "aws_account_id")

    @aws_account_id.setter
    def aws_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "aws_account_id", value)

    @property
    @pulumi.getter
    def definition(self) -> Optional[pulumi.Input['AnalysisDefinitionArgs']]:
        return pulumi.get(self, "definition")

    @definition.setter
    def definition(self, value: Optional[pulumi.Input['AnalysisDefinitionArgs']]):
        pulumi.set(self, "definition", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input['AnalysisParametersArgs']]:
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input['AnalysisParametersArgs']]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AnalysisResourcePermissionArgs']]]]:
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AnalysisResourcePermissionArgs']]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter(name="sourceEntity")
    def source_entity(self) -> Optional[pulumi.Input['AnalysisSourceEntityArgs']]:
        return pulumi.get(self, "source_entity")

    @source_entity.setter
    def source_entity(self, value: Optional[pulumi.Input['AnalysisSourceEntityArgs']]):
        pulumi.set(self, "source_entity", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['AnalysisResourceStatus']]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['AnalysisResourceStatus']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AnalysisTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AnalysisTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="themeArn")
    def theme_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "theme_arn")

    @theme_arn.setter
    def theme_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "theme_arn", value)


class Analysis(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 analysis_id: Optional[pulumi.Input[str]] = None,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 definition: Optional[pulumi.Input[pulumi.InputType['AnalysisDefinitionArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[pulumi.InputType['AnalysisParametersArgs']]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnalysisResourcePermissionArgs']]]]] = None,
                 source_entity: Optional[pulumi.Input[pulumi.InputType['AnalysisSourceEntityArgs']]] = None,
                 status: Optional[pulumi.Input['AnalysisResourceStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnalysisTagArgs']]]]] = None,
                 theme_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Definition of the AWS::QuickSight::Analysis Resource Type.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AnalysisArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of the AWS::QuickSight::Analysis Resource Type.

        :param str resource_name: The name of the resource.
        :param AnalysisArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AnalysisArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 analysis_id: Optional[pulumi.Input[str]] = None,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 definition: Optional[pulumi.Input[pulumi.InputType['AnalysisDefinitionArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[pulumi.InputType['AnalysisParametersArgs']]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnalysisResourcePermissionArgs']]]]] = None,
                 source_entity: Optional[pulumi.Input[pulumi.InputType['AnalysisSourceEntityArgs']]] = None,
                 status: Optional[pulumi.Input['AnalysisResourceStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnalysisTagArgs']]]]] = None,
                 theme_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AnalysisArgs.__new__(AnalysisArgs)

            if analysis_id is None and not opts.urn:
                raise TypeError("Missing required property 'analysis_id'")
            __props__.__dict__["analysis_id"] = analysis_id
            if aws_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'aws_account_id'")
            __props__.__dict__["aws_account_id"] = aws_account_id
            __props__.__dict__["definition"] = definition
            __props__.__dict__["name"] = name
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["permissions"] = permissions
            __props__.__dict__["source_entity"] = source_entity
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
            __props__.__dict__["theme_arn"] = theme_arn
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_time"] = None
            __props__.__dict__["data_set_arns"] = None
            __props__.__dict__["errors"] = None
            __props__.__dict__["last_updated_time"] = None
            __props__.__dict__["sheets"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["analysis_id", "aws_account_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Analysis, __self__).__init__(
            'aws-native:quicksight:Analysis',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Analysis':
        """
        Get an existing Analysis resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AnalysisArgs.__new__(AnalysisArgs)

        __props__.__dict__["analysis_id"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["aws_account_id"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["data_set_arns"] = None
        __props__.__dict__["definition"] = None
        __props__.__dict__["errors"] = None
        __props__.__dict__["last_updated_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["permissions"] = None
        __props__.__dict__["sheets"] = None
        __props__.__dict__["source_entity"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["theme_arn"] = None
        return Analysis(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="analysisId")
    def analysis_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "analysis_id")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "aws_account_id")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="dataSetArns")
    def data_set_arns(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "data_set_arns")

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Output[Optional['outputs.AnalysisDefinition']]:
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter
    def errors(self) -> pulumi.Output[Sequence['outputs.AnalysisError']]:
        return pulumi.get(self, "errors")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional['outputs.AnalysisParameters']]:
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[Sequence['outputs.AnalysisResourcePermission']]]:
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def sheets(self) -> pulumi.Output[Sequence['outputs.AnalysisSheet']]:
        return pulumi.get(self, "sheets")

    @property
    @pulumi.getter(name="sourceEntity")
    def source_entity(self) -> pulumi.Output[Optional['outputs.AnalysisSourceEntity']]:
        return pulumi.get(self, "source_entity")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional['AnalysisResourceStatus']]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.AnalysisTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="themeArn")
    def theme_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "theme_arn")

