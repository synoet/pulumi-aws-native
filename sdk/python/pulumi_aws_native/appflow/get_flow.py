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
    'GetFlowResult',
    'AwaitableGetFlowResult',
    'get_flow',
    'get_flow_output',
]

@pulumi.output_type
class GetFlowResult:
    def __init__(__self__, description=None, destination_flow_config_list=None, flow_arn=None, flow_status=None, metadata_catalog_config=None, source_flow_config=None, tags=None, tasks=None, trigger_config=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if destination_flow_config_list and not isinstance(destination_flow_config_list, list):
            raise TypeError("Expected argument 'destination_flow_config_list' to be a list")
        pulumi.set(__self__, "destination_flow_config_list", destination_flow_config_list)
        if flow_arn and not isinstance(flow_arn, str):
            raise TypeError("Expected argument 'flow_arn' to be a str")
        pulumi.set(__self__, "flow_arn", flow_arn)
        if flow_status and not isinstance(flow_status, str):
            raise TypeError("Expected argument 'flow_status' to be a str")
        pulumi.set(__self__, "flow_status", flow_status)
        if metadata_catalog_config and not isinstance(metadata_catalog_config, dict):
            raise TypeError("Expected argument 'metadata_catalog_config' to be a dict")
        pulumi.set(__self__, "metadata_catalog_config", metadata_catalog_config)
        if source_flow_config and not isinstance(source_flow_config, dict):
            raise TypeError("Expected argument 'source_flow_config' to be a dict")
        pulumi.set(__self__, "source_flow_config", source_flow_config)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if tasks and not isinstance(tasks, list):
            raise TypeError("Expected argument 'tasks' to be a list")
        pulumi.set(__self__, "tasks", tasks)
        if trigger_config and not isinstance(trigger_config, dict):
            raise TypeError("Expected argument 'trigger_config' to be a dict")
        pulumi.set(__self__, "trigger_config", trigger_config)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the flow.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destinationFlowConfigList")
    def destination_flow_config_list(self) -> Optional[Sequence['outputs.FlowDestinationFlowConfig']]:
        """
        List of Destination connectors of the flow.
        """
        return pulumi.get(self, "destination_flow_config_list")

    @property
    @pulumi.getter(name="flowArn")
    def flow_arn(self) -> Optional[str]:
        """
        ARN identifier of the flow.
        """
        return pulumi.get(self, "flow_arn")

    @property
    @pulumi.getter(name="flowStatus")
    def flow_status(self) -> Optional['FlowStatus']:
        """
        Flow activation status for Scheduled- and Event-triggered flows
        """
        return pulumi.get(self, "flow_status")

    @property
    @pulumi.getter(name="metadataCatalogConfig")
    def metadata_catalog_config(self) -> Optional['outputs.FlowMetadataCatalogConfig']:
        """
        Configurations of metadata catalog of the flow.
        """
        return pulumi.get(self, "metadata_catalog_config")

    @property
    @pulumi.getter(name="sourceFlowConfig")
    def source_flow_config(self) -> Optional['outputs.FlowSourceFlowConfig']:
        """
        Configurations of Source connector of the flow.
        """
        return pulumi.get(self, "source_flow_config")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.FlowTag']]:
        """
        List of Tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def tasks(self) -> Optional[Sequence['outputs.FlowTask']]:
        """
        List of tasks for the flow.
        """
        return pulumi.get(self, "tasks")

    @property
    @pulumi.getter(name="triggerConfig")
    def trigger_config(self) -> Optional['outputs.FlowTriggerConfig']:
        """
        Trigger settings of the flow.
        """
        return pulumi.get(self, "trigger_config")


class AwaitableGetFlowResult(GetFlowResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFlowResult(
            description=self.description,
            destination_flow_config_list=self.destination_flow_config_list,
            flow_arn=self.flow_arn,
            flow_status=self.flow_status,
            metadata_catalog_config=self.metadata_catalog_config,
            source_flow_config=self.source_flow_config,
            tags=self.tags,
            tasks=self.tasks,
            trigger_config=self.trigger_config)


def get_flow(flow_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFlowResult:
    """
    Resource schema for AWS::AppFlow::Flow.


    :param str flow_name: Name of the flow.
    """
    __args__ = dict()
    __args__['flowName'] = flow_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:appflow:getFlow', __args__, opts=opts, typ=GetFlowResult).value

    return AwaitableGetFlowResult(
        description=__ret__.description,
        destination_flow_config_list=__ret__.destination_flow_config_list,
        flow_arn=__ret__.flow_arn,
        flow_status=__ret__.flow_status,
        metadata_catalog_config=__ret__.metadata_catalog_config,
        source_flow_config=__ret__.source_flow_config,
        tags=__ret__.tags,
        tasks=__ret__.tasks,
        trigger_config=__ret__.trigger_config)


@_utilities.lift_output_func(get_flow)
def get_flow_output(flow_name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFlowResult]:
    """
    Resource schema for AWS::AppFlow::Flow.


    :param str flow_name: Name of the flow.
    """
    ...
