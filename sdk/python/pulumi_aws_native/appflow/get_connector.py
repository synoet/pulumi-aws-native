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
    'GetConnectorResult',
    'AwaitableGetConnectorResult',
    'get_connector',
    'get_connector_output',
]

@pulumi.output_type
class GetConnectorResult:
    def __init__(__self__, connector_arn=None, connector_provisioning_config=None, connector_provisioning_type=None, description=None):
        if connector_arn and not isinstance(connector_arn, str):
            raise TypeError("Expected argument 'connector_arn' to be a str")
        pulumi.set(__self__, "connector_arn", connector_arn)
        if connector_provisioning_config and not isinstance(connector_provisioning_config, dict):
            raise TypeError("Expected argument 'connector_provisioning_config' to be a dict")
        pulumi.set(__self__, "connector_provisioning_config", connector_provisioning_config)
        if connector_provisioning_type and not isinstance(connector_provisioning_type, str):
            raise TypeError("Expected argument 'connector_provisioning_type' to be a str")
        pulumi.set(__self__, "connector_provisioning_type", connector_provisioning_type)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="connectorArn")
    def connector_arn(self) -> Optional[str]:
        """
         The arn of the connector. The arn is unique for each ConnectorRegistration in your AWS account.
        """
        return pulumi.get(self, "connector_arn")

    @property
    @pulumi.getter(name="connectorProvisioningConfig")
    def connector_provisioning_config(self) -> Optional['outputs.ConnectorProvisioningConfig']:
        """
        Contains information about the configuration of the connector being registered.
        """
        return pulumi.get(self, "connector_provisioning_config")

    @property
    @pulumi.getter(name="connectorProvisioningType")
    def connector_provisioning_type(self) -> Optional[str]:
        """
        The provisioning type of the connector. Currently the only supported value is LAMBDA. 
        """
        return pulumi.get(self, "connector_provisioning_type")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description about the connector that's being registered.
        """
        return pulumi.get(self, "description")


class AwaitableGetConnectorResult(GetConnectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConnectorResult(
            connector_arn=self.connector_arn,
            connector_provisioning_config=self.connector_provisioning_config,
            connector_provisioning_type=self.connector_provisioning_type,
            description=self.description)


def get_connector(connector_label: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConnectorResult:
    """
    Resource schema for AWS::AppFlow::Connector


    :param str connector_label:  The name of the connector. The name is unique for each ConnectorRegistration in your AWS account.
    """
    __args__ = dict()
    __args__['connectorLabel'] = connector_label
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:appflow:getConnector', __args__, opts=opts, typ=GetConnectorResult).value

    return AwaitableGetConnectorResult(
        connector_arn=__ret__.connector_arn,
        connector_provisioning_config=__ret__.connector_provisioning_config,
        connector_provisioning_type=__ret__.connector_provisioning_type,
        description=__ret__.description)


@_utilities.lift_output_func(get_connector)
def get_connector_output(connector_label: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConnectorResult]:
    """
    Resource schema for AWS::AppFlow::Connector


    :param str connector_label:  The name of the connector. The name is unique for each ConnectorRegistration in your AWS account.
    """
    ...
