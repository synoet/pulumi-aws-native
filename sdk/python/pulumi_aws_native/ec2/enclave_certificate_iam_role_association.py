# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['EnclaveCertificateIamRoleAssociationArgs', 'EnclaveCertificateIamRoleAssociation']

@pulumi.input_type
class EnclaveCertificateIamRoleAssociationArgs:
    def __init__(__self__, *,
                 certificate_arn: pulumi.Input[str],
                 role_arn: pulumi.Input[str]):
        """
        The set of arguments for constructing a EnclaveCertificateIamRoleAssociation resource.
        :param pulumi.Input[str] certificate_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-enclavecertificateiamroleassociation.html#cfn-ec2-enclavecertificateiamroleassociation-certificatearn
        :param pulumi.Input[str] role_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-enclavecertificateiamroleassociation.html#cfn-ec2-enclavecertificateiamroleassociation-rolearn
        """
        pulumi.set(__self__, "certificate_arn", certificate_arn)
        pulumi.set(__self__, "role_arn", role_arn)

    @property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-enclavecertificateiamroleassociation.html#cfn-ec2-enclavecertificateiamroleassociation-certificatearn
        """
        return pulumi.get(self, "certificate_arn")

    @certificate_arn.setter
    def certificate_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "certificate_arn", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-enclavecertificateiamroleassociation.html#cfn-ec2-enclavecertificateiamroleassociation-rolearn
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)


class EnclaveCertificateIamRoleAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-enclavecertificateiamroleassociation.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-enclavecertificateiamroleassociation.html#cfn-ec2-enclavecertificateiamroleassociation-certificatearn
        :param pulumi.Input[str] role_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-enclavecertificateiamroleassociation.html#cfn-ec2-enclavecertificateiamroleassociation-rolearn
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EnclaveCertificateIamRoleAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-enclavecertificateiamroleassociation.html

        :param str resource_name: The name of the resource.
        :param EnclaveCertificateIamRoleAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnclaveCertificateIamRoleAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
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
            __props__ = EnclaveCertificateIamRoleAssociationArgs.__new__(EnclaveCertificateIamRoleAssociationArgs)

            if certificate_arn is None and not opts.urn:
                raise TypeError("Missing required property 'certificate_arn'")
            __props__.__dict__["certificate_arn"] = certificate_arn
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["certificate_s3_bucket_name"] = None
            __props__.__dict__["certificate_s3_object_key"] = None
            __props__.__dict__["encryption_kms_key_id"] = None
        super(EnclaveCertificateIamRoleAssociation, __self__).__init__(
            'aws-native:ec2:EnclaveCertificateIamRoleAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EnclaveCertificateIamRoleAssociation':
        """
        Get an existing EnclaveCertificateIamRoleAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EnclaveCertificateIamRoleAssociationArgs.__new__(EnclaveCertificateIamRoleAssociationArgs)

        __props__.__dict__["certificate_arn"] = None
        __props__.__dict__["certificate_s3_bucket_name"] = None
        __props__.__dict__["certificate_s3_object_key"] = None
        __props__.__dict__["encryption_kms_key_id"] = None
        __props__.__dict__["role_arn"] = None
        return EnclaveCertificateIamRoleAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> pulumi.Output[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-enclavecertificateiamroleassociation.html#cfn-ec2-enclavecertificateiamroleassociation-certificatearn
        """
        return pulumi.get(self, "certificate_arn")

    @property
    @pulumi.getter(name="certificateS3BucketName")
    def certificate_s3_bucket_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "certificate_s3_bucket_name")

    @property
    @pulumi.getter(name="certificateS3ObjectKey")
    def certificate_s3_object_key(self) -> pulumi.Output[str]:
        return pulumi.get(self, "certificate_s3_object_key")

    @property
    @pulumi.getter(name="encryptionKmsKeyId")
    def encryption_kms_key_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "encryption_kms_key_id")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-enclavecertificateiamroleassociation.html#cfn-ec2-enclavecertificateiamroleassociation-rolearn
        """
        return pulumi.get(self, "role_arn")

