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

__all__ = ['InstanceProfileArgs', 'InstanceProfile']

@pulumi.input_type
class InstanceProfileArgs:
    def __init__(__self__, *,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_profile_identifier: Optional[pulumi.Input[str]] = None,
                 instance_profile_name: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 network_type: Optional[pulumi.Input['InstanceProfileNetworkType']] = None,
                 publicly_accessible: Optional[pulumi.Input[bool]] = None,
                 subnet_group_identifier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceProfileTagArgs']]]] = None,
                 vpc_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a InstanceProfile resource.
        :param pulumi.Input[str] availability_zone: The property describes an availability zone of the instance profile.
        :param pulumi.Input[str] description: The optional description of the instance profile.
        :param pulumi.Input[str] instance_profile_identifier: The property describes an identifier for the instance profile. It is used for describing/deleting/modifying. Can be name/arn
        :param pulumi.Input[str] instance_profile_name: The property describes a name for the instance profile.
        :param pulumi.Input[str] kms_key_arn: The property describes kms key arn for the instance profile.
        :param pulumi.Input['InstanceProfileNetworkType'] network_type: The property describes a network type for the instance profile.
        :param pulumi.Input[bool] publicly_accessible: The property describes the publicly accessible of the instance profile
        :param pulumi.Input[str] subnet_group_identifier: The property describes a subnet group identifier for the instance profile.
        :param pulumi.Input[Sequence[pulumi.Input['InstanceProfileTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] vpc_security_groups: The property describes vps security groups for the instance profile.
        """
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if instance_profile_identifier is not None:
            pulumi.set(__self__, "instance_profile_identifier", instance_profile_identifier)
        if instance_profile_name is not None:
            pulumi.set(__self__, "instance_profile_name", instance_profile_name)
        if kms_key_arn is not None:
            pulumi.set(__self__, "kms_key_arn", kms_key_arn)
        if network_type is not None:
            pulumi.set(__self__, "network_type", network_type)
        if publicly_accessible is not None:
            pulumi.set(__self__, "publicly_accessible", publicly_accessible)
        if subnet_group_identifier is not None:
            pulumi.set(__self__, "subnet_group_identifier", subnet_group_identifier)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vpc_security_groups is not None:
            pulumi.set(__self__, "vpc_security_groups", vpc_security_groups)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The property describes an availability zone of the instance profile.
        """
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The optional description of the instance profile.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="instanceProfileIdentifier")
    def instance_profile_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The property describes an identifier for the instance profile. It is used for describing/deleting/modifying. Can be name/arn
        """
        return pulumi.get(self, "instance_profile_identifier")

    @instance_profile_identifier.setter
    def instance_profile_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_profile_identifier", value)

    @property
    @pulumi.getter(name="instanceProfileName")
    def instance_profile_name(self) -> Optional[pulumi.Input[str]]:
        """
        The property describes a name for the instance profile.
        """
        return pulumi.get(self, "instance_profile_name")

    @instance_profile_name.setter
    def instance_profile_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_profile_name", value)

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The property describes kms key arn for the instance profile.
        """
        return pulumi.get(self, "kms_key_arn")

    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_arn", value)

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input['InstanceProfileNetworkType']]:
        """
        The property describes a network type for the instance profile.
        """
        return pulumi.get(self, "network_type")

    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input['InstanceProfileNetworkType']]):
        pulumi.set(self, "network_type", value)

    @property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[bool]]:
        """
        The property describes the publicly accessible of the instance profile
        """
        return pulumi.get(self, "publicly_accessible")

    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "publicly_accessible", value)

    @property
    @pulumi.getter(name="subnetGroupIdentifier")
    def subnet_group_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The property describes a subnet group identifier for the instance profile.
        """
        return pulumi.get(self, "subnet_group_identifier")

    @subnet_group_identifier.setter
    def subnet_group_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_group_identifier", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InstanceProfileTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceProfileTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vpcSecurityGroups")
    def vpc_security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The property describes vps security groups for the instance profile.
        """
        return pulumi.get(self, "vpc_security_groups")

    @vpc_security_groups.setter
    def vpc_security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "vpc_security_groups", value)


class InstanceProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_profile_identifier: Optional[pulumi.Input[str]] = None,
                 instance_profile_name: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 network_type: Optional[pulumi.Input['InstanceProfileNetworkType']] = None,
                 publicly_accessible: Optional[pulumi.Input[bool]] = None,
                 subnet_group_identifier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceProfileTagArgs']]]]] = None,
                 vpc_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::DMS::InstanceProfile.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] availability_zone: The property describes an availability zone of the instance profile.
        :param pulumi.Input[str] description: The optional description of the instance profile.
        :param pulumi.Input[str] instance_profile_identifier: The property describes an identifier for the instance profile. It is used for describing/deleting/modifying. Can be name/arn
        :param pulumi.Input[str] instance_profile_name: The property describes a name for the instance profile.
        :param pulumi.Input[str] kms_key_arn: The property describes kms key arn for the instance profile.
        :param pulumi.Input['InstanceProfileNetworkType'] network_type: The property describes a network type for the instance profile.
        :param pulumi.Input[bool] publicly_accessible: The property describes the publicly accessible of the instance profile
        :param pulumi.Input[str] subnet_group_identifier: The property describes a subnet group identifier for the instance profile.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceProfileTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] vpc_security_groups: The property describes vps security groups for the instance profile.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[InstanceProfileArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::DMS::InstanceProfile.

        :param str resource_name: The name of the resource.
        :param InstanceProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_profile_identifier: Optional[pulumi.Input[str]] = None,
                 instance_profile_name: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 network_type: Optional[pulumi.Input['InstanceProfileNetworkType']] = None,
                 publicly_accessible: Optional[pulumi.Input[bool]] = None,
                 subnet_group_identifier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceProfileTagArgs']]]]] = None,
                 vpc_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstanceProfileArgs.__new__(InstanceProfileArgs)

            __props__.__dict__["availability_zone"] = availability_zone
            __props__.__dict__["description"] = description
            __props__.__dict__["instance_profile_identifier"] = instance_profile_identifier
            __props__.__dict__["instance_profile_name"] = instance_profile_name
            __props__.__dict__["kms_key_arn"] = kms_key_arn
            __props__.__dict__["network_type"] = network_type
            __props__.__dict__["publicly_accessible"] = publicly_accessible
            __props__.__dict__["subnet_group_identifier"] = subnet_group_identifier
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vpc_security_groups"] = vpc_security_groups
            __props__.__dict__["instance_profile_arn"] = None
            __props__.__dict__["instance_profile_creation_time"] = None
        super(InstanceProfile, __self__).__init__(
            'aws-native:dms:InstanceProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InstanceProfile':
        """
        Get an existing InstanceProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InstanceProfileArgs.__new__(InstanceProfileArgs)

        __props__.__dict__["availability_zone"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["instance_profile_arn"] = None
        __props__.__dict__["instance_profile_creation_time"] = None
        __props__.__dict__["instance_profile_identifier"] = None
        __props__.__dict__["instance_profile_name"] = None
        __props__.__dict__["kms_key_arn"] = None
        __props__.__dict__["network_type"] = None
        __props__.__dict__["publicly_accessible"] = None
        __props__.__dict__["subnet_group_identifier"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpc_security_groups"] = None
        return InstanceProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[Optional[str]]:
        """
        The property describes an availability zone of the instance profile.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The optional description of the instance profile.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="instanceProfileArn")
    def instance_profile_arn(self) -> pulumi.Output[str]:
        """
        The property describes an ARN of the instance profile.
        """
        return pulumi.get(self, "instance_profile_arn")

    @property
    @pulumi.getter(name="instanceProfileCreationTime")
    def instance_profile_creation_time(self) -> pulumi.Output[str]:
        """
        The property describes a creating time of the instance profile.
        """
        return pulumi.get(self, "instance_profile_creation_time")

    @property
    @pulumi.getter(name="instanceProfileIdentifier")
    def instance_profile_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        The property describes an identifier for the instance profile. It is used for describing/deleting/modifying. Can be name/arn
        """
        return pulumi.get(self, "instance_profile_identifier")

    @property
    @pulumi.getter(name="instanceProfileName")
    def instance_profile_name(self) -> pulumi.Output[Optional[str]]:
        """
        The property describes a name for the instance profile.
        """
        return pulumi.get(self, "instance_profile_name")

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The property describes kms key arn for the instance profile.
        """
        return pulumi.get(self, "kms_key_arn")

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> pulumi.Output[Optional['InstanceProfileNetworkType']]:
        """
        The property describes a network type for the instance profile.
        """
        return pulumi.get(self, "network_type")

    @property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> pulumi.Output[Optional[bool]]:
        """
        The property describes the publicly accessible of the instance profile
        """
        return pulumi.get(self, "publicly_accessible")

    @property
    @pulumi.getter(name="subnetGroupIdentifier")
    def subnet_group_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        The property describes a subnet group identifier for the instance profile.
        """
        return pulumi.get(self, "subnet_group_identifier")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.InstanceProfileTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcSecurityGroups")
    def vpc_security_groups(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The property describes vps security groups for the instance profile.
        """
        return pulumi.get(self, "vpc_security_groups")

