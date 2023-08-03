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
    'GetGraphQlApiResult',
    'AwaitableGetGraphQlApiResult',
    'get_graph_ql_api',
    'get_graph_ql_api_output',
]

@pulumi.output_type
class GetGraphQlApiResult:
    def __init__(__self__, additional_authentication_providers=None, api_id=None, arn=None, authentication_type=None, graph_ql_dns=None, graph_ql_url=None, id=None, lambda_authorizer_config=None, log_config=None, merged_api_execution_role_arn=None, name=None, open_id_connect_config=None, owner_contact=None, realtime_dns=None, realtime_url=None, tags=None, user_pool_config=None, xray_enabled=None):
        if additional_authentication_providers and not isinstance(additional_authentication_providers, list):
            raise TypeError("Expected argument 'additional_authentication_providers' to be a list")
        pulumi.set(__self__, "additional_authentication_providers", additional_authentication_providers)
        if api_id and not isinstance(api_id, str):
            raise TypeError("Expected argument 'api_id' to be a str")
        pulumi.set(__self__, "api_id", api_id)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if authentication_type and not isinstance(authentication_type, str):
            raise TypeError("Expected argument 'authentication_type' to be a str")
        pulumi.set(__self__, "authentication_type", authentication_type)
        if graph_ql_dns and not isinstance(graph_ql_dns, str):
            raise TypeError("Expected argument 'graph_ql_dns' to be a str")
        pulumi.set(__self__, "graph_ql_dns", graph_ql_dns)
        if graph_ql_url and not isinstance(graph_ql_url, str):
            raise TypeError("Expected argument 'graph_ql_url' to be a str")
        pulumi.set(__self__, "graph_ql_url", graph_ql_url)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lambda_authorizer_config and not isinstance(lambda_authorizer_config, dict):
            raise TypeError("Expected argument 'lambda_authorizer_config' to be a dict")
        pulumi.set(__self__, "lambda_authorizer_config", lambda_authorizer_config)
        if log_config and not isinstance(log_config, dict):
            raise TypeError("Expected argument 'log_config' to be a dict")
        pulumi.set(__self__, "log_config", log_config)
        if merged_api_execution_role_arn and not isinstance(merged_api_execution_role_arn, str):
            raise TypeError("Expected argument 'merged_api_execution_role_arn' to be a str")
        pulumi.set(__self__, "merged_api_execution_role_arn", merged_api_execution_role_arn)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if open_id_connect_config and not isinstance(open_id_connect_config, dict):
            raise TypeError("Expected argument 'open_id_connect_config' to be a dict")
        pulumi.set(__self__, "open_id_connect_config", open_id_connect_config)
        if owner_contact and not isinstance(owner_contact, str):
            raise TypeError("Expected argument 'owner_contact' to be a str")
        pulumi.set(__self__, "owner_contact", owner_contact)
        if realtime_dns and not isinstance(realtime_dns, str):
            raise TypeError("Expected argument 'realtime_dns' to be a str")
        pulumi.set(__self__, "realtime_dns", realtime_dns)
        if realtime_url and not isinstance(realtime_url, str):
            raise TypeError("Expected argument 'realtime_url' to be a str")
        pulumi.set(__self__, "realtime_url", realtime_url)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if user_pool_config and not isinstance(user_pool_config, dict):
            raise TypeError("Expected argument 'user_pool_config' to be a dict")
        pulumi.set(__self__, "user_pool_config", user_pool_config)
        if xray_enabled and not isinstance(xray_enabled, bool):
            raise TypeError("Expected argument 'xray_enabled' to be a bool")
        pulumi.set(__self__, "xray_enabled", xray_enabled)

    @property
    @pulumi.getter(name="additionalAuthenticationProviders")
    def additional_authentication_providers(self) -> Optional[Sequence['outputs.GraphQlApiAdditionalAuthenticationProvider']]:
        return pulumi.get(self, "additional_authentication_providers")

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[str]:
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[str]:
        return pulumi.get(self, "authentication_type")

    @property
    @pulumi.getter(name="graphQlDns")
    def graph_ql_dns(self) -> Optional[str]:
        return pulumi.get(self, "graph_ql_dns")

    @property
    @pulumi.getter(name="graphQlUrl")
    def graph_ql_url(self) -> Optional[str]:
        return pulumi.get(self, "graph_ql_url")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(self) -> Optional['outputs.GraphQlApiLambdaAuthorizerConfig']:
        return pulumi.get(self, "lambda_authorizer_config")

    @property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional['outputs.GraphQlApiLogConfig']:
        return pulumi.get(self, "log_config")

    @property
    @pulumi.getter(name="mergedApiExecutionRoleArn")
    def merged_api_execution_role_arn(self) -> Optional[str]:
        return pulumi.get(self, "merged_api_execution_role_arn")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="openIdConnectConfig")
    def open_id_connect_config(self) -> Optional['outputs.GraphQlApiOpenIdConnectConfig']:
        return pulumi.get(self, "open_id_connect_config")

    @property
    @pulumi.getter(name="ownerContact")
    def owner_contact(self) -> Optional[str]:
        return pulumi.get(self, "owner_contact")

    @property
    @pulumi.getter(name="realtimeDns")
    def realtime_dns(self) -> Optional[str]:
        return pulumi.get(self, "realtime_dns")

    @property
    @pulumi.getter(name="realtimeUrl")
    def realtime_url(self) -> Optional[str]:
        return pulumi.get(self, "realtime_url")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.GraphQlApiTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userPoolConfig")
    def user_pool_config(self) -> Optional['outputs.GraphQlApiUserPoolConfig']:
        return pulumi.get(self, "user_pool_config")

    @property
    @pulumi.getter(name="xrayEnabled")
    def xray_enabled(self) -> Optional[bool]:
        return pulumi.get(self, "xray_enabled")


