// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.VpcLattice
{
    /// <summary>
    /// Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon Kinesis Data Firehose. The service network owner can use the access logs to audit the services in the network. The service network owner will only see access logs from clients and services that are associated with their service network. Access log entries represent traffic originated from VPCs associated with that network.
    /// </summary>
    [AwsNativeResourceType("aws-native:vpclattice:AccessLogSubscription")]
    public partial class AccessLogSubscription : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("destinationArn")]
        public Output<string> DestinationArn { get; private set; } = null!;

        [Output("resourceArn")]
        public Output<string> ResourceArn { get; private set; } = null!;

        [Output("resourceId")]
        public Output<string> ResourceId { get; private set; } = null!;

        [Output("resourceIdentifier")]
        public Output<string?> ResourceIdentifier { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.AccessLogSubscriptionTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a AccessLogSubscription resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AccessLogSubscription(string name, AccessLogSubscriptionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:vpclattice:AccessLogSubscription", name, args ?? new AccessLogSubscriptionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AccessLogSubscription(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:vpclattice:AccessLogSubscription", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "resourceIdentifier",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing AccessLogSubscription resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AccessLogSubscription Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new AccessLogSubscription(name, id, options);
        }
    }

    public sealed class AccessLogSubscriptionArgs : global::Pulumi.ResourceArgs
    {
        [Input("destinationArn", required: true)]
        public Input<string> DestinationArn { get; set; } = null!;

        [Input("resourceIdentifier")]
        public Input<string>? ResourceIdentifier { get; set; }

        [Input("tags")]
        private InputList<Inputs.AccessLogSubscriptionTagArgs>? _tags;
        public InputList<Inputs.AccessLogSubscriptionTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.AccessLogSubscriptionTagArgs>());
            set => _tags = value;
        }

        public AccessLogSubscriptionArgs()
        {
        }
        public static new AccessLogSubscriptionArgs Empty => new AccessLogSubscriptionArgs();
    }
}
