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
    'GetDomainResult',
    'AwaitableGetDomainResult',
    'get_domain',
    'get_domain_output',
]

@pulumi.output_type
class GetDomainResult:
    def __init__(__self__, app_security_group_management=None, default_user_settings=None, domain_arn=None, domain_id=None, domain_settings=None, home_efs_file_system_id=None, security_group_id_for_domain_boundary=None, single_sign_on_managed_application_instance_id=None, url=None):
        if app_security_group_management and not isinstance(app_security_group_management, str):
            raise TypeError("Expected argument 'app_security_group_management' to be a str")
        pulumi.set(__self__, "app_security_group_management", app_security_group_management)
        if default_user_settings and not isinstance(default_user_settings, dict):
            raise TypeError("Expected argument 'default_user_settings' to be a dict")
        pulumi.set(__self__, "default_user_settings", default_user_settings)
        if domain_arn and not isinstance(domain_arn, str):
            raise TypeError("Expected argument 'domain_arn' to be a str")
        pulumi.set(__self__, "domain_arn", domain_arn)
        if domain_id and not isinstance(domain_id, str):
            raise TypeError("Expected argument 'domain_id' to be a str")
        pulumi.set(__self__, "domain_id", domain_id)
        if domain_settings and not isinstance(domain_settings, dict):
            raise TypeError("Expected argument 'domain_settings' to be a dict")
        pulumi.set(__self__, "domain_settings", domain_settings)
        if home_efs_file_system_id and not isinstance(home_efs_file_system_id, str):
            raise TypeError("Expected argument 'home_efs_file_system_id' to be a str")
        pulumi.set(__self__, "home_efs_file_system_id", home_efs_file_system_id)
        if security_group_id_for_domain_boundary and not isinstance(security_group_id_for_domain_boundary, str):
            raise TypeError("Expected argument 'security_group_id_for_domain_boundary' to be a str")
        pulumi.set(__self__, "security_group_id_for_domain_boundary", security_group_id_for_domain_boundary)
        if single_sign_on_managed_application_instance_id and not isinstance(single_sign_on_managed_application_instance_id, str):
            raise TypeError("Expected argument 'single_sign_on_managed_application_instance_id' to be a str")
        pulumi.set(__self__, "single_sign_on_managed_application_instance_id", single_sign_on_managed_application_instance_id)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="appSecurityGroupManagement")
    def app_security_group_management(self) -> Optional['DomainAppSecurityGroupManagement']:
        """
        The entity that creates and manages the required security groups for inter-app communication in VPCOnly mode. Required when CreateDomain.AppNetworkAccessType is VPCOnly and DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn is provided.
        """
        return pulumi.get(self, "app_security_group_management")

    @property
    @pulumi.getter(name="defaultUserSettings")
    def default_user_settings(self) -> Optional['outputs.DomainUserSettings']:
        """
        The default user settings.
        """
        return pulumi.get(self, "default_user_settings")

    @property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the created domain.
        """
        return pulumi.get(self, "domain_arn")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[str]:
        """
        The domain name.
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter(name="domainSettings")
    def domain_settings(self) -> Optional['outputs.DomainSettings']:
        return pulumi.get(self, "domain_settings")

    @property
    @pulumi.getter(name="homeEfsFileSystemId")
    def home_efs_file_system_id(self) -> Optional[str]:
        """
        The ID of the Amazon Elastic File System (EFS) managed by this Domain.
        """
        return pulumi.get(self, "home_efs_file_system_id")

    @property
    @pulumi.getter(name="securityGroupIdForDomainBoundary")
    def security_group_id_for_domain_boundary(self) -> Optional[str]:
        """
        The ID of the security group that authorizes traffic between the RSessionGateway apps and the RStudioServerPro app.
        """
        return pulumi.get(self, "security_group_id_for_domain_boundary")

    @property
    @pulumi.getter(name="singleSignOnManagedApplicationInstanceId")
    def single_sign_on_managed_application_instance_id(self) -> Optional[str]:
        """
        The SSO managed application instance ID.
        """
        return pulumi.get(self, "single_sign_on_managed_application_instance_id")

    @property
    @pulumi.getter
    def url(self) -> Optional[str]:
        """
        The URL to the created domain.
        """
        return pulumi.get(self, "url")


class AwaitableGetDomainResult(GetDomainResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainResult(
            app_security_group_management=self.app_security_group_management,
            default_user_settings=self.default_user_settings,
            domain_arn=self.domain_arn,
            domain_id=self.domain_id,
            domain_settings=self.domain_settings,
            home_efs_file_system_id=self.home_efs_file_system_id,
            security_group_id_for_domain_boundary=self.security_group_id_for_domain_boundary,
            single_sign_on_managed_application_instance_id=self.single_sign_on_managed_application_instance_id,
            url=self.url)


def get_domain(domain_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainResult:
    """
    Resource Type definition for AWS::SageMaker::Domain


    :param str domain_id: The domain name.
    """
    __args__ = dict()
    __args__['domainId'] = domain_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:sagemaker:getDomain', __args__, opts=opts, typ=GetDomainResult).value

    return AwaitableGetDomainResult(
        app_security_group_management=__ret__.app_security_group_management,
        default_user_settings=__ret__.default_user_settings,
        domain_arn=__ret__.domain_arn,
        domain_id=__ret__.domain_id,
        domain_settings=__ret__.domain_settings,
        home_efs_file_system_id=__ret__.home_efs_file_system_id,
        security_group_id_for_domain_boundary=__ret__.security_group_id_for_domain_boundary,
        single_sign_on_managed_application_instance_id=__ret__.single_sign_on_managed_application_instance_id,
        url=__ret__.url)


@_utilities.lift_output_func(get_domain)
def get_domain_output(domain_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainResult]:
    """
    Resource Type definition for AWS::SageMaker::Domain


    :param str domain_id: The domain name.
    """
    ...
