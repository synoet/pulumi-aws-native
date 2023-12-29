// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Location
{
    /// <summary>
    /// Definition of AWS::Location::Tracker Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:location:Tracker")]
    public partial class Tracker : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("eventBridgeEnabled")]
        public Output<bool?> EventBridgeEnabled { get; private set; } = null!;

        [Output("kmsKeyEnableGeospatialQueries")]
        public Output<bool?> KmsKeyEnableGeospatialQueries { get; private set; } = null!;

        [Output("kmsKeyId")]
        public Output<string?> KmsKeyId { get; private set; } = null!;

        [Output("positionFiltering")]
        public Output<Pulumi.AwsNative.Location.TrackerPositionFiltering?> PositionFiltering { get; private set; } = null!;

        [Output("pricingPlan")]
        public Output<Pulumi.AwsNative.Location.TrackerPricingPlan?> PricingPlan { get; private set; } = null!;

        [Output("pricingPlanDataSource")]
        public Output<string?> PricingPlanDataSource { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.TrackerTag>> Tags { get; private set; } = null!;

        [Output("trackerArn")]
        public Output<string> TrackerArn { get; private set; } = null!;

        [Output("trackerName")]
        public Output<string> TrackerName { get; private set; } = null!;

        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;


        /// <summary>
        /// Create a Tracker resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Tracker(string name, TrackerArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:location:Tracker", name, args ?? new TrackerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Tracker(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:location:Tracker", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "kmsKeyId",
                    "trackerName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Tracker resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Tracker Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Tracker(name, id, options);
        }
    }

    public sealed class TrackerArgs : global::Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("eventBridgeEnabled")]
        public Input<bool>? EventBridgeEnabled { get; set; }

        [Input("kmsKeyEnableGeospatialQueries")]
        public Input<bool>? KmsKeyEnableGeospatialQueries { get; set; }

        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        [Input("positionFiltering")]
        public Input<Pulumi.AwsNative.Location.TrackerPositionFiltering>? PositionFiltering { get; set; }

        [Input("pricingPlan")]
        public Input<Pulumi.AwsNative.Location.TrackerPricingPlan>? PricingPlan { get; set; }

        [Input("pricingPlanDataSource")]
        public Input<string>? PricingPlanDataSource { get; set; }

        [Input("tags")]
        private InputList<Inputs.TrackerTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.TrackerTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.TrackerTagArgs>());
            set => _tags = value;
        }

        [Input("trackerName")]
        public Input<string>? TrackerName { get; set; }

        public TrackerArgs()
        {
        }
        public static new TrackerArgs Empty => new TrackerArgs();
    }
}
