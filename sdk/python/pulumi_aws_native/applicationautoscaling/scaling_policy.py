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
from ._inputs import *

__all__ = ['ScalingPolicyArgs', 'ScalingPolicy']

@pulumi.input_type
class ScalingPolicyArgs:
    def __init__(__self__, *,
                 policy_name: pulumi.Input[str],
                 policy_type: pulumi.Input[str],
                 resource_id: Optional[pulumi.Input[str]] = None,
                 scalable_dimension: Optional[pulumi.Input[str]] = None,
                 scaling_target_id: Optional[pulumi.Input[str]] = None,
                 service_namespace: Optional[pulumi.Input[str]] = None,
                 step_scaling_policy_configuration: Optional[pulumi.Input['ScalingPolicyStepScalingPolicyConfigurationArgs']] = None,
                 target_tracking_scaling_policy_configuration: Optional[pulumi.Input['ScalingPolicyTargetTrackingScalingPolicyConfigurationArgs']] = None):
        """
        The set of arguments for constructing a ScalingPolicy resource.
        """
        pulumi.set(__self__, "policy_name", policy_name)
        pulumi.set(__self__, "policy_type", policy_type)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if scalable_dimension is not None:
            pulumi.set(__self__, "scalable_dimension", scalable_dimension)
        if scaling_target_id is not None:
            pulumi.set(__self__, "scaling_target_id", scaling_target_id)
        if service_namespace is not None:
            pulumi.set(__self__, "service_namespace", service_namespace)
        if step_scaling_policy_configuration is not None:
            pulumi.set(__self__, "step_scaling_policy_configuration", step_scaling_policy_configuration)
        if target_tracking_scaling_policy_configuration is not None:
            pulumi.set(__self__, "target_tracking_scaling_policy_configuration", target_tracking_scaling_policy_configuration)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_type", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="scalableDimension")
    def scalable_dimension(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "scalable_dimension")

    @scalable_dimension.setter
    def scalable_dimension(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scalable_dimension", value)

    @property
    @pulumi.getter(name="scalingTargetId")
    def scaling_target_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "scaling_target_id")

    @scaling_target_id.setter
    def scaling_target_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scaling_target_id", value)

    @property
    @pulumi.getter(name="serviceNamespace")
    def service_namespace(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "service_namespace")

    @service_namespace.setter
    def service_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_namespace", value)

    @property
    @pulumi.getter(name="stepScalingPolicyConfiguration")
    def step_scaling_policy_configuration(self) -> Optional[pulumi.Input['ScalingPolicyStepScalingPolicyConfigurationArgs']]:
        return pulumi.get(self, "step_scaling_policy_configuration")

    @step_scaling_policy_configuration.setter
    def step_scaling_policy_configuration(self, value: Optional[pulumi.Input['ScalingPolicyStepScalingPolicyConfigurationArgs']]):
        pulumi.set(self, "step_scaling_policy_configuration", value)

    @property
    @pulumi.getter(name="targetTrackingScalingPolicyConfiguration")
    def target_tracking_scaling_policy_configuration(self) -> Optional[pulumi.Input['ScalingPolicyTargetTrackingScalingPolicyConfigurationArgs']]:
        return pulumi.get(self, "target_tracking_scaling_policy_configuration")

    @target_tracking_scaling_policy_configuration.setter
    def target_tracking_scaling_policy_configuration(self, value: Optional[pulumi.Input['ScalingPolicyTargetTrackingScalingPolicyConfigurationArgs']]):
        pulumi.set(self, "target_tracking_scaling_policy_configuration", value)


warnings.warn("""ScalingPolicy is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ScalingPolicy(pulumi.CustomResource):
    warnings.warn("""ScalingPolicy is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 scalable_dimension: Optional[pulumi.Input[str]] = None,
                 scaling_target_id: Optional[pulumi.Input[str]] = None,
                 service_namespace: Optional[pulumi.Input[str]] = None,
                 step_scaling_policy_configuration: Optional[pulumi.Input[pulumi.InputType['ScalingPolicyStepScalingPolicyConfigurationArgs']]] = None,
                 target_tracking_scaling_policy_configuration: Optional[pulumi.Input[pulumi.InputType['ScalingPolicyTargetTrackingScalingPolicyConfigurationArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ApplicationAutoScaling::ScalingPolicy

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScalingPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ApplicationAutoScaling::ScalingPolicy

        :param str resource_name: The name of the resource.
        :param ScalingPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScalingPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 scalable_dimension: Optional[pulumi.Input[str]] = None,
                 scaling_target_id: Optional[pulumi.Input[str]] = None,
                 service_namespace: Optional[pulumi.Input[str]] = None,
                 step_scaling_policy_configuration: Optional[pulumi.Input[pulumi.InputType['ScalingPolicyStepScalingPolicyConfigurationArgs']]] = None,
                 target_tracking_scaling_policy_configuration: Optional[pulumi.Input[pulumi.InputType['ScalingPolicyTargetTrackingScalingPolicyConfigurationArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""ScalingPolicy is deprecated: ScalingPolicy is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScalingPolicyArgs.__new__(ScalingPolicyArgs)

            if policy_name is None and not opts.urn:
                raise TypeError("Missing required property 'policy_name'")
            __props__.__dict__["policy_name"] = policy_name
            if policy_type is None and not opts.urn:
                raise TypeError("Missing required property 'policy_type'")
            __props__.__dict__["policy_type"] = policy_type
            __props__.__dict__["resource_id"] = resource_id
            __props__.__dict__["scalable_dimension"] = scalable_dimension
            __props__.__dict__["scaling_target_id"] = scaling_target_id
            __props__.__dict__["service_namespace"] = service_namespace
            __props__.__dict__["step_scaling_policy_configuration"] = step_scaling_policy_configuration
            __props__.__dict__["target_tracking_scaling_policy_configuration"] = target_tracking_scaling_policy_configuration
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["policy_name", "resource_id", "scalable_dimension", "scaling_target_id", "service_namespace"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ScalingPolicy, __self__).__init__(
            'aws-native:applicationautoscaling:ScalingPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ScalingPolicy':
        """
        Get an existing ScalingPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScalingPolicyArgs.__new__(ScalingPolicyArgs)

        __props__.__dict__["policy_name"] = None
        __props__.__dict__["policy_type"] = None
        __props__.__dict__["resource_id"] = None
        __props__.__dict__["scalable_dimension"] = None
        __props__.__dict__["scaling_target_id"] = None
        __props__.__dict__["service_namespace"] = None
        __props__.__dict__["step_scaling_policy_configuration"] = None
        __props__.__dict__["target_tracking_scaling_policy_configuration"] = None
        return ScalingPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="scalableDimension")
    def scalable_dimension(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "scalable_dimension")

    @property
    @pulumi.getter(name="scalingTargetId")
    def scaling_target_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "scaling_target_id")

    @property
    @pulumi.getter(name="serviceNamespace")
    def service_namespace(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "service_namespace")

    @property
    @pulumi.getter(name="stepScalingPolicyConfiguration")
    def step_scaling_policy_configuration(self) -> pulumi.Output[Optional['outputs.ScalingPolicyStepScalingPolicyConfiguration']]:
        return pulumi.get(self, "step_scaling_policy_configuration")

    @property
    @pulumi.getter(name="targetTrackingScalingPolicyConfiguration")
    def target_tracking_scaling_policy_configuration(self) -> pulumi.Output[Optional['outputs.ScalingPolicyTargetTrackingScalingPolicyConfiguration']]:
        return pulumi.get(self, "target_tracking_scaling_policy_configuration")

