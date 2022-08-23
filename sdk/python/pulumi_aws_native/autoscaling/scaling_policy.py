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
                 auto_scaling_group_name: pulumi.Input[str],
                 adjustment_type: Optional[pulumi.Input[str]] = None,
                 cooldown: Optional[pulumi.Input[str]] = None,
                 estimated_instance_warmup: Optional[pulumi.Input[int]] = None,
                 metric_aggregation_type: Optional[pulumi.Input[str]] = None,
                 min_adjustment_magnitude: Optional[pulumi.Input[int]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 predictive_scaling_configuration: Optional[pulumi.Input['ScalingPolicyPredictiveScalingConfigurationArgs']] = None,
                 scaling_adjustment: Optional[pulumi.Input[int]] = None,
                 step_adjustments: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPolicyStepAdjustmentArgs']]]] = None,
                 target_tracking_configuration: Optional[pulumi.Input['ScalingPolicyTargetTrackingConfigurationArgs']] = None):
        """
        The set of arguments for constructing a ScalingPolicy resource.
        :param pulumi.Input[str] auto_scaling_group_name: The name of the Auto Scaling group.
        :param pulumi.Input[str] adjustment_type: Specifies how the scaling adjustment is interpreted. The valid values are ChangeInCapacity, ExactCapacity, and PercentChangeInCapacity.
        :param pulumi.Input[str] cooldown: The duration of the policy's cooldown period, in seconds. When a cooldown period is specified here, it overrides the default cooldown period defined for the Auto Scaling group.
        :param pulumi.Input[int] estimated_instance_warmup: The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. If not provided, the default is to use the value from the default cooldown period for the Auto Scaling group. Valid only if the policy type is TargetTrackingScaling or StepScaling.
        :param pulumi.Input[str] metric_aggregation_type: The aggregation type for the CloudWatch metrics. The valid values are Minimum, Maximum, and Average. If the aggregation type is null, the value is treated as Average. Valid only if the policy type is StepScaling.
        :param pulumi.Input[int] min_adjustment_magnitude: The minimum value to scale by when the adjustment type is PercentChangeInCapacity. For example, suppose that you create a step scaling policy to scale out an Auto Scaling group by 25 percent and you specify a MinAdjustmentMagnitude of 2. If the group has 4 instances and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a MinAdjustmentMagnitude of 2, Amazon EC2 Auto Scaling scales out the group by 2 instances.
        :param pulumi.Input[str] policy_type: One of the following policy types: TargetTrackingScaling, StepScaling, SimpleScaling (default), PredictiveScaling
        :param pulumi.Input['ScalingPolicyPredictiveScalingConfigurationArgs'] predictive_scaling_configuration: A predictive scaling policy. Includes support for predefined metrics only.
        :param pulumi.Input[int] scaling_adjustment: The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity. For exact capacity, you must specify a positive value. Required if the policy type is SimpleScaling. (Not used with any other policy type.)
        :param pulumi.Input[Sequence[pulumi.Input['ScalingPolicyStepAdjustmentArgs']]] step_adjustments: A set of adjustments that enable you to scale based on the size of the alarm breach. Required if the policy type is StepScaling. (Not used with any other policy type.)
        :param pulumi.Input['ScalingPolicyTargetTrackingConfigurationArgs'] target_tracking_configuration: A target tracking scaling policy. Includes support for predefined or customized metrics.
        """
        pulumi.set(__self__, "auto_scaling_group_name", auto_scaling_group_name)
        if adjustment_type is not None:
            pulumi.set(__self__, "adjustment_type", adjustment_type)
        if cooldown is not None:
            pulumi.set(__self__, "cooldown", cooldown)
        if estimated_instance_warmup is not None:
            pulumi.set(__self__, "estimated_instance_warmup", estimated_instance_warmup)
        if metric_aggregation_type is not None:
            pulumi.set(__self__, "metric_aggregation_type", metric_aggregation_type)
        if min_adjustment_magnitude is not None:
            pulumi.set(__self__, "min_adjustment_magnitude", min_adjustment_magnitude)
        if policy_type is not None:
            pulumi.set(__self__, "policy_type", policy_type)
        if predictive_scaling_configuration is not None:
            pulumi.set(__self__, "predictive_scaling_configuration", predictive_scaling_configuration)
        if scaling_adjustment is not None:
            pulumi.set(__self__, "scaling_adjustment", scaling_adjustment)
        if step_adjustments is not None:
            pulumi.set(__self__, "step_adjustments", step_adjustments)
        if target_tracking_configuration is not None:
            pulumi.set(__self__, "target_tracking_configuration", target_tracking_configuration)

    @property
    @pulumi.getter(name="autoScalingGroupName")
    def auto_scaling_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Auto Scaling group.
        """
        return pulumi.get(self, "auto_scaling_group_name")

    @auto_scaling_group_name.setter
    def auto_scaling_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "auto_scaling_group_name", value)

    @property
    @pulumi.getter(name="adjustmentType")
    def adjustment_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies how the scaling adjustment is interpreted. The valid values are ChangeInCapacity, ExactCapacity, and PercentChangeInCapacity.
        """
        return pulumi.get(self, "adjustment_type")

    @adjustment_type.setter
    def adjustment_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "adjustment_type", value)

    @property
    @pulumi.getter
    def cooldown(self) -> Optional[pulumi.Input[str]]:
        """
        The duration of the policy's cooldown period, in seconds. When a cooldown period is specified here, it overrides the default cooldown period defined for the Auto Scaling group.
        """
        return pulumi.get(self, "cooldown")

    @cooldown.setter
    def cooldown(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cooldown", value)

    @property
    @pulumi.getter(name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> Optional[pulumi.Input[int]]:
        """
        The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. If not provided, the default is to use the value from the default cooldown period for the Auto Scaling group. Valid only if the policy type is TargetTrackingScaling or StepScaling.
        """
        return pulumi.get(self, "estimated_instance_warmup")

    @estimated_instance_warmup.setter
    def estimated_instance_warmup(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "estimated_instance_warmup", value)

    @property
    @pulumi.getter(name="metricAggregationType")
    def metric_aggregation_type(self) -> Optional[pulumi.Input[str]]:
        """
        The aggregation type for the CloudWatch metrics. The valid values are Minimum, Maximum, and Average. If the aggregation type is null, the value is treated as Average. Valid only if the policy type is StepScaling.
        """
        return pulumi.get(self, "metric_aggregation_type")

    @metric_aggregation_type.setter
    def metric_aggregation_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_aggregation_type", value)

    @property
    @pulumi.getter(name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> Optional[pulumi.Input[int]]:
        """
        The minimum value to scale by when the adjustment type is PercentChangeInCapacity. For example, suppose that you create a step scaling policy to scale out an Auto Scaling group by 25 percent and you specify a MinAdjustmentMagnitude of 2. If the group has 4 instances and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a MinAdjustmentMagnitude of 2, Amazon EC2 Auto Scaling scales out the group by 2 instances.
        """
        return pulumi.get(self, "min_adjustment_magnitude")

    @min_adjustment_magnitude.setter
    def min_adjustment_magnitude(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_adjustment_magnitude", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[str]]:
        """
        One of the following policy types: TargetTrackingScaling, StepScaling, SimpleScaling (default), PredictiveScaling
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_type", value)

    @property
    @pulumi.getter(name="predictiveScalingConfiguration")
    def predictive_scaling_configuration(self) -> Optional[pulumi.Input['ScalingPolicyPredictiveScalingConfigurationArgs']]:
        """
        A predictive scaling policy. Includes support for predefined metrics only.
        """
        return pulumi.get(self, "predictive_scaling_configuration")

    @predictive_scaling_configuration.setter
    def predictive_scaling_configuration(self, value: Optional[pulumi.Input['ScalingPolicyPredictiveScalingConfigurationArgs']]):
        pulumi.set(self, "predictive_scaling_configuration", value)

    @property
    @pulumi.getter(name="scalingAdjustment")
    def scaling_adjustment(self) -> Optional[pulumi.Input[int]]:
        """
        The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity. For exact capacity, you must specify a positive value. Required if the policy type is SimpleScaling. (Not used with any other policy type.)
        """
        return pulumi.get(self, "scaling_adjustment")

    @scaling_adjustment.setter
    def scaling_adjustment(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "scaling_adjustment", value)

    @property
    @pulumi.getter(name="stepAdjustments")
    def step_adjustments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPolicyStepAdjustmentArgs']]]]:
        """
        A set of adjustments that enable you to scale based on the size of the alarm breach. Required if the policy type is StepScaling. (Not used with any other policy type.)
        """
        return pulumi.get(self, "step_adjustments")

    @step_adjustments.setter
    def step_adjustments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPolicyStepAdjustmentArgs']]]]):
        pulumi.set(self, "step_adjustments", value)

    @property
    @pulumi.getter(name="targetTrackingConfiguration")
    def target_tracking_configuration(self) -> Optional[pulumi.Input['ScalingPolicyTargetTrackingConfigurationArgs']]:
        """
        A target tracking scaling policy. Includes support for predefined or customized metrics.
        """
        return pulumi.get(self, "target_tracking_configuration")

    @target_tracking_configuration.setter
    def target_tracking_configuration(self, value: Optional[pulumi.Input['ScalingPolicyTargetTrackingConfigurationArgs']]):
        pulumi.set(self, "target_tracking_configuration", value)


class ScalingPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 adjustment_type: Optional[pulumi.Input[str]] = None,
                 auto_scaling_group_name: Optional[pulumi.Input[str]] = None,
                 cooldown: Optional[pulumi.Input[str]] = None,
                 estimated_instance_warmup: Optional[pulumi.Input[int]] = None,
                 metric_aggregation_type: Optional[pulumi.Input[str]] = None,
                 min_adjustment_magnitude: Optional[pulumi.Input[int]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 predictive_scaling_configuration: Optional[pulumi.Input[pulumi.InputType['ScalingPolicyPredictiveScalingConfigurationArgs']]] = None,
                 scaling_adjustment: Optional[pulumi.Input[int]] = None,
                 step_adjustments: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingPolicyStepAdjustmentArgs']]]]] = None,
                 target_tracking_configuration: Optional[pulumi.Input[pulumi.InputType['ScalingPolicyTargetTrackingConfigurationArgs']]] = None,
                 __props__=None):
        """
        The AWS::AutoScaling::ScalingPolicy resource specifies an Amazon EC2 Auto Scaling scaling policy so that the Auto Scaling group can scale the number of instances available for your application.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] adjustment_type: Specifies how the scaling adjustment is interpreted. The valid values are ChangeInCapacity, ExactCapacity, and PercentChangeInCapacity.
        :param pulumi.Input[str] auto_scaling_group_name: The name of the Auto Scaling group.
        :param pulumi.Input[str] cooldown: The duration of the policy's cooldown period, in seconds. When a cooldown period is specified here, it overrides the default cooldown period defined for the Auto Scaling group.
        :param pulumi.Input[int] estimated_instance_warmup: The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. If not provided, the default is to use the value from the default cooldown period for the Auto Scaling group. Valid only if the policy type is TargetTrackingScaling or StepScaling.
        :param pulumi.Input[str] metric_aggregation_type: The aggregation type for the CloudWatch metrics. The valid values are Minimum, Maximum, and Average. If the aggregation type is null, the value is treated as Average. Valid only if the policy type is StepScaling.
        :param pulumi.Input[int] min_adjustment_magnitude: The minimum value to scale by when the adjustment type is PercentChangeInCapacity. For example, suppose that you create a step scaling policy to scale out an Auto Scaling group by 25 percent and you specify a MinAdjustmentMagnitude of 2. If the group has 4 instances and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a MinAdjustmentMagnitude of 2, Amazon EC2 Auto Scaling scales out the group by 2 instances.
        :param pulumi.Input[str] policy_type: One of the following policy types: TargetTrackingScaling, StepScaling, SimpleScaling (default), PredictiveScaling
        :param pulumi.Input[pulumi.InputType['ScalingPolicyPredictiveScalingConfigurationArgs']] predictive_scaling_configuration: A predictive scaling policy. Includes support for predefined metrics only.
        :param pulumi.Input[int] scaling_adjustment: The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity. For exact capacity, you must specify a positive value. Required if the policy type is SimpleScaling. (Not used with any other policy type.)
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingPolicyStepAdjustmentArgs']]]] step_adjustments: A set of adjustments that enable you to scale based on the size of the alarm breach. Required if the policy type is StepScaling. (Not used with any other policy type.)
        :param pulumi.Input[pulumi.InputType['ScalingPolicyTargetTrackingConfigurationArgs']] target_tracking_configuration: A target tracking scaling policy. Includes support for predefined or customized metrics.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScalingPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::AutoScaling::ScalingPolicy resource specifies an Amazon EC2 Auto Scaling scaling policy so that the Auto Scaling group can scale the number of instances available for your application.

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
                 adjustment_type: Optional[pulumi.Input[str]] = None,
                 auto_scaling_group_name: Optional[pulumi.Input[str]] = None,
                 cooldown: Optional[pulumi.Input[str]] = None,
                 estimated_instance_warmup: Optional[pulumi.Input[int]] = None,
                 metric_aggregation_type: Optional[pulumi.Input[str]] = None,
                 min_adjustment_magnitude: Optional[pulumi.Input[int]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 predictive_scaling_configuration: Optional[pulumi.Input[pulumi.InputType['ScalingPolicyPredictiveScalingConfigurationArgs']]] = None,
                 scaling_adjustment: Optional[pulumi.Input[int]] = None,
                 step_adjustments: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingPolicyStepAdjustmentArgs']]]]] = None,
                 target_tracking_configuration: Optional[pulumi.Input[pulumi.InputType['ScalingPolicyTargetTrackingConfigurationArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScalingPolicyArgs.__new__(ScalingPolicyArgs)

            __props__.__dict__["adjustment_type"] = adjustment_type
            if auto_scaling_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'auto_scaling_group_name'")
            __props__.__dict__["auto_scaling_group_name"] = auto_scaling_group_name
            __props__.__dict__["cooldown"] = cooldown
            __props__.__dict__["estimated_instance_warmup"] = estimated_instance_warmup
            __props__.__dict__["metric_aggregation_type"] = metric_aggregation_type
            __props__.__dict__["min_adjustment_magnitude"] = min_adjustment_magnitude
            __props__.__dict__["policy_type"] = policy_type
            __props__.__dict__["predictive_scaling_configuration"] = predictive_scaling_configuration
            __props__.__dict__["scaling_adjustment"] = scaling_adjustment
            __props__.__dict__["step_adjustments"] = step_adjustments
            __props__.__dict__["target_tracking_configuration"] = target_tracking_configuration
            __props__.__dict__["arn"] = None
            __props__.__dict__["policy_name"] = None
        super(ScalingPolicy, __self__).__init__(
            'aws-native:autoscaling:ScalingPolicy',
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

        __props__.__dict__["adjustment_type"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["auto_scaling_group_name"] = None
        __props__.__dict__["cooldown"] = None
        __props__.__dict__["estimated_instance_warmup"] = None
        __props__.__dict__["metric_aggregation_type"] = None
        __props__.__dict__["min_adjustment_magnitude"] = None
        __props__.__dict__["policy_name"] = None
        __props__.__dict__["policy_type"] = None
        __props__.__dict__["predictive_scaling_configuration"] = None
        __props__.__dict__["scaling_adjustment"] = None
        __props__.__dict__["step_adjustments"] = None
        __props__.__dict__["target_tracking_configuration"] = None
        return ScalingPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adjustmentType")
    def adjustment_type(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies how the scaling adjustment is interpreted. The valid values are ChangeInCapacity, ExactCapacity, and PercentChangeInCapacity.
        """
        return pulumi.get(self, "adjustment_type")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the AutoScaling scaling policy
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="autoScalingGroupName")
    def auto_scaling_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Auto Scaling group.
        """
        return pulumi.get(self, "auto_scaling_group_name")

    @property
    @pulumi.getter
    def cooldown(self) -> pulumi.Output[Optional[str]]:
        """
        The duration of the policy's cooldown period, in seconds. When a cooldown period is specified here, it overrides the default cooldown period defined for the Auto Scaling group.
        """
        return pulumi.get(self, "cooldown")

    @property
    @pulumi.getter(name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> pulumi.Output[Optional[int]]:
        """
        The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. If not provided, the default is to use the value from the default cooldown period for the Auto Scaling group. Valid only if the policy type is TargetTrackingScaling or StepScaling.
        """
        return pulumi.get(self, "estimated_instance_warmup")

    @property
    @pulumi.getter(name="metricAggregationType")
    def metric_aggregation_type(self) -> pulumi.Output[Optional[str]]:
        """
        The aggregation type for the CloudWatch metrics. The valid values are Minimum, Maximum, and Average. If the aggregation type is null, the value is treated as Average. Valid only if the policy type is StepScaling.
        """
        return pulumi.get(self, "metric_aggregation_type")

    @property
    @pulumi.getter(name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> pulumi.Output[Optional[int]]:
        """
        The minimum value to scale by when the adjustment type is PercentChangeInCapacity. For example, suppose that you create a step scaling policy to scale out an Auto Scaling group by 25 percent and you specify a MinAdjustmentMagnitude of 2. If the group has 4 instances and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a MinAdjustmentMagnitude of 2, Amazon EC2 Auto Scaling scales out the group by 2 instances.
        """
        return pulumi.get(self, "min_adjustment_magnitude")

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[Optional[str]]:
        """
        One of the following policy types: TargetTrackingScaling, StepScaling, SimpleScaling (default), PredictiveScaling
        """
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter(name="predictiveScalingConfiguration")
    def predictive_scaling_configuration(self) -> pulumi.Output[Optional['outputs.ScalingPolicyPredictiveScalingConfiguration']]:
        """
        A predictive scaling policy. Includes support for predefined metrics only.
        """
        return pulumi.get(self, "predictive_scaling_configuration")

    @property
    @pulumi.getter(name="scalingAdjustment")
    def scaling_adjustment(self) -> pulumi.Output[Optional[int]]:
        """
        The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity. For exact capacity, you must specify a positive value. Required if the policy type is SimpleScaling. (Not used with any other policy type.)
        """
        return pulumi.get(self, "scaling_adjustment")

    @property
    @pulumi.getter(name="stepAdjustments")
    def step_adjustments(self) -> pulumi.Output[Optional[Sequence['outputs.ScalingPolicyStepAdjustment']]]:
        """
        A set of adjustments that enable you to scale based on the size of the alarm breach. Required if the policy type is StepScaling. (Not used with any other policy type.)
        """
        return pulumi.get(self, "step_adjustments")

    @property
    @pulumi.getter(name="targetTrackingConfiguration")
    def target_tracking_configuration(self) -> pulumi.Output[Optional['outputs.ScalingPolicyTargetTrackingConfiguration']]:
        """
        A target tracking scaling policy. Includes support for predefined or customized metrics.
        """
        return pulumi.get(self, "target_tracking_configuration")

