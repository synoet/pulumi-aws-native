# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from .. import outputs as _root_outputs

__all__ = [
    'AnalyzerArchiveRule',
    'AnalyzerAttributes',
    'AnalyzerFilter',
    'AnalyzerProperties',
]

@pulumi.output_type
class AnalyzerArchiveRule(dict):
    """
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html
    """
    def __init__(__self__, *,
                 filter: Sequence['outputs.AnalyzerFilter'],
                 rule_name: str):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html
        :param Sequence['AnalyzerFilterArgs'] filter: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html#cfn-accessanalyzer-analyzer-archiverule-filter
        :param str rule_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html#cfn-accessanalyzer-analyzer-archiverule-rulename
        """
        pulumi.set(__self__, "filter", filter)
        pulumi.set(__self__, "rule_name", rule_name)

    @property
    @pulumi.getter(name="Filter")
    def filter(self) -> Sequence['outputs.AnalyzerFilter']:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html#cfn-accessanalyzer-analyzer-archiverule-filter
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter(name="RuleName")
    def rule_name(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html#cfn-accessanalyzer-analyzer-archiverule-rulename
        """
        return pulumi.get(self, "rule_name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class AnalyzerAttributes(dict):
    def __init__(__self__, *,
                 arn: str):
        pulumi.set(__self__, "arn", arn)

    @property
    @pulumi.getter(name="Arn")
    def arn(self) -> str:
        return pulumi.get(self, "arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class AnalyzerFilter(dict):
    """
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html
    """
    def __init__(__self__, *,
                 property: str,
                 contains: Optional[Sequence[str]] = None,
                 eq: Optional[Sequence[str]] = None,
                 exists: Optional[bool] = None,
                 neq: Optional[Sequence[str]] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html
        :param str property: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-property
        :param Sequence[str] contains: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-contains
        :param Sequence[str] eq: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-eq
        :param bool exists: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-exists
        :param Sequence[str] neq: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-neq
        """
        pulumi.set(__self__, "property", property)
        if contains is not None:
            pulumi.set(__self__, "contains", contains)
        if eq is not None:
            pulumi.set(__self__, "eq", eq)
        if exists is not None:
            pulumi.set(__self__, "exists", exists)
        if neq is not None:
            pulumi.set(__self__, "neq", neq)

    @property
    @pulumi.getter(name="Contains")
    def contains(self) -> Optional[Sequence[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-contains
        """
        return pulumi.get(self, "contains")

    @property
    @pulumi.getter(name="Eq")
    def eq(self) -> Optional[Sequence[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-eq
        """
        return pulumi.get(self, "eq")

    @property
    @pulumi.getter(name="Exists")
    def exists(self) -> Optional[bool]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-exists
        """
        return pulumi.get(self, "exists")

    @property
    @pulumi.getter(name="Neq")
    def neq(self) -> Optional[Sequence[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-neq
        """
        return pulumi.get(self, "neq")

    @property
    @pulumi.getter(name="Property")
    def property(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-property
        """
        return pulumi.get(self, "property")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class AnalyzerProperties(dict):
    """
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html
    """
    def __init__(__self__, *,
                 type: str,
                 analyzer_name: Optional[str] = None,
                 archive_rules: Optional[Sequence['outputs.AnalyzerArchiveRule']] = None,
                 tags: Optional[Sequence['_root_outputs.Tag']] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html
        :param str type: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-type
        :param str analyzer_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-analyzername
        :param Sequence['AnalyzerArchiveRuleArgs'] archive_rules: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-archiverules
        :param Sequence['_root_inputs.TagArgs'] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-tags
        """
        pulumi.set(__self__, "type", type)
        if analyzer_name is not None:
            pulumi.set(__self__, "analyzer_name", analyzer_name)
        if archive_rules is not None:
            pulumi.set(__self__, "archive_rules", archive_rules)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="Type")
    def type(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="AnalyzerName")
    def analyzer_name(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-analyzername
        """
        return pulumi.get(self, "analyzer_name")

    @property
    @pulumi.getter(name="ArchiveRules")
    def archive_rules(self) -> Optional[Sequence['outputs.AnalyzerArchiveRule']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-archiverules
        """
        return pulumi.get(self, "archive_rules")

    @property
    @pulumi.getter(name="Tags")
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-tags
        """
        return pulumi.get(self, "tags")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

