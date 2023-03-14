# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['AuthPolicyArgs', 'AuthPolicy']

@pulumi.input_type
class AuthPolicyArgs:
    def __init__(__self__, *,
                 policy: Any,
                 resource_identifier: pulumi.Input[str]):
        """
        The set of arguments for constructing a AuthPolicy resource.
        """
        pulumi.set(__self__, "policy", policy)
        pulumi.set(__self__, "resource_identifier", resource_identifier)

    @property
    @pulumi.getter
    def policy(self) -> Any:
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Any):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> pulumi.Input[str]:
        return pulumi.get(self, "resource_identifier")

    @resource_identifier.setter
    def resource_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_identifier", value)


class AuthPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy: Optional[Any] = None,
                 resource_identifier: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Description

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AuthPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Description

        :param str resource_name: The name of the resource.
        :param AuthPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AuthPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy: Optional[Any] = None,
                 resource_identifier: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AuthPolicyArgs.__new__(AuthPolicyArgs)

            if policy is None and not opts.urn:
                raise TypeError("Missing required property 'policy'")
            __props__.__dict__["policy"] = policy
            if resource_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'resource_identifier'")
            __props__.__dict__["resource_identifier"] = resource_identifier
            __props__.__dict__["state"] = None
        super(AuthPolicy, __self__).__init__(
            'aws-native:vpclattice:AuthPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AuthPolicy':
        """
        Get an existing AuthPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AuthPolicyArgs.__new__(AuthPolicyArgs)

        __props__.__dict__["policy"] = None
        __props__.__dict__["resource_identifier"] = None
        __props__.__dict__["state"] = None
        return AuthPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[Any]:
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "resource_identifier")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output['AuthPolicyState']:
        return pulumi.get(self, "state")

