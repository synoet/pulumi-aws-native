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
from ._inputs import *

__all__ = ['ConnectorDefinitionVersionInitArgs', 'ConnectorDefinitionVersion']

@pulumi.input_type
class ConnectorDefinitionVersionInitArgs:
    def __init__(__self__, *,
                 connector_definition_id: pulumi.Input[str],
                 connectors: pulumi.Input[Sequence[pulumi.Input['ConnectorDefinitionVersionConnectorArgs']]]):
        """
        The set of arguments for constructing a ConnectorDefinitionVersion resource.
        """
        pulumi.set(__self__, "connector_definition_id", connector_definition_id)
        pulumi.set(__self__, "connectors", connectors)

    @property
    @pulumi.getter(name="connectorDefinitionId")
    def connector_definition_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "connector_definition_id")

    @connector_definition_id.setter
    def connector_definition_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "connector_definition_id", value)

    @property
    @pulumi.getter
    def connectors(self) -> pulumi.Input[Sequence[pulumi.Input['ConnectorDefinitionVersionConnectorArgs']]]:
        return pulumi.get(self, "connectors")

    @connectors.setter
    def connectors(self, value: pulumi.Input[Sequence[pulumi.Input['ConnectorDefinitionVersionConnectorArgs']]]):
        pulumi.set(self, "connectors", value)


warnings.warn("""ConnectorDefinitionVersion is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ConnectorDefinitionVersion(pulumi.CustomResource):
    warnings.warn("""ConnectorDefinitionVersion is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connector_definition_id: Optional[pulumi.Input[str]] = None,
                 connectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectorDefinitionVersionConnectorArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Greengrass::ConnectorDefinitionVersion

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectorDefinitionVersionInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Greengrass::ConnectorDefinitionVersion

        :param str resource_name: The name of the resource.
        :param ConnectorDefinitionVersionInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectorDefinitionVersionInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connector_definition_id: Optional[pulumi.Input[str]] = None,
                 connectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectorDefinitionVersionConnectorArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""ConnectorDefinitionVersion is deprecated: ConnectorDefinitionVersion is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectorDefinitionVersionInitArgs.__new__(ConnectorDefinitionVersionInitArgs)

            if connector_definition_id is None and not opts.urn:
                raise TypeError("Missing required property 'connector_definition_id'")
            __props__.__dict__["connector_definition_id"] = connector_definition_id
            if connectors is None and not opts.urn:
                raise TypeError("Missing required property 'connectors'")
            __props__.__dict__["connectors"] = connectors
        super(ConnectorDefinitionVersion, __self__).__init__(
            'aws-native:greengrass:ConnectorDefinitionVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConnectorDefinitionVersion':
        """
        Get an existing ConnectorDefinitionVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectorDefinitionVersionInitArgs.__new__(ConnectorDefinitionVersionInitArgs)

        __props__.__dict__["connector_definition_id"] = None
        __props__.__dict__["connectors"] = None
        return ConnectorDefinitionVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectorDefinitionId")
    def connector_definition_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "connector_definition_id")

    @property
    @pulumi.getter
    def connectors(self) -> pulumi.Output[Sequence['outputs.ConnectorDefinitionVersionConnector']]:
        return pulumi.get(self, "connectors")

