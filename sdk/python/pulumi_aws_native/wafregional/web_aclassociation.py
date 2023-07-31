# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['WebACLAssociationArgs', 'WebACLAssociation']

@pulumi.input_type
class WebACLAssociationArgs:
    def __init__(__self__, *,
                 resource_arn: pulumi.Input[str],
                 web_acl_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a WebACLAssociation resource.
        """
        pulumi.set(__self__, "resource_arn", resource_arn)
        pulumi.set(__self__, "web_acl_id", web_acl_id)

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "resource_arn")

    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_arn", value)

    @property
    @pulumi.getter(name="webAclId")
    def web_acl_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "web_acl_id")

    @web_acl_id.setter
    def web_acl_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "web_acl_id", value)


warnings.warn("""WebACLAssociation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class WebACLAssociation(pulumi.CustomResource):
    warnings.warn("""WebACLAssociation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_arn: Optional[pulumi.Input[str]] = None,
                 web_acl_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::WAFRegional::WebACLAssociation

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebACLAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::WAFRegional::WebACLAssociation

        :param str resource_name: The name of the resource.
        :param WebACLAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebACLAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_arn: Optional[pulumi.Input[str]] = None,
                 web_acl_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""WebACLAssociation is deprecated: WebACLAssociation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WebACLAssociationArgs.__new__(WebACLAssociationArgs)

            if resource_arn is None and not opts.urn:
                raise TypeError("Missing required property 'resource_arn'")
            __props__.__dict__["resource_arn"] = resource_arn
            if web_acl_id is None and not opts.urn:
                raise TypeError("Missing required property 'web_acl_id'")
            __props__.__dict__["web_acl_id"] = web_acl_id
        super(WebACLAssociation, __self__).__init__(
            'aws-native:wafregional:WebACLAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WebACLAssociation':
        """
        Get an existing WebACLAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebACLAssociationArgs.__new__(WebACLAssociationArgs)

        __props__.__dict__["resource_arn"] = None
        __props__.__dict__["web_acl_id"] = None
        return WebACLAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "resource_arn")

    @property
    @pulumi.getter(name="webAclId")
    def web_acl_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "web_acl_id")

