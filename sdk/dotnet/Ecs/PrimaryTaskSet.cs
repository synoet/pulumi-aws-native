// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ecs
{
    /// <summary>
    /// A pseudo-resource that manages which of your ECS task sets is primary.
    /// </summary>
    [AwsNativeResourceType("aws-native:ecs:PrimaryTaskSet")]
    public partial class PrimaryTaskSet : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.
        /// </summary>
        [Output("cluster")]
        public Output<string> Cluster { get; private set; } = null!;

        /// <summary>
        /// The short name or full Amazon Resource Name (ARN) of the service to create the task set in.
        /// </summary>
        [Output("service")]
        public Output<string> Service { get; private set; } = null!;

        /// <summary>
        /// The ID or full Amazon Resource Name (ARN) of the task set.
        /// </summary>
        [Output("taskSetId")]
        public Output<string> TaskSetId { get; private set; } = null!;


        /// <summary>
        /// Create a PrimaryTaskSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PrimaryTaskSet(string name, PrimaryTaskSetArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ecs:PrimaryTaskSet", name, args ?? new PrimaryTaskSetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private PrimaryTaskSet(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ecs:PrimaryTaskSet", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "cluster",
                    "service",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing PrimaryTaskSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PrimaryTaskSet Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new PrimaryTaskSet(name, id, options);
        }
    }

    public sealed class PrimaryTaskSetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.
        /// </summary>
        [Input("cluster", required: true)]
        public Input<string> Cluster { get; set; } = null!;

        /// <summary>
        /// The short name or full Amazon Resource Name (ARN) of the service to create the task set in.
        /// </summary>
        [Input("service", required: true)]
        public Input<string> Service { get; set; } = null!;

        /// <summary>
        /// The ID or full Amazon Resource Name (ARN) of the task set.
        /// </summary>
        [Input("taskSetId", required: true)]
        public Input<string> TaskSetId { get; set; } = null!;

        public PrimaryTaskSetArgs()
        {
        }
        public static new PrimaryTaskSetArgs Empty => new PrimaryTaskSetArgs();
    }
}
