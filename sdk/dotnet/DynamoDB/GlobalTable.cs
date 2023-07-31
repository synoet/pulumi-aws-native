// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DynamoDB
{
    /// <summary>
    /// Version: None. Resource Type definition for AWS::DynamoDB::GlobalTable
    /// </summary>
    [AwsNativeResourceType("aws-native:dynamodb:GlobalTable")]
    public partial class GlobalTable : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("attributeDefinitions")]
        public Output<ImmutableArray<Outputs.GlobalTableAttributeDefinition>> AttributeDefinitions { get; private set; } = null!;

        [Output("billingMode")]
        public Output<string?> BillingMode { get; private set; } = null!;

        [Output("globalSecondaryIndexes")]
        public Output<ImmutableArray<Outputs.GlobalTableGlobalSecondaryIndex>> GlobalSecondaryIndexes { get; private set; } = null!;

        [Output("keySchema")]
        public Output<ImmutableArray<Outputs.GlobalTableKeySchema>> KeySchema { get; private set; } = null!;

        [Output("localSecondaryIndexes")]
        public Output<ImmutableArray<Outputs.GlobalTableLocalSecondaryIndex>> LocalSecondaryIndexes { get; private set; } = null!;

        [Output("replicas")]
        public Output<ImmutableArray<Outputs.GlobalTableReplicaSpecification>> Replicas { get; private set; } = null!;

        [Output("sseSpecification")]
        public Output<Outputs.GlobalTableSSESpecification?> SseSpecification { get; private set; } = null!;

        [Output("streamArn")]
        public Output<string> StreamArn { get; private set; } = null!;

        [Output("streamSpecification")]
        public Output<Outputs.GlobalTableStreamSpecification?> StreamSpecification { get; private set; } = null!;

        [Output("tableId")]
        public Output<string> TableId { get; private set; } = null!;

        [Output("tableName")]
        public Output<string?> TableName { get; private set; } = null!;

        [Output("timeToLiveSpecification")]
        public Output<Outputs.GlobalTableTimeToLiveSpecification?> TimeToLiveSpecification { get; private set; } = null!;

        [Output("writeProvisionedThroughputSettings")]
        public Output<Outputs.GlobalTableWriteProvisionedThroughputSettings?> WriteProvisionedThroughputSettings { get; private set; } = null!;


        /// <summary>
        /// Create a GlobalTable resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public GlobalTable(string name, GlobalTableArgs args, CustomResourceOptions? options = null)
            : base("aws-native:dynamodb:GlobalTable", name, args ?? new GlobalTableArgs(), MakeResourceOptions(options, ""))
        {
        }

        private GlobalTable(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:dynamodb:GlobalTable", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing GlobalTable resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static GlobalTable Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new GlobalTable(name, id, options);
        }
    }

    public sealed class GlobalTableArgs : global::Pulumi.ResourceArgs
    {
        [Input("attributeDefinitions", required: true)]
        private InputList<Inputs.GlobalTableAttributeDefinitionArgs>? _attributeDefinitions;
        public InputList<Inputs.GlobalTableAttributeDefinitionArgs> AttributeDefinitions
        {
            get => _attributeDefinitions ?? (_attributeDefinitions = new InputList<Inputs.GlobalTableAttributeDefinitionArgs>());
            set => _attributeDefinitions = value;
        }

        [Input("billingMode")]
        public Input<string>? BillingMode { get; set; }

        [Input("globalSecondaryIndexes")]
        private InputList<Inputs.GlobalTableGlobalSecondaryIndexArgs>? _globalSecondaryIndexes;
        public InputList<Inputs.GlobalTableGlobalSecondaryIndexArgs> GlobalSecondaryIndexes
        {
            get => _globalSecondaryIndexes ?? (_globalSecondaryIndexes = new InputList<Inputs.GlobalTableGlobalSecondaryIndexArgs>());
            set => _globalSecondaryIndexes = value;
        }

        [Input("keySchema", required: true)]
        private InputList<Inputs.GlobalTableKeySchemaArgs>? _keySchema;
        public InputList<Inputs.GlobalTableKeySchemaArgs> KeySchema
        {
            get => _keySchema ?? (_keySchema = new InputList<Inputs.GlobalTableKeySchemaArgs>());
            set => _keySchema = value;
        }

        [Input("localSecondaryIndexes")]
        private InputList<Inputs.GlobalTableLocalSecondaryIndexArgs>? _localSecondaryIndexes;
        public InputList<Inputs.GlobalTableLocalSecondaryIndexArgs> LocalSecondaryIndexes
        {
            get => _localSecondaryIndexes ?? (_localSecondaryIndexes = new InputList<Inputs.GlobalTableLocalSecondaryIndexArgs>());
            set => _localSecondaryIndexes = value;
        }

        [Input("replicas", required: true)]
        private InputList<Inputs.GlobalTableReplicaSpecificationArgs>? _replicas;
        public InputList<Inputs.GlobalTableReplicaSpecificationArgs> Replicas
        {
            get => _replicas ?? (_replicas = new InputList<Inputs.GlobalTableReplicaSpecificationArgs>());
            set => _replicas = value;
        }

        [Input("sseSpecification")]
        public Input<Inputs.GlobalTableSSESpecificationArgs>? SseSpecification { get; set; }

        [Input("streamSpecification")]
        public Input<Inputs.GlobalTableStreamSpecificationArgs>? StreamSpecification { get; set; }

        [Input("tableName")]
        public Input<string>? TableName { get; set; }

        [Input("timeToLiveSpecification")]
        public Input<Inputs.GlobalTableTimeToLiveSpecificationArgs>? TimeToLiveSpecification { get; set; }

        [Input("writeProvisionedThroughputSettings")]
        public Input<Inputs.GlobalTableWriteProvisionedThroughputSettingsArgs>? WriteProvisionedThroughputSettings { get; set; }

        public GlobalTableArgs()
        {
        }
        public static new GlobalTableArgs Empty => new GlobalTableArgs();
    }
}
