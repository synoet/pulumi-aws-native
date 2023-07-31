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
    'GetDataSourceResult',
    'AwaitableGetDataSourceResult',
    'get_data_source',
    'get_data_source_output',
]

@pulumi.output_type
class GetDataSourceResult:
    def __init__(__self__, data_source_arn=None, description=None, dynamo_db_config=None, elasticsearch_config=None, event_bridge_config=None, http_config=None, id=None, lambda_config=None, open_search_service_config=None, relational_database_config=None, service_role_arn=None, type=None):
        if data_source_arn and not isinstance(data_source_arn, str):
            raise TypeError("Expected argument 'data_source_arn' to be a str")
        pulumi.set(__self__, "data_source_arn", data_source_arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if dynamo_db_config and not isinstance(dynamo_db_config, dict):
            raise TypeError("Expected argument 'dynamo_db_config' to be a dict")
        pulumi.set(__self__, "dynamo_db_config", dynamo_db_config)
        if elasticsearch_config and not isinstance(elasticsearch_config, dict):
            raise TypeError("Expected argument 'elasticsearch_config' to be a dict")
        pulumi.set(__self__, "elasticsearch_config", elasticsearch_config)
        if event_bridge_config and not isinstance(event_bridge_config, dict):
            raise TypeError("Expected argument 'event_bridge_config' to be a dict")
        pulumi.set(__self__, "event_bridge_config", event_bridge_config)
        if http_config and not isinstance(http_config, dict):
            raise TypeError("Expected argument 'http_config' to be a dict")
        pulumi.set(__self__, "http_config", http_config)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lambda_config and not isinstance(lambda_config, dict):
            raise TypeError("Expected argument 'lambda_config' to be a dict")
        pulumi.set(__self__, "lambda_config", lambda_config)
        if open_search_service_config and not isinstance(open_search_service_config, dict):
            raise TypeError("Expected argument 'open_search_service_config' to be a dict")
        pulumi.set(__self__, "open_search_service_config", open_search_service_config)
        if relational_database_config and not isinstance(relational_database_config, dict):
            raise TypeError("Expected argument 'relational_database_config' to be a dict")
        pulumi.set(__self__, "relational_database_config", relational_database_config)
        if service_role_arn and not isinstance(service_role_arn, str):
            raise TypeError("Expected argument 'service_role_arn' to be a str")
        pulumi.set(__self__, "service_role_arn", service_role_arn)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="dataSourceArn")
    def data_source_arn(self) -> Optional[str]:
        return pulumi.get(self, "data_source_arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dynamoDbConfig")
    def dynamo_db_config(self) -> Optional['outputs.DataSourceDynamoDBConfig']:
        return pulumi.get(self, "dynamo_db_config")

    @property
    @pulumi.getter(name="elasticsearchConfig")
    def elasticsearch_config(self) -> Optional['outputs.DataSourceElasticsearchConfig']:
        return pulumi.get(self, "elasticsearch_config")

    @property
    @pulumi.getter(name="eventBridgeConfig")
    def event_bridge_config(self) -> Optional['outputs.DataSourceEventBridgeConfig']:
        return pulumi.get(self, "event_bridge_config")

    @property
    @pulumi.getter(name="httpConfig")
    def http_config(self) -> Optional['outputs.DataSourceHttpConfig']:
        return pulumi.get(self, "http_config")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lambdaConfig")
    def lambda_config(self) -> Optional['outputs.DataSourceLambdaConfig']:
        return pulumi.get(self, "lambda_config")

    @property
    @pulumi.getter(name="openSearchServiceConfig")
    def open_search_service_config(self) -> Optional['outputs.DataSourceOpenSearchServiceConfig']:
        return pulumi.get(self, "open_search_service_config")

    @property
    @pulumi.getter(name="relationalDatabaseConfig")
    def relational_database_config(self) -> Optional['outputs.DataSourceRelationalDatabaseConfig']:
        return pulumi.get(self, "relational_database_config")

    @property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> Optional[str]:
        return pulumi.get(self, "service_role_arn")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")


class AwaitableGetDataSourceResult(GetDataSourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataSourceResult(
            data_source_arn=self.data_source_arn,
            description=self.description,
            dynamo_db_config=self.dynamo_db_config,
            elasticsearch_config=self.elasticsearch_config,
            event_bridge_config=self.event_bridge_config,
            http_config=self.http_config,
            id=self.id,
            lambda_config=self.lambda_config,
            open_search_service_config=self.open_search_service_config,
            relational_database_config=self.relational_database_config,
            service_role_arn=self.service_role_arn,
            type=self.type)


def get_data_source(id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataSourceResult:
    """
    Resource Type definition for AWS::AppSync::DataSource
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:appsync:getDataSource', __args__, opts=opts, typ=GetDataSourceResult).value

    return AwaitableGetDataSourceResult(
        data_source_arn=pulumi.get(__ret__, 'data_source_arn'),
        description=pulumi.get(__ret__, 'description'),
        dynamo_db_config=pulumi.get(__ret__, 'dynamo_db_config'),
        elasticsearch_config=pulumi.get(__ret__, 'elasticsearch_config'),
        event_bridge_config=pulumi.get(__ret__, 'event_bridge_config'),
        http_config=pulumi.get(__ret__, 'http_config'),
        id=pulumi.get(__ret__, 'id'),
        lambda_config=pulumi.get(__ret__, 'lambda_config'),
        open_search_service_config=pulumi.get(__ret__, 'open_search_service_config'),
        relational_database_config=pulumi.get(__ret__, 'relational_database_config'),
        service_role_arn=pulumi.get(__ret__, 'service_role_arn'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_data_source)
def get_data_source_output(id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDataSourceResult]:
    """
    Resource Type definition for AWS::AppSync::DataSource
    """
    ...
