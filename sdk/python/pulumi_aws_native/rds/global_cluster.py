# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GlobalClusterArgs', 'GlobalCluster']

@pulumi.input_type
class GlobalClusterArgs:
    def __init__(__self__, *,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 global_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 source_db_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 storage_encrypted: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a GlobalCluster resource.
        :param pulumi.Input[bool] deletion_protection: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-deletionprotection
        :param pulumi.Input[str] engine: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-engine
        :param pulumi.Input[str] engine_version: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-engineversion
        :param pulumi.Input[str] global_cluster_identifier: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-globalclusteridentifier
        :param pulumi.Input[str] source_db_cluster_identifier: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-sourcedbclusteridentifier
        :param pulumi.Input[bool] storage_encrypted: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-storageencrypted
        """
        if deletion_protection is not None:
            pulumi.set(__self__, "deletion_protection", deletion_protection)
        if engine is not None:
            pulumi.set(__self__, "engine", engine)
        if engine_version is not None:
            pulumi.set(__self__, "engine_version", engine_version)
        if global_cluster_identifier is not None:
            pulumi.set(__self__, "global_cluster_identifier", global_cluster_identifier)
        if source_db_cluster_identifier is not None:
            pulumi.set(__self__, "source_db_cluster_identifier", source_db_cluster_identifier)
        if storage_encrypted is not None:
            pulumi.set(__self__, "storage_encrypted", storage_encrypted)

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-deletionprotection
        """
        return pulumi.get(self, "deletion_protection")

    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "deletion_protection", value)

    @property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-engine
        """
        return pulumi.get(self, "engine")

    @engine.setter
    def engine(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "engine", value)

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-engineversion
        """
        return pulumi.get(self, "engine_version")

    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "engine_version", value)

    @property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-globalclusteridentifier
        """
        return pulumi.get(self, "global_cluster_identifier")

    @global_cluster_identifier.setter
    def global_cluster_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "global_cluster_identifier", value)

    @property
    @pulumi.getter(name="sourceDBClusterIdentifier")
    def source_db_cluster_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-sourcedbclusteridentifier
        """
        return pulumi.get(self, "source_db_cluster_identifier")

    @source_db_cluster_identifier.setter
    def source_db_cluster_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_db_cluster_identifier", value)

    @property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> Optional[pulumi.Input[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-storageencrypted
        """
        return pulumi.get(self, "storage_encrypted")

    @storage_encrypted.setter
    def storage_encrypted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "storage_encrypted", value)


class GlobalCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 global_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 source_db_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 storage_encrypted: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] deletion_protection: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-deletionprotection
        :param pulumi.Input[str] engine: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-engine
        :param pulumi.Input[str] engine_version: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-engineversion
        :param pulumi.Input[str] global_cluster_identifier: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-globalclusteridentifier
        :param pulumi.Input[str] source_db_cluster_identifier: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-sourcedbclusteridentifier
        :param pulumi.Input[bool] storage_encrypted: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-storageencrypted
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[GlobalClusterArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html

        :param str resource_name: The name of the resource.
        :param GlobalClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GlobalClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 global_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 source_db_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 storage_encrypted: Optional[pulumi.Input[bool]] = None,
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
            __props__ = GlobalClusterArgs.__new__(GlobalClusterArgs)

            __props__.__dict__["deletion_protection"] = deletion_protection
            __props__.__dict__["engine"] = engine
            __props__.__dict__["engine_version"] = engine_version
            __props__.__dict__["global_cluster_identifier"] = global_cluster_identifier
            __props__.__dict__["source_db_cluster_identifier"] = source_db_cluster_identifier
            __props__.__dict__["storage_encrypted"] = storage_encrypted
        super(GlobalCluster, __self__).__init__(
            'aws-native:rds:GlobalCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GlobalCluster':
        """
        Get an existing GlobalCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GlobalClusterArgs.__new__(GlobalClusterArgs)

        __props__.__dict__["deletion_protection"] = None
        __props__.__dict__["engine"] = None
        __props__.__dict__["engine_version"] = None
        __props__.__dict__["global_cluster_identifier"] = None
        __props__.__dict__["source_db_cluster_identifier"] = None
        __props__.__dict__["storage_encrypted"] = None
        return GlobalCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-deletionprotection
        """
        return pulumi.get(self, "deletion_protection")

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-engine
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-engineversion
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-globalclusteridentifier
        """
        return pulumi.get(self, "global_cluster_identifier")

    @property
    @pulumi.getter(name="sourceDBClusterIdentifier")
    def source_db_cluster_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-sourcedbclusteridentifier
        """
        return pulumi.get(self, "source_db_cluster_identifier")

    @property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> pulumi.Output[Optional[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-storageencrypted
        """
        return pulumi.get(self, "storage_encrypted")

