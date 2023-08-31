// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.BillingConductor
{
    /// <summary>
    /// A billing group is a set of linked account which belong to the same end customer. It can be seen as a virtual consolidated billing family.
    /// </summary>
    [Obsolete(@"BillingGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:billingconductor:BillingGroup")]
    public partial class BillingGroup : global::Pulumi.CustomResource
    {
        [Output("accountGrouping")]
        public Output<Outputs.BillingGroupAccountGrouping> AccountGrouping { get; private set; } = null!;

        /// <summary>
        /// Billing Group ARN
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("computationPreference")]
        public Output<Outputs.BillingGroupComputationPreference> ComputationPreference { get; private set; } = null!;

        /// <summary>
        /// Creation timestamp in UNIX epoch time format
        /// </summary>
        [Output("creationTime")]
        public Output<int> CreationTime { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Latest modified timestamp in UNIX epoch time format
        /// </summary>
        [Output("lastModifiedTime")]
        public Output<int> LastModifiedTime { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// This account will act as a virtual payer account of the billing group
        /// </summary>
        [Output("primaryAccountId")]
        public Output<string> PrimaryAccountId { get; private set; } = null!;

        /// <summary>
        /// Number of accounts in the billing group
        /// </summary>
        [Output("size")]
        public Output<int> Size { get; private set; } = null!;

        [Output("status")]
        public Output<Pulumi.AwsNative.BillingConductor.BillingGroupStatus> Status { get; private set; } = null!;

        [Output("statusReason")]
        public Output<string> StatusReason { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.BillingGroupTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a BillingGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BillingGroup(string name, BillingGroupArgs args, CustomResourceOptions? options = null)
            : base("aws-native:billingconductor:BillingGroup", name, args ?? new BillingGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private BillingGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:billingconductor:BillingGroup", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "primaryAccountId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing BillingGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BillingGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new BillingGroup(name, id, options);
        }
    }

    public sealed class BillingGroupArgs : global::Pulumi.ResourceArgs
    {
        [Input("accountGrouping", required: true)]
        public Input<Inputs.BillingGroupAccountGroupingArgs> AccountGrouping { get; set; } = null!;

        [Input("computationPreference", required: true)]
        public Input<Inputs.BillingGroupComputationPreferenceArgs> ComputationPreference { get; set; } = null!;

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// This account will act as a virtual payer account of the billing group
        /// </summary>
        [Input("primaryAccountId", required: true)]
        public Input<string> PrimaryAccountId { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.BillingGroupTagArgs>? _tags;
        public InputList<Inputs.BillingGroupTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.BillingGroupTagArgs>());
            set => _tags = value;
        }

        public BillingGroupArgs()
        {
        }
        public static new BillingGroupArgs Empty => new BillingGroupArgs();
    }
}
