// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTAnalytics
{
    /// <summary>
    /// Resource Type definition for AWS::IoTAnalytics::Dataset
    /// </summary>
    [AwsNativeResourceType("aws-native:iotanalytics:Dataset")]
    public partial class Dataset : global::Pulumi.CustomResource
    {
        [Output("actions")]
        public Output<ImmutableArray<Outputs.DatasetAction>> Actions { get; private set; } = null!;

        [Output("contentDeliveryRules")]
        public Output<ImmutableArray<Outputs.DatasetContentDeliveryRule>> ContentDeliveryRules { get; private set; } = null!;

        [Output("datasetName")]
        public Output<string?> DatasetName { get; private set; } = null!;

        [Output("lateDataRules")]
        public Output<ImmutableArray<Outputs.DatasetLateDataRule>> LateDataRules { get; private set; } = null!;

        [Output("retentionPeriod")]
        public Output<Outputs.DatasetRetentionPeriod?> RetentionPeriod { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.DatasetTag>> Tags { get; private set; } = null!;

        [Output("triggers")]
        public Output<ImmutableArray<Outputs.DatasetTrigger>> Triggers { get; private set; } = null!;

        [Output("versioningConfiguration")]
        public Output<Outputs.DatasetVersioningConfiguration?> VersioningConfiguration { get; private set; } = null!;


        /// <summary>
        /// Create a Dataset resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Dataset(string name, DatasetArgs args, CustomResourceOptions? options = null)
            : base("aws-native:iotanalytics:Dataset", name, args ?? new DatasetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Dataset(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iotanalytics:Dataset", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "datasetName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Dataset resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Dataset Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Dataset(name, id, options);
        }
    }

    public sealed class DatasetArgs : global::Pulumi.ResourceArgs
    {
        [Input("actions", required: true)]
        private InputList<Inputs.DatasetActionArgs>? _actions;
        public InputList<Inputs.DatasetActionArgs> Actions
        {
            get => _actions ?? (_actions = new InputList<Inputs.DatasetActionArgs>());
            set => _actions = value;
        }

        [Input("contentDeliveryRules")]
        private InputList<Inputs.DatasetContentDeliveryRuleArgs>? _contentDeliveryRules;
        public InputList<Inputs.DatasetContentDeliveryRuleArgs> ContentDeliveryRules
        {
            get => _contentDeliveryRules ?? (_contentDeliveryRules = new InputList<Inputs.DatasetContentDeliveryRuleArgs>());
            set => _contentDeliveryRules = value;
        }

        [Input("datasetName")]
        public Input<string>? DatasetName { get; set; }

        [Input("lateDataRules")]
        private InputList<Inputs.DatasetLateDataRuleArgs>? _lateDataRules;
        public InputList<Inputs.DatasetLateDataRuleArgs> LateDataRules
        {
            get => _lateDataRules ?? (_lateDataRules = new InputList<Inputs.DatasetLateDataRuleArgs>());
            set => _lateDataRules = value;
        }

        [Input("retentionPeriod")]
        public Input<Inputs.DatasetRetentionPeriodArgs>? RetentionPeriod { get; set; }

        [Input("tags")]
        private InputList<Inputs.DatasetTagArgs>? _tags;
        public InputList<Inputs.DatasetTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.DatasetTagArgs>());
            set => _tags = value;
        }

        [Input("triggers")]
        private InputList<Inputs.DatasetTriggerArgs>? _triggers;
        public InputList<Inputs.DatasetTriggerArgs> Triggers
        {
            get => _triggers ?? (_triggers = new InputList<Inputs.DatasetTriggerArgs>());
            set => _triggers = value;
        }

        [Input("versioningConfiguration")]
        public Input<Inputs.DatasetVersioningConfigurationArgs>? VersioningConfiguration { get; set; }

        public DatasetArgs()
        {
        }
        public static new DatasetArgs Empty => new DatasetArgs();
    }
}
