// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppConfig
{
    /// <summary>
    /// Resource Type definition for AWS::AppConfig::DeploymentStrategy
    /// </summary>
    [Obsolete(@"DeploymentStrategy is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:appconfig:DeploymentStrategy")]
    public partial class DeploymentStrategy : Pulumi.CustomResource
    {
        [Output("deploymentDurationInMinutes")]
        public Output<double> DeploymentDurationInMinutes { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("finalBakeTimeInMinutes")]
        public Output<double?> FinalBakeTimeInMinutes { get; private set; } = null!;

        [Output("growthFactor")]
        public Output<double> GrowthFactor { get; private set; } = null!;

        [Output("growthType")]
        public Output<string?> GrowthType { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("replicateTo")]
        public Output<string> ReplicateTo { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.DeploymentStrategyTags>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a DeploymentStrategy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DeploymentStrategy(string name, DeploymentStrategyArgs args, CustomResourceOptions? options = null)
            : base("aws-native:appconfig:DeploymentStrategy", name, args ?? new DeploymentStrategyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DeploymentStrategy(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:appconfig:DeploymentStrategy", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing DeploymentStrategy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DeploymentStrategy Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DeploymentStrategy(name, id, options);
        }
    }

    public sealed class DeploymentStrategyArgs : Pulumi.ResourceArgs
    {
        [Input("deploymentDurationInMinutes", required: true)]
        public Input<double> DeploymentDurationInMinutes { get; set; } = null!;

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("finalBakeTimeInMinutes")]
        public Input<double>? FinalBakeTimeInMinutes { get; set; }

        [Input("growthFactor", required: true)]
        public Input<double> GrowthFactor { get; set; } = null!;

        [Input("growthType")]
        public Input<string>? GrowthType { get; set; }

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("replicateTo", required: true)]
        public Input<string> ReplicateTo { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.DeploymentStrategyTagsArgs>? _tags;
        public InputList<Inputs.DeploymentStrategyTagsArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.DeploymentStrategyTagsArgs>());
            set => _tags = value;
        }

        public DeploymentStrategyArgs()
        {
        }
    }
}
