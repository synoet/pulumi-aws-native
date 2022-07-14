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
    'GetDatasetResult',
    'AwaitableGetDatasetResult',
    'get_dataset',
    'get_dataset_output',
]

@pulumi.output_type
class GetDatasetResult:
    def __init__(__self__, arn=None, data_frequency=None, dataset_type=None, domain=None, encryption_config=None, schema=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if data_frequency and not isinstance(data_frequency, str):
            raise TypeError("Expected argument 'data_frequency' to be a str")
        pulumi.set(__self__, "data_frequency", data_frequency)
        if dataset_type and not isinstance(dataset_type, str):
            raise TypeError("Expected argument 'dataset_type' to be a str")
        pulumi.set(__self__, "dataset_type", dataset_type)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if encryption_config and not isinstance(encryption_config, dict):
            raise TypeError("Expected argument 'encryption_config' to be a dict")
        pulumi.set(__self__, "encryption_config", encryption_config)
        if schema and not isinstance(schema, dict):
            raise TypeError("Expected argument 'schema' to be a dict")
        pulumi.set(__self__, "schema", schema)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="dataFrequency")
    def data_frequency(self) -> Optional[str]:
        """
        Frequency of data collection. This parameter is required for RELATED_TIME_SERIES
        """
        return pulumi.get(self, "data_frequency")

    @property
    @pulumi.getter(name="datasetType")
    def dataset_type(self) -> Optional['DatasetType']:
        """
        The dataset type
        """
        return pulumi.get(self, "dataset_type")

    @property
    @pulumi.getter
    def domain(self) -> Optional['DatasetDomain']:
        """
        The domain associated with the dataset
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional['outputs.EncryptionConfigProperties']:
        return pulumi.get(self, "encryption_config")

    @property
    @pulumi.getter
    def schema(self) -> Optional['outputs.SchemaProperties']:
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.TagsItemProperties']]:
        return pulumi.get(self, "tags")


class AwaitableGetDatasetResult(GetDatasetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatasetResult(
            arn=self.arn,
            data_frequency=self.data_frequency,
            dataset_type=self.dataset_type,
            domain=self.domain,
            encryption_config=self.encryption_config,
            schema=self.schema,
            tags=self.tags)


def get_dataset(arn: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatasetResult:
    """
    Resource Type Definition for AWS::Forecast::Dataset
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:forecast:getDataset', __args__, opts=opts, typ=GetDatasetResult).value

    return AwaitableGetDatasetResult(
        arn=__ret__.arn,
        data_frequency=__ret__.data_frequency,
        dataset_type=__ret__.dataset_type,
        domain=__ret__.domain,
        encryption_config=__ret__.encryption_config,
        schema=__ret__.schema,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_dataset)
def get_dataset_output(arn: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatasetResult]:
    """
    Resource Type Definition for AWS::Forecast::Dataset
    """
    ...
