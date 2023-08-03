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
    public sealed class PipeSourceDynamoDbStreamParameters
    {
        public readonly int? BatchSize;
        public readonly Outputs.PipeDeadLetterConfig? DeadLetterConfig;
        public readonly int? MaximumBatchingWindowInSeconds;
        public readonly int? MaximumRecordAgeInSeconds;
        public readonly int? MaximumRetryAttempts;
        public readonly Pulumi.AwsNative.Pipes.PipeOnPartialBatchItemFailureStreams? OnPartialBatchItemFailure;
        public readonly int? ParallelizationFactor;
        public readonly Pulumi.AwsNative.Pipes.PipeDynamoDbStreamStartPosition StartingPosition;

        [OutputConstructor]
        private PipeSourceDynamoDbStreamParameters(
            int? batchSize,

            Outputs.PipeDeadLetterConfig? deadLetterConfig,

            int? maximumBatchingWindowInSeconds,

            int? maximumRecordAgeInSeconds,

            int? maximumRetryAttempts,

            Pulumi.AwsNative.Pipes.PipeOnPartialBatchItemFailureStreams? onPartialBatchItemFailure,

            int? parallelizationFactor,

            Pulumi.AwsNative.Pipes.PipeDynamoDbStreamStartPosition startingPosition)
        {
            BatchSize = batchSize;
            DeadLetterConfig = deadLetterConfig;
            MaximumBatchingWindowInSeconds = maximumBatchingWindowInSeconds;
            MaximumRecordAgeInSeconds = maximumRecordAgeInSeconds;
            MaximumRetryAttempts = maximumRetryAttempts;
            OnPartialBatchItemFailure = onPartialBatchItemFailure;
            ParallelizationFactor = parallelizationFactor;
            StartingPosition = startingPosition;
        }
    }
}
