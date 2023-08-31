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
from ._inputs import *

__all__ = ['DomainConfigurationArgs', 'DomainConfiguration']

@pulumi.input_type
class DomainConfigurationArgs:
    def __init__(__self__, *,
                 authorizer_config: Optional[pulumi.Input['DomainConfigurationAuthorizerConfigArgs']] = None,
                 domain_configuration_name: Optional[pulumi.Input[str]] = None,
                 domain_configuration_status: Optional[pulumi.Input['DomainConfigurationStatus']] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 server_certificate_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_type: Optional[pulumi.Input['DomainConfigurationServiceType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DomainConfigurationTagArgs']]]] = None,
                 tls_config: Optional[pulumi.Input['DomainConfigurationTlsConfigArgs']] = None,
                 validation_certificate_arn: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DomainConfiguration resource.
        """
        if authorizer_config is not None:
            pulumi.set(__self__, "authorizer_config", authorizer_config)
        if domain_configuration_name is not None:
            pulumi.set(__self__, "domain_configuration_name", domain_configuration_name)
        if domain_configuration_status is not None:
            pulumi.set(__self__, "domain_configuration_status", domain_configuration_status)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if server_certificate_arns is not None:
            pulumi.set(__self__, "server_certificate_arns", server_certificate_arns)
        if service_type is not None:
            pulumi.set(__self__, "service_type", service_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tls_config is not None:
            pulumi.set(__self__, "tls_config", tls_config)
        if validation_certificate_arn is not None:
            pulumi.set(__self__, "validation_certificate_arn", validation_certificate_arn)

    @property
    @pulumi.getter(name="authorizerConfig")
    def authorizer_config(self) -> Optional[pulumi.Input['DomainConfigurationAuthorizerConfigArgs']]:
        return pulumi.get(self, "authorizer_config")

    @authorizer_config.setter
    def authorizer_config(self, value: Optional[pulumi.Input['DomainConfigurationAuthorizerConfigArgs']]):
        pulumi.set(self, "authorizer_config", value)

    @property
    @pulumi.getter(name="domainConfigurationName")
    def domain_configuration_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "domain_configuration_name")

    @domain_configuration_name.setter
    def domain_configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_configuration_name", value)

    @property
    @pulumi.getter(name="domainConfigurationStatus")
    def domain_configuration_status(self) -> Optional[pulumi.Input['DomainConfigurationStatus']]:
        return pulumi.get(self, "domain_configuration_status")

    @domain_configuration_status.setter
    def domain_configuration_status(self, value: Optional[pulumi.Input['DomainConfigurationStatus']]):
        pulumi.set(self, "domain_configuration_status", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="serverCertificateArns")
    def server_certificate_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "server_certificate_arns")

    @server_certificate_arns.setter
    def server_certificate_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "server_certificate_arns", value)

    @property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> Optional[pulumi.Input['DomainConfigurationServiceType']]:
        return pulumi.get(self, "service_type")

    @service_type.setter
    def service_type(self, value: Optional[pulumi.Input['DomainConfigurationServiceType']]):
        pulumi.set(self, "service_type", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainConfigurationTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainConfigurationTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> Optional[pulumi.Input['DomainConfigurationTlsConfigArgs']]:
        return pulumi.get(self, "tls_config")

    @tls_config.setter
    def tls_config(self, value: Optional[pulumi.Input['DomainConfigurationTlsConfigArgs']]):
        pulumi.set(self, "tls_config", value)

    @property
    @pulumi.getter(name="validationCertificateArn")
    def validation_certificate_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "validation_certificate_arn")

    @validation_certificate_arn.setter
    def validation_certificate_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "validation_certificate_arn", value)


class DomainConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorizer_config: Optional[pulumi.Input[pulumi.InputType['DomainConfigurationAuthorizerConfigArgs']]] = None,
                 domain_configuration_name: Optional[pulumi.Input[str]] = None,
                 domain_configuration_status: Optional[pulumi.Input['DomainConfigurationStatus']] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 server_certificate_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_type: Optional[pulumi.Input['DomainConfigurationServiceType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainConfigurationTagArgs']]]]] = None,
                 tls_config: Optional[pulumi.Input[pulumi.InputType['DomainConfigurationTlsConfigArgs']]] = None,
                 validation_certificate_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create and manage a Domain Configuration

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DomainConfigurationArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create and manage a Domain Configuration

        :param str resource_name: The name of the resource.
        :param DomainConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorizer_config: Optional[pulumi.Input[pulumi.InputType['DomainConfigurationAuthorizerConfigArgs']]] = None,
                 domain_configuration_name: Optional[pulumi.Input[str]] = None,
                 domain_configuration_status: Optional[pulumi.Input['DomainConfigurationStatus']] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 server_certificate_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_type: Optional[pulumi.Input['DomainConfigurationServiceType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainConfigurationTagArgs']]]]] = None,
                 tls_config: Optional[pulumi.Input[pulumi.InputType['DomainConfigurationTlsConfigArgs']]] = None,
                 validation_certificate_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainConfigurationArgs.__new__(DomainConfigurationArgs)

            __props__.__dict__["authorizer_config"] = authorizer_config
            __props__.__dict__["domain_configuration_name"] = domain_configuration_name
            __props__.__dict__["domain_configuration_status"] = domain_configuration_status
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["server_certificate_arns"] = server_certificate_arns
            __props__.__dict__["service_type"] = service_type
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tls_config"] = tls_config
            __props__.__dict__["validation_certificate_arn"] = validation_certificate_arn
            __props__.__dict__["arn"] = None
            __props__.__dict__["domain_type"] = None
            __props__.__dict__["server_certificates"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["domain_configuration_name", "domain_name", "server_certificate_arns[*]", "service_type", "validation_certificate_arn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DomainConfiguration, __self__).__init__(
            'aws-native:iot:DomainConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DomainConfiguration':
        """
        Get an existing DomainConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DomainConfigurationArgs.__new__(DomainConfigurationArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["authorizer_config"] = None
        __props__.__dict__["domain_configuration_name"] = None
        __props__.__dict__["domain_configuration_status"] = None
        __props__.__dict__["domain_name"] = None
        __props__.__dict__["domain_type"] = None
        __props__.__dict__["server_certificate_arns"] = None
        __props__.__dict__["server_certificates"] = None
        __props__.__dict__["service_type"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["tls_config"] = None
        __props__.__dict__["validation_certificate_arn"] = None
        return DomainConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="authorizerConfig")
    def authorizer_config(self) -> pulumi.Output[Optional['outputs.DomainConfigurationAuthorizerConfig']]:
        return pulumi.get(self, "authorizer_config")

    @property
    @pulumi.getter(name="domainConfigurationName")
    def domain_configuration_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "domain_configuration_name")

    @property
    @pulumi.getter(name="domainConfigurationStatus")
    def domain_configuration_status(self) -> pulumi.Output[Optional['DomainConfigurationStatus']]:
        return pulumi.get(self, "domain_configuration_status")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="domainType")
    def domain_type(self) -> pulumi.Output['DomainConfigurationDomainType']:
        return pulumi.get(self, "domain_type")

    @property
    @pulumi.getter(name="serverCertificateArns")
    def server_certificate_arns(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "server_certificate_arns")

    @property
    @pulumi.getter(name="serverCertificates")
    def server_certificates(self) -> pulumi.Output[Sequence['outputs.DomainConfigurationServerCertificateSummary']]:
        return pulumi.get(self, "server_certificates")

    @property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> pulumi.Output[Optional['DomainConfigurationServiceType']]:
        return pulumi.get(self, "service_type")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DomainConfigurationTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> pulumi.Output[Optional['outputs.DomainConfigurationTlsConfig']]:
        return pulumi.get(self, "tls_config")

    @property
    @pulumi.getter(name="validationCertificateArn")
    def validation_certificate_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "validation_certificate_arn")

