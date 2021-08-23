# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ReplicationSetArgs', 'ReplicationSet']

@pulumi.input_type
class ReplicationSetArgs:
    def __init__(__self__, *,
                 regions: pulumi.Input[Sequence[pulumi.Input['ReplicationSetReplicationRegionArgs']]],
                 deletion_protected: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a ReplicationSet resource.
        :param pulumi.Input[Sequence[pulumi.Input['ReplicationSetReplicationRegionArgs']]] regions: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-regions
        :param pulumi.Input[bool] deletion_protected: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-deletionprotected
        """
        pulumi.set(__self__, "regions", regions)
        if deletion_protected is not None:
            pulumi.set(__self__, "deletion_protected", deletion_protected)

    @property
    @pulumi.getter
    def regions(self) -> pulumi.Input[Sequence[pulumi.Input['ReplicationSetReplicationRegionArgs']]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-regions
        """
        return pulumi.get(self, "regions")

    @regions.setter
    def regions(self, value: pulumi.Input[Sequence[pulumi.Input['ReplicationSetReplicationRegionArgs']]]):
        pulumi.set(self, "regions", value)

    @property
    @pulumi.getter(name="deletionProtected")
    def deletion_protected(self) -> Optional[pulumi.Input[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-deletionprotected
        """
        return pulumi.get(self, "deletion_protected")

    @deletion_protected.setter
    def deletion_protected(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "deletion_protected", value)


class ReplicationSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deletion_protected: Optional[pulumi.Input[bool]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReplicationSetReplicationRegionArgs']]]]] = None,
                 __props__=None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] deletion_protected: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-deletionprotected
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReplicationSetReplicationRegionArgs']]]] regions: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-regions
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReplicationSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html

        :param str resource_name: The name of the resource.
        :param ReplicationSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReplicationSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deletion_protected: Optional[pulumi.Input[bool]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReplicationSetReplicationRegionArgs']]]]] = None,
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
            __props__ = ReplicationSetArgs.__new__(ReplicationSetArgs)

            __props__.__dict__["deletion_protected"] = deletion_protected
            if regions is None and not opts.urn:
                raise TypeError("Missing required property 'regions'")
            __props__.__dict__["regions"] = regions
            __props__.__dict__["arn"] = None
        super(ReplicationSet, __self__).__init__(
            'aws-native:ssmincidents:ReplicationSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ReplicationSet':
        """
        Get an existing ReplicationSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ReplicationSetArgs.__new__(ReplicationSetArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["deletion_protected"] = None
        __props__.__dict__["regions"] = None
        return ReplicationSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="deletionProtected")
    def deletion_protected(self) -> pulumi.Output[Optional[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-deletionprotected
        """
        return pulumi.get(self, "deletion_protected")

    @property
    @pulumi.getter
    def regions(self) -> pulumi.Output[Sequence['outputs.ReplicationSetReplicationRegion']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-regions
        """
        return pulumi.get(self, "regions")

