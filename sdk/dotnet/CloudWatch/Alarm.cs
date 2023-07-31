// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudWatch
{
    /// <summary>
    /// Resource Type definition for AWS::CloudWatch::Alarm
    /// </summary>
    [Obsolete(@"Alarm is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:cloudwatch:Alarm")]
    public partial class Alarm : global::Pulumi.CustomResource
    {
        [Output("actionsEnabled")]
        public Output<bool?> ActionsEnabled { get; private set; } = null!;

        [Output("alarmActions")]
        public Output<ImmutableArray<string>> AlarmActions { get; private set; } = null!;

        [Output("alarmDescription")]
        public Output<string?> AlarmDescription { get; private set; } = null!;

        [Output("alarmName")]
        public Output<string?> AlarmName { get; private set; } = null!;

        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("comparisonOperator")]
        public Output<string> ComparisonOperator { get; private set; } = null!;

        [Output("datapointsToAlarm")]
        public Output<int?> DatapointsToAlarm { get; private set; } = null!;

        [Output("dimensions")]
        public Output<ImmutableArray<Outputs.AlarmDimension>> Dimensions { get; private set; } = null!;

        [Output("evaluateLowSampleCountPercentile")]
        public Output<string?> EvaluateLowSampleCountPercentile { get; private set; } = null!;

        [Output("evaluationPeriods")]
        public Output<int> EvaluationPeriods { get; private set; } = null!;

        [Output("extendedStatistic")]
        public Output<string?> ExtendedStatistic { get; private set; } = null!;

        [Output("insufficientDataActions")]
        public Output<ImmutableArray<string>> InsufficientDataActions { get; private set; } = null!;

        [Output("metricName")]
        public Output<string?> MetricName { get; private set; } = null!;

        [Output("metrics")]
        public Output<ImmutableArray<Outputs.AlarmMetricDataQuery>> Metrics { get; private set; } = null!;

        [Output("namespace")]
        public Output<string?> Namespace { get; private set; } = null!;

        [Output("okActions")]
        public Output<ImmutableArray<string>> OkActions { get; private set; } = null!;

        [Output("period")]
        public Output<int?> Period { get; private set; } = null!;

        [Output("statistic")]
        public Output<string?> Statistic { get; private set; } = null!;

        [Output("threshold")]
        public Output<double?> Threshold { get; private set; } = null!;

        [Output("thresholdMetricId")]
        public Output<string?> ThresholdMetricId { get; private set; } = null!;

        [Output("treatMissingData")]
        public Output<string?> TreatMissingData { get; private set; } = null!;

        [Output("unit")]
        public Output<string?> Unit { get; private set; } = null!;


        /// <summary>
        /// Create a Alarm resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Alarm(string name, AlarmArgs args, CustomResourceOptions? options = null)
            : base("aws-native:cloudwatch:Alarm", name, args ?? new AlarmArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Alarm(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:cloudwatch:Alarm", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Alarm resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Alarm Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Alarm(name, id, options);
        }
    }

    public sealed class AlarmArgs : global::Pulumi.ResourceArgs
    {
        [Input("actionsEnabled")]
        public Input<bool>? ActionsEnabled { get; set; }

        [Input("alarmActions")]
        private InputList<string>? _alarmActions;
        public InputList<string> AlarmActions
        {
            get => _alarmActions ?? (_alarmActions = new InputList<string>());
            set => _alarmActions = value;
        }

        [Input("alarmDescription")]
        public Input<string>? AlarmDescription { get; set; }

        [Input("alarmName")]
        public Input<string>? AlarmName { get; set; }

        [Input("comparisonOperator", required: true)]
        public Input<string> ComparisonOperator { get; set; } = null!;

        [Input("datapointsToAlarm")]
        public Input<int>? DatapointsToAlarm { get; set; }

        [Input("dimensions")]
        private InputList<Inputs.AlarmDimensionArgs>? _dimensions;
        public InputList<Inputs.AlarmDimensionArgs> Dimensions
        {
            get => _dimensions ?? (_dimensions = new InputList<Inputs.AlarmDimensionArgs>());
            set => _dimensions = value;
        }

        [Input("evaluateLowSampleCountPercentile")]
        public Input<string>? EvaluateLowSampleCountPercentile { get; set; }

        [Input("evaluationPeriods", required: true)]
        public Input<int> EvaluationPeriods { get; set; } = null!;

        [Input("extendedStatistic")]
        public Input<string>? ExtendedStatistic { get; set; }

        [Input("insufficientDataActions")]
        private InputList<string>? _insufficientDataActions;
        public InputList<string> InsufficientDataActions
        {
            get => _insufficientDataActions ?? (_insufficientDataActions = new InputList<string>());
            set => _insufficientDataActions = value;
        }

        [Input("metricName")]
        public Input<string>? MetricName { get; set; }

        [Input("metrics")]
        private InputList<Inputs.AlarmMetricDataQueryArgs>? _metrics;
        public InputList<Inputs.AlarmMetricDataQueryArgs> Metrics
        {
            get => _metrics ?? (_metrics = new InputList<Inputs.AlarmMetricDataQueryArgs>());
            set => _metrics = value;
        }

        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        [Input("okActions")]
        private InputList<string>? _okActions;
        public InputList<string> OkActions
        {
            get => _okActions ?? (_okActions = new InputList<string>());
            set => _okActions = value;
        }

        [Input("period")]
        public Input<int>? Period { get; set; }

        [Input("statistic")]
        public Input<string>? Statistic { get; set; }

        [Input("threshold")]
        public Input<double>? Threshold { get; set; }

        [Input("thresholdMetricId")]
        public Input<string>? ThresholdMetricId { get; set; }

        [Input("treatMissingData")]
        public Input<string>? TreatMissingData { get; set; }

        [Input("unit")]
        public Input<string>? Unit { get; set; }

        public AlarmArgs()
        {
        }
        public static new AlarmArgs Empty => new AlarmArgs();
    }
}
