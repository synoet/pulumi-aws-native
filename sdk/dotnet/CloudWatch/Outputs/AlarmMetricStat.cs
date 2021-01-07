// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.CloudWatch.Outputs
{

    [OutputType]
    public sealed class AlarmMetricStat
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-metric
        /// </summary>
        public readonly Outputs.AlarmMetric Metric;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-period
        /// </summary>
        public readonly int Period;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-stat
        /// </summary>
        public readonly string Stat;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-unit
        /// </summary>
        public readonly string? Unit;

        [OutputConstructor]
        private AlarmMetricStat(
            Outputs.AlarmMetric Metric,

            int Period,

            string Stat,

            string? Unit)
        {
            this.Metric = Metric;
            this.Period = Period;
            this.Stat = Stat;
            this.Unit = Unit;
        }
    }
}