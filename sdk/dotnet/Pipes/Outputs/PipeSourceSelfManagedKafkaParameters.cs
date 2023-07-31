// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pipes.Outputs
{

    [OutputType]
    public sealed class PipeSourceSelfManagedKafkaParameters
    {
        public readonly ImmutableArray<string> AdditionalBootstrapServers;
        public readonly int? BatchSize;
        public readonly string? ConsumerGroupID;
        public readonly object? Credentials;
        public readonly int? MaximumBatchingWindowInSeconds;
        /// <summary>
        /// Optional SecretManager ARN which stores the database credentials
        /// </summary>
        public readonly string? ServerRootCaCertificate;
        public readonly Pulumi.AwsNative.Pipes.PipeSelfManagedKafkaStartPosition? StartingPosition;
        public readonly string TopicName;
        public readonly Outputs.PipeSelfManagedKafkaAccessConfigurationVpc? Vpc;

        [OutputConstructor]
        private PipeSourceSelfManagedKafkaParameters(
            ImmutableArray<string> additionalBootstrapServers,

            int? batchSize,

            string? consumerGroupID,

            object? credentials,

            int? maximumBatchingWindowInSeconds,

            string? serverRootCaCertificate,

            Pulumi.AwsNative.Pipes.PipeSelfManagedKafkaStartPosition? startingPosition,

            string topicName,

            Outputs.PipeSelfManagedKafkaAccessConfigurationVpc? vpc)
        {
            AdditionalBootstrapServers = additionalBootstrapServers;
            BatchSize = batchSize;
            ConsumerGroupID = consumerGroupID;
            Credentials = credentials;
            MaximumBatchingWindowInSeconds = maximumBatchingWindowInSeconds;
            ServerRootCaCertificate = serverRootCaCertificate;
            StartingPosition = startingPosition;
            TopicName = topicName;
            Vpc = vpc;
        }
    }
}
