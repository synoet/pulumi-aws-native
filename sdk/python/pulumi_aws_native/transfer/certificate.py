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

__all__ = ['CertificateArgs', 'Certificate']

@pulumi.input_type
class CertificateArgs:
    def __init__(__self__, *,
                 certificate: pulumi.Input[str],
                 usage: pulumi.Input['CertificateUsage'],
                 active_date: Optional[pulumi.Input[str]] = None,
                 certificate_chain: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 inactive_date: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['CertificateTagArgs']]]] = None):
        """
        The set of arguments for constructing a Certificate resource.
        :param pulumi.Input[str] certificate: Specifies the certificate body to be imported.
        :param pulumi.Input['CertificateUsage'] usage: Specifies the usage type for the certificate.
        :param pulumi.Input[str] active_date: Specifies the active date for the certificate.
        :param pulumi.Input[str] certificate_chain: Specifies the certificate chain to be imported.
        :param pulumi.Input[str] description: A textual description for the certificate.
        :param pulumi.Input[str] inactive_date: Specifies the inactive date for the certificate.
        :param pulumi.Input[str] private_key: Specifies the private key for the certificate.
        :param pulumi.Input[Sequence[pulumi.Input['CertificateTagArgs']]] tags: Key-value pairs that can be used to group and search for certificates. Tags are metadata attached to certificates for any purpose.
        """
        pulumi.set(__self__, "certificate", certificate)
        pulumi.set(__self__, "usage", usage)
        if active_date is not None:
            pulumi.set(__self__, "active_date", active_date)
        if certificate_chain is not None:
            pulumi.set(__self__, "certificate_chain", certificate_chain)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if inactive_date is not None:
            pulumi.set(__self__, "inactive_date", inactive_date)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Input[str]:
        """
        Specifies the certificate body to be imported.
        """
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: pulumi.Input[str]):
        pulumi.set(self, "certificate", value)

    @property
    @pulumi.getter
    def usage(self) -> pulumi.Input['CertificateUsage']:
        """
        Specifies the usage type for the certificate.
        """
        return pulumi.get(self, "usage")

    @usage.setter
    def usage(self, value: pulumi.Input['CertificateUsage']):
        pulumi.set(self, "usage", value)

    @property
    @pulumi.getter(name="activeDate")
    def active_date(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the active date for the certificate.
        """
        return pulumi.get(self, "active_date")

    @active_date.setter
    def active_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "active_date", value)

    @property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the certificate chain to be imported.
        """
        return pulumi.get(self, "certificate_chain")

    @certificate_chain.setter
    def certificate_chain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_chain", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A textual description for the certificate.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="inactiveDate")
    def inactive_date(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the inactive date for the certificate.
        """
        return pulumi.get(self, "inactive_date")

    @inactive_date.setter
    def inactive_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "inactive_date", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the private key for the certificate.
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CertificateTagArgs']]]]:
        """
        Key-value pairs that can be used to group and search for certificates. Tags are metadata attached to certificates for any purpose.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CertificateTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Certificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active_date: Optional[pulumi.Input[str]] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 certificate_chain: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 inactive_date: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CertificateTagArgs']]]]] = None,
                 usage: Optional[pulumi.Input['CertificateUsage']] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Transfer::Certificate

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] active_date: Specifies the active date for the certificate.
        :param pulumi.Input[str] certificate: Specifies the certificate body to be imported.
        :param pulumi.Input[str] certificate_chain: Specifies the certificate chain to be imported.
        :param pulumi.Input[str] description: A textual description for the certificate.
        :param pulumi.Input[str] inactive_date: Specifies the inactive date for the certificate.
        :param pulumi.Input[str] private_key: Specifies the private key for the certificate.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CertificateTagArgs']]]] tags: Key-value pairs that can be used to group and search for certificates. Tags are metadata attached to certificates for any purpose.
        :param pulumi.Input['CertificateUsage'] usage: Specifies the usage type for the certificate.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Transfer::Certificate

        :param str resource_name: The name of the resource.
        :param CertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active_date: Optional[pulumi.Input[str]] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 certificate_chain: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 inactive_date: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CertificateTagArgs']]]]] = None,
                 usage: Optional[pulumi.Input['CertificateUsage']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CertificateArgs.__new__(CertificateArgs)

            __props__.__dict__["active_date"] = active_date
            if certificate is None and not opts.urn:
                raise TypeError("Missing required property 'certificate'")
            __props__.__dict__["certificate"] = certificate
            __props__.__dict__["certificate_chain"] = certificate_chain
            __props__.__dict__["description"] = description
            __props__.__dict__["inactive_date"] = inactive_date
            __props__.__dict__["private_key"] = private_key
            __props__.__dict__["tags"] = tags
            if usage is None and not opts.urn:
                raise TypeError("Missing required property 'usage'")
            __props__.__dict__["usage"] = usage
            __props__.__dict__["arn"] = None
            __props__.__dict__["certificate_id"] = None
            __props__.__dict__["not_after_date"] = None
            __props__.__dict__["not_before_date"] = None
            __props__.__dict__["serial"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["certificate", "certificate_chain", "private_key"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Certificate, __self__).__init__(
            'aws-native:transfer:Certificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Certificate':
        """
        Get an existing Certificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CertificateArgs.__new__(CertificateArgs)

        __props__.__dict__["active_date"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["certificate"] = None
        __props__.__dict__["certificate_chain"] = None
        __props__.__dict__["certificate_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["inactive_date"] = None
        __props__.__dict__["not_after_date"] = None
        __props__.__dict__["not_before_date"] = None
        __props__.__dict__["private_key"] = None
        __props__.__dict__["serial"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["usage"] = None
        return Certificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="activeDate")
    def active_date(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the active date for the certificate.
        """
        return pulumi.get(self, "active_date")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Specifies the unique Amazon Resource Name (ARN) for the agreement.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[str]:
        """
        Specifies the certificate body to be imported.
        """
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the certificate chain to be imported.
        """
        return pulumi.get(self, "certificate_chain")

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> pulumi.Output[str]:
        """
        A unique identifier for the certificate.
        """
        return pulumi.get(self, "certificate_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A textual description for the certificate.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="inactiveDate")
    def inactive_date(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the inactive date for the certificate.
        """
        return pulumi.get(self, "inactive_date")

    @property
    @pulumi.getter(name="notAfterDate")
    def not_after_date(self) -> pulumi.Output[str]:
        """
        Specifies the not after date for the certificate.
        """
        return pulumi.get(self, "not_after_date")

    @property
    @pulumi.getter(name="notBeforeDate")
    def not_before_date(self) -> pulumi.Output[str]:
        """
        Specifies the not before date for the certificate.
        """
        return pulumi.get(self, "not_before_date")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the private key for the certificate.
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter
    def serial(self) -> pulumi.Output[str]:
        """
        Specifies Certificate's serial.
        """
        return pulumi.get(self, "serial")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['CertificateStatus']:
        """
        A status description for the certificate.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.CertificateTag']]]:
        """
        Key-value pairs that can be used to group and search for certificates. Tags are metadata attached to certificates for any purpose.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output['CertificateType']:
        """
        Describing the type of certificate. With or without a private key.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def usage(self) -> pulumi.Output['CertificateUsage']:
        """
        Specifies the usage type for the certificate.
        """
        return pulumi.get(self, "usage")

