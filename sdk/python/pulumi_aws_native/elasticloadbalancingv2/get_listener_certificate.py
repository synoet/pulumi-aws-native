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
    'GetListenerCertificateResult',
    'AwaitableGetListenerCertificateResult',
    'get_listener_certificate',
    'get_listener_certificate_output',
]

@pulumi.output_type
class GetListenerCertificateResult:
    def __init__(__self__, certificates=None, id=None):
        if certificates and not isinstance(certificates, list):
            raise TypeError("Expected argument 'certificates' to be a list")
        pulumi.set(__self__, "certificates", certificates)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def certificates(self) -> Optional[Sequence['outputs.ListenerCertificateCertificate']]:
        return pulumi.get(self, "certificates")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetListenerCertificateResult(GetListenerCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetListenerCertificateResult(
            certificates=self.certificates,
            id=self.id)


def get_listener_certificate(id: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetListenerCertificateResult:
    """
    Resource Type definition for AWS::ElasticLoadBalancingV2::ListenerCertificate
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:elasticloadbalancingv2:getListenerCertificate', __args__, opts=opts, typ=GetListenerCertificateResult).value

    return AwaitableGetListenerCertificateResult(
        certificates=__ret__.certificates,
        id=__ret__.id)


@_utilities.lift_output_func(get_listener_certificate)
def get_listener_certificate_output(id: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetListenerCertificateResult]:
    """
    Resource Type definition for AWS::ElasticLoadBalancingV2::ListenerCertificate
    """
    ...