class AwaitableGetGraphQlApiResult(GetGraphQlApiResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGraphQlApiResult(
            additional_authentication_providers=self.additional_authentication_providers,
            api_id=self.api_id,
            arn=self.arn,
            authentication_type=self.authentication_type,
            graph_ql_dns=self.graph_ql_dns,
            graph_ql_url=self.graph_ql_url,
            id=self.id,
            lambda_authorizer_config=self.lambda_authorizer_config,
            log_config=self.log_config,
            merged_api_execution_role_arn=self.merged_api_execution_role_arn,
            name=self.name,
            open_id_connect_config=self.open_id_connect_config,
            owner_contact=self.owner_contact,
            realtime_dns=self.realtime_dns,
            realtime_url=self.realtime_url,
            tags=self.tags,
            user_pool_config=self.user_pool_config,
            xray_enabled=self.xray_enabled)


def get_graph_ql_api(id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGraphQlApiResult:
    """
    Resource Type definition for AWS::AppSync::GraphQLApi
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:appsync:getGraphQlApi', __args__, opts=opts, typ=GetGraphQlApiResult).value

    return AwaitableGetGraphQlApiResult(
        additional_authentication_providers=pulumi.get(__ret__, 'additional_authentication_providers'),
        api_id=pulumi.get(__ret__, 'api_id'),
        arn=pulumi.get(__ret__, 'arn'),
        authentication_type=pulumi.get(__ret__, 'authentication_type'),
        graph_ql_dns=pulumi.get(__ret__, 'graph_ql_dns'),
        graph_ql_url=pulumi.get(__ret__, 'graph_ql_url'),
        id=pulumi.get(__ret__, 'id'),
        lambda_authorizer_config=pulumi.get(__ret__, 'lambda_authorizer_config'),
        log_config=pulumi.get(__ret__, 'log_config'),
        merged_api_execution_role_arn=pulumi.get(__ret__, 'merged_api_execution_role_arn'),
        name=pulumi.get(__ret__, 'name'),
        open_id_connect_config=pulumi.get(__ret__, 'open_id_connect_config'),
        owner_contact=pulumi.get(__ret__, 'owner_contact'),
        realtime_dns=pulumi.get(__ret__, 'realtime_dns'),
        realtime_url=pulumi.get(__ret__, 'realtime_url'),
        tags=pulumi.get(__ret__, 'tags'),
        user_pool_config=pulumi.get(__ret__, 'user_pool_config'),
        xray_enabled=pulumi.get(__ret__, 'xray_enabled'))


@_utilities.lift_output_func(get_graph_ql_api)
def get_graph_ql_api_output(id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGraphQlApiResult]:
    """
    Resource Type definition for AWS::AppSync::GraphQLApi
    """
    ...
