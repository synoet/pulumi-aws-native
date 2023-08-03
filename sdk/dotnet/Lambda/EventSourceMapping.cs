// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lambda
{
    /// <summary>
    /// Resource Type definition for AWS::Lambda::EventSourceMapping
    /// </summary>
    [AwsNativeResourceType("aws-native:lambda:EventSourceMapping")]
    public partial class EventSourceMapping : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Specific configuration settings for an MSK event source.
        /// </summary>
        [Output("amazonManagedKafkaEventSourceConfig")]
        public Output<Outputs.EventSourceMappingAmazonManagedKafkaEventSourceConfig?> AmazonManagedKafkaEventSourceConfig { get; private set; } = null!;

        /// <summary>
        /// The maximum number of items to retrieve in a single batch.
        /// </summary>
        [Output("batchSize")]
        public Output<int?> BatchSize { get; private set; } = null!;

        /// <summary>
        /// (Streams) If the function returns an error, split the batch in two and retry.
        /// </summary>
        [Output("bisectBatchOnFunctionError")]
        public Output<bool?> BisectBatchOnFunctionError { get; private set; } = null!;

        /// <summary>
        /// (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.
        /// </summary>
        [Output("destinationConfig")]
        public Output<Outputs.EventSourceMappingDestinationConfig?> DestinationConfig { get; private set; } = null!;

        /// <summary>
        /// Document db event source config.
        /// </summary>
        [Output("documentDbEventSourceConfig")]
        public Output<Outputs.EventSourceMappingDocumentDbEventSourceConfig?> DocumentDbEventSourceConfig { get; private set; } = null!;

        /// <summary>
        /// Disables the event source mapping to pause polling and invocation.
        /// </summary>
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the event source.
        /// </summary>
        [Output("eventSourceArn")]
        public Output<string?> EventSourceArn { get; private set; } = null!;

        /// <summary>
        /// The filter criteria to control event filtering.
        /// </summary>
        [Output("filterCriteria")]
        public Output<Outputs.EventSourceMappingFilterCriteria?> FilterCriteria { get; private set; } = null!;

        /// <summary>
        /// The name of the Lambda function.
        /// </summary>
        [Output("functionName")]
        public Output<string> FunctionName { get; private set; } = null!;

        /// <summary>
        /// (Streams) A list of response types supported by the function.
        /// </summary>
        [Output("functionResponseTypes")]
        public Output<ImmutableArray<Pulumi.AwsNative.Lambda.EventSourceMappingFunctionResponseTypesItem>> FunctionResponseTypes { get; private set; } = null!;

        /// <summary>
        /// (Streams) The maximum amount of time to gather records before invoking the function, in seconds.
        /// </summary>
        [Output("maximumBatchingWindowInSeconds")]
        public Output<int?> MaximumBatchingWindowInSeconds { get; private set; } = null!;

        /// <summary>
        /// (Streams) The maximum age of a record that Lambda sends to a function for processing.
        /// </summary>
        [Output("maximumRecordAgeInSeconds")]
        public Output<int?> MaximumRecordAgeInSeconds { get; private set; } = null!;

        /// <summary>
        /// (Streams) The maximum number of times to retry when the function returns an error.
        /// </summary>
        [Output("maximumRetryAttempts")]
        public Output<int?> MaximumRetryAttempts { get; private set; } = null!;

        /// <summary>
        /// (Streams) The number of batches to process from each shard concurrently.
        /// </summary>
        [Output("parallelizationFactor")]
        public Output<int?> ParallelizationFactor { get; private set; } = null!;

        /// <summary>
        /// (ActiveMQ) A list of ActiveMQ queues.
        /// </summary>
        [Output("queues")]
        public Output<ImmutableArray<string>> Queues { get; private set; } = null!;

        /// <summary>
        /// The scaling configuration for the event source.
        /// </summary>
        [Output("scalingConfig")]
        public Output<Outputs.EventSourceMappingScalingConfig?> ScalingConfig { get; private set; } = null!;

        /// <summary>
        /// Self-managed event source endpoints.
        /// </summary>
        [Output("selfManagedEventSource")]
        public Output<Outputs.EventSourceMappingSelfManagedEventSource?> SelfManagedEventSource { get; private set; } = null!;

        /// <summary>
        /// Specific configuration settings for a Self-Managed Apache Kafka event source.
        /// </summary>
        [Output("selfManagedKafkaEventSourceConfig")]
        public Output<Outputs.EventSourceMappingSelfManagedKafkaEventSourceConfig?> SelfManagedKafkaEventSourceConfig { get; private set; } = null!;

        /// <summary>
        /// A list of SourceAccessConfiguration.
        /// </summary>
        [Output("sourceAccessConfigurations")]
        public Output<ImmutableArray<Outputs.EventSourceMappingSourceAccessConfiguration>> SourceAccessConfigurations { get; private set; } = null!;

        /// <summary>
        /// The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Streams sources.
        /// </summary>
        [Output("startingPosition")]
        public Output<string?> StartingPosition { get; private set; } = null!;

        /// <summary>
        /// With StartingPosition set to AT_TIMESTAMP, the time from which to start reading, in Unix time seconds.
        /// </summary>
        [Output("startingPositionTimestamp")]
        public Output<double?> StartingPositionTimestamp { get; private set; } = null!;

        /// <summary>
        /// (Kafka) A list of Kafka topics.
        /// </summary>
        [Output("topics")]
        public Output<ImmutableArray<string>> Topics { get; private set; } = null!;

        /// <summary>
        /// (Streams) Tumbling window (non-overlapping time window) duration to perform aggregations.
        /// </summary>
        [Output("tumblingWindowInSeconds")]
        public Output<int?> TumblingWindowInSeconds { get; private set; } = null!;


        /// <summary>
        /// Create a EventSourceMapping resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public EventSourceMapping(string name, EventSourceMappingArgs args, CustomResourceOptions? options = null)
            : base("aws-native:lambda:EventSourceMapping", name, args ?? new EventSourceMappingArgs(), MakeResourceOptions(options, ""))
        {
        }

        private EventSourceMapping(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:lambda:EventSourceMapping", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing EventSourceMapping resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static EventSourceMapping Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new EventSourceMapping(name, id, options);
        }
    }

    public sealed class EventSourceMappingArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specific configuration settings for an MSK event source.
        /// </summary>
        [Input("amazonManagedKafkaEventSourceConfig")]
        public Input<Inputs.EventSourceMappingAmazonManagedKafkaEventSourceConfigArgs>? AmazonManagedKafkaEventSourceConfig { get; set; }

        /// <summary>
        /// The maximum number of items to retrieve in a single batch.
        /// </summary>
        [Input("batchSize")]
        public Input<int>? BatchSize { get; set; }

        /// <summary>
        /// (Streams) If the function returns an error, split the batch in two and retry.
        /// </summary>
        [Input("bisectBatchOnFunctionError")]
        public Input<bool>? BisectBatchOnFunctionError { get; set; }

        /// <summary>
        /// (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.
        /// </summary>
        [Input("destinationConfig")]
        public Input<Inputs.EventSourceMappingDestinationConfigArgs>? DestinationConfig { get; set; }

        /// <summary>
        /// Document db event source config.
        /// </summary>
        [Input("documentDbEventSourceConfig")]
        public Input<Inputs.EventSourceMappingDocumentDbEventSourceConfigArgs>? DocumentDbEventSourceConfig { get; set; }

        /// <summary>
        /// Disables the event source mapping to pause polling and invocation.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the event source.
        /// </summary>
        [Input("eventSourceArn")]
        public Input<string>? EventSourceArn { get; set; }

        /// <summary>
        /// The filter criteria to control event filtering.
        /// </summary>
        [Input("filterCriteria")]
        public Input<Inputs.EventSourceMappingFilterCriteriaArgs>? FilterCriteria { get; set; }

        /// <summary>
        /// The name of the Lambda function.
        /// </summary>
        [Input("functionName", required: true)]
        public Input<string> FunctionName { get; set; } = null!;

        [Input("functionResponseTypes")]
        private InputList<Pulumi.AwsNative.Lambda.EventSourceMappingFunctionResponseTypesItem>? _functionResponseTypes;

        /// <summary>
        /// (Streams) A list of response types supported by the function.
        /// </summary>
        public InputList<Pulumi.AwsNative.Lambda.EventSourceMappingFunctionResponseTypesItem> FunctionResponseTypes
        {
            get => _functionResponseTypes ?? (_functionResponseTypes = new InputList<Pulumi.AwsNative.Lambda.EventSourceMappingFunctionResponseTypesItem>());
            set => _functionResponseTypes = value;
        }

        /// <summary>
        /// (Streams) The maximum amount of time to gather records before invoking the function, in seconds.
        /// </summary>
        [Input("maximumBatchingWindowInSeconds")]
        public Input<int>? MaximumBatchingWindowInSeconds { get; set; }

        /// <summary>
        /// (Streams) The maximum age of a record that Lambda sends to a function for processing.
        /// </summary>
        [Input("maximumRecordAgeInSeconds")]
        public Input<int>? MaximumRecordAgeInSeconds { get; set; }

        /// <summary>
        /// (Streams) The maximum number of times to retry when the function returns an error.
        /// </summary>
        [Input("maximumRetryAttempts")]
        public Input<int>? MaximumRetryAttempts { get; set; }

        /// <summary>
        /// (Streams) The number of batches to process from each shard concurrently.
        /// </summary>
        [Input("parallelizationFactor")]
        public Input<int>? ParallelizationFactor { get; set; }

        [Input("queues")]
        private InputList<string>? _queues;

        /// <summary>
        /// (ActiveMQ) A list of ActiveMQ queues.
        /// </summary>
        public InputList<string> Queues
        {
            get => _queues ?? (_queues = new InputList<string>());
            set => _queues = value;
        }

        /// <summary>
        /// The scaling configuration for the event source.
        /// </summary>
        [Input("scalingConfig")]
        public Input<Inputs.EventSourceMappingScalingConfigArgs>? ScalingConfig { get; set; }

        /// <summary>
        /// Self-managed event source endpoints.
        /// </summary>
        [Input("selfManagedEventSource")]
        public Input<Inputs.EventSourceMappingSelfManagedEventSourceArgs>? SelfManagedEventSource { get; set; }

        /// <summary>
        /// Specific configuration settings for a Self-Managed Apache Kafka event source.
        /// </summary>
        [Input("selfManagedKafkaEventSourceConfig")]
        public Input<Inputs.EventSourceMappingSelfManagedKafkaEventSourceConfigArgs>? SelfManagedKafkaEventSourceConfig { get; set; }

        [Input("sourceAccessConfigurations")]
        private InputList<Inputs.EventSourceMappingSourceAccessConfigurationArgs>? _sourceAccessConfigurations;

        /// <summary>
        /// A list of SourceAccessConfiguration.
        /// </summary>
        public InputList<Inputs.EventSourceMappingSourceAccessConfigurationArgs> SourceAccessConfigurations
        {
            get => _sourceAccessConfigurations ?? (_sourceAccessConfigurations = new InputList<Inputs.EventSourceMappingSourceAccessConfigurationArgs>());
            set => _sourceAccessConfigurations = value;
        }

        /// <summary>
        /// The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Streams sources.
        /// </summary>
        [Input("startingPosition")]
        public Input<string>? StartingPosition { get; set; }

        /// <summary>
        /// With StartingPosition set to AT_TIMESTAMP, the time from which to start reading, in Unix time seconds.
        /// </summary>
        [Input("startingPositionTimestamp")]
        public Input<double>? StartingPositionTimestamp { get; set; }

        [Input("topics")]
        private InputList<string>? _topics;

        /// <summary>
        /// (Kafka) A list of Kafka topics.
        /// </summary>
        public InputList<string> Topics
        {
            get => _topics ?? (_topics = new InputList<string>());
            set => _topics = value;
        }

        /// <summary>
        /// (Streams) Tumbling window (non-overlapping time window) duration to perform aggregations.
        /// </summary>
        [Input("tumblingWindowInSeconds")]
        public Input<int>? TumblingWindowInSeconds { get; set; }

        public EventSourceMappingArgs()
        {
        }
        public static new EventSourceMappingArgs Empty => new EventSourceMappingArgs();
    }
}
