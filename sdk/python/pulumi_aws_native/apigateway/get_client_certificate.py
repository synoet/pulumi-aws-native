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
    'GetClientCertificateResult',
    'AwaitableGetClientCertificateResult',
    'get_client_certificate',
    'get_client_certificate_output',
]

@pulumi.output_type
class GetClientCertificateResult:
    def __init__(__self__, client_certificate_id=None, description=None, tags=None):
        if client_certificate_id and not isinstance(client_certificate_id, str):
            raise TypeError("Expected argument 'client_certificate_id' to be a str")
        pulumi.set(__self__, "client_certificate_id", client_certificate_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="clientCertificateId")
    def client_certificate_id(self) -> Optional[str]:
        return pulumi.get(self, "client_certificate_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the client certificate.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ClientCertificateTag']]:
        """
        The collection of tags. Each tag element is associated with a given resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetClientCertificateResult(GetClientCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClientCertificateResult(
            client_certificate_id=self.client_certificate_id,
            description=self.description,
            tags=self.tags)


def get_client_certificate(client_certificate_id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClientCertificateResult:
    """
    The ``AWS::ApiGateway::ClientCertificate`` resource creates a client certificate that API Gateway uses to configure client-side SSL authentication for sending requests to the integration endpoint.
    """
    __args__ = dict()
    __args__['clientCertificateId'] = client_certificate_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:apigateway:getClientCertificate', __args__, opts=opts, typ=GetClientCertificateResult).value

    return AwaitableGetClientCertificateResult(
        client_certificate_id=pulumi.get(__ret__, 'client_certificate_id'),
        description=pulumi.get(__ret__, 'description'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_client_certificate)
def get_client_certificate_output(client_certificate_id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClientCertificateResult]:
    """
    The ``AWS::ApiGateway::ClientCertificate`` resource creates a client certificate that API Gateway uses to configure client-side SSL authentication for sending requests to the integration endpoint.
    """
    ...
