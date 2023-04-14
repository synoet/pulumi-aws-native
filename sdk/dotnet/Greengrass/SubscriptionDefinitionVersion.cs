// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Greengrass
{
    /// <summary>
    /// Resource Type definition for AWS::Greengrass::SubscriptionDefinitionVersion
    /// </summary>
    [Obsolete(@"SubscriptionDefinitionVersion is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:greengrass:SubscriptionDefinitionVersion")]
    public partial class SubscriptionDefinitionVersion : global::Pulumi.CustomResource
    {
        [Output("subscriptionDefinitionId")]
        public Output<string> SubscriptionDefinitionId { get; private set; } = null!;

        [Output("subscriptions")]
        public Output<ImmutableArray<Outputs.SubscriptionDefinitionVersionSubscription>> Subscriptions { get; private set; } = null!;


        /// <summary>
        /// Create a SubscriptionDefinitionVersion resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SubscriptionDefinitionVersion(string name, SubscriptionDefinitionVersionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:greengrass:SubscriptionDefinitionVersion", name, args ?? new SubscriptionDefinitionVersionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SubscriptionDefinitionVersion(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:greengrass:SubscriptionDefinitionVersion", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing SubscriptionDefinitionVersion resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SubscriptionDefinitionVersion Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new SubscriptionDefinitionVersion(name, id, options);
        }
    }

    public sealed class SubscriptionDefinitionVersionArgs : global::Pulumi.ResourceArgs
    {
        [Input("subscriptionDefinitionId", required: true)]
        public Input<string> SubscriptionDefinitionId { get; set; } = null!;

        [Input("subscriptions", required: true)]
        private InputList<Inputs.SubscriptionDefinitionVersionSubscriptionArgs>? _subscriptions;
        public InputList<Inputs.SubscriptionDefinitionVersionSubscriptionArgs> Subscriptions
        {
            get => _subscriptions ?? (_subscriptions = new InputList<Inputs.SubscriptionDefinitionVersionSubscriptionArgs>());
            set => _subscriptions = value;
        }

        public SubscriptionDefinitionVersionArgs()
        {
        }
        public static new SubscriptionDefinitionVersionArgs Empty => new SubscriptionDefinitionVersionArgs();
    }
}
