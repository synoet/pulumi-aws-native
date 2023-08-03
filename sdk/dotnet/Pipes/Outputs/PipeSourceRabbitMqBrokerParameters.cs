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
    public sealed class PipeSourceRabbitMqBrokerParameters
    {
        public readonly int? BatchSize;
        public readonly Outputs.PipeMqBrokerAccessCredentialsProperties Credentials;
        public readonly int? MaximumBatchingWindowInSeconds;
        public readonly string QueueName;
        public readonly string? VirtualHost;

        [OutputConstructor]
        private PipeSourceRabbitMqBrokerParameters(
            int? batchSize,

            Outputs.PipeMqBrokerAccessCredentialsProperties credentials,

            int? maximumBatchingWindowInSeconds,

            string queueName,

            string? virtualHost)
        {
            BatchSize = batchSize;
            Credentials = credentials;
            MaximumBatchingWindowInSeconds = maximumBatchingWindowInSeconds;
            QueueName = queueName;
            VirtualHost = virtualHost;
        }
    }
}
