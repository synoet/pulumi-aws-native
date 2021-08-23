# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs

__all__ = ['KeyArgs', 'Key']

@pulumi.input_type
class KeyArgs:
    def __init__(__self__, *,
                 key_policy: pulumi.Input[Union[Any, str]],
                 description: Optional[pulumi.Input[str]] = None,
                 enable_key_rotation: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 key_spec: Optional[pulumi.Input[str]] = None,
                 key_usage: Optional[pulumi.Input[str]] = None,
                 multi_region: Optional[pulumi.Input[bool]] = None,
                 pending_window_in_days: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Key resource.
        :param pulumi.Input[Union[Any, str]] key_policy: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keypolicy
        :param pulumi.Input[str] description: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-description
        :param pulumi.Input[bool] enable_key_rotation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enablekeyrotation
        :param pulumi.Input[bool] enabled: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enabled
        :param pulumi.Input[str] key_spec: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keyspec
        :param pulumi.Input[str] key_usage: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keyusage
        :param pulumi.Input[bool] multi_region: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-multiregion
        :param pulumi.Input[int] pending_window_in_days: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-pendingwindowindays
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-tags
        """
        pulumi.set(__self__, "key_policy", key_policy)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable_key_rotation is not None:
            pulumi.set(__self__, "enable_key_rotation", enable_key_rotation)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if key_spec is not None:
            pulumi.set(__self__, "key_spec", key_spec)
        if key_usage is not None:
            pulumi.set(__self__, "key_usage", key_usage)
        if multi_region is not None:
            pulumi.set(__self__, "multi_region", multi_region)
        if pending_window_in_days is not None:
            pulumi.set(__self__, "pending_window_in_days", pending_window_in_days)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="keyPolicy")
    def key_policy(self) -> pulumi.Input[Union[Any, str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keypolicy
        """
        return pulumi.get(self, "key_policy")

    @key_policy.setter
    def key_policy(self, value: pulumi.Input[Union[Any, str]]):
        pulumi.set(self, "key_policy", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="enableKeyRotation")
    def enable_key_rotation(self) -> Optional[pulumi.Input[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enablekeyrotation
        """
        return pulumi.get(self, "enable_key_rotation")

    @enable_key_rotation.setter
    def enable_key_rotation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_key_rotation", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enabled
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="keySpec")
    def key_spec(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keyspec
        """
        return pulumi.get(self, "key_spec")

    @key_spec.setter
    def key_spec(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_spec", value)

    @property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keyusage
        """
        return pulumi.get(self, "key_usage")

    @key_usage.setter
    def key_usage(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_usage", value)

    @property
    @pulumi.getter(name="multiRegion")
    def multi_region(self) -> Optional[pulumi.Input[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-multiregion
        """
        return pulumi.get(self, "multi_region")

    @multi_region.setter
    def multi_region(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "multi_region", value)

    @property
    @pulumi.getter(name="pendingWindowInDays")
    def pending_window_in_days(self) -> Optional[pulumi.Input[int]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-pendingwindowindays
        """
        return pulumi.get(self, "pending_window_in_days")

    @pending_window_in_days.setter
    def pending_window_in_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "pending_window_in_days", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Key(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_key_rotation: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 key_policy: Optional[pulumi.Input[Union[Any, str]]] = None,
                 key_spec: Optional[pulumi.Input[str]] = None,
                 key_usage: Optional[pulumi.Input[str]] = None,
                 multi_region: Optional[pulumi.Input[bool]] = None,
                 pending_window_in_days: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-description
        :param pulumi.Input[bool] enable_key_rotation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enablekeyrotation
        :param pulumi.Input[bool] enabled: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enabled
        :param pulumi.Input[Union[Any, str]] key_policy: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keypolicy
        :param pulumi.Input[str] key_spec: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keyspec
        :param pulumi.Input[str] key_usage: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keyusage
        :param pulumi.Input[bool] multi_region: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-multiregion
        :param pulumi.Input[int] pending_window_in_days: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-pendingwindowindays
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html

        :param str resource_name: The name of the resource.
        :param KeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_key_rotation: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 key_policy: Optional[pulumi.Input[Union[Any, str]]] = None,
                 key_spec: Optional[pulumi.Input[str]] = None,
                 key_usage: Optional[pulumi.Input[str]] = None,
                 multi_region: Optional[pulumi.Input[bool]] = None,
                 pending_window_in_days: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
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
            __props__ = KeyArgs.__new__(KeyArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["enable_key_rotation"] = enable_key_rotation
            __props__.__dict__["enabled"] = enabled
            if key_policy is None and not opts.urn:
                raise TypeError("Missing required property 'key_policy'")
            __props__.__dict__["key_policy"] = key_policy
            __props__.__dict__["key_spec"] = key_spec
            __props__.__dict__["key_usage"] = key_usage
            __props__.__dict__["multi_region"] = multi_region
            __props__.__dict__["pending_window_in_days"] = pending_window_in_days
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["key_id"] = None
        super(Key, __self__).__init__(
            'aws-native:kms:Key',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Key':
        """
        Get an existing Key resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = KeyArgs.__new__(KeyArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["enable_key_rotation"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["key_id"] = None
        __props__.__dict__["key_policy"] = None
        __props__.__dict__["key_spec"] = None
        __props__.__dict__["key_usage"] = None
        __props__.__dict__["multi_region"] = None
        __props__.__dict__["pending_window_in_days"] = None
        __props__.__dict__["tags"] = None
        return Key(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="enableKeyRotation")
    def enable_key_rotation(self) -> pulumi.Output[Optional[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enablekeyrotation
        """
        return pulumi.get(self, "enable_key_rotation")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enabled
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter(name="keyPolicy")
    def key_policy(self) -> pulumi.Output[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keypolicy
        """
        return pulumi.get(self, "key_policy")

    @property
    @pulumi.getter(name="keySpec")
    def key_spec(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keyspec
        """
        return pulumi.get(self, "key_spec")

    @property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keyusage
        """
        return pulumi.get(self, "key_usage")

    @property
    @pulumi.getter(name="multiRegion")
    def multi_region(self) -> pulumi.Output[Optional[bool]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-multiregion
        """
        return pulumi.get(self, "multi_region")

    @property
    @pulumi.getter(name="pendingWindowInDays")
    def pending_window_in_days(self) -> pulumi.Output[Optional[int]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-pendingwindowindays
        """
        return pulumi.get(self, "pending_window_in_days")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-tags
        """
        return pulumi.get(self, "tags")

