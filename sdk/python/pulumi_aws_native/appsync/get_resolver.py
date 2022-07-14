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
    'GetResolverResult',
    'AwaitableGetResolverResult',
    'get_resolver',
    'get_resolver_output',
]

@pulumi.output_type
class GetResolverResult:
    def __init__(__self__, caching_config=None, data_source_name=None, id=None, kind=None, max_batch_size=None, pipeline_config=None, request_mapping_template=None, request_mapping_template_s3_location=None, resolver_arn=None, response_mapping_template=None, response_mapping_template_s3_location=None, sync_config=None):
        if caching_config and not isinstance(caching_config, dict):
            raise TypeError("Expected argument 'caching_config' to be a dict")
        pulumi.set(__self__, "caching_config", caching_config)
        if data_source_name and not isinstance(data_source_name, str):
            raise TypeError("Expected argument 'data_source_name' to be a str")
        pulumi.set(__self__, "data_source_name", data_source_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if max_batch_size and not isinstance(max_batch_size, int):
            raise TypeError("Expected argument 'max_batch_size' to be a int")
        pulumi.set(__self__, "max_batch_size", max_batch_size)
        if pipeline_config and not isinstance(pipeline_config, dict):
            raise TypeError("Expected argument 'pipeline_config' to be a dict")
        pulumi.set(__self__, "pipeline_config", pipeline_config)
        if request_mapping_template and not isinstance(request_mapping_template, str):
            raise TypeError("Expected argument 'request_mapping_template' to be a str")
        pulumi.set(__self__, "request_mapping_template", request_mapping_template)
        if request_mapping_template_s3_location and not isinstance(request_mapping_template_s3_location, str):
            raise TypeError("Expected argument 'request_mapping_template_s3_location' to be a str")
        pulumi.set(__self__, "request_mapping_template_s3_location", request_mapping_template_s3_location)
        if resolver_arn and not isinstance(resolver_arn, str):
            raise TypeError("Expected argument 'resolver_arn' to be a str")
        pulumi.set(__self__, "resolver_arn", resolver_arn)
        if response_mapping_template and not isinstance(response_mapping_template, str):
            raise TypeError("Expected argument 'response_mapping_template' to be a str")
        pulumi.set(__self__, "response_mapping_template", response_mapping_template)
        if response_mapping_template_s3_location and not isinstance(response_mapping_template_s3_location, str):
            raise TypeError("Expected argument 'response_mapping_template_s3_location' to be a str")
        pulumi.set(__self__, "response_mapping_template_s3_location", response_mapping_template_s3_location)
        if sync_config and not isinstance(sync_config, dict):
            raise TypeError("Expected argument 'sync_config' to be a dict")
        pulumi.set(__self__, "sync_config", sync_config)

    @property
    @pulumi.getter(name="cachingConfig")
    def caching_config(self) -> Optional['outputs.ResolverCachingConfig']:
        return pulumi.get(self, "caching_config")

    @property
    @pulumi.getter(name="dataSourceName")
    def data_source_name(self) -> Optional[str]:
        return pulumi.get(self, "data_source_name")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="maxBatchSize")
    def max_batch_size(self) -> Optional[int]:
        return pulumi.get(self, "max_batch_size")

    @property
    @pulumi.getter(name="pipelineConfig")
    def pipeline_config(self) -> Optional['outputs.ResolverPipelineConfig']:
        return pulumi.get(self, "pipeline_config")

    @property
    @pulumi.getter(name="requestMappingTemplate")
    def request_mapping_template(self) -> Optional[str]:
        return pulumi.get(self, "request_mapping_template")

    @property
    @pulumi.getter(name="requestMappingTemplateS3Location")
    def request_mapping_template_s3_location(self) -> Optional[str]:
        return pulumi.get(self, "request_mapping_template_s3_location")

    @property
    @pulumi.getter(name="resolverArn")
    def resolver_arn(self) -> Optional[str]:
        return pulumi.get(self, "resolver_arn")

    @property
    @pulumi.getter(name="responseMappingTemplate")
    def response_mapping_template(self) -> Optional[str]:
        return pulumi.get(self, "response_mapping_template")

    @property
    @pulumi.getter(name="responseMappingTemplateS3Location")
    def response_mapping_template_s3_location(self) -> Optional[str]:
        return pulumi.get(self, "response_mapping_template_s3_location")

    @property
    @pulumi.getter(name="syncConfig")
    def sync_config(self) -> Optional['outputs.ResolverSyncConfig']:
        return pulumi.get(self, "sync_config")


class AwaitableGetResolverResult(GetResolverResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResolverResult(
            caching_config=self.caching_config,
            data_source_name=self.data_source_name,
            id=self.id,
            kind=self.kind,
            max_batch_size=self.max_batch_size,
            pipeline_config=self.pipeline_config,
            request_mapping_template=self.request_mapping_template,
            request_mapping_template_s3_location=self.request_mapping_template_s3_location,
            resolver_arn=self.resolver_arn,
            response_mapping_template=self.response_mapping_template,
            response_mapping_template_s3_location=self.response_mapping_template_s3_location,
            sync_config=self.sync_config)


def get_resolver(id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResolverResult:
    """
    Resource Type definition for AWS::AppSync::Resolver
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:appsync:getResolver', __args__, opts=opts, typ=GetResolverResult).value

    return AwaitableGetResolverResult(
        caching_config=__ret__.caching_config,
        data_source_name=__ret__.data_source_name,
        id=__ret__.id,
        kind=__ret__.kind,
        max_batch_size=__ret__.max_batch_size,
        pipeline_config=__ret__.pipeline_config,
        request_mapping_template=__ret__.request_mapping_template,
        request_mapping_template_s3_location=__ret__.request_mapping_template_s3_location,
        resolver_arn=__ret__.resolver_arn,
        response_mapping_template=__ret__.response_mapping_template,
        response_mapping_template_s3_location=__ret__.response_mapping_template_s3_location,
        sync_config=__ret__.sync_config)


@_utilities.lift_output_func(get_resolver)
def get_resolver_output(id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResolverResult]:
    """
    Resource Type definition for AWS::AppSync::Resolver
    """
    ...
