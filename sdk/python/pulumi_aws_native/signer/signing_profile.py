# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['SigningProfileArgs', 'SigningProfile']

@pulumi.input_type
class SigningProfileArgs:
    def __init__(__self__, *,
                 platform_id: pulumi.Input['SigningProfilePlatformId'],
                 signature_validity_period: Optional[pulumi.Input['SigningProfileSignatureValidityPeriodArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['SigningProfileTagArgs']]]] = None):
        """
        The set of arguments for constructing a SigningProfile resource.
        :param pulumi.Input['SigningProfilePlatformId'] platform_id: The ID of the target signing platform.
        :param pulumi.Input['SigningProfileSignatureValidityPeriodArgs'] signature_validity_period: Signature validity period of the profile.
        :param pulumi.Input[Sequence[pulumi.Input['SigningProfileTagArgs']]] tags: A list of tags associated with the signing profile.
        """
        pulumi.set(__self__, "platform_id", platform_id)
        if signature_validity_period is not None:
            pulumi.set(__self__, "signature_validity_period", signature_validity_period)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="platformId")
    def platform_id(self) -> pulumi.Input['SigningProfilePlatformId']:
        """
        The ID of the target signing platform.
        """
        return pulumi.get(self, "platform_id")

    @platform_id.setter
    def platform_id(self, value: pulumi.Input['SigningProfilePlatformId']):
        pulumi.set(self, "platform_id", value)

    @property
    @pulumi.getter(name="signatureValidityPeriod")
    def signature_validity_period(self) -> Optional[pulumi.Input['SigningProfileSignatureValidityPeriodArgs']]:
        """
        Signature validity period of the profile.
        """
        return pulumi.get(self, "signature_validity_period")

    @signature_validity_period.setter
    def signature_validity_period(self, value: Optional[pulumi.Input['SigningProfileSignatureValidityPeriodArgs']]):
        pulumi.set(self, "signature_validity_period", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SigningProfileTagArgs']]]]:
        """
        A list of tags associated with the signing profile.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SigningProfileTagArgs']]]]):
        pulumi.set(self, "tags", value)


class SigningProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 platform_id: Optional[pulumi.Input['SigningProfilePlatformId']] = None,
                 signature_validity_period: Optional[pulumi.Input[pulumi.InputType['SigningProfileSignatureValidityPeriodArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SigningProfileTagArgs']]]]] = None,
                 __props__=None):
        """
        A signing profile is a signing template that can be used to carry out a pre-defined signing job.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['SigningProfilePlatformId'] platform_id: The ID of the target signing platform.
        :param pulumi.Input[pulumi.InputType['SigningProfileSignatureValidityPeriodArgs']] signature_validity_period: Signature validity period of the profile.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SigningProfileTagArgs']]]] tags: A list of tags associated with the signing profile.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SigningProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A signing profile is a signing template that can be used to carry out a pre-defined signing job.

        :param str resource_name: The name of the resource.
        :param SigningProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SigningProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 platform_id: Optional[pulumi.Input['SigningProfilePlatformId']] = None,
                 signature_validity_period: Optional[pulumi.Input[pulumi.InputType['SigningProfileSignatureValidityPeriodArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SigningProfileTagArgs']]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SigningProfileArgs.__new__(SigningProfileArgs)

            if platform_id is None and not opts.urn:
                raise TypeError("Missing required property 'platform_id'")
            __props__.__dict__["platform_id"] = platform_id
            __props__.__dict__["signature_validity_period"] = signature_validity_period
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["profile_name"] = None
            __props__.__dict__["profile_version"] = None
            __props__.__dict__["profile_version_arn"] = None
        super(SigningProfile, __self__).__init__(
            'aws-native:signer:SigningProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SigningProfile':
        """
        Get an existing SigningProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SigningProfileArgs.__new__(SigningProfileArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["platform_id"] = None
        __props__.__dict__["profile_name"] = None
        __props__.__dict__["profile_version"] = None
        __props__.__dict__["profile_version_arn"] = None
        __props__.__dict__["signature_validity_period"] = None
        __props__.__dict__["tags"] = None
        return SigningProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the specified signing profile.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="platformId")
    def platform_id(self) -> pulumi.Output['SigningProfilePlatformId']:
        """
        The ID of the target signing platform.
        """
        return pulumi.get(self, "platform_id")

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Output[str]:
        """
        A name for the signing profile. AWS CloudFormation generates a unique physical ID and uses that ID for the signing profile name. 
        """
        return pulumi.get(self, "profile_name")

    @property
    @pulumi.getter(name="profileVersion")
    def profile_version(self) -> pulumi.Output[str]:
        """
        A version for the signing profile. AWS Signer generates a unique version for each profile of the same profile name.
        """
        return pulumi.get(self, "profile_version")

    @property
    @pulumi.getter(name="profileVersionArn")
    def profile_version_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the specified signing profile version.
        """
        return pulumi.get(self, "profile_version_arn")

    @property
    @pulumi.getter(name="signatureValidityPeriod")
    def signature_validity_period(self) -> pulumi.Output[Optional['outputs.SigningProfileSignatureValidityPeriod']]:
        """
        Signature validity period of the profile.
        """
        return pulumi.get(self, "signature_validity_period")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.SigningProfileTag']]]:
        """
        A list of tags associated with the signing profile.
        """
        return pulumi.get(self, "tags")

