// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    /// <summary>
    /// Resource schema for AWS::EC2::NetworkInsightsAnalysis
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:NetworkInsightsAnalysis")]
    public partial class NetworkInsightsAnalysis : global::Pulumi.CustomResource
    {
        [Output("additionalAccounts")]
        public Output<ImmutableArray<string>> AdditionalAccounts { get; private set; } = null!;

        [Output("alternatePathHints")]
        public Output<ImmutableArray<Outputs.NetworkInsightsAnalysisAlternatePathHint>> AlternatePathHints { get; private set; } = null!;

        [Output("explanations")]
        public Output<ImmutableArray<Outputs.NetworkInsightsAnalysisExplanation>> Explanations { get; private set; } = null!;

        [Output("filterInArns")]
        public Output<ImmutableArray<string>> FilterInArns { get; private set; } = null!;

        [Output("forwardPathComponents")]
        public Output<ImmutableArray<Outputs.NetworkInsightsAnalysisPathComponent>> ForwardPathComponents { get; private set; } = null!;

        [Output("networkInsightsAnalysisArn")]
        public Output<string> NetworkInsightsAnalysisArn { get; private set; } = null!;

        [Output("networkInsightsAnalysisId")]
        public Output<string> NetworkInsightsAnalysisId { get; private set; } = null!;

        [Output("networkInsightsPathId")]
        public Output<string> NetworkInsightsPathId { get; private set; } = null!;

        [Output("networkPathFound")]
        public Output<bool> NetworkPathFound { get; private set; } = null!;

        [Output("returnPathComponents")]
        public Output<ImmutableArray<Outputs.NetworkInsightsAnalysisPathComponent>> ReturnPathComponents { get; private set; } = null!;

        [Output("startDate")]
        public Output<string> StartDate { get; private set; } = null!;

        [Output("status")]
        public Output<Pulumi.AwsNative.EC2.NetworkInsightsAnalysisStatus> Status { get; private set; } = null!;

        [Output("statusMessage")]
        public Output<string> StatusMessage { get; private set; } = null!;

        [Output("suggestedAccounts")]
        public Output<ImmutableArray<string>> SuggestedAccounts { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.NetworkInsightsAnalysisTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a NetworkInsightsAnalysis resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NetworkInsightsAnalysis(string name, NetworkInsightsAnalysisArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:NetworkInsightsAnalysis", name, args ?? new NetworkInsightsAnalysisArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NetworkInsightsAnalysis(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:NetworkInsightsAnalysis", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing NetworkInsightsAnalysis resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NetworkInsightsAnalysis Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new NetworkInsightsAnalysis(name, id, options);
        }
    }

    public sealed class NetworkInsightsAnalysisArgs : global::Pulumi.ResourceArgs
    {
        [Input("additionalAccounts")]
        private InputList<string>? _additionalAccounts;
        public InputList<string> AdditionalAccounts
        {
            get => _additionalAccounts ?? (_additionalAccounts = new InputList<string>());
            set => _additionalAccounts = value;
        }

        [Input("filterInArns")]
        private InputList<string>? _filterInArns;
        public InputList<string> FilterInArns
        {
            get => _filterInArns ?? (_filterInArns = new InputList<string>());
            set => _filterInArns = value;
        }

        [Input("networkInsightsPathId", required: true)]
        public Input<string> NetworkInsightsPathId { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.NetworkInsightsAnalysisTagArgs>? _tags;
        public InputList<Inputs.NetworkInsightsAnalysisTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.NetworkInsightsAnalysisTagArgs>());
            set => _tags = value;
        }

        public NetworkInsightsAnalysisArgs()
        {
        }
        public static new NetworkInsightsAnalysisArgs Empty => new NetworkInsightsAnalysisArgs();
    }
}
