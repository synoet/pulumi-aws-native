// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Evidently
{
    /// <summary>
    /// Resource Type definition for AWS::Evidently::Experiment.
    /// </summary>
    [AwsNativeResourceType("aws-native:evidently:Experiment")]
    public partial class Experiment : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("metricGoals")]
        public Output<ImmutableArray<Outputs.ExperimentMetricGoalObject>> MetricGoals { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("onlineAbConfig")]
        public Output<Outputs.ExperimentOnlineAbConfigObject> OnlineAbConfig { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        [Output("randomizationSalt")]
        public Output<string?> RandomizationSalt { get; private set; } = null!;

        [Output("removeSegment")]
        public Output<bool?> RemoveSegment { get; private set; } = null!;

        /// <summary>
        /// Start Experiment. Default is False
        /// </summary>
        [Output("runningStatus")]
        public Output<Outputs.ExperimentRunningStatusObject?> RunningStatus { get; private set; } = null!;

        [Output("samplingRate")]
        public Output<int?> SamplingRate { get; private set; } = null!;

        [Output("segment")]
        public Output<string?> Segment { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ExperimentTag>> Tags { get; private set; } = null!;

        [Output("treatments")]
        public Output<ImmutableArray<Outputs.ExperimentTreatmentObject>> Treatments { get; private set; } = null!;


        /// <summary>
        /// Create a Experiment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Experiment(string name, ExperimentArgs args, CustomResourceOptions? options = null)
            : base("aws-native:evidently:Experiment", name, args ?? new ExperimentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Experiment(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:evidently:Experiment", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Experiment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Experiment Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Experiment(name, id, options);
        }
    }

    public sealed class ExperimentArgs : global::Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("metricGoals", required: true)]
        private InputList<Inputs.ExperimentMetricGoalObjectArgs>? _metricGoals;
        public InputList<Inputs.ExperimentMetricGoalObjectArgs> MetricGoals
        {
            get => _metricGoals ?? (_metricGoals = new InputList<Inputs.ExperimentMetricGoalObjectArgs>());
            set => _metricGoals = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("onlineAbConfig", required: true)]
        public Input<Inputs.ExperimentOnlineAbConfigObjectArgs> OnlineAbConfig { get; set; } = null!;

        [Input("project", required: true)]
        public Input<string> Project { get; set; } = null!;

        [Input("randomizationSalt")]
        public Input<string>? RandomizationSalt { get; set; }

        [Input("removeSegment")]
        public Input<bool>? RemoveSegment { get; set; }

        /// <summary>
        /// Start Experiment. Default is False
        /// </summary>
        [Input("runningStatus")]
        public Input<Inputs.ExperimentRunningStatusObjectArgs>? RunningStatus { get; set; }

        [Input("samplingRate")]
        public Input<int>? SamplingRate { get; set; }

        [Input("segment")]
        public Input<string>? Segment { get; set; }

        [Input("tags")]
        private InputList<Inputs.ExperimentTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.ExperimentTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ExperimentTagArgs>());
            set => _tags = value;
        }

        [Input("treatments", required: true)]
        private InputList<Inputs.ExperimentTreatmentObjectArgs>? _treatments;
        public InputList<Inputs.ExperimentTreatmentObjectArgs> Treatments
        {
            get => _treatments ?? (_treatments = new InputList<Inputs.ExperimentTreatmentObjectArgs>());
            set => _treatments = value;
        }

        public ExperimentArgs()
        {
        }
        public static new ExperimentArgs Empty => new ExperimentArgs();
    }
}
