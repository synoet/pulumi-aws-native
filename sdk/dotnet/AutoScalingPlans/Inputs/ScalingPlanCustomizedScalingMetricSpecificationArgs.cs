// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.AutoScalingPlans.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html
    /// </summary>
    public sealed class ScalingPlanCustomizedScalingMetricSpecificationArgs : Pulumi.ResourceArgs
    {
        [Input("Dimensions")]
        private InputList<Inputs.ScalingPlanMetricDimensionArgs>? _Dimensions;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-dimensions
        /// </summary>
        public InputList<Inputs.ScalingPlanMetricDimensionArgs> Dimensions
        {
            get => _Dimensions ?? (_Dimensions = new InputList<Inputs.ScalingPlanMetricDimensionArgs>());
            set => _Dimensions = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-metricname
        /// </summary>
        [Input("MetricName", required: true)]
        public Input<string> MetricName { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-namespace
        /// </summary>
        [Input("Namespace", required: true)]
        public Input<string> Namespace { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-statistic
        /// </summary>
        [Input("Statistic", required: true)]
        public Input<string> Statistic { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-unit
        /// </summary>
        [Input("Unit")]
        public Input<string>? Unit { get; set; }

        public ScalingPlanCustomizedScalingMetricSpecificationArgs()
        {
        }
    }
}