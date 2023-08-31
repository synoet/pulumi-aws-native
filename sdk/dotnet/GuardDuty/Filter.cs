// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GuardDuty
{
    /// <summary>
    /// Resource Type definition for AWS::GuardDuty::Filter
    /// </summary>
    [Obsolete(@"Filter is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:guardduty:Filter")]
    public partial class Filter : global::Pulumi.CustomResource
    {
        [Output("action")]
        public Output<string> Action { get; private set; } = null!;

        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        [Output("detectorId")]
        public Output<string> DetectorId { get; private set; } = null!;

        [Output("findingCriteria")]
        public Output<Outputs.FilterFindingCriteria> FindingCriteria { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("rank")]
        public Output<int> Rank { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.FilterTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Filter resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Filter(string name, FilterArgs args, CustomResourceOptions? options = null)
            : base("aws-native:guardduty:Filter", name, args ?? new FilterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Filter(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:guardduty:Filter", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "detectorId",
                    "name",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Filter resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Filter Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Filter(name, id, options);
        }
    }

    public sealed class FilterArgs : global::Pulumi.ResourceArgs
    {
        [Input("action", required: true)]
        public Input<string> Action { get; set; } = null!;

        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        [Input("detectorId", required: true)]
        public Input<string> DetectorId { get; set; } = null!;

        [Input("findingCriteria", required: true)]
        public Input<Inputs.FilterFindingCriteriaArgs> FindingCriteria { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("rank", required: true)]
        public Input<int> Rank { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.FilterTagArgs>? _tags;
        public InputList<Inputs.FilterTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.FilterTagArgs>());
            set => _tags = value;
        }

        public FilterArgs()
        {
        }
        public static new FilterArgs Empty => new FilterArgs();
    }
}
