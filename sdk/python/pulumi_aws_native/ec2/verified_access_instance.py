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
from ._inputs import *

__all__ = ['VerifiedAccessInstanceArgs', 'VerifiedAccessInstance']

@pulumi.input_type
class VerifiedAccessInstanceArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 logging_configurations: Optional[pulumi.Input['VerifiedAccessInstanceVerifiedAccessLogsArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['VerifiedAccessInstanceTagArgs']]]] = None,
                 verified_access_trust_provider_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 verified_access_trust_providers: Optional[pulumi.Input[Sequence[pulumi.Input['VerifiedAccessInstanceVerifiedAccessTrustProviderArgs']]]] = None):
        """
        The set of arguments for constructing a VerifiedAccessInstance resource.
        :param pulumi.Input[str] description: A description for the AWS Verified Access instance.
        :param pulumi.Input['VerifiedAccessInstanceVerifiedAccessLogsArgs'] logging_configurations: The configuration options for AWS Verified Access instances.
        :param pulumi.Input[Sequence[pulumi.Input['VerifiedAccessInstanceTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] verified_access_trust_provider_ids: The IDs of the AWS Verified Access trust providers.
        :param pulumi.Input[Sequence[pulumi.Input['VerifiedAccessInstanceVerifiedAccessTrustProviderArgs']]] verified_access_trust_providers: AWS Verified Access trust providers.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if logging_configurations is not None:
            pulumi.set(__self__, "logging_configurations", logging_configurations)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if verified_access_trust_provider_ids is not None:
            pulumi.set(__self__, "verified_access_trust_provider_ids", verified_access_trust_provider_ids)
        if verified_access_trust_providers is not None:
            pulumi.set(__self__, "verified_access_trust_providers", verified_access_trust_providers)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the AWS Verified Access instance.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="loggingConfigurations")
    def logging_configurations(self) -> Optional[pulumi.Input['VerifiedAccessInstanceVerifiedAccessLogsArgs']]:
        """
        The configuration options for AWS Verified Access instances.
        """
        return pulumi.get(self, "logging_configurations")

    @logging_configurations.setter
    def logging_configurations(self, value: Optional[pulumi.Input['VerifiedAccessInstanceVerifiedAccessLogsArgs']]):
        pulumi.set(self, "logging_configurations", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VerifiedAccessInstanceTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VerifiedAccessInstanceTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="verifiedAccessTrustProviderIds")
    def verified_access_trust_provider_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The IDs of the AWS Verified Access trust providers.
        """
        return pulumi.get(self, "verified_access_trust_provider_ids")

    @verified_access_trust_provider_ids.setter
    def verified_access_trust_provider_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "verified_access_trust_provider_ids", value)

    @property
    @pulumi.getter(name="verifiedAccessTrustProviders")
    def verified_access_trust_providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VerifiedAccessInstanceVerifiedAccessTrustProviderArgs']]]]:
        """
        AWS Verified Access trust providers.
        """
        return pulumi.get(self, "verified_access_trust_providers")

    @verified_access_trust_providers.setter
    def verified_access_trust_providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VerifiedAccessInstanceVerifiedAccessTrustProviderArgs']]]]):
        pulumi.set(self, "verified_access_trust_providers", value)


class VerifiedAccessInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 logging_configurations: Optional[pulumi.Input[pulumi.InputType['VerifiedAccessInstanceVerifiedAccessLogsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VerifiedAccessInstanceTagArgs']]]]] = None,
                 verified_access_trust_provider_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 verified_access_trust_providers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VerifiedAccessInstanceVerifiedAccessTrustProviderArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::EC2::VerifiedAccessInstance resource creates an AWS EC2 Verified Access Instance.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description for the AWS Verified Access instance.
        :param pulumi.Input[pulumi.InputType['VerifiedAccessInstanceVerifiedAccessLogsArgs']] logging_configurations: The configuration options for AWS Verified Access instances.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VerifiedAccessInstanceTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] verified_access_trust_provider_ids: The IDs of the AWS Verified Access trust providers.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VerifiedAccessInstanceVerifiedAccessTrustProviderArgs']]]] verified_access_trust_providers: AWS Verified Access trust providers.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[VerifiedAccessInstanceArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::EC2::VerifiedAccessInstance resource creates an AWS EC2 Verified Access Instance.

        :param str resource_name: The name of the resource.
        :param VerifiedAccessInstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VerifiedAccessInstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 logging_configurations: Optional[pulumi.Input[pulumi.InputType['VerifiedAccessInstanceVerifiedAccessLogsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VerifiedAccessInstanceTagArgs']]]]] = None,
                 verified_access_trust_provider_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 verified_access_trust_providers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VerifiedAccessInstanceVerifiedAccessTrustProviderArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VerifiedAccessInstanceArgs.__new__(VerifiedAccessInstanceArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["logging_configurations"] = logging_configurations
            __props__.__dict__["tags"] = tags
            __props__.__dict__["verified_access_trust_provider_ids"] = verified_access_trust_provider_ids
            __props__.__dict__["verified_access_trust_providers"] = verified_access_trust_providers
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["last_updated_time"] = None
            __props__.__dict__["verified_access_instance_id"] = None
        super(VerifiedAccessInstance, __self__).__init__(
            'aws-native:ec2:VerifiedAccessInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VerifiedAccessInstance':
        """
        Get an existing VerifiedAccessInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VerifiedAccessInstanceArgs.__new__(VerifiedAccessInstanceArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["last_updated_time"] = None
        __props__.__dict__["logging_configurations"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["verified_access_instance_id"] = None
        __props__.__dict__["verified_access_trust_provider_ids"] = None
        __props__.__dict__["verified_access_trust_providers"] = None
        return VerifiedAccessInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        Time this Verified Access Instance was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the AWS Verified Access instance.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[str]:
        """
        Time this Verified Access Instance was last updated.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter(name="loggingConfigurations")
    def logging_configurations(self) -> pulumi.Output[Optional['outputs.VerifiedAccessInstanceVerifiedAccessLogs']]:
        """
        The configuration options for AWS Verified Access instances.
        """
        return pulumi.get(self, "logging_configurations")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.VerifiedAccessInstanceTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="verifiedAccessInstanceId")
    def verified_access_instance_id(self) -> pulumi.Output[str]:
        """
        The ID of the AWS Verified Access instance.
        """
        return pulumi.get(self, "verified_access_instance_id")

    @property
    @pulumi.getter(name="verifiedAccessTrustProviderIds")
    def verified_access_trust_provider_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The IDs of the AWS Verified Access trust providers.
        """
        return pulumi.get(self, "verified_access_trust_provider_ids")

    @property
    @pulumi.getter(name="verifiedAccessTrustProviders")
    def verified_access_trust_providers(self) -> pulumi.Output[Optional[Sequence['outputs.VerifiedAccessInstanceVerifiedAccessTrustProvider']]]:
        """
        AWS Verified Access trust providers.
        """
        return pulumi.get(self, "verified_access_trust_providers")

