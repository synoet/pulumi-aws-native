# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ServiceLinkedRoleArgs', 'ServiceLinkedRole']

@pulumi.input_type
class ServiceLinkedRoleArgs:
    def __init__(__self__, *,
                 a_ws_service_name: pulumi.Input[str],
                 custom_suffix: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ServiceLinkedRole resource.
        """
        pulumi.set(__self__, "a_ws_service_name", a_ws_service_name)
        if custom_suffix is not None:
            pulumi.set(__self__, "custom_suffix", custom_suffix)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="aWSServiceName")
    def a_ws_service_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "a_ws_service_name")

    @a_ws_service_name.setter
    def a_ws_service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "a_ws_service_name", value)

    @property
    @pulumi.getter(name="customSuffix")
    def custom_suffix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "custom_suffix")

    @custom_suffix.setter
    def custom_suffix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_suffix", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


warnings.warn("""ServiceLinkedRole is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ServiceLinkedRole(pulumi.CustomResource):
    warnings.warn("""ServiceLinkedRole is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 a_ws_service_name: Optional[pulumi.Input[str]] = None,
                 custom_suffix: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::IAM::ServiceLinkedRole

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceLinkedRoleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::IAM::ServiceLinkedRole

        :param str resource_name: The name of the resource.
        :param ServiceLinkedRoleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceLinkedRoleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 a_ws_service_name: Optional[pulumi.Input[str]] = None,
                 custom_suffix: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""ServiceLinkedRole is deprecated: ServiceLinkedRole is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceLinkedRoleArgs.__new__(ServiceLinkedRoleArgs)

            if a_ws_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'a_ws_service_name'")
            __props__.__dict__["a_ws_service_name"] = a_ws_service_name
            __props__.__dict__["custom_suffix"] = custom_suffix
            __props__.__dict__["description"] = description
        super(ServiceLinkedRole, __self__).__init__(
            'aws-native:iam:ServiceLinkedRole',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServiceLinkedRole':
        """
        Get an existing ServiceLinkedRole resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServiceLinkedRoleArgs.__new__(ServiceLinkedRoleArgs)

        __props__.__dict__["a_ws_service_name"] = None
        __props__.__dict__["custom_suffix"] = None
        __props__.__dict__["description"] = None
        return ServiceLinkedRole(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aWSServiceName")
    def a_ws_service_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "a_ws_service_name")

    @property
    @pulumi.getter(name="customSuffix")
    def custom_suffix(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "custom_suffix")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

