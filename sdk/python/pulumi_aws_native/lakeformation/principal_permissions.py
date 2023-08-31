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

__all__ = ['PrincipalPermissionsArgs', 'PrincipalPermissions']

@pulumi.input_type
class PrincipalPermissionsArgs:
    def __init__(__self__, *,
                 permissions: pulumi.Input[Sequence[pulumi.Input['PrincipalPermissionsPermission']]],
                 permissions_with_grant_option: pulumi.Input[Sequence[pulumi.Input['PrincipalPermissionsPermission']]],
                 principal: pulumi.Input['PrincipalPermissionsDataLakePrincipalArgs'],
                 resource: pulumi.Input['PrincipalPermissionsResourceArgs'],
                 catalog: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PrincipalPermissions resource.
        """
        pulumi.set(__self__, "permissions", permissions)
        pulumi.set(__self__, "permissions_with_grant_option", permissions_with_grant_option)
        pulumi.set(__self__, "principal", principal)
        pulumi.set(__self__, "resource", resource)
        if catalog is not None:
            pulumi.set(__self__, "catalog", catalog)

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Input[Sequence[pulumi.Input['PrincipalPermissionsPermission']]]:
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: pulumi.Input[Sequence[pulumi.Input['PrincipalPermissionsPermission']]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter(name="permissionsWithGrantOption")
    def permissions_with_grant_option(self) -> pulumi.Input[Sequence[pulumi.Input['PrincipalPermissionsPermission']]]:
        return pulumi.get(self, "permissions_with_grant_option")

    @permissions_with_grant_option.setter
    def permissions_with_grant_option(self, value: pulumi.Input[Sequence[pulumi.Input['PrincipalPermissionsPermission']]]):
        pulumi.set(self, "permissions_with_grant_option", value)

    @property
    @pulumi.getter
    def principal(self) -> pulumi.Input['PrincipalPermissionsDataLakePrincipalArgs']:
        return pulumi.get(self, "principal")

    @principal.setter
    def principal(self, value: pulumi.Input['PrincipalPermissionsDataLakePrincipalArgs']):
        pulumi.set(self, "principal", value)

    @property
    @pulumi.getter
    def resource(self) -> pulumi.Input['PrincipalPermissionsResourceArgs']:
        return pulumi.get(self, "resource")

    @resource.setter
    def resource(self, value: pulumi.Input['PrincipalPermissionsResourceArgs']):
        pulumi.set(self, "resource", value)

    @property
    @pulumi.getter
    def catalog(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "catalog")

    @catalog.setter
    def catalog(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog", value)


class PrincipalPermissions(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input['PrincipalPermissionsPermission']]]] = None,
                 permissions_with_grant_option: Optional[pulumi.Input[Sequence[pulumi.Input['PrincipalPermissionsPermission']]]] = None,
                 principal: Optional[pulumi.Input[pulumi.InputType['PrincipalPermissionsDataLakePrincipalArgs']]] = None,
                 resource: Optional[pulumi.Input[pulumi.InputType['PrincipalPermissionsResourceArgs']]] = None,
                 __props__=None):
        """
        A resource schema representing a Lake Formation Permission.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrincipalPermissionsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A resource schema representing a Lake Formation Permission.

        :param str resource_name: The name of the resource.
        :param PrincipalPermissionsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrincipalPermissionsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input['PrincipalPermissionsPermission']]]] = None,
                 permissions_with_grant_option: Optional[pulumi.Input[Sequence[pulumi.Input['PrincipalPermissionsPermission']]]] = None,
                 principal: Optional[pulumi.Input[pulumi.InputType['PrincipalPermissionsDataLakePrincipalArgs']]] = None,
                 resource: Optional[pulumi.Input[pulumi.InputType['PrincipalPermissionsResourceArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrincipalPermissionsArgs.__new__(PrincipalPermissionsArgs)

            __props__.__dict__["catalog"] = catalog
            if permissions is None and not opts.urn:
                raise TypeError("Missing required property 'permissions'")
            __props__.__dict__["permissions"] = permissions
            if permissions_with_grant_option is None and not opts.urn:
                raise TypeError("Missing required property 'permissions_with_grant_option'")
            __props__.__dict__["permissions_with_grant_option"] = permissions_with_grant_option
            if principal is None and not opts.urn:
                raise TypeError("Missing required property 'principal'")
            __props__.__dict__["principal"] = principal
            if resource is None and not opts.urn:
                raise TypeError("Missing required property 'resource'")
            __props__.__dict__["resource"] = resource
            __props__.__dict__["principal_identifier"] = None
            __props__.__dict__["resource_identifier"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["catalog", "permissions[*]", "permissions_with_grant_option[*]", "principal", "resource"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(PrincipalPermissions, __self__).__init__(
            'aws-native:lakeformation:PrincipalPermissions',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrincipalPermissions':
        """
        Get an existing PrincipalPermissions resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PrincipalPermissionsArgs.__new__(PrincipalPermissionsArgs)

        __props__.__dict__["catalog"] = None
        __props__.__dict__["permissions"] = None
        __props__.__dict__["permissions_with_grant_option"] = None
        __props__.__dict__["principal"] = None
        __props__.__dict__["principal_identifier"] = None
        __props__.__dict__["resource"] = None
        __props__.__dict__["resource_identifier"] = None
        return PrincipalPermissions(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def catalog(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "catalog")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Sequence['PrincipalPermissionsPermission']]:
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="permissionsWithGrantOption")
    def permissions_with_grant_option(self) -> pulumi.Output[Sequence['PrincipalPermissionsPermission']]:
        return pulumi.get(self, "permissions_with_grant_option")

    @property
    @pulumi.getter
    def principal(self) -> pulumi.Output['outputs.PrincipalPermissionsDataLakePrincipal']:
        return pulumi.get(self, "principal")

    @property
    @pulumi.getter(name="principalIdentifier")
    def principal_identifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "principal_identifier")

    @property
    @pulumi.getter
    def resource(self) -> pulumi.Output['outputs.PrincipalPermissionsResource']:
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "resource_identifier")

