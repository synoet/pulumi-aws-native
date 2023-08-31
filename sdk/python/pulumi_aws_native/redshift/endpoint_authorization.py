# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['EndpointAuthorizationArgs', 'EndpointAuthorization']

@pulumi.input_type
class EndpointAuthorizationArgs:
    def __init__(__self__, *,
                 account: pulumi.Input[str],
                 cluster_identifier: pulumi.Input[str],
                 force: Optional[pulumi.Input[bool]] = None,
                 vpc_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a EndpointAuthorization resource.
        :param pulumi.Input[str] account: The target AWS account ID to grant or revoke access for.
        :param pulumi.Input[str] cluster_identifier: The cluster identifier.
        :param pulumi.Input[bool] force:  Indicates whether to force the revoke action. If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] vpc_ids: The virtual private cloud (VPC) identifiers to grant or revoke access to.
        """
        pulumi.set(__self__, "account", account)
        pulumi.set(__self__, "cluster_identifier", cluster_identifier)
        if force is not None:
            pulumi.set(__self__, "force", force)
        if vpc_ids is not None:
            pulumi.set(__self__, "vpc_ids", vpc_ids)

    @property
    @pulumi.getter
    def account(self) -> pulumi.Input[str]:
        """
        The target AWS account ID to grant or revoke access for.
        """
        return pulumi.get(self, "account")

    @account.setter
    def account(self, value: pulumi.Input[str]):
        pulumi.set(self, "account", value)

    @property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Input[str]:
        """
        The cluster identifier.
        """
        return pulumi.get(self, "cluster_identifier")

    @cluster_identifier.setter
    def cluster_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_identifier", value)

    @property
    @pulumi.getter
    def force(self) -> Optional[pulumi.Input[bool]]:
        """
         Indicates whether to force the revoke action. If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.
        """
        return pulumi.get(self, "force")

    @force.setter
    def force(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force", value)

    @property
    @pulumi.getter(name="vpcIds")
    def vpc_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The virtual private cloud (VPC) identifiers to grant or revoke access to.
        """
        return pulumi.get(self, "vpc_ids")

    @vpc_ids.setter
    def vpc_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "vpc_ids", value)


class EndpointAuthorization(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account: Optional[pulumi.Input[str]] = None,
                 cluster_identifier: Optional[pulumi.Input[str]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 vpc_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Describes an endpoint authorization for authorizing Redshift-managed VPC endpoint access to a cluster across AWS accounts.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account: The target AWS account ID to grant or revoke access for.
        :param pulumi.Input[str] cluster_identifier: The cluster identifier.
        :param pulumi.Input[bool] force:  Indicates whether to force the revoke action. If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] vpc_ids: The virtual private cloud (VPC) identifiers to grant or revoke access to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EndpointAuthorizationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Describes an endpoint authorization for authorizing Redshift-managed VPC endpoint access to a cluster across AWS accounts.

        :param str resource_name: The name of the resource.
        :param EndpointAuthorizationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EndpointAuthorizationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account: Optional[pulumi.Input[str]] = None,
                 cluster_identifier: Optional[pulumi.Input[str]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 vpc_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EndpointAuthorizationArgs.__new__(EndpointAuthorizationArgs)

            if account is None and not opts.urn:
                raise TypeError("Missing required property 'account'")
            __props__.__dict__["account"] = account
            if cluster_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_identifier'")
            __props__.__dict__["cluster_identifier"] = cluster_identifier
            __props__.__dict__["force"] = force
            __props__.__dict__["vpc_ids"] = vpc_ids
            __props__.__dict__["allowed_all_vpcs"] = None
            __props__.__dict__["allowed_vpcs"] = None
            __props__.__dict__["authorize_time"] = None
            __props__.__dict__["cluster_status"] = None
            __props__.__dict__["endpoint_count"] = None
            __props__.__dict__["grantee"] = None
            __props__.__dict__["grantor"] = None
            __props__.__dict__["status"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["account", "cluster_identifier"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(EndpointAuthorization, __self__).__init__(
            'aws-native:redshift:EndpointAuthorization',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EndpointAuthorization':
        """
        Get an existing EndpointAuthorization resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EndpointAuthorizationArgs.__new__(EndpointAuthorizationArgs)

        __props__.__dict__["account"] = None
        __props__.__dict__["allowed_all_vpcs"] = None
        __props__.__dict__["allowed_vpcs"] = None
        __props__.__dict__["authorize_time"] = None
        __props__.__dict__["cluster_identifier"] = None
        __props__.__dict__["cluster_status"] = None
        __props__.__dict__["endpoint_count"] = None
        __props__.__dict__["force"] = None
        __props__.__dict__["grantee"] = None
        __props__.__dict__["grantor"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["vpc_ids"] = None
        return EndpointAuthorization(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def account(self) -> pulumi.Output[str]:
        """
        The target AWS account ID to grant or revoke access for.
        """
        return pulumi.get(self, "account")

    @property
    @pulumi.getter(name="allowedAllVpcs")
    def allowed_all_vpcs(self) -> pulumi.Output[bool]:
        """
        Indicates whether all VPCs in the grantee account are allowed access to the cluster.
        """
        return pulumi.get(self, "allowed_all_vpcs")

    @property
    @pulumi.getter(name="allowedVpcs")
    def allowed_vpcs(self) -> pulumi.Output[Sequence[str]]:
        """
        The VPCs allowed access to the cluster.
        """
        return pulumi.get(self, "allowed_vpcs")

    @property
    @pulumi.getter(name="authorizeTime")
    def authorize_time(self) -> pulumi.Output[str]:
        """
        The time (UTC) when the authorization was created.
        """
        return pulumi.get(self, "authorize_time")

    @property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Output[str]:
        """
        The cluster identifier.
        """
        return pulumi.get(self, "cluster_identifier")

    @property
    @pulumi.getter(name="clusterStatus")
    def cluster_status(self) -> pulumi.Output[str]:
        """
        The status of the cluster.
        """
        return pulumi.get(self, "cluster_status")

    @property
    @pulumi.getter(name="endpointCount")
    def endpoint_count(self) -> pulumi.Output[int]:
        """
        The number of Redshift-managed VPC endpoints created for the authorization.
        """
        return pulumi.get(self, "endpoint_count")

    @property
    @pulumi.getter
    def force(self) -> pulumi.Output[Optional[bool]]:
        """
         Indicates whether to force the revoke action. If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.
        """
        return pulumi.get(self, "force")

    @property
    @pulumi.getter
    def grantee(self) -> pulumi.Output[str]:
        """
        The AWS account ID of the grantee of the cluster.
        """
        return pulumi.get(self, "grantee")

    @property
    @pulumi.getter
    def grantor(self) -> pulumi.Output[str]:
        """
        The AWS account ID of the cluster owner.
        """
        return pulumi.get(self, "grantor")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the authorization action.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="vpcIds")
    def vpc_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The virtual private cloud (VPC) identifiers to grant or revoke access to.
        """
        return pulumi.get(self, "vpc_ids")

