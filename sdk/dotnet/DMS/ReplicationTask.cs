// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DMS
{
    /// <summary>
    /// Resource Type definition for AWS::DMS::ReplicationTask
    /// </summary>
    [Obsolete(@"ReplicationTask is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:dms:ReplicationTask")]
    public partial class ReplicationTask : Pulumi.CustomResource
    {
        [Output("cdcStartPosition")]
        public Output<string?> CdcStartPosition { get; private set; } = null!;

        [Output("cdcStartTime")]
        public Output<double?> CdcStartTime { get; private set; } = null!;

        [Output("cdcStopPosition")]
        public Output<string?> CdcStopPosition { get; private set; } = null!;

        [Output("migrationType")]
        public Output<string> MigrationType { get; private set; } = null!;

        [Output("replicationInstanceArn")]
        public Output<string> ReplicationInstanceArn { get; private set; } = null!;

        [Output("replicationTaskIdentifier")]
        public Output<string?> ReplicationTaskIdentifier { get; private set; } = null!;

        [Output("replicationTaskSettings")]
        public Output<string?> ReplicationTaskSettings { get; private set; } = null!;

        [Output("resourceIdentifier")]
        public Output<string?> ResourceIdentifier { get; private set; } = null!;

        [Output("sourceEndpointArn")]
        public Output<string> SourceEndpointArn { get; private set; } = null!;

        [Output("tableMappings")]
        public Output<string> TableMappings { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.ReplicationTaskTag>> Tags { get; private set; } = null!;

        [Output("targetEndpointArn")]
        public Output<string> TargetEndpointArn { get; private set; } = null!;

        [Output("taskData")]
        public Output<string?> TaskData { get; private set; } = null!;


        /// <summary>
        /// Create a ReplicationTask resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ReplicationTask(string name, ReplicationTaskArgs args, CustomResourceOptions? options = null)
            : base("aws-native:dms:ReplicationTask", name, args ?? new ReplicationTaskArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ReplicationTask(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:dms:ReplicationTask", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ReplicationTask resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ReplicationTask Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ReplicationTask(name, id, options);
        }
    }

    public sealed class ReplicationTaskArgs : Pulumi.ResourceArgs
    {
        [Input("cdcStartPosition")]
        public Input<string>? CdcStartPosition { get; set; }

        [Input("cdcStartTime")]
        public Input<double>? CdcStartTime { get; set; }

        [Input("cdcStopPosition")]
        public Input<string>? CdcStopPosition { get; set; }

        [Input("migrationType", required: true)]
        public Input<string> MigrationType { get; set; } = null!;

        [Input("replicationInstanceArn", required: true)]
        public Input<string> ReplicationInstanceArn { get; set; } = null!;

        [Input("replicationTaskIdentifier")]
        public Input<string>? ReplicationTaskIdentifier { get; set; }

        [Input("replicationTaskSettings")]
        public Input<string>? ReplicationTaskSettings { get; set; }

        [Input("resourceIdentifier")]
        public Input<string>? ResourceIdentifier { get; set; }

        [Input("sourceEndpointArn", required: true)]
        public Input<string> SourceEndpointArn { get; set; } = null!;

        [Input("tableMappings", required: true)]
        public Input<string> TableMappings { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.ReplicationTaskTagArgs>? _tags;
        public InputList<Inputs.ReplicationTaskTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ReplicationTaskTagArgs>());
            set => _tags = value;
        }

        [Input("targetEndpointArn", required: true)]
        public Input<string> TargetEndpointArn { get; set; } = null!;

        [Input("taskData")]
        public Input<string>? TaskData { get; set; }

        public ReplicationTaskArgs()
        {
        }
    }
}
