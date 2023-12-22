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
    'GetCertificateProviderResult',
    'AwaitableGetCertificateProviderResult',
    'get_certificate_provider',
    'get_certificate_provider_output',
]

@pulumi.output_type
class GetCertificateProviderResult:
    def __init__(__self__, account_default_for_operations=None, arn=None, lambda_function_arn=None, tags=None):
        if account_default_for_operations and not isinstance(account_default_for_operations, list):
            raise TypeError("Expected argument 'account_default_for_operations' to be a list")
        pulumi.set(__self__, "account_default_for_operations", account_default_for_operations)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if lambda_function_arn and not isinstance(lambda_function_arn, str):
            raise TypeError("Expected argument 'lambda_function_arn' to be a str")
        pulumi.set(__self__, "lambda_function_arn", lambda_function_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="accountDefaultForOperations")
    def account_default_for_operations(self) -> Optional[Sequence['CertificateProviderOperation']]:
        return pulumi.get(self, "account_default_for_operations")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="lambdaFunctionArn")
    def lambda_function_arn(self) -> Optional[str]:
        return pulumi.get(self, "lambda_function_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.CertificateProviderTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetCertificateProviderResult(GetCertificateProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCertificateProviderResult(
            account_default_for_operations=self.account_default_for_operations,
            arn=self.arn,
            lambda_function_arn=self.lambda_function_arn,
            tags=self.tags)


def get_certificate_provider(certificate_provider_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCertificateProviderResult:
    """
    Use the AWS::IoT::CertificateProvider resource to declare an AWS IoT Certificate Provider.
    """
    __args__ = dict()
    __args__['certificateProviderName'] = certificate_provider_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iot:getCertificateProvider', __args__, opts=opts, typ=GetCertificateProviderResult).value

    return AwaitableGetCertificateProviderResult(
        account_default_for_operations=pulumi.get(__ret__, 'account_default_for_operations'),
        arn=pulumi.get(__ret__, 'arn'),
        lambda_function_arn=pulumi.get(__ret__, 'lambda_function_arn'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_certificate_provider)
def get_certificate_provider_output(certificate_provider_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCertificateProviderResult]:
    """
    Use the AWS::IoT::CertificateProvider resource to declare an AWS IoT Certificate Provider.
    """
    ...
