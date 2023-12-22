// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Dms
{
    /// <summary>
    /// A replication configuration that you later provide to configure and start a AWS DMS Serverless replication
    /// </summary>
    [AwsNativeResourceType("aws-native:dms:ReplicationConfig")]
    public partial class ReplicationConfig : global::Pulumi.CustomResource
    {
        [Output("computeConfig")]
        public Output<Outputs.ReplicationConfigComputeConfig?> ComputeConfig { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Replication Config
        /// </summary>
        [Output("replicationConfigArn")]
        public Output<string?> ReplicationConfigArn { get; private set; } = null!;

        /// <summary>
        /// A unique identifier of replication configuration
        /// </summary>
        [Output("replicationConfigIdentifier")]
        public Output<string?> ReplicationConfigIdentifier { get; private set; } = null!;

        /// <summary>
        /// JSON settings for Servereless replications that are provisioned using this replication configuration
        /// </summary>
        [Output("replicationSettings")]
        public Output<object?> ReplicationSettings { get; private set; } = null!;

        /// <summary>
        /// The type of AWS DMS Serverless replication to provision using this replication configuration
        /// </summary>
        [Output("replicationType")]
        public Output<Pulumi.AwsNative.Dms.ReplicationConfigReplicationType?> ReplicationType { get; private set; } = null!;

        /// <summary>
        /// A unique value or name that you get set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource
        /// </summary>
        [Output("resourceIdentifier")]
        public Output<string?> ResourceIdentifier { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration
        /// </summary>
        [Output("sourceEndpointArn")]
        public Output<string?> SourceEndpointArn { get; private set; } = null!;

        /// <summary>
        /// JSON settings for specifying supplemental data
        /// </summary>
        [Output("supplementalSettings")]
        public Output<object?> SupplementalSettings { get; private set; } = null!;

        /// <summary>
        /// JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration
        /// </summary>
        [Output("tableMappings")]
        public Output<object?> TableMappings { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.&lt;/p&gt;
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ReplicationConfigTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS Serverless replication configuration
        /// </summary>
        [Output("targetEndpointArn")]
        public Output<string?> TargetEndpointArn { get; private set; } = null!;


        /// <summary>
        /// Create a ReplicationConfig resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ReplicationConfig(string name, ReplicationConfigArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:dms:ReplicationConfig", name, args ?? new ReplicationConfigArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ReplicationConfig(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:dms:ReplicationConfig", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ReplicationConfig resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ReplicationConfig Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ReplicationConfig(name, id, options);
        }
    }

    public sealed class ReplicationConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("computeConfig")]
        public Input<Inputs.ReplicationConfigComputeConfigArgs>? ComputeConfig { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Replication Config
        /// </summary>
        [Input("replicationConfigArn")]
        public Input<string>? ReplicationConfigArn { get; set; }

        /// <summary>
        /// A unique identifier of replication configuration
        /// </summary>
        [Input("replicationConfigIdentifier")]
        public Input<string>? ReplicationConfigIdentifier { get; set; }

        /// <summary>
        /// JSON settings for Servereless replications that are provisioned using this replication configuration
        /// </summary>
        [Input("replicationSettings")]
        public Input<object>? ReplicationSettings { get; set; }

        /// <summary>
        /// The type of AWS DMS Serverless replication to provision using this replication configuration
        /// </summary>
        [Input("replicationType")]
        public Input<Pulumi.AwsNative.Dms.ReplicationConfigReplicationType>? ReplicationType { get; set; }

        /// <summary>
        /// A unique value or name that you get set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource
        /// </summary>
        [Input("resourceIdentifier")]
        public Input<string>? ResourceIdentifier { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration
        /// </summary>
        [Input("sourceEndpointArn")]
        public Input<string>? SourceEndpointArn { get; set; }

        /// <summary>
        /// JSON settings for specifying supplemental data
        /// </summary>
        [Input("supplementalSettings")]
        public Input<object>? SupplementalSettings { get; set; }

        /// <summary>
        /// JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration
        /// </summary>
        [Input("tableMappings")]
        public Input<object>? TableMappings { get; set; }

        [Input("tags")]
        private InputList<Inputs.ReplicationConfigTagArgs>? _tags;

        /// <summary>
        /// &lt;p&gt;Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.&lt;/p&gt;
        /// </summary>
        public InputList<Inputs.ReplicationConfigTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ReplicationConfigTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS Serverless replication configuration
        /// </summary>
        [Input("targetEndpointArn")]
        public Input<string>? TargetEndpointArn { get; set; }

        public ReplicationConfigArgs()
        {
        }
        public static new ReplicationConfigArgs Empty => new ReplicationConfigArgs();
    }
}
