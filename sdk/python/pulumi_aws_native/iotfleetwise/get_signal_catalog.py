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
    'GetSignalCatalogResult',
    'AwaitableGetSignalCatalogResult',
    'get_signal_catalog',
    'get_signal_catalog_output',
]

@pulumi.output_type
class GetSignalCatalogResult:
    def __init__(__self__, arn=None, creation_time=None, description=None, last_modification_time=None, node_counts=None, nodes=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if last_modification_time and not isinstance(last_modification_time, str):
            raise TypeError("Expected argument 'last_modification_time' to be a str")
        pulumi.set(__self__, "last_modification_time", last_modification_time)
        if node_counts and not isinstance(node_counts, dict):
            raise TypeError("Expected argument 'node_counts' to be a dict")
        pulumi.set(__self__, "node_counts", node_counts)
        if nodes and not isinstance(nodes, list):
            raise TypeError("Expected argument 'nodes' to be a list")
        pulumi.set(__self__, "nodes", nodes)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastModificationTime")
    def last_modification_time(self) -> Optional[str]:
        return pulumi.get(self, "last_modification_time")

    @property
    @pulumi.getter(name="nodeCounts")
    def node_counts(self) -> Optional['outputs.SignalCatalogNodeCounts']:
        return pulumi.get(self, "node_counts")

    @property
    @pulumi.getter
    def nodes(self) -> Optional[Sequence[Any]]:
        return pulumi.get(self, "nodes")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.SignalCatalogTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetSignalCatalogResult(GetSignalCatalogResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSignalCatalogResult(
            arn=self.arn,
            creation_time=self.creation_time,
            description=self.description,
            last_modification_time=self.last_modification_time,
            node_counts=self.node_counts,
            nodes=self.nodes,
            tags=self.tags)


def get_signal_catalog(name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSignalCatalogResult:
    """
    Definition of AWS::IoTFleetWise::SignalCatalog Resource Type
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iotfleetwise:getSignalCatalog', __args__, opts=opts, typ=GetSignalCatalogResult).value

    return AwaitableGetSignalCatalogResult(
        arn=pulumi.get(__ret__, 'arn'),
        creation_time=pulumi.get(__ret__, 'creation_time'),
        description=pulumi.get(__ret__, 'description'),
        last_modification_time=pulumi.get(__ret__, 'last_modification_time'),
        node_counts=pulumi.get(__ret__, 'node_counts'),
        nodes=pulumi.get(__ret__, 'nodes'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_signal_catalog)
def get_signal_catalog_output(name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSignalCatalogResult]:
    """
    Definition of AWS::IoTFleetWise::SignalCatalog Resource Type
    """
    ...
