// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * The AWS::AutoScaling::ScalingPolicy resource specifies an Amazon EC2 Auto Scaling scaling policy so that the Auto Scaling group can scale the number of instances available for your application.
 */
export function getScalingPolicy(args: GetScalingPolicyArgs, opts?: pulumi.InvokeOptions): Promise<GetScalingPolicyResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:autoscaling:getScalingPolicy", {
        "arn": args.arn,
    }, opts);
}

export interface GetScalingPolicyArgs {
    /**
     * The ARN of the AutoScaling scaling policy
     */
    arn: string;
}

export interface GetScalingPolicyResult {
    /**
     * Specifies how the scaling adjustment is interpreted. The valid values are ChangeInCapacity, ExactCapacity, and PercentChangeInCapacity.
     */
    readonly adjustmentType?: string;
    /**
     * The ARN of the AutoScaling scaling policy
     */
    readonly arn?: string;
    /**
     * The duration of the policy's cooldown period, in seconds. When a cooldown period is specified here, it overrides the default cooldown period defined for the Auto Scaling group.
     */
    readonly cooldown?: string;
    /**
     * The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. If not provided, the default is to use the value from the default cooldown period for the Auto Scaling group. Valid only if the policy type is TargetTrackingScaling or StepScaling.
     */
    readonly estimatedInstanceWarmup?: number;
    /**
     * The aggregation type for the CloudWatch metrics. The valid values are Minimum, Maximum, and Average. If the aggregation type is null, the value is treated as Average. Valid only if the policy type is StepScaling.
     */
    readonly metricAggregationType?: string;
    /**
     * The minimum value to scale by when the adjustment type is PercentChangeInCapacity. For example, suppose that you create a step scaling policy to scale out an Auto Scaling group by 25 percent and you specify a MinAdjustmentMagnitude of 2. If the group has 4 instances and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a MinAdjustmentMagnitude of 2, Amazon EC2 Auto Scaling scales out the group by 2 instances.
     */
    readonly minAdjustmentMagnitude?: number;
    readonly policyName?: string;
    /**
     * One of the following policy types: TargetTrackingScaling, StepScaling, SimpleScaling (default), PredictiveScaling
     */
    readonly policyType?: string;
    /**
     * A predictive scaling policy. Includes support for predefined metrics only.
     */
    readonly predictiveScalingConfiguration?: outputs.autoscaling.ScalingPolicyPredictiveScalingConfiguration;
    /**
     * The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity. For exact capacity, you must specify a positive value. Required if the policy type is SimpleScaling. (Not used with any other policy type.)
     */
    readonly scalingAdjustment?: number;
    /**
     * A set of adjustments that enable you to scale based on the size of the alarm breach. Required if the policy type is StepScaling. (Not used with any other policy type.)
     */
    readonly stepAdjustments?: outputs.autoscaling.ScalingPolicyStepAdjustment[];
    /**
     * A target tracking scaling policy. Includes support for predefined or customized metrics.
     */
    readonly targetTrackingConfiguration?: outputs.autoscaling.ScalingPolicyTargetTrackingConfiguration;
}

export function getScalingPolicyOutput(args: GetScalingPolicyOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetScalingPolicyResult> {
    return pulumi.output(args).apply(a => getScalingPolicy(a, opts))
}

export interface GetScalingPolicyOutputArgs {
    /**
     * The ARN of the AutoScaling scaling policy
     */
    arn: pulumi.Input<string>;
}
