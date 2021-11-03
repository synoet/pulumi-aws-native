# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ConfigurationSetArgs', 'ConfigurationSet']

@pulumi.input_type
class ConfigurationSetArgs:
    def __init__(__self__, *,
                 delivery_options: Optional[pulumi.Input['ConfigurationSetDeliveryOptionsArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 reputation_options: Optional[pulumi.Input['ConfigurationSetReputationOptionsArgs']] = None,
                 sending_options: Optional[pulumi.Input['ConfigurationSetSendingOptionsArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationSetTagsArgs']]]] = None,
                 tracking_options: Optional[pulumi.Input['ConfigurationSetTrackingOptionsArgs']] = None):
        """
        The set of arguments for constructing a ConfigurationSet resource.
        """
        if delivery_options is not None:
            pulumi.set(__self__, "delivery_options", delivery_options)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if reputation_options is not None:
            pulumi.set(__self__, "reputation_options", reputation_options)
        if sending_options is not None:
            pulumi.set(__self__, "sending_options", sending_options)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tracking_options is not None:
            pulumi.set(__self__, "tracking_options", tracking_options)

    @property
    @pulumi.getter(name="deliveryOptions")
    def delivery_options(self) -> Optional[pulumi.Input['ConfigurationSetDeliveryOptionsArgs']]:
        return pulumi.get(self, "delivery_options")

    @delivery_options.setter
    def delivery_options(self, value: Optional[pulumi.Input['ConfigurationSetDeliveryOptionsArgs']]):
        pulumi.set(self, "delivery_options", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="reputationOptions")
    def reputation_options(self) -> Optional[pulumi.Input['ConfigurationSetReputationOptionsArgs']]:
        return pulumi.get(self, "reputation_options")

    @reputation_options.setter
    def reputation_options(self, value: Optional[pulumi.Input['ConfigurationSetReputationOptionsArgs']]):
        pulumi.set(self, "reputation_options", value)

    @property
    @pulumi.getter(name="sendingOptions")
    def sending_options(self) -> Optional[pulumi.Input['ConfigurationSetSendingOptionsArgs']]:
        return pulumi.get(self, "sending_options")

    @sending_options.setter
    def sending_options(self, value: Optional[pulumi.Input['ConfigurationSetSendingOptionsArgs']]):
        pulumi.set(self, "sending_options", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationSetTagsArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationSetTagsArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="trackingOptions")
    def tracking_options(self) -> Optional[pulumi.Input['ConfigurationSetTrackingOptionsArgs']]:
        return pulumi.get(self, "tracking_options")

    @tracking_options.setter
    def tracking_options(self, value: Optional[pulumi.Input['ConfigurationSetTrackingOptionsArgs']]):
        pulumi.set(self, "tracking_options", value)


warnings.warn("""ConfigurationSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ConfigurationSet(pulumi.CustomResource):
    warnings.warn("""ConfigurationSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delivery_options: Optional[pulumi.Input[pulumi.InputType['ConfigurationSetDeliveryOptionsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 reputation_options: Optional[pulumi.Input[pulumi.InputType['ConfigurationSetReputationOptionsArgs']]] = None,
                 sending_options: Optional[pulumi.Input[pulumi.InputType['ConfigurationSetSendingOptionsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigurationSetTagsArgs']]]]] = None,
                 tracking_options: Optional[pulumi.Input[pulumi.InputType['ConfigurationSetTrackingOptionsArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::PinpointEmail::ConfigurationSet

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ConfigurationSetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::PinpointEmail::ConfigurationSet

        :param str resource_name: The name of the resource.
        :param ConfigurationSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigurationSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delivery_options: Optional[pulumi.Input[pulumi.InputType['ConfigurationSetDeliveryOptionsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 reputation_options: Optional[pulumi.Input[pulumi.InputType['ConfigurationSetReputationOptionsArgs']]] = None,
                 sending_options: Optional[pulumi.Input[pulumi.InputType['ConfigurationSetSendingOptionsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigurationSetTagsArgs']]]]] = None,
                 tracking_options: Optional[pulumi.Input[pulumi.InputType['ConfigurationSetTrackingOptionsArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""ConfigurationSet is deprecated: ConfigurationSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigurationSetArgs.__new__(ConfigurationSetArgs)

            __props__.__dict__["delivery_options"] = delivery_options
            __props__.__dict__["name"] = name
            __props__.__dict__["reputation_options"] = reputation_options
            __props__.__dict__["sending_options"] = sending_options
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tracking_options"] = tracking_options
        super(ConfigurationSet, __self__).__init__(
            'aws-native:pinpointemail:ConfigurationSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConfigurationSet':
        """
        Get an existing ConfigurationSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConfigurationSetArgs.__new__(ConfigurationSetArgs)

        __props__.__dict__["delivery_options"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["reputation_options"] = None
        __props__.__dict__["sending_options"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["tracking_options"] = None
        return ConfigurationSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deliveryOptions")
    def delivery_options(self) -> pulumi.Output[Optional['outputs.ConfigurationSetDeliveryOptions']]:
        return pulumi.get(self, "delivery_options")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="reputationOptions")
    def reputation_options(self) -> pulumi.Output[Optional['outputs.ConfigurationSetReputationOptions']]:
        return pulumi.get(self, "reputation_options")

    @property
    @pulumi.getter(name="sendingOptions")
    def sending_options(self) -> pulumi.Output[Optional['outputs.ConfigurationSetSendingOptions']]:
        return pulumi.get(self, "sending_options")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ConfigurationSetTags']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trackingOptions")
    def tracking_options(self) -> pulumi.Output[Optional['outputs.ConfigurationSetTrackingOptions']]:
        return pulumi.get(self, "tracking_options")

