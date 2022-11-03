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
    'GetUserPoolResult',
    'AwaitableGetUserPoolResult',
    'get_user_pool',
    'get_user_pool_output',
]

@pulumi.output_type
class GetUserPoolResult:
    def __init__(__self__, account_recovery_setting=None, admin_create_user_config=None, alias_attributes=None, arn=None, auto_verified_attributes=None, deletion_protection=None, device_configuration=None, email_configuration=None, email_verification_message=None, email_verification_subject=None, enabled_mfas=None, id=None, lambda_config=None, mfa_configuration=None, policies=None, provider_name=None, provider_url=None, schema=None, sms_authentication_message=None, sms_configuration=None, sms_verification_message=None, user_attribute_update_settings=None, user_pool_add_ons=None, user_pool_name=None, user_pool_tags=None, username_attributes=None, username_configuration=None, verification_message_template=None):
        if account_recovery_setting and not isinstance(account_recovery_setting, dict):
            raise TypeError("Expected argument 'account_recovery_setting' to be a dict")
        pulumi.set(__self__, "account_recovery_setting", account_recovery_setting)
        if admin_create_user_config and not isinstance(admin_create_user_config, dict):
            raise TypeError("Expected argument 'admin_create_user_config' to be a dict")
        pulumi.set(__self__, "admin_create_user_config", admin_create_user_config)
        if alias_attributes and not isinstance(alias_attributes, list):
            raise TypeError("Expected argument 'alias_attributes' to be a list")
        pulumi.set(__self__, "alias_attributes", alias_attributes)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if auto_verified_attributes and not isinstance(auto_verified_attributes, list):
            raise TypeError("Expected argument 'auto_verified_attributes' to be a list")
        pulumi.set(__self__, "auto_verified_attributes", auto_verified_attributes)
        if deletion_protection and not isinstance(deletion_protection, str):
            raise TypeError("Expected argument 'deletion_protection' to be a str")
        pulumi.set(__self__, "deletion_protection", deletion_protection)
        if device_configuration and not isinstance(device_configuration, dict):
            raise TypeError("Expected argument 'device_configuration' to be a dict")
        pulumi.set(__self__, "device_configuration", device_configuration)
        if email_configuration and not isinstance(email_configuration, dict):
            raise TypeError("Expected argument 'email_configuration' to be a dict")
        pulumi.set(__self__, "email_configuration", email_configuration)
        if email_verification_message and not isinstance(email_verification_message, str):
            raise TypeError("Expected argument 'email_verification_message' to be a str")
        pulumi.set(__self__, "email_verification_message", email_verification_message)
        if email_verification_subject and not isinstance(email_verification_subject, str):
            raise TypeError("Expected argument 'email_verification_subject' to be a str")
        pulumi.set(__self__, "email_verification_subject", email_verification_subject)
        if enabled_mfas and not isinstance(enabled_mfas, list):
            raise TypeError("Expected argument 'enabled_mfas' to be a list")
        pulumi.set(__self__, "enabled_mfas", enabled_mfas)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lambda_config and not isinstance(lambda_config, dict):
            raise TypeError("Expected argument 'lambda_config' to be a dict")
        pulumi.set(__self__, "lambda_config", lambda_config)
        if mfa_configuration and not isinstance(mfa_configuration, str):
            raise TypeError("Expected argument 'mfa_configuration' to be a str")
        pulumi.set(__self__, "mfa_configuration", mfa_configuration)
        if policies and not isinstance(policies, dict):
            raise TypeError("Expected argument 'policies' to be a dict")
        pulumi.set(__self__, "policies", policies)
        if provider_name and not isinstance(provider_name, str):
            raise TypeError("Expected argument 'provider_name' to be a str")
        pulumi.set(__self__, "provider_name", provider_name)
        if provider_url and not isinstance(provider_url, str):
            raise TypeError("Expected argument 'provider_url' to be a str")
        pulumi.set(__self__, "provider_url", provider_url)
        if schema and not isinstance(schema, list):
            raise TypeError("Expected argument 'schema' to be a list")
        pulumi.set(__self__, "schema", schema)
        if sms_authentication_message and not isinstance(sms_authentication_message, str):
            raise TypeError("Expected argument 'sms_authentication_message' to be a str")
        pulumi.set(__self__, "sms_authentication_message", sms_authentication_message)
        if sms_configuration and not isinstance(sms_configuration, dict):
            raise TypeError("Expected argument 'sms_configuration' to be a dict")
        pulumi.set(__self__, "sms_configuration", sms_configuration)
        if sms_verification_message and not isinstance(sms_verification_message, str):
            raise TypeError("Expected argument 'sms_verification_message' to be a str")
        pulumi.set(__self__, "sms_verification_message", sms_verification_message)
        if user_attribute_update_settings and not isinstance(user_attribute_update_settings, dict):
            raise TypeError("Expected argument 'user_attribute_update_settings' to be a dict")
        pulumi.set(__self__, "user_attribute_update_settings", user_attribute_update_settings)
        if user_pool_add_ons and not isinstance(user_pool_add_ons, dict):
            raise TypeError("Expected argument 'user_pool_add_ons' to be a dict")
        pulumi.set(__self__, "user_pool_add_ons", user_pool_add_ons)
        if user_pool_name and not isinstance(user_pool_name, str):
            raise TypeError("Expected argument 'user_pool_name' to be a str")
        pulumi.set(__self__, "user_pool_name", user_pool_name)
        if user_pool_tags and not isinstance(user_pool_tags, dict):
            raise TypeError("Expected argument 'user_pool_tags' to be a dict")
        pulumi.set(__self__, "user_pool_tags", user_pool_tags)
        if username_attributes and not isinstance(username_attributes, list):
            raise TypeError("Expected argument 'username_attributes' to be a list")
        pulumi.set(__self__, "username_attributes", username_attributes)
        if username_configuration and not isinstance(username_configuration, dict):
            raise TypeError("Expected argument 'username_configuration' to be a dict")
        pulumi.set(__self__, "username_configuration", username_configuration)
        if verification_message_template and not isinstance(verification_message_template, dict):
            raise TypeError("Expected argument 'verification_message_template' to be a dict")
        pulumi.set(__self__, "verification_message_template", verification_message_template)

    @property
    @pulumi.getter(name="accountRecoverySetting")
    def account_recovery_setting(self) -> Optional['outputs.UserPoolAccountRecoverySetting']:
        return pulumi.get(self, "account_recovery_setting")

    @property
    @pulumi.getter(name="adminCreateUserConfig")
    def admin_create_user_config(self) -> Optional['outputs.UserPoolAdminCreateUserConfig']:
        return pulumi.get(self, "admin_create_user_config")

    @property
    @pulumi.getter(name="aliasAttributes")
    def alias_attributes(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "alias_attributes")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="autoVerifiedAttributes")
    def auto_verified_attributes(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "auto_verified_attributes")

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[str]:
        return pulumi.get(self, "deletion_protection")

    @property
    @pulumi.getter(name="deviceConfiguration")
    def device_configuration(self) -> Optional['outputs.UserPoolDeviceConfiguration']:
        return pulumi.get(self, "device_configuration")

    @property
    @pulumi.getter(name="emailConfiguration")
    def email_configuration(self) -> Optional['outputs.UserPoolEmailConfiguration']:
        return pulumi.get(self, "email_configuration")

    @property
    @pulumi.getter(name="emailVerificationMessage")
    def email_verification_message(self) -> Optional[str]:
        return pulumi.get(self, "email_verification_message")

    @property
    @pulumi.getter(name="emailVerificationSubject")
    def email_verification_subject(self) -> Optional[str]:
        return pulumi.get(self, "email_verification_subject")

    @property
    @pulumi.getter(name="enabledMfas")
    def enabled_mfas(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "enabled_mfas")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lambdaConfig")
    def lambda_config(self) -> Optional['outputs.UserPoolLambdaConfig']:
        return pulumi.get(self, "lambda_config")

    @property
    @pulumi.getter(name="mfaConfiguration")
    def mfa_configuration(self) -> Optional[str]:
        return pulumi.get(self, "mfa_configuration")

    @property
    @pulumi.getter
    def policies(self) -> Optional['outputs.UserPoolPolicies']:
        return pulumi.get(self, "policies")

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> Optional[str]:
        return pulumi.get(self, "provider_name")

    @property
    @pulumi.getter(name="providerURL")
    def provider_url(self) -> Optional[str]:
        return pulumi.get(self, "provider_url")

    @property
    @pulumi.getter
    def schema(self) -> Optional[Sequence['outputs.UserPoolSchemaAttribute']]:
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter(name="smsAuthenticationMessage")
    def sms_authentication_message(self) -> Optional[str]:
        return pulumi.get(self, "sms_authentication_message")

    @property
    @pulumi.getter(name="smsConfiguration")
    def sms_configuration(self) -> Optional['outputs.UserPoolSmsConfiguration']:
        return pulumi.get(self, "sms_configuration")

    @property
    @pulumi.getter(name="smsVerificationMessage")
    def sms_verification_message(self) -> Optional[str]:
        return pulumi.get(self, "sms_verification_message")

    @property
    @pulumi.getter(name="userAttributeUpdateSettings")
    def user_attribute_update_settings(self) -> Optional['outputs.UserPoolUserAttributeUpdateSettings']:
        return pulumi.get(self, "user_attribute_update_settings")

    @property
    @pulumi.getter(name="userPoolAddOns")
    def user_pool_add_ons(self) -> Optional['outputs.UserPoolAddOns']:
        return pulumi.get(self, "user_pool_add_ons")

    @property
    @pulumi.getter(name="userPoolName")
    def user_pool_name(self) -> Optional[str]:
        return pulumi.get(self, "user_pool_name")

    @property
    @pulumi.getter(name="userPoolTags")
    def user_pool_tags(self) -> Optional[Any]:
        return pulumi.get(self, "user_pool_tags")

    @property
    @pulumi.getter(name="usernameAttributes")
    def username_attributes(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "username_attributes")

    @property
    @pulumi.getter(name="usernameConfiguration")
    def username_configuration(self) -> Optional['outputs.UserPoolUsernameConfiguration']:
        return pulumi.get(self, "username_configuration")

    @property
    @pulumi.getter(name="verificationMessageTemplate")
    def verification_message_template(self) -> Optional['outputs.UserPoolVerificationMessageTemplate']:
        return pulumi.get(self, "verification_message_template")


class AwaitableGetUserPoolResult(GetUserPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserPoolResult(
            account_recovery_setting=self.account_recovery_setting,
            admin_create_user_config=self.admin_create_user_config,
            alias_attributes=self.alias_attributes,
            arn=self.arn,
            auto_verified_attributes=self.auto_verified_attributes,
            deletion_protection=self.deletion_protection,
            device_configuration=self.device_configuration,
            email_configuration=self.email_configuration,
            email_verification_message=self.email_verification_message,
            email_verification_subject=self.email_verification_subject,
            enabled_mfas=self.enabled_mfas,
            id=self.id,
            lambda_config=self.lambda_config,
            mfa_configuration=self.mfa_configuration,
            policies=self.policies,
            provider_name=self.provider_name,
            provider_url=self.provider_url,
            schema=self.schema,
            sms_authentication_message=self.sms_authentication_message,
            sms_configuration=self.sms_configuration,
            sms_verification_message=self.sms_verification_message,
            user_attribute_update_settings=self.user_attribute_update_settings,
            user_pool_add_ons=self.user_pool_add_ons,
            user_pool_name=self.user_pool_name,
            user_pool_tags=self.user_pool_tags,
            username_attributes=self.username_attributes,
            username_configuration=self.username_configuration,
            verification_message_template=self.verification_message_template)


def get_user_pool(id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserPoolResult:
    """
    Resource Type definition for AWS::Cognito::UserPool
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cognito:getUserPool', __args__, opts=opts, typ=GetUserPoolResult).value

    return AwaitableGetUserPoolResult(
        account_recovery_setting=__ret__.account_recovery_setting,
        admin_create_user_config=__ret__.admin_create_user_config,
        alias_attributes=__ret__.alias_attributes,
        arn=__ret__.arn,
        auto_verified_attributes=__ret__.auto_verified_attributes,
        deletion_protection=__ret__.deletion_protection,
        device_configuration=__ret__.device_configuration,
        email_configuration=__ret__.email_configuration,
        email_verification_message=__ret__.email_verification_message,
        email_verification_subject=__ret__.email_verification_subject,
        enabled_mfas=__ret__.enabled_mfas,
        id=__ret__.id,
        lambda_config=__ret__.lambda_config,
        mfa_configuration=__ret__.mfa_configuration,
        policies=__ret__.policies,
        provider_name=__ret__.provider_name,
        provider_url=__ret__.provider_url,
        schema=__ret__.schema,
        sms_authentication_message=__ret__.sms_authentication_message,
        sms_configuration=__ret__.sms_configuration,
        sms_verification_message=__ret__.sms_verification_message,
        user_attribute_update_settings=__ret__.user_attribute_update_settings,
        user_pool_add_ons=__ret__.user_pool_add_ons,
        user_pool_name=__ret__.user_pool_name,
        user_pool_tags=__ret__.user_pool_tags,
        username_attributes=__ret__.username_attributes,
        username_configuration=__ret__.username_configuration,
        verification_message_template=__ret__.verification_message_template)


@_utilities.lift_output_func(get_user_pool)
def get_user_pool_output(id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserPoolResult]:
    """
    Resource Type definition for AWS::Cognito::UserPool
    """
    ...
